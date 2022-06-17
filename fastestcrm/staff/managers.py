from django.db import models


class KOManager(models.Manager):
    def _get_ko(self):
        return self.filter(departament=self.model.DEPARTAMENT_KO)

    def all(self):
        return self._get_ko()

    def active(self):
        return self._get_ko().exclude(is_locking=True).filter(user__is_active=True)