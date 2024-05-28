class TenantRouter:
    def db_for_read(self, model, **hints):
        return getattr(model, "_database", "default")

    def db_for_write(self, model, **hints):
        return getattr(model, "_database", "default")

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == "default"
