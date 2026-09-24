from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import (
    Banner, NewsCategory, News, Leadership, Department,
    StateSymbol, AdmissionInfo, AdmissionApplication, Olympiad, ContactMessage
)

def home_view(request):
    banners = Banner.objects.filter(is_active=True)
    featured_news = News.objects.filter(is_featured=True)[:3]
    latest_news = News.objects.all()[:6]
    leadership_members = Leadership.objects.all()[:4]
    departments = Department.objects.all()
    active_olympiads = Olympiad.objects.filter(is_active=True)[:3]
    admission_info = AdmissionInfo.objects.filter(is_active=True).first()

    context = {
        'banners': banners,
        'featured_news': featured_news,
        'latest_news': latest_news,
        'leadership_members': leadership_members,
        'departments': departments,
        'active_olympiads': active_olympiads,
        'admission_info': admission_info,
    }
    return render(request, 'index.html', context)


def news_list_view(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')

    news_qs = News.objects.all()

    if category_slug:
        news_qs = news_qs.filter(category__slug=category_slug)

    if query:
        news_qs = news_qs.filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query) |
            Q(content__icontains=query)
        )

    categories = NewsCategory.objects.all()

    context = {
        'news_list': news_qs,
        'categories': categories,
        'selected_category': category_slug,
        'search_query': query,
    }
    return render(request, 'news_list.html', context)


def news_detail_view(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    # Increment views count
    news_item.views_count += 1
    news_item.save(update_fields=['views_count'])

    related_news = News.objects.exclude(id=news_item.id)[:4]

    context = {
        'news': news_item,
        'related_news': related_news,
    }
    return render(request, 'news_detail.html', context)


def leadership_view(request):
    members = Leadership.objects.all()
    return render(request, 'leadership.html', {'members': members})


def departments_view(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})


def state_symbols_view(request, symbol_type=None):
    symbols = StateSymbol.objects.all()
    selected_symbol = None
    if symbol_type:
        selected_symbol = StateSymbol.objects.filter(symbol_type=symbol_type).first()
    if not selected_symbol and symbols.exists():
        selected_symbol = symbols.first()

    context = {
        'symbols': symbols,
        'selected_symbol': selected_symbol,
    }
    return render(request, 'state_symbols.html', context)


def admission_view(request):
    """Litsey tarixi va Ustav sahifasi"""
    return render(request, 'admission.html')


def qabul_view(request):
    """Qabul 2025-2026 ma'lumotlari sahifasi"""
    admission_info = AdmissionInfo.objects.filter(is_active=True).first()
    context = {
        'admission_info': admission_info,
    }
    return render(request, 'qabul.html', context)


def olympiad_view(request):
    olympiads = Olympiad.objects.all()
    return render(request, 'olympiad.html', {'olympiads': olympiads})


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and phone and message:
            ContactMessage.objects.create(
                name=name,
                phone=phone,
                email=email,
                subject=subject or 'Sayt orqali murojaat',
                message=message,
            )
            messages.success(request, "Murojaatingiz yuborildi. Rahmat!")
            return redirect('contact')

    return render(request, 'contact.html')
