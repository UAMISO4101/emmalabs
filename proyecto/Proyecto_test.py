# coding=utf-8
from unittest import TestCase
from selenium import webdriver

class ProyectoTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000/proyectos')
        self.assertIn('Proyectos', self.browser.title)