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

        migrate_command = f"python manage.py migrate --database={db_name}"
        os.system(migrate_command)
        print("hecho")
