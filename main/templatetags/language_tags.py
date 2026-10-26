from django import template

register = template.Library()

UI_TRANSLATIONS = {
    'Asosiy': {'ru': 'Главная', 'en': 'Home'},
    "Litsey va ta'lim": {'ru': 'Лицей и образование', 'en': 'Lyceum and education'},
    'Rahbariyat': {'ru': 'Руководство', 'en': 'Leadership'},
    "Kafedralar va Yo'nalishlar": {'ru': 'Кафедры и направления', 'en': 'Departments and programs'},
    'Litsey Tarixi va Nizomi': {'ru': 'История и устав лицея', 'en': 'Lyceum history and charter'},
    "O'quvchilar uchun": {'ru': 'Ученикам', 'en': 'For students'},
    'Dars va Imtihon jadvali': {'ru': 'Расписание занятий и экзаменов', 'en': 'Class and exam schedules'},
    'To\'garaklar va Klubatlar': {'ru': 'Кружки и клубы', 'en': 'Clubs and activities'},
    'Elektron Kutubxona': {'ru': 'Электронная библиотека', 'en': 'Digital library'},
    'Yangiliklar': {'ru': 'Новости', 'en': 'News'},
    "Ma'lumotlar": {'ru': 'Информация', 'en': 'Information'},
    'Statistika va Yutuqlar': {'ru': 'Статистика и достижения', 'en': 'Statistics and achievements'},
    'Ochiq ma\'lumotlar': {'ru': 'Открытые данные', 'en': 'Open data'},
    'Davlat ramzlari': {'ru': 'Государственные символы', 'en': 'National symbols'},
    'Qabul 2026-2027': {'ru': 'Приём 2026-2027', 'en': 'Admissions 2026-2027'},
    'Fan olimpiadalari': {'ru': 'Предметные олимпиады', 'en': 'Subject Olympiads'},
    "Olimpiada e'lonlari": {'ru': 'Объявления об олимпиадах', 'en': 'Olympiad announcements'},
    'Natijalar': {'ru': 'Результаты', 'en': 'Results'},
    'Litsey Haqida': {'ru': 'О лицее', 'en': 'About the lyceum'},
    'Tezkor Havolalar': {'ru': 'Быстрые ссылки', 'en': 'Quick links'},
    "Yangiliklar va E'lonlar": {'ru': 'Новости и объявления', 'en': 'News and announcements'},
    'Asosiy sahifa': {'ru': 'Главная страница', 'en': 'Home page'},
    'Rahbariyat tarkibi': {'ru': 'Руководство', 'en': 'Leadership team'},
    'Fan olimpiadalari': {'ru': 'Предметные олимпиады', 'en': 'Subject Olympiads'},
    'Bog\'lanish': {'ru': 'Контакты', 'en': 'Contact'},
    "Barcha huquqlar himoyalangan.": {'ru': 'Все права защищены.', 'en': 'All rights reserved.'},
    "O'quvchilar Soni": {'ru': 'Количество учеников', 'en': 'Number of students'},
    "Malakali O'qituvchilar": {'ru': 'Квалифицированные преподаватели', 'en': 'Qualified teachers'},
    'Zamonaviy Laboratoriyalar': {'ru': 'Современные лаборатории', 'en': 'Modern laboratories'},
    "Litseyimizdagi eng so'nggi yangilik va voqealar bilan tanishing": {'ru': 'Последние новости и события нашего лицея', 'en': 'The latest news and events from our lyceum'},
    'Barcha yangiliklar &rarr;': {'ru': 'Все новости &rarr;', 'en': 'All news &rarr;'},
    "Batafsil o'qish &rarr;": {'ru': 'Читать далее &rarr;', 'en': 'Read more &rarr;'},
    'Hozircha yangiliklar joylanmagan.': {'ru': 'Пока новостей нет.', 'en': 'No news has been published yet.'},
    'Litsey Rahbariyati': {'ru': 'Руководство лицея', 'en': 'Lyceum leadership'},
    'Kafedralar va O\'quv Yo\'nalishlari': {'ru': 'Кафедры и учебные направления', 'en': 'Departments and academic programs'},
    'Fan Olimpiadalari va Musobaqalar': {'ru': 'Предметные олимпиады и соревнования', 'en': 'Subject Olympiads and competitions'},
    'O\'zbekiston Respublikasi Davlat Ramzlari': {'ru': 'Государственные символы Республики Узбекистан', 'en': 'State symbols of the Republic of Uzbekistan'},
    'Ramzlar menyusi': {'ru': 'Меню символов', 'en': 'Symbols menu'},
    'Ma\'lumot topilmadi.': {'ru': 'Информация не найдена.', 'en': 'Information not found.'},
    'Qidirish': {'ru': 'Поиск', 'en': 'Search'},
    'Barchasi': {'ru': 'Все', 'en': 'All'},
    'Qidirish...': {'ru': 'Поиск...', 'en': 'Search...'},
    "Sizning so'rovingiz bo'yicha hech qanday yangilik topilmadi.": {'ru': 'По вашему запросу ничего не найдено.', 'en': 'No news matched your search.'},
    "Shuningdek o'qing": {'ru': 'Читайте также', 'en': 'Related stories'},
    "Biz Bilan Bog'lanish": {'ru': 'Свяжитесь с нами', 'en': 'Contact us'},
    "Savol, taklif yoki murojaatlaringiz bo'lsa bizga xabar qoldiring": {'ru': 'Оставьте нам сообщение, если у вас есть вопрос, предложение или обращение', 'en': 'Send us a message if you have a question, suggestion, or request'},
    "Aloqa Ma'lumotlari": {'ru': 'Контактная информация', 'en': 'Contact information'},
    'Manzil': {'ru': 'Адрес', 'en': 'Address'},
    'Telefon raqamlar': {'ru': 'Телефоны', 'en': 'Phone numbers'},
    'Elektron Pochta': {'ru': 'Электронная почта', 'en': 'Email'},
    'Ish tartibi': {'ru': 'График работы', 'en': 'Working hours'},
    'Murojaat Yuborish': {'ru': 'Отправить обращение', 'en': 'Send a message'},
    'Ismingiz *': {'ru': 'Ваше имя *', 'en': 'Your name *'},
    'Ism va familiyangiz': {'ru': 'Имя и фамилия', 'en': 'First and last name'},
    'Telefon raqam *': {'ru': 'Номер телефона *', 'en': 'Phone number *'},
    'E-pochta (ixtiyoriy)': {'ru': 'Электронная почта (необязательно)', 'en': 'Email (optional)'},
    'Mavzu': {'ru': 'Тема', 'en': 'Subject'},
    'Murojaat mavzusi': {'ru': 'Тема обращения', 'en': 'Message subject'},
    'Xabar matni *': {'ru': 'Текст сообщения *', 'en': 'Message *'},
    'Xabaringizni shu yerga yozing...': {'ru': 'Напишите сообщение здесь...', 'en': 'Write your message here...'},
    'Xabarni Yuborish &rarr;': {'ru': 'Отправить сообщение &rarr;', 'en': 'Send message &rarr;'},
    'Qabul muddati': {'ru': 'Сроки приёма', 'en': 'Admission period'},
    'Umumiy kvota': {'ru': 'Общая квота', 'en': 'Total quota'},
    'Imtihon shakli': {'ru': 'Формат экзамена', 'en': 'Exam format'},
    'Talabgor': {'ru': 'Кандидаты', 'en': 'Applicants'},
    'Qabul 2025-2026': {'ru': 'Приём 2025-2026', 'en': 'Admissions 2025-2026'},
    'Ta\'lim yo\'nalishlari': {'ru': 'Направления обучения', 'en': 'Study programs'},
    'Kerakli hujjatlar ro\'yxati': {'ru': 'Список необходимых документов', 'en': 'Required documents'},
    'Qabul komissiyasi': {'ru': 'Приёмная комиссия', 'en': 'Admissions office'},
    'Savollaringiz bo\'lsa, biz bilan bog\'laning:': {'ru': 'Если у вас есть вопросы, свяжитесь с нами:', 'en': 'Contact us if you have any questions:'},
    'Qabul bosqichlari': {'ru': 'Этапы приёма', 'en': 'Admission steps'},
    'Hujjat topshirish': {'ru': 'Подача документов', 'en': 'Submit documents'},
    'Natijalar e\'lon qilinishi': {'ru': 'Объявление результатов', 'en': 'Results announcement'},
    'Fan olimpiadalari e\'lonlari va natijalari': {'ru': 'Объявления и результаты предметных олимпиад', 'en': 'Subject Olympiad announcements and results'},
    'Natijalar faylini yuklab olish (PDF)': {'ru': 'Скачать файл с результатами (PDF)', 'en': 'Download results (PDF)'},
    'Hozirda faol fan olimpiadalari e\'lon qilinmagan.': {'ru': 'Активные предметные олимпиады пока не объявлены.', 'en': 'There are no active Olympiad announcements yet.'},
}


@register.simple_tag(takes_context=True)
def localized(context, instance, field_name):
    language_code = context['request'].LANGUAGE_CODE
    if language_code in {'ru', 'en'}:
        translated_value = getattr(instance, f'{field_name}_{language_code}', '')
        if translated_value:
            return translated_value
    return getattr(instance, field_name, '')


@register.simple_tag(takes_context=True)
def ui(context, text):
    language_code = context['request'].LANGUAGE_CODE
    return UI_TRANSLATIONS.get(text, {}).get(language_code, text)
