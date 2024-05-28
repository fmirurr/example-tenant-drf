from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from tenants.models import Tenant

import subprocess

import socket
import psycopg2
import os


@receiver(post_save, sender=Tenant)
def create_tenant_database(sender, instance, created, **kwargs):
    if created:
        db_name = instance.database_name
        # create_db_command = f"createdb {db_name}"
        # subprocess.run(create_db_command, shell=True)
        conn = psycopg2.connect(
            user="postgres", password="admin", host="localhost", port="5432"
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Crear nueva base de datos
        cur.execute("CREATE DATABASE {}".format(db_name))
        cur.close()
        conn.close()

        import time
        time.sleep(15)
        # migrate_command = f"python manage.py migrate --database={db_name}"
        # subprocess.run(migrate_command, shell=True)
        from django.conf import settings
        from django.db import connections
        from django.core.management import call_command

        default_db_config = settings.DATABASES['default']
        connections.databases[db_name] = {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": db_name,
            "USER": "postgres",
            "PASSWORD": "admin",
            "HOST": "localhost",
            "PORT": 5432,
            "TIME_ZONE": settings.TIME_ZONE,
            'CONN_MAX_AGE': None,
            "CONN_HEALTH_CHECKS": False,
            'OPTIONS': default_db_config.get('OPTIONS', {}),
        }

        # Ejecutar migraciones para la base de datos del inquilino
        call_command("migrate", database=db_name)
        print("hecho")
