from django.db import models
from django.utils.text import slugify

class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Kichik sarlavha")
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
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
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
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategoriya")
    image = models.ImageField(upload_to='news/', verbose_name="Muqova rasmi")
    summary = models.TextField(verbose_name="Qisqacha mazmun")
    content = models.TextField(verbose_name="To'liq matn")
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
    position = models.CharField(max_length=150, verbose_name="Lavozimi")
    degree = models.CharField(max_length=150, blank=True, verbose_name="Ilmiy darajasi/Unvoni")
    photo = models.ImageField(upload_to='leadership/', verbose_name="Fotosurat")
    phone = models.CharField(max_length=50, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="E-pochta")
    reception_hours = models.CharField(max_length=150, verbose_name="Qabul kunlari")
    bio = models.TextField(blank=True, verbose_name="Tarjimai hol / Ma'lumot")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Rahbariyat a'zosi"
        verbose_name_plural = "Rahbariyat"
        ordering = ['order', 'full_name']

    def __str__(self):
        return f"{self.full_name} ({self.position})"


class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name="Kafedra / Yo'nalish nomi")
    code = models.CharField(max_length=50, blank=True, verbose_name="Kodi / Yo'nalishi")
    description = models.TextField(verbose_name="Tavsifi")
    image = models.ImageField(upload_to='departments/', blank=True, null=True, verbose_name="Rasm")
    head_name = models.CharField(max_length=150, blank=True, verbose_name="Kafedra mudiri")

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
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Qisqacha ta'rif")
    content = models.TextField(verbose_name="Batafsil matn / Qonun/Madhiya matni")
    image = models.ImageField(upload_to='symbols/', blank=True, null=True, verbose_name="Tasvir")

    class Meta:
        verbose_name = "Davlat ramzi"
        verbose_name_plural = "Davlat ramzlari"

    def __str__(self):
        return self.title


class AdmissionInfo(models.Model):
    academic_year = models.CharField(max_length=20, default="2025-2026", verbose_name="O'quv yili")
    title = models.CharField(max_length=255, verbose_name="Qabul sarlavhasi")
    content = models.TextField(verbose_name="Qabul nizam va shartlari")
    document_file = models.FileField(upload_to='admissions/', blank=True, null=True, verbose_name="Nizom fayli (PDF)")
    quota_info = models.TextField(blank=True, verbose_name="Kvotalar haqida ma'lumot")
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
    title = models.CharField(max_length=255, verbose_name="Olimpiada nomi")
    subject = models.CharField(max_length=100, verbose_name="Fan")
    event_date = models.DateField(verbose_name="O'tkazilish sanasi")
    description = models.TextField(verbose_name="Tavsifi va nizomi")
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
