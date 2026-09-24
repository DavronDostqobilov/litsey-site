from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import (
    Banner, NewsCategory, News, Leadership, Department,
    StateSymbol, AdmissionInfo, Olympiad
)

class Command(BaseCommand):
    help = "Seeds default data for SamDAQI Academic Lyceum site"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # 1. Superuser creation
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@litsey.uz', 'admin123')
            self.stdout.write(self.style.SUCCESS("Superuser created: username='admin', password='admin123'"))

        # 2. Hero Banner
        if not Banner.objects.exists():
            Banner.objects.create(
                title="MIRZO ULUGBEK NOMIDAGI SAMARQAND DAVLAT ARXITEKTURA-QURILISH UNIVERSITETI AKADEMIK LITSEYI",
                subtitle="Zamonaviy bilimlar va nufuzli ta'lim maskani",
                image="hero_architectural.jpg",
                order=1,
                is_active=True
            )
            self.stdout.write(self.style.SUCCESS("Banner created."))

        # 3. News Categories
        cat_education, _ = NewsCategory.objects.get_or_create(name="Ta'lim va Fan", slug="talim-va-fan")
        cat_events, _ = NewsCategory.objects.get_or_create(name="Tadbirlar", slug="tadbirlar")
        cat_sports, _ = NewsCategory.objects.get_or_create(name="Sport va Madaniyat", slug="sport-va-madaniyat")

        # 4. News Articles
        if not News.objects.exists():
            News.objects.create(
                title="2025-2026 o'quv yili uchun qabul jarayonlari boshlandi",
                slug="2025-2026-oquv-yili-qabul-jarayonlari",
                category=cat_education,
                image="lyceum_building.jpg",
                summary="Mirzo Ulug'bek nomidagi Samarqand Davlat Arxitektura-Qurilish Universiteti Akademik Litseyiga 9-sinf bitiruvchilaridan arizalar qabul qilinmoqda.",
                content="SamDAQI Akademik Litseyiga 2025-2026 o'quv yili uchun qabul jarayonlari rasman start oldi. Abituriyentlar online shaklda va litsey qabul komissiyasi orqali hujjat topshirishlari mumkin. Akademik litseyda Aniq fanlar (Texnika va Iqtisod) hamda Xorijiy filologiya yo'nalishlari bo'yicha chuqurlashtirilgan mashg'ulotlar olib boriladi.",
                is_featured=True,
                views_count=142
            )

            News.objects.create(
                title="Litsey o'quvchilari respublika fan olimpiadasida faxrli o'rinlarni egallashdi",
                slug="respublika-fan-olimpiadasi-yutuqlari",
                category=cat_events,
                image="hero_architectural.jpg",
                summary="Matematika va fizika fanlari bo'yicha o'tkazilgan respublika olimpiadasida litseyimiz o'quvchilari oltin va kumush medallarga sazovor bo'lishdi.",
                content="Joriy yilda o'tkazilgan Respublika fan olimpiadasining yakuniy bosqichida Samarqand Davlat Arxitektura-Qurilish Universiteti Akademik Litseyi 2-bosqich o'quvchilari yuqori natijalarni ko'rsatishdi. G'oliblarga oliy o'quv yurtlariga imtiyozli kirish sertifikatlari topshirildi.",
                is_featured=True,
                views_count=98
            )

            News.objects.create(
                title="Arxitektura va loyihalash laboratoriyasiga yangi zamonaviy uskunalar keltirildi",
                slug="arxitektura-laboratoriyasi-yangilandi",
                category=cat_education,
                image="hero_architectural.jpg",
                summary="3D modellashtirish va grafik dizayn mashg'ulotlari uchun mo'ljallangan yangi kompyuter laboratoriyasi foydalanishga topshirildi.",
                content="Litseyimizda iqtidorli yoshlarni qo'llab-quvvatlash va zamonaviy arxitektura asoslarini amalda o'rgatish maqsadida eng so'nggi rusumdagi grafik stansiyalar va 3D printerlar bilan jihozlangan laboratoriya tashkil etildi.",
                is_featured=False,
                views_count=75
            )
            self.stdout.write(self.style.SUCCESS("News articles created."))

        # 5. Leadership
        if not Leadership.objects.exists():
            Leadership.objects.create(
                full_name="Prof. Ergashev Nodirbek Rahmonovich",
                position="Litsey Direktori",
                degree="Texnika fanlari nomzodi, Dotsent",
                phone="+998 66 237-12-34",
                email="director@samdaqi-litsey.uz",
                reception_hours="Dushanba - Chorshanba (14:00 - 17:00)",
                bio="Ko'p yillik ta'lim va ilmiy-pedagogik tajribaga ega mutaxassis.",
                order=1
            )
            Leadership.objects.create(
                full_name="Karimov Jamshid Boburovich",
                position="O'quv ishlari bo'yicha direktor o'rinbosari",
                degree="Pedagogika fanlari bo'yicha falsafa doktori (PhD)",
                phone="+998 66 237-12-35",
                email="oquv@samdaqi-litsey.uz",
                reception_hours="Seshanba - Juma (10:00 - 13:00)",
                bio="O'quv rejalari va innovatsion pedagogik texnologiyalarni joriy etishga mas'ul.",
                order=2
            )
            Leadership.objects.create(
                full_name="Tursunova Nilufar Akbarovna",
                position="Ma'naviyat va ma'rifat ishlari bo'yicha o'rinbosar",
                degree="Katta o'qituvchi",
                phone="+998 66 237-12-36",
                email="manaviyat@samdaqi-litsey.uz",
                reception_hours="Dushanba - Payshanba (09:00 - 12:00)",
                bio="Ma'naviy-ma'rifiy va tarbiyaviy ishlarni tashkil etadi.",
                order=3
            )
            self.stdout.write(self.style.SUCCESS("Leadership seeded."))

        # 6. Departments
        if not Department.objects.exists():
            Department.objects.create(
                name="Aniq Fanlar (Texnika)",
                code="310001",
                description="Matematika, Fizika va Informatika fanlari chuqurlashtirilgan holda o'qitiladi. Arxitektura va muhandislik yo'nalishlariga tayyorlaydi.",
                head_name="Ismoilov Temur Malikovich"
            )
            Department.objects.create(
                name="Aniq Fanlar (Iqtisod)",
                code="310002",
                description="Matematika, Ingliz tili va Ona tili yo'nalishi bo'yicha tayyorgarlik ko'riladi.",
                head_name="Sharipova Malika Rustamovna"
            )
            Department.objects.create(
                name="Xorijiy Filologiya",
                code="320001",
                description="Ingliz, Nemis va Fransuz tillari hamda jahon adabiyoti chuqurlashtirib o'rgatiladi.",
                head_name="Jonibekov Shavkat Hamidovich"
            )
            self.stdout.write(self.style.SUCCESS("Departments seeded."))

        # 7. State Symbols
        if not StateSymbol.objects.exists():
            StateSymbol.objects.create(
                symbol_type="flag",
                title="O'zbekiston Respublikasi Davlat Bayrog'i",
                description="O'zbekiston Respublikasi Davlat bayrog'i 1991-yil 18-noyabrda qabul qilingan.",
                content="O'zbekiston Respublikasining Davlat bayrog'i O'zbekiston Respublikasi davlat suverenitetining ramzidir. Bayroqdagi moviy rang — musaffo osmon va obihayot ramzi. Oq rang — tinchlik va poklik timsoli. Yashil rang — tabiatning yangilanishi va serhosillik ramzi. Qizil chiziqlar — har bir tirik jonzotning tomirida jo'sh urayotgan hayotiy kuchdir."
            )
            StateSymbol.objects.create(
                symbol_type="emblem",
                title="O'zbekiston Respublikasi Davlat Gerbi",
                description="O'zbekiston Respublikasi Davlat gerbi 1992-yil 2-iyulda qabul qilingan.",
                content="O'zbekiston Respublikasi Davlat gerbi tasvirida: tog'lar, daryolar va so'l tomoni bug'doy boshoqlaridan, o'ng tomoni esa chanoqlari ochilgan paxta shoxlaridan iborat chambarakka o'ralgan cheksiz quyosh nurlari sochib turgan musaffo osmon aks etgan."
            )
            StateSymbol.objects.create(
                symbol_type="anthem",
                title="O'zbekiston Respublikasi Davlat Madhiyasi",
                description="O'zbekiston Respublikasi Davlat madhiyasi 1992-yil 10-dekabrda qabul qilingan. She'ri: Abdulla Oripov, Musiqasi: Mutal Burhonov.",
                content="Serquyosh hurlk o'lkam, elga baht, najot,\nSen o'zing do'stlarga yo'ldosh, mehribon!\nYashnagay to abad ilmu fan, ijod,\nShuhrating porlasin toki bor jahon!\n\nNaqorat:\nOltin bu vodiylar — jon O'zbekiston,\nAjdodlar mardona ruhi senga yor!\nUlug' el qudrati jo'sh urgan zamon,\nOlamni mahliyo aylagan diyor!"
            )
            StateSymbol.objects.create(
                symbol_type="constitution",
                title="O'zbekiston Respublikasi Konstitutsiyasi",
                description="O'zbekiston Respublikasi Konstitutsiyasi (Yangi tahrirdagi Konstitutsiya 2023-yil 30-aprelda umumxalq referendumi orqali qabul qilingan).",
                content="Konstitutsiya inson va fuqaroning huquq hamda erkinliklarini, davlat tuzilishi va hokimiyat organlari tizimini belgilovchi oliy yuridik kuchga ega davlat qonunidir."
            )
            self.stdout.write(self.style.SUCCESS("State symbols seeded."))

        # 8. Admission Info
        if not AdmissionInfo.objects.exists():
            AdmissionInfo.objects.create(
                academic_year="2025-2026",
                title="2025-2026 o'quv yili uchun abituriyentlarni qabul qilish tartibi",
                content="Akademik litseyga hujjatlar qabul qilish 2025-yil 10-iyundan 10-julgacha davom etadi. Qabul imtihonlari 2 bosqichda: yozma ish va DTM test sinovlari shaklida o'tkaziladi.",
                quota_info="Jami qabul kvotasi: 240 ta o'rin. Aniq fanlar (Texnika): 120 ta, Aniq fanlar (Iqtisod): 60 ta, Xorijiy filologiya: 60 ta."
            )
            self.stdout.write(self.style.SUCCESS("Admission info seeded."))

        # 9. Olympiad
        if not Olympiad.objects.exists():
            Olympiad.objects.create(
                title="Matematika va Geometriya Fanidan Litsey Ochiq Olimpiadasi",
                subject="Matematika",
                event_date="2025-10-15",
                description="Umumta'lim maktablarining 9-sinf o'quvchilari o'rtasida o'tkaziladigan viloyat ochiq olimpiadasi.",
                is_active=True
            )
            self.stdout.write(self.style.SUCCESS("Olympiad seeded."))

        self.stdout.write(self.style.SUCCESS("Data seeding completed successfully!"))
