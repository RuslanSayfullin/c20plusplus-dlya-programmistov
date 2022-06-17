import requests
from django.conf import settings


def send_sms(message, recipient_phone):
    """
    :param message:
    :param recipient_phone: 79000000000
    :return:
    """

    params = {
        "apiKey": settings.P1SMS_API_KEY,
        "sms": [
            {
                "channel": "char",
                "phone": recipient_phone,
                "text": message,
                "sender": settings.P1SMS_SENDER
            }
        ]
    }

    try:
        the_response = requests.post(settings.P1SMS_API_SERVER, json=params, timeout=0.7)
        # the_response.text
    except requests.exceptions.RequestException:
        pass


def get_sms_text2(staff_object, designer_object, start_datetime):
    date = start_datetime.strftime("%d.%m.%y")
    time = start_datetime.strftime("%H:%M")

    if staff_object.departament == Staff.DEPARTAMENT_VD:
        sms_message = u'Дата и время замера {date} в {time} т. 2991170 Реформа'.format(
            date=date, time=time,
        )
    else:  # DEPARTAMENT_SDM, DEPARTAMENT_SDP, DEPARTAMENT_SDE, DEPARTAMENT_OFI, DEPARTAMENT_MOS
        address = ''
        if staff_object.departament == Staff.DEPARTAMENT_SDM:
            address = 'Менделеева 145'
        elif staff_object.departament == Staff.DEPARTAMENT_SDP:
            address = 'пр.Октября 170'
        elif staff_object.departament == Staff.DEPARTAMENT_SDE:
            address = 'Энтузиастов 14'
        elif staff_object.departament == Staff.DEPARTAMENT_OFI:
            address = 'Энтузиастов 14'
        elif staff_object.departament == Staff.DEPARTAMENT_MOS:
            address = 'Энтузиастов 14'
        sms_message = u'Вы записаны {date} в {time} в салон {address} т.2991170 Реформа'.format(
            date=date, time=time, address=address,
        )
    return sms_message
