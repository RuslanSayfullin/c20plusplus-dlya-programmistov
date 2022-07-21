from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.formats import date_format


# Create your models here.
from .dizaynerskoevoznagrazhdenie import DizaynerskoeVoznagrazhdenie
from inquery.models import Inquery


class Dogovor(models.Model):
    class Meta:
        db_table = "dogovora"
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

    TIPY_DOGOVOROV = (
        # Изготовление мебели
        ('furniture_making_ooo-refabrik', 'Изготовление мебели | ООО «Ре-фабрик»'),
        ('izgotovlenie_2021_02_mebeli_ip_frolov', 'Изготовление мебели | ИП Фролов'),
        ('izgotovlenie_2021_02_mebeli_ip_bagautdinov', 'Изготовление мебели | ИП Багаутдинов'),
        ('izgotovlenie_2021_02_mebeli_ip_sadykov', 'Изготовление мебели | ИП Садыков'),
        ('izgotovlenie_2021_02_mebeli_ip_hafizov', 'Изготовление мебели | ИП Хафизов'),

        # Мягкая мебель
        ('upholstered_furniture_ooo-refabrik', 'Мягкая мебель | ООО «Ре-фабрик»'),
        ('mygkaya_2021_02_mebel_ip_frolov', 'Мягкая мебель | ИП Фролов'),
        ('mygkaya_2021_02_mebel_ip_bagautdinov', 'Мягкая мебель | ИП Багаутдинов'),
        ('mygkaya_2021_02_mebel_ip_sadykov', 'Мягкая мебель | ИП Садыков'),
        ('mygkaya_2021_02_mebel_ip_hafizov', 'Мягкая мебель | ИП Хафизов'),
        # Техника
        ('technic_2021_04_ip_frolov', 'Техника | ИП Фролов'),
        # ('technic_2021_04_ip_bagautdinov', 'Техника | ИП Багаутдинов'),
        ('technic_2021_04_ip_sadykov', 'Техника | ИП Садыков'),
        # ('technic_2021_04_ip_hafizov', 'Техника | ИП Хафизов'),
        ('ooo_reforma_plus_tehnika', 'Техника | ООО «Ре-форма плюс»'),
        # ('ooo_refabrik_tehnika', 'Техника | ООО «Ре-фабрик»'),
        # ООО
        ('ooo_reforma_plus', 'ООО «Ре-форма плюс»'),
        # ('ooo_refabrik', 'ООО «Ре-фабрик»'),
        # Подключение техники
        ('podklyuchenie_2021_06_tehniki_frolov', 'Подключение техники | ИП Фролов'),
        # ('podklyuchenie_2021_06_tehniki_bagautdinov', 'Подключение техники | ИП Багаутдинов'),
        ('podklyuchenie_2021_06_tehniki_sadykov', 'Подключение техники | ИП Садыков'),
        # ('podklyuchenie_2021_06_tehniki_hafizov', 'Подключение техники | ИП Хафизов'),
        ('podklyuchenie_2021_06_tehniki_ooo_reforma_plus_yur', 'Подключение техники | ООО «Ре-форма плюс» | Юр'),
        # Матрасы
        ('mattresses_ooo-refabrik', 'Матрасы | ООО «Ре-фабрик»'),
        ('matrasy_2021_06_frolov', 'Матрасы | ИП Фролов'),
        ('matrasy_2021_06_bagautdinov', 'Матрасы | ИП Багаутдинов'),
        ('matrasy_2021_06_sadykov', 'Матрасы | ИП Садыков'),
        ('matrasy_2021_06_hafizov', 'Матрасы | ИП Хафизов'),
        # Договор Orac на декоры
        ('decoration_sadykov', 'Декор | ИП Садыков'),
        # Готовая мебель (мебель выставочного образца)
        ('gotovaya_mebel_2021_06_frolov', 'Готовая мебель (выставочный образец) | ИП Фролов'),
        ('gotovaya_mebel_2021_06_bagautdinov', 'Готовая мебель (выставочный образец) | ИП Багаутдинов'),
        ('gotovaya_mebel_2021_06_sadykov', 'Готовая мебель (выставочный образец) | ИП Садыков'),
        ('gotovaya_mebel_2021_06_hafizov', 'Готовая мебель (выставочный образец) | ИП Хафизов'),
        # Искусственный камень
        ('artificial_stone_ooo-refabrik', 'Искусственный камень | ООО «Ре-фабрик»'),
        ('iskusstvenny_2021_02_kamen_frolov', 'Искусственный камень | ИП Фролов'),
        ('iskusstvenny_2021_02_kamen_bagautdinov', 'Искусственный камень | ИП Багаутдинов'),
        ('iskusstvenny_2021_02_kamen_sadykov', 'Искусственный камень | ИП Садыков'),
        ('iskusstvenny_2021_02_kamen_hafizov', 'Искусственный камень | ИП Хафизов'),
        ('iskusstvenny_kamen_ooo_re_forma_plus', 'Искусственный камень | ООО «Ре-форма плюс»'),
        # ('iskusstvenny_kamen_ooo_refabrik', 'Искусственный камень | ООО «Ре-фабрик»'),
        # Текстиль
        ('tekstil_ip_sadykov_fiz', 'Текстиль | ИП Садыков | Физ'),
        # ('tekstil_ip_sadykov_yur', 'Текстиль | ИП Садыков | Юр'),
        # Двери
        ('door_manufacturing_ooo-refabrik', 'Двери | ООО «Ре-фабрик»'),
        ('dveri_ip_frolov', 'Двери | ИП Фролов'),
        ('dveri_ip_bagautdinov', 'Двери | ИП Багаутдинов'),
        ('dveri_ip_sadykov', 'Двери | ИП Садыков'),
        ('dveri_ip_hafizov', 'Двери | ИП Хафизов'),
        # Оказание транспортных услуг
        ('transportation_services_ooo-refabrik', 'Оказание транспортных услуг | ООО «Ре-фабрик»'),
        ('delivery_ip_frolov', 'Оказание транспортных услуг | ИП Фролов'),
        ('delivery_ip_bagautdinov', 'Оказание транспортных услуг | ИП Багаутдинов'),
        ('delivery_ip_sadykov', 'Оказание транспортных услуг | ИП Садыков'),
        ('delivery_ip_hafizov', 'Оказание транспортных услуг | ИП Хафизов'),
        ('transportation_services_ooo_reforma_plus_yur', 'Оказание транспортных услуг | ООО «Ре-форма плюс» | Юр'),
        # Монтаж/демонтаж
        ('montazh_demontazh_ip_sadykov_fiz', 'Монтаж/демонтаж | ИП Садыков | Физ'),
        ('montazh_demontazh_ooo_reforma_plus_yur', 'Монтаж/демонтаж | ООО «Ре-форма плюс» | Юр'),
        # Экспресс дизайн–проект
        ('ekspress_dizayn_sadykov', 'Экспресс дизайн–проект | ИП Садыков | Физ'),
    )

    froze = models.OneToOneField(Inquery, db_index=True, on_delete=models.CASCADE, verbose_name="Заявка")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    published = models.DateTimeField(default=timezone.now, verbose_name="Дата Создания")

    passport_familiya = models.CharField(max_length=200, default='', db_index=True, blank=True)
    passport_imya = models.CharField(max_length=200, default='', db_index=True, blank=True)
    passport_otchestvo = models.CharField(max_length=200, default='', db_index=True, blank=True)

    passport_birthday_date = models.DateField(default=None, blank=True, null=True)
    passport_birthday_place = models.CharField(max_length=200, default='', blank=True, null=True)
    passport_seria = models.CharField(max_length=4, default=None, blank=True, null=True)
    passport_nomer = models.CharField(max_length=6, default=None, blank=True, null=True)
    passport_kem_vydan = models.CharField(max_length=200, default='', blank=True, null=True)
    passport_kogda_vydan = models.DateField(default=None, blank=True, null=True)
    passport_kp = models.CharField(max_length=7, default=None, blank=True, null=True)
    adres_propiski = models.CharField(max_length=200, default='', blank=True, null=True)
    adres_ustanovki = models.CharField(max_length=200, default='', blank=True, null=True)

    vsego_k_oplate = models.PositiveIntegerField(default=None, blank=True, null=True)
    # oplata_predoplata_procent = models.PositiveSmallIntegerField(default=0)
    oplata_predoplata_rub = models.PositiveIntegerField(default=None, blank=True, null=True)
    # oplata_ostatok_procent = models.PositiveSmallIntegerField(default=0)
    # oplata_ostatok_rub = models.PositiveIntegerField(default=0)
    naimenov_soputstv_izdeliy = models.CharField(max_length=200, default='', blank=True, null=True)  # Наименования сопутствующих изделий
    summa_za_soputstv_uslugi = models.PositiveIntegerField(default=None, blank=True, null=True)  # Указать сумму за сопутств.услугу(если они есть)
    stoimost_dostavki_vne_ufa = models.PositiveIntegerField(default=None, blank=True, null=True)

    data_podpisaniya = models.DateField(default=None, blank=True, null=True)
    srok_ispolneniya_rabot = models.PositiveSmallIntegerField(default=None, blank=True, null=True)
    tip_dogovora = models.CharField(db_index=True, max_length=100, choices=TIPY_DOGOVOROV, default=0, blank=True, null=True, verbose_name="Тип договора")
    nomer_dogovora = models.CharField(max_length=20, default='', blank=True, null=True, verbose_name="Номер договора")  # Номер договора
    tip_opisanie_izdeliya = models.CharField(max_length=500, default='', blank=True, null=True)  # Тип (описание) изделия
    doverennye_lica = models.CharField(max_length=500, default='', blank=True, null=True)  # Доверенные лица
    doverennye_lica_telefony = models.CharField(max_length=500, default='', blank=True, null=True)  # Телефоны доверенных лиц
    nachalo_rabot_data = models.DateField(default=None, blank=True, null=True)  # Начало работ
    okonchanie_rabot_data = models.DateField(default=None, blank=True, null=True)  # Окончание работ

    tovarny_chek_tehnika = models.TextField(default='', blank=True, null=True)  # ТОВАРНЫЙ ЧЕК (10 строк в табл.)
    uslugi_po_podklyucheniyu_tehniki = models.TextField(default='', blank=True, null=True)  # УСЛУГИ ПО ПОДКЛЮЧЕНИЮ БЫТОВОЙ ТЕХНИКИ
    mygkaya_mebel_prilozhenie = models.TextField(default='', blank=True, null=True)  # Приложение к договору №1 - mygkaya_mebel

    dizaynerskoe_voznagrazhdenie = models.CharField(max_length=200, default='', blank=True, null=True)  # дизайн.вознаграждение
    akciya = models.ForeignKey(DizaynerskoeVoznagrazhdenie, default=None, blank=True, null=True, on_delete=models.CASCADE)

    technics_sroki_dostavki_tehniki = models.PositiveIntegerField(default=None, blank=True, null=True)
    technics_sroki_dostavki_tehniki_v_dnyah = models.PositiveIntegerField(default=None, blank=True, null=True)

    drugoy_dogovor = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '№ {nomer_dogovora} ("{kakoy_tip_dogovora_na_kirillice}", {data_podpisaniya}, {passport_familiya}, ' \
               '{passport_imya1}. {passport_otchestvo1}.)'.format(
                nomer_dogovora=str(self.nomer_dogovora) if self.nomer_dogovora else '',
                kakoy_tip_dogovora_na_kirillice=self.kakoy_tip_dogovora_na_kirillice(),
                data_podpisaniya=date_format(self.data_podpisaniya, format="d.m.Y") if self.data_podpisaniya else '',
                passport_familiya=str(self.passport_familiya) if self.passport_familiya else '',
                passport_imya1=str(self.passport_imya)[:1] if self.passport_imya else '',
                passport_otchestvo1=str(self.passport_otchestvo)[:1] if self.passport_otchestvo else '',
                )

    def kakoy_tip_dogovora(self):
        if self.tip_dogovora is None:
            return ''
        if self.tip_dogovora == 'ooo_reforma' or self.tip_dogovora == 'ooo_reforma_sever':
            return 'ooo_reforma'
        if self.tip_dogovora == 'ooo_reforma_plus_tehnika' or self.tip_dogovora == 'ooo_reforma_sever_tehnika':
            return 'ooo_reforma_tehnika'
        if self.tip_dogovora == 'tekstil_ip_sadykov_fiz':
            return 'tekstil_ip_sadykov_fiz'
        if self.tip_dogovora == 'tekstil_ip_sadykov_yur':
            return 'tekstil_ip_sadykov_yur'
        if self.tip_dogovora == 'montazh_demontazh_ip_sadykov_fiz':
            return 'montazh_demontazh_ip_sadykov_fiz'
        if self.tip_dogovora == 'montazh_demontazh_ooo_reforma_plus_yur':
            return 'montazh_demontazh_ooo_reforma_plus_yur'
        if self.tip_dogovora == 'iskusstvenny_kamen_ooo_re_forma_plus':
            return 'iskusstvenny_kamen_ooo_re_forma_plus'
        if self.tip_dogovora == 'iskusstvenny_kamen_ooo_refabrik':
            return 'iskusstvenny_kamen_ooo_refabrik'
        if 'dveri' in self.tip_dogovora:
            return 'dveri'
        if 'izgotovlenie_mebeli' in self.tip_dogovora:
            return 'izgotovlenie_mebeli'
        if 'mygkaya_mebel' in self.tip_dogovora:
            return 'mygkaya_mebel'
        if 'tehnika' in self.tip_dogovora:
            return 'tehnika'
        if 'technic_2021_04' in self.tip_dogovora:
            return 'technic_2021_04'
        if 'delivery' in self.tip_dogovora:
            return 'delivery'
        if 'izgotovlenie_2019_11_mebeli' in self.tip_dogovora:
            return 'izgotovlenie_2019_11_mebeli'
        if 'izgotovlenie_2020_09_mebeli' in self.tip_dogovora:
            return 'izgotovlenie_2020_09_mebeli'
        if 'izgotovlenie_2021_02_mebeli' in self.tip_dogovora:
            return 'izgotovlenie_2021_02_mebeli'
        if 'kuhonny_2021_07_garnitur_lite' in self.tip_dogovora:
            return 'kuhonny_2021_07_garnitur_lite'
        if 'mygkaya_2019_11_mebel' in self.tip_dogovora:
            return 'mygkaya_2019_11_mebel'
        if 'mygkaya_2020_09_mebel' in self.tip_dogovora:
            return 'mygkaya_2020_09_mebel'
        if 'mygkaya_2021_02_mebel' in self.tip_dogovora:
            return 'mygkaya_2021_02_mebel'
        if 'iskusstvenny_kamen' in self.tip_dogovora:
            return 'iskusstvenny_kamen'
        if 'iskusstvenny_2021_02_kamen' in self.tip_dogovora:
            return 'iskusstvenny_2021_02_kamen'
        if 'ekspress_dizayn' in self.tip_dogovora:
            return 'ekspress_dizayn'
        if 'podklyuchenie_2021_06_tehniki' in self.tip_dogovora:
            return 'podklyuchenie_2021_06_tehniki'
        if 'matrasy_2021_06' in self.tip_dogovora:
            return 'matrasy_2021_06'
        if 'decoration' in self.tip_dogovora:
            return 'decoration'
        if 'gotovaya_mebel_2021_06' in self.tip_dogovora:
            return 'gotovaya_mebel_2021_06'
        """Договоры физ.лиц с ООО Ре-фабрик"""
        if 'furniture_making_ooo-refabrik' in self.tip_dogovora:
            return 'furniture_making'
        if 'upholstered_furniture_ooo-refabrik' in self.tip_dogovora:
            return 'upholstered_furniture'
        if 'mattresses_ooo-refabrik' in self.tip_dogovora:
            return 'mattresses'
        if 'artificial_stone_ooo-refabrik' in self.tip_dogovora:
            return 'artificial_stone'
        if 'door_manufacturing_ooo-refabrik' in self.tip_dogovora:
            return 'door_manufacturing'
        if 'transportation_services_ooo-refabrik' in self.tip_dogovora:
            return 'transportation_services'

    def kakoy_tip_dogovora_na_kirillice(self):
        if self.tip_dogovora is None:
            return ''
        if self.tip_dogovora == 'ooo_reforma_plus':
            return 'ООО «Ре-форма плюс»'
        if self.tip_dogovora == 'ooo_reforma_sever':
            return 'ООО «Ре-форма Север»'
        if self.tip_dogovora == 'ooo_refabrik':
            return 'ООО «Ре-фабрик»'
        if self.tip_dogovora == 'ooo_reforma_plus_tehnika':
            return 'ООО «Ре-форма плюс» | Техника'
        if self.tip_dogovora == 'ooo_reforma_sever_tehnika':
            return 'ООО «Ре-форма Север» | Техника'
        if self.tip_dogovora == 'ooo_refabrik_tehnika':
            return 'ООО «Ре-фабрик» | Техника'
        if self.tip_dogovora == 'ooo_reforma_plus_s_nds':
            return 'ООО «Ре-форма плюс» | С НДС'
        if self.tip_dogovora == 'ooo_reforma_plus_bez_nds':
            return 'ООО «Ре-форма плюс» | Без НДС'
        if self.tip_dogovora == 'ooo_reforma_sever_s_nds':
            return 'ООО «Ре-форма Север» | С НДС'
        if self.tip_dogovora == 'ooo_reforma_sever_bez_nds':
            return 'ООО «Ре-форма Север» | Без НДС'
        if self.tip_dogovora == 'tekstil_ip_sadykov_fiz':
            return 'Текстиль | ИП Садыков | Физ'
        if self.tip_dogovora == 'tekstil_ip_sadykov_yur':
            return 'Текстиль | ИП Садыков | Юр'
        if self.tip_dogovora == 'montazh_demontazh_ip_sadykov_fiz':
            return 'Монтаж/демонтаж | ИП Садыков | Физ'
        if self.tip_dogovora == 'montazh_demontazh_ooo_reforma_plus_yur':
            return 'Монтаж/демонтаж | ООО «Ре-форма плюс» | Юр'
        if self.tip_dogovora == 'iskusstvenny_kamen_ooo_re_forma_plus':
            return 'Искусственный камень | ООО «Ре-форма плюс»'
        if self.tip_dogovora == 'iskusstvenny_kamen_ooo_refabrik':
            return 'Искусственный камень | ООО «Ре-фабрик»'
        if 'dveri' in self.tip_dogovora:
            return 'Двери'
        if 'izgotovlenie' in self.tip_dogovora:
            return 'Изготовление мебели'
        if 'garnitur_lite' in self.tip_dogovora:
            return 'Кухонный гарнитур Lite'
        if 'mygkaya' in self.tip_dogovora:
            return 'Мягкая мебель'
        if 'tehnika' in self.tip_dogovora or 'technic_2021_04' in self.tip_dogovora:
            return 'Техника'
        if 'delivery' in self.tip_dogovora:
            return 'Оказание транспортных услуг'
        if 'iskusstvenny' in self.tip_dogovora:
            return 'Искусственный камень'
        if 'ekspress_dizayn' in self.tip_dogovora:
            return 'Экспресс дизайн–проект'
        if 'podklyuchenie' in self.tip_dogovora:
            return 'Подключение техники'
        if 'matrasy' in self.tip_dogovora:
            return 'Матрасы'
        if 'decoration' in self.tip_dogovora:
            return 'Декор'
        if 'gotovaya' in self.tip_dogovora:
            return 'Готовая мебель'
        """Договоры физ.лиц с ООО Ре-фабрик"""
        if self.tip_dogovora == 'furniture_making_ooo-refabrik':
            return 'Изготовление мебели ООО «Ре-фабрик»'
        if self.tip_dogovora == 'upholstered_furniture_ooo-refabrik':
            return 'Мягкая мебель ООО «Ре-фабрик»'
        if self.tip_dogovora == 'mattresses_ooo-refabrik':
            return 'Матрасы ООО «Ре-фабрик»'
        if self.tip_dogovora == 'martificial_stone_ooo-refabrik':
            return 'Искусственный камень ООО «Ре-фабрик»'
        if self.tip_dogovora == 'door_manufacturing_ooo-refabrik':
            return 'Двери ООО «Ре-фабрик»'
        if self.tip_dogovora == 'transportation_services_ooo-refabrik':
            return 'Оказание транспортных услуг «Ре-фабрик»'

    def kakoe_yur_lico_na_kirillice(self):
        if 'frolov' in self.tip_dogovora:
            return 'ИП Фролов'
        elif 'bagautdinov' in self.tip_dogovora:
            return 'ИП Багаутдинов'
        elif 'sadykov' in self.tip_dogovora:
            return 'ИП Садыков'
        elif 'hafizov' in self.tip_dogovora:
            return 'ИП Хафизов'
        elif 'chuchelenko' in self.tip_dogovora:
            return 'ИП Чучеленко'
        elif 'buharmetov' in self.tip_dogovora:
            return 'ИП Бухарметов'
        elif self.tip_dogovora == 'ooo_reforma_plus_s_nds':
            return 'ООО «Ре-форма плюс» | С НДС'
        elif self.tip_dogovora == 'ooo_reforma_plus_bez_nds':
            return 'ООО «Ре-форма плюс» | Без НДС'
        elif self.tip_dogovora == 'ooo_reforma_sever_s_nds':
            return 'ООО «Ре-форма Север» | С НДС'
        elif self.tip_dogovora == 'ooo_reforma_sever_bez_nds':
            return 'ООО «Ре-форма Север» | Без НДС'
        elif 'ooo_reforma_plus' in self.tip_dogovora or 'ooo_re_forma_plus' in self.tip_dogovora:
            return 'ООО «Ре-форма плюс»'
        elif 'ooo_reforma_sever' in self.tip_dogovora:
            return 'ООО «Ре-форма Север»'
        elif 'ooo_refabrik' in self.tip_dogovora:
            return 'ООО «Ре--фабрик»'

        elif 'ooo-refabrik' in self.tip_dogovora:
            return 'ООО «Ре-фабрик»'
        return ''

    def postavshik(self):
        postavshik = {}
        postavshik['otkaz'] = {}
        if 'frolov' in self.tip_dogovora:
            postavshik['fio'] = 'Фролов Алексей Александрович'
            postavshik['svidetelstvo'] = ''
            postavshik['adres1'] = '450006, Республика Башкортостан, '
            postavshik['adres2'] = 'г. Уфа, ул. Пархоменко, д.117, кв.37'
            postavshik['adres1_post'] = '450106, Республика Башкортостан, '
            postavshik['adres2_post'] = 'г. Уфа, ул. Менделеева,  д.128, корп.1'
            postavshik['inn'] = '025803156617'
            postavshik['ogrnip'] = '321028000092443'
            postavshik['rs'] = '40802810406000067854'
            postavshik['otkaz']['mygkaya_mebel'] = ''
            postavshik['otkaz']['izgotovlenie_mebeli'] = ''
            postavshik['otkaz']['dveri'] = ''
            postavshik['doverennost'] = 'б/н от 21.06.2021 г.'
            postavshik['adres_poryadok_razresheniya_sporov'] = '__'

        elif 'ooo-refabrik' in self.tip_dogovora:
            postavshik['fio'] = 'РЕ - ФАБРИК'
            postavshik['svidetelstvo'] = ''
            postavshik['adres1'] = '450022, Республика Башкортостан, '
            postavshik['adres2'] = 'г. Уфа, ул. Менделеева,  д.145, пом.20'
            postavshik['adres1_post'] = '450112, Республика Башкортостан, '
            postavshik['adres2_post'] = 'г. Уфа, ул. Ульяновых, д.57'
            postavshik['inn'] = '0278931524'
            postavshik['kpp'] = '027801001'
            postavshik['ogrn'] = '1170280042008'
            postavshik['rs'] = '40702810306000021744'
            postavshik['otkaz']['izgotovlenie_mebeli'] = ''
            # postavshik['otkaz']['mygkaya_mebel'] = ''
            #postavshik['otkaz']['dveri'] = ''
            postavshik['doverennost'] = '-'
            postavshik['adres_poryadok_razresheniya_sporov'] = '__'

        elif 'bagautdinov' in self.tip_dogovora:
            postavshik['fio'] = 'Багаутдинов Эмиль Разитович'
            postavshik['svidetelstvo'] = '007758247 от 23.12.2016'
            postavshik['adres1'] = '452410, Республика Башкортостан,  '
            postavshik['adres2'] = 'Иглинский р-н, Иглино с., Мухина ул., д.45'
            postavshik['adres1_post'] = '450096, Республика Башкортостан, '
            postavshik['adres2_post'] = 'г.Уфа, ул.Энтузиастов д.14'
            postavshik['inn'] = '027319282852'
            postavshik['ogrnip'] = '319028000164001'
            postavshik['rs'] = '40802810606000041421'
            postavshik['otkaz']['mygkaya_mebel'] = '450096, РБ, г. Уфа, ул.Энтузиастов 14'
            postavshik['otkaz']['izgotovlenie_mebeli'] = '450096, РБ, г. Уфа, ул.Энтузиастов 14'
            postavshik['otkaz']['dveri'] = '450096, РБ, г. Уфа, ул.Энтузиастов 14'
            postavshik['doverennost'] = '02 АА 5056584 от 15.11.2019г.'
            postavshik['adres_poryadok_razresheniya_sporov'] = '450096, Республика Башкортостан, г. Уфа, ул. Энтузиастов 14'
        elif 'sadykov' in self.tip_dogovora:
            postavshik['fio'] = 'Садыков Фархад Идиятуллович'
            postavshik['svidetelstvo'] = '007108676 от 03.06.2014'
            postavshik['adres1'] = '452163, Республика Башкортостан, Чишминский р-н,'
            postavshik['adres2'] = 'Новотроицкое с., Школьная ул., дом № 2, кв. 1'
            postavshik['adres1_post'] = '450112, Республика Башкортостан, '
            postavshik['adres2_post'] = 'г. Уфа, ул. Ульяновых, д.57'
            postavshik['inn'] = '022402661350'
            postavshik['ogrnip'] = '314028000072800'
            postavshik['rs'] = '40802810806000015299'
            postavshik['otkaz']['mygkaya_mebel'] = '450112, РБ, г. Уфа, ул. Ульяновых, д. 57'
            postavshik['otkaz']['izgotovlenie_mebeli'] = '450112, РБ, г. Уфа, ул. Ульяновых, д. 57'
            postavshik['otkaz']['dveri'] = '450112, Республика Башкортостан,  г. Уфа, ул. Ульяновых, д. 57'
            postavshik['doverennost'] = '02 АА 4175422  от 15.02.2018г.'
            if self.tip_dogovora == 'tekstil_ip_sadykov_fiz' or self.tip_dogovora == 'tekstil_ip_sadykov_yur':
                postavshik['doverennost'] = '02 АА 5116982  от 03.09.2020 г.'  # Текстиль
            postavshik['adres_poryadok_razresheniya_sporov'] = '450112, Республика Башкортостан, г. Уфа, ул. Ульяновых, д. 57'
        elif 'hafizov' in self.tip_dogovora:
            postavshik['fio'] = 'Хафизов Азат Ильдарович'
            postavshik['svidetelstvo'] = '007857653 от 23.12.2016'
            postavshik['adres1'] = '450017, Республика Башкортостан, г.Уфа,'
            postavshik['adres2'] = 'ул. Ахметова, дом № 320, корп. 1, кв. 122'
            postavshik['adres1_post'] = '450022, Республика Башкортостан, '
            postavshik['adres2_post'] = 'г.Уфа, ул.Менделеева, д.145'
            postavshik['inn'] = '027813125266'
            postavshik['ogrnip'] = '316028000223382'
            postavshik['rs'] = '40802810406000015589'
            postavshik['otkaz']['mygkaya_mebel'] = '450022, РБ, г. Уфа, ул. Менделеева, д. 145'
            postavshik['otkaz']['izgotovlenie_mebeli'] = '450022, РБ, г. Уфа, ул. Менделеева, д. 145'
            postavshik['otkaz']['dveri'] = '450022, РБ, г. Уфа, ул. Менделеева, д. 145'
            postavshik['doverennost'] = '02 АА 5056586 от 15.11.2019г.'
            postavshik['adres_poryadok_razresheniya_sporov'] = '450022, Республика Башкортостан, г. Уфа, ул. Менделеева, д. 145'
        # OTHER
        elif 'chuchelenko' in self.tip_dogovora:
            postavshik['fio'] = 'Чучеленко Владимир Сергеевич'
            postavshik['svidetelstvo'] = '007857654 от 23.12.2016'
            postavshik['adres1'] = '450074, Республика Башкортостан, г.Уфа,'
            postavshik['adres2'] = 'ул. Испытателей, дом № 3, кв. 2'
            postavshik['adres1_post'] = '450096, Республика'
            postavshik['adres2_post'] = 'Башкортостан, г.Уфа, ул.Энтузиастов 14'
            postavshik['inn'] = '027415499777'
            postavshik['ogrnip'] = '316028000223371'
            postavshik['rs'] = '40802810106000015591'
            postavshik['otkaz']['mygkaya_mebel'] = '450055, РБ, г. Уфа, пр. Октября, д. 170'
            postavshik['otkaz']['izgotovlenie_mebeli'] = '450106, РБ, г. Уфа, ул. Менделеева, д. 128, корп. 1'
            postavshik['otkaz']['dveri'] = '450106, РБ, г. Уфа, ул. Менделеева, д. 128, корп. 1'
            postavshik['doverennost'] = '02 АА 5056585 от 15.11.2019г.'
        elif 'buharmetov' in self.tip_dogovora:
            postavshik['fio'] = 'Бухарметов Роберт Альфредович'
            postavshik['svidetelstvo'] = '007758247 от 23.12.2016'
            postavshik['adres1'] = '450055, Республика Башкортостан, '
            postavshik['adres2'] = 'г. Уфа, пр. Октября, д. 170'
            postavshik['inn'] = '027401773959'
            postavshik['ogrnip'] = '316028000223445'
            postavshik['rs'] = '40802810806000015590'
            postavshik['otkaz']['mygkaya_mebel'] = '450055, РБ, г. Уфа, пр. Октября, д. 170'
            postavshik['otkaz']['izgotovlenie_mebeli'] = '450055, РБ, г. Уфа, пр. Октября, д. 170'
            postavshik['otkaz']['dveri'] = '450055, РБ, г. Уфа, пр. Октября, д. 170'
            postavshik['doverennost'] = '02 АА 4175420 от 15.02.2018г.'
        else:
            postavshik['fio'] = '___ ____ ___________'
            postavshik['svidetelstvo'] = ''
            postavshik['adres1'] = '__________________'
            postavshik['adres2'] = '__________________'
            postavshik['adres1_post'] = '__________________'
            postavshik['adres2_post'] = '__________________'
            postavshik['inn'] = '__________________'
            postavshik['ogrnip'] = '__________________'
            postavshik['rs'] = '__________________'
            postavshik['doverennost'] = '__________________'

        postavshik['nomer_dog'] = postavshik['fio'][0]
        postavshik['bank1'] = 'БАШКИРСКОЕ ОТДЕЛЕНИЕ № 8598'
        postavshik['bank2'] = 'ПАО СБЕРБАНК г. УФА'
        postavshik['ks'] = '30101810300000000601'
        postavshik['bik'] = '048073601'
        inicialy = postavshik['fio'].split(' ')
        postavshik['inicialy'] = inicialy[0] + ' ' + inicialy[1][0:1] + '.' + inicialy[2][0:1] + '.'
        return postavshik
