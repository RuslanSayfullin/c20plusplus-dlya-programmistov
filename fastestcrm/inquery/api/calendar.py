from django.core.exceptions import ObjectDoesNotExist
import uuid

from inquery.models import InqueryStatus, Inquery, Event


def is_busy_datetime(designer, start_datetime):
    """
    Проверка свободного времени у дизайнера/менеджера в заданный промежуток времени
    :param designer: django.contrib.auth
    :param start_datetime: datetime.datetime
    :return: Type boolean
    """

    if InqueryStatus.objects.filter(inquery__designer=designer, start_datetime=start_datetime)\
            .exclude(inquery__status=Inquery.INQUERY_CANCELED).count():
        return True

    if Event.objects.filter(designer=designer, start_datetime=start_datetime).count():
        return True

    return False


def get_unique_uuid(model):
    while True:
        new_uuid = uuid.uuid4().hex
        try:
            model.objects.get(uuid=new_uuid)
        except ObjectDoesNotExist:
            return new_uuid
