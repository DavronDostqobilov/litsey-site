from django.template import Context, Template
from django.conf import settings
from django.test import RequestFactory, SimpleTestCase, TestCase
from django.urls import reverse

from .models import Banner


class LocalizedContentTests(SimpleTestCase):
	def setUp(self):
		self.request = RequestFactory().get('/')

	def render_title(self, language_code, **values):
		self.request.LANGUAGE_CODE = language_code
		banner = Banner(title='Uzbek title', **values)
		template = Template("{% load language_tags %}{% localized banner 'title' %}")
		return template.render(Context({'request': self.request, 'banner': banner}))

	def test_uses_selected_translation(self):
		self.assertEqual(self.render_title('ru', title_ru='Русский заголовок'), 'Русский заголовок')

	def test_falls_back_to_uzbek_when_translation_is_empty(self):
		self.assertEqual(self.render_title('en', title_en=''), 'Uzbek title')


class SiteLanguageTests(TestCase):
	def test_main_pages_render_in_all_supported_languages(self):
		paths = [
			'/', '/yangiliklar/', '/rahbariyat/', '/kafedralar/',
			'/davlat-ramzlari/', '/fan-olimpiadalari/',
			'/qabul-2025-2026/', '/litsey-tarixi-va-nizomi/', '/boglanish/',
		]
		for language_code in ('uz', 'ru', 'en'):
			self.client.cookies[settings.LANGUAGE_COOKIE_NAME] = language_code
			for path in paths:
				with self.subTest(language=language_code, path=path):
					self.assertEqual(self.client.get(path).status_code, 200)

	def test_language_switch_translates_navigation(self):
		response = self.client.post(reverse('set_language'), {'language': 'ru', 'next': '/'})
		self.assertEqual(response.status_code, 302)
		self.assertContains(self.client.get('/'), 'Главная')
