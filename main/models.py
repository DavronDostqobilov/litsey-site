from django.db import models
from django.utils.text import slugify

class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha (O'zbekcha)")
    title_ru = models.CharField(max_length=255, default="", verbose_name="Sarlavha (Ruscha)")
    title_en = models.CharField(max_length=255, default="", verbose_name="Sarlavha (Inglizcha)")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Kichik sarlavha (O'zbekcha)")
    subtitle_ru = models.CharField(max_length=255, blank=True, default="", verbose_name="Kichik sarlavha (Ruscha)")
    subtitle_en = models.CharField(max_length=255, blank=True, default="", verbose_name="Kichik sarlavha (Inglizcha)")
    image = models.ImageField(upload_to='banners/', verbose_name="Rasm")
    link = models.CharField(max_length=255, blank=True, verbose_name="Havola (ixtiyoriy)")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class NewsCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi (O'zbekcha)")
    name_ru = models.CharField(max_length=100, default="", verbose_name="Kategoriya nomi (Ruscha)")
    name_en = models.CharField(max_length=100, default="", verbose_name="Kategoriya nomi (Inglizcha)")
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Yangilik kategoriyasi"
        verbose_name_plural = "Yangilik kategoriyalari"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha (O'zbekcha)")
    title_ru = models.CharField(max_length=255, default="", verbose_name="Sarlavha (Ruscha)")
    title_en = models.CharField(max_length=255, default="", verbose_name="Sarlavha (Inglizcha)")
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategoriya")
    image = models.ImageField(upload_to='news/', verbose_name="Muqova rasmi")
    summary = models.TextField(verbose_name="Qisqacha mazmun (O'zbekcha)")
    summary_ru = models.TextField(default="", verbose_name="Qisqacha mazmun (Ruscha)")
    summary_en = models.TextField(default="", verbose_name="Qisqacha mazmun (Inglizcha)")
    content = models.TextField(verbose_name="To'liq matn (O'zbekcha)")
    content_ru = models.TextField(default="", verbose_name="To'liq matn (Ruscha)")
    content_en = models.TextField(default="", verbose_name="To'liq matn (Inglizcha)")
    is_featured = models.BooleanField(default=False, verbose_name="Muhim (Asosiy sahifada)")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar va E'lonlar"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Leadership(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="F.I.SH.")
    position = models.CharField(max_length=150, verbose_name="Lavozimi (O'zbekcha)")
    position_ru = models.CharField(max_length=150, default="", verbose_name="Lavozimi (Ruscha)")
    position_en = models.CharField(max_length=150, default="", verbose_name="Lavozimi (Inglizcha)")
    degree = models.CharField(max_length=150, blank=True, verbose_name="Ilmiy darajasi/Unvoni (O'zbekcha)")
    degree_ru = models.CharField(max_length=150, blank=True, default="", verbose_name="Ilmiy darajasi/Unvoni (Ruscha)")
    degree_en = models.CharField(max_length=150, blank=True, default="", verbose_name="Ilmiy darajasi/Unvoni (Inglizcha)")
    photo = models.ImageField(upload_to='leadership/', verbose_name="Fotosurat")
    phone = models.CharField(max_length=50, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="E-pochta")
    reception_hours = models.CharField(max_length=150, verbose_name="Qabul kunlari (O'zbekcha)")
    reception_hours_ru = models.CharField(max_length=150, default="", verbose_name="Qabul kunlari (Ruscha)")
    reception_hours_en = models.CharField(max_length=150, default="", verbose_name="Qabul kunlari (Inglizcha)")
    bio = models.TextField(blank=True, verbose_name="Tarjimai hol / Ma'lumot (O'zbekcha)")
    bio_ru = models.TextField(blank=True, default="", verbose_name="Tarjimai hol / Ma'lumot (Ruscha)")
    bio_en = models.TextField(blank=True, default="", verbose_name="Tarjimai hol / Ma'lumot (Inglizcha)")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Rahbariyat a'zosi"
        verbose_name_plural = "Rahbariyat"
        ordering = ['order', 'full_name']

    def __str__(self):
        return f"{self.full_name} ({self.position})"


class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name="Kafedra / Yo'nalish nomi (O'zbekcha)")
    name_ru = models.CharField(max_length=150, default="", verbose_name="Kafedra / Yo'nalish nomi (Ruscha)")
    name_en = models.CharField(max_length=150, default="", verbose_name="Kafedra / Yo'nalish nomi (Inglizcha)")
    code = models.CharField(max_length=50, blank=True, verbose_name="Kodi / Yo'nalishi")
    description = models.TextField(verbose_name="Tavsifi (O'zbekcha)")
    description_ru = models.TextField(default="", verbose_name="Tavsifi (Ruscha)")
    description_en = models.TextField(default="", verbose_name="Tavsifi (Inglizcha)")
    image = models.ImageField(upload_to='departments/', blank=True, null=True, verbose_name="Rasm")
    head_name = models.CharField(max_length=150, blank=True, verbose_name="Kafedra mudiri (O'zbekcha)")
    head_name_ru = models.CharField(max_length=150, blank=True, default="", verbose_name="Kafedra mudiri (Ruscha)")
    head_name_en = models.CharField(max_length=150, blank=True, default="", verbose_name="Kafedra mudiri (Inglizcha)")

    class Meta:
        verbose_name = "Kafedra / Yo'nalish"
        verbose_name_plural = "Kafedralar va Yo'nalishlar"

    def __str__(self):
        return self.name


class StateSymbol(models.Model):
    SYMBOL_TYPES = [
        ('flag', 'O\'zbekiston Respublikasi Bayrog\'i'),
        ('emblem', 'O\'zbekiston Respublikasi Gerbi'),
        ('anthem', 'O\'zbekiston Respublikasi Madhiyasi'),
        ('constitution', 'O\'zbekiston Respublikasi Konstitutsiyasi'),
    ]

    symbol_type = models.CharField(max_length=20, choices=SYMBOL_TYPES, unique=True, verbose_name="Ramz turi")
    title = models.CharField(max_length=255, verbose_name="Sarlavha (O'zbekcha)")
    title_ru = models.CharField(max_length=255, default="", verbose_name="Sarlavha (Ruscha)")
    title_en = models.CharField(max_length=255, default="", verbose_name="Sarlavha (Inglizcha)")
    description = models.TextField(verbose_name="Qisqacha ta'rif (O'zbekcha)")
    description_ru = models.TextField(default="", verbose_name="Qisqacha ta'rif (Ruscha)")
    description_en = models.TextField(default="", verbose_name="Qisqacha ta'rif (Inglizcha)")
    content = models.TextField(verbose_name="Batafsil matn / Qonun/Madhiya matni (O'zbekcha)")
    content_ru = models.TextField(default="", verbose_name="Batafsil matn (Ruscha)")
    content_en = models.TextField(default="", verbose_name="Batafsil matn (Inglizcha)")
    image = models.ImageField(upload_to='symbols/', blank=True, null=True, verbose_name="Tasvir")

    class Meta:
        verbose_name = "Davlat ramzi"
        verbose_name_plural = "Davlat ramzlari"

    def __str__(self):
        return self.title


class AdmissionInfo(models.Model):
    academic_year = models.CharField(max_length=20, default="2025-2026", verbose_name="O'quv yili")
    title = models.CharField(max_length=255, verbose_name="Qabul sarlavhasi (O'zbekcha)")
    title_ru = models.CharField(max_length=255, default="", verbose_name="Qabul sarlavhasi (Ruscha)")
    title_en = models.CharField(max_length=255, default="", verbose_name="Qabul sarlavhasi (Inglizcha)")
    content = models.TextField(verbose_name="Qabul nizomi va shartlari (O'zbekcha)")
    content_ru = models.TextField(default="", verbose_name="Qabul shartlari (Ruscha)")
    content_en = models.TextField(default="", verbose_name="Qabul shartlari (Inglizcha)")
    document_file = models.FileField(upload_to='admissions/', blank=True, null=True, verbose_name="Nizom fayli (PDF)")
    quota_info = models.TextField(blank=True, verbose_name="Kvotalar haqida ma'lumot (O'zbekcha)")
    quota_info_ru = models.TextField(blank=True, default="", verbose_name="Kvotalar haqida ma'lumot (Ruscha)")
    quota_info_en = models.TextField(blank=True, default="", verbose_name="Kvotalar haqida ma'lumot (Inglizcha)")
    is_active = models.BooleanField(default=True, verbose_name="Qabul ochiq")

    class Meta:
        verbose_name = "Qabul ma'lumoti"
        verbose_name_plural = "Qabul 2025-2026 Ma'lumotlari"

    def __str__(self):
        return f"Qabul {self.academic_year}: {self.title}"


class AdmissionApplication(models.Model):
    DIRECTION_CHOICES = [
        ('aniq_texnika', 'Aniq fanlar - Texnika yo\'nalishi (Matematika, Fizika, Ingliz tili)'),
        ('aniq_iqtisod', 'Aniq fanlar - Iqtisod yo\'nalishi (Matematika, Ingliz tili, Ona tili)'),
        ('tabiiy_fanlar', 'Tabiiy fanlar yo\'nalishi (Kimyo, Biologiya, Ona tili)'),
        ('xorijiy_filologiya', 'Xorijiy filologiya yo\'nalishi (Ingliz tili, Ona tili, Tarix)'),
    ]

    STATUS_CHOICES = [
        ('yangi', 'Yangi'),
        ('korib_chiqilmoqda', 'Ko\'rib chiqilmoqda'),
        ('qabul_qilindi', 'Qabul qilindi'),
        ('rad_etildi', 'Rad etildi'),
    ]

    full_name = models.CharField(max_length=150, verbose_name="Abituriyent F.I.SH.")
    phone = models.CharField(max_length=30, verbose_name="Telefon raqami")
    birth_date = models.DateField(verbose_name="Tug'ilgan sanasi")
    direction = models.CharField(max_length=50, choices=DIRECTION_CHOICES, verbose_name="Tanlagan yo'nalishi")
    previous_school = models.CharField(max_length=200, verbose_name="Bitirgan maktabi (tuman/shahar)")
    address = models.CharField(max_length=255, verbose_name="Yashash manzili")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='yangi', verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Topshirilgan sana")

    class Meta:
        verbose_name = "Qabul arizasi"
        verbose_name_plural = "Qabul arizalari"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.get_direction_display()}"


class Olympiad(models.Model):
    title = models.CharField(max_length=255, verbose_name="Olimpiada nomi (O'zbekcha)")
    title_ru = models.CharField(max_length=255, default="", verbose_name="Olimpiada nomi (Ruscha)")
    title_en = models.CharField(max_length=255, default="", verbose_name="Olimpiada nomi (Inglizcha)")
    subject = models.CharField(max_length=100, verbose_name="Fan (O'zbekcha)")
    subject_ru = models.CharField(max_length=100, default="", verbose_name="Fan (Ruscha)")
    subject_en = models.CharField(max_length=100, default="", verbose_name="Fan (Inglizcha)")
    event_date = models.DateField(verbose_name="O'tkazilish sanasi")
    description = models.TextField(verbose_name="Tavsifi va nizomi (O'zbekcha)")
    description_ru = models.TextField(default="", verbose_name="Tavsifi va nizomi (Ruscha)")
    description_en = models.TextField(default="", verbose_name="Tavsifi va nizomi (Inglizcha)")
    results_file = models.FileField(upload_to='olympiads/', blank=True, null=True, verbose_name="Natijalar fayli (PDF/Excel)")
    is_active = models.BooleanField(default=True, verbose_name="E'londa")

    class Meta:
        verbose_name = "Fan olimpiadasi"
        verbose_name_plural = "Fan olimpiadalari"
        ordering = ['-event_date']

    def __str__(self):
        return f"{self.subject}: {self.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ismi")
    phone = models.CharField(max_length=30, verbose_name="Telefon raqami")
    email = models.EmailField(blank=True, verbose_name="E-pochta")
    subject = models.CharField(max_length=200, verbose_name="Mavzu")
    message = models.TextField(verbose_name="Xabar matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan sana")
    is_read = models.BooleanField(default=False, verbose_name="O'qildi")

    class Meta:
        verbose_name = "Murojaat"
        verbose_name_plural = "Fuqarolar murojaatlari"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
