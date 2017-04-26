
from __future__ import absolute_import

import os
from unittest import TestCase

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1024, 768)
        self.browser.implicitly_wait(5000)

    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Emma Labs', self.browser.title)

    def test_2_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()


        login_usuario = self.browser.find_element_by_id('id_username_login')
        login_usuario.send_keys('santiago')

        login_clave = self.browser.find_element_by_id('id_password_login')
        login_clave.send_keys('g0d1n3s25')

        botonIngresar = self.browser.find_element_by_id('btn_login')
        botonIngresar.click()

        botonSesion = self.browser.find_element_by_id('sesion')
        botonSesion.click()

        label_usuario = self.browser.find_element_by_id('user')
        self.assertIn('USUARIO: SANTIAGO', label_usuario.text)

    def test_3_perfil_cientifico(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()


        login_usuario = self.browser.find_element_by_id('id_username_login')
        login_usuario.send_keys('cientifico')

        login_clave = self.browser.find_element_by_id('id_password_login')
        login_clave.send_keys('1a2s3d4f5g')

        botonIngresar = self.browser.find_element_by_id('btn_login')
        botonIngresar.click()

        botonSesion = self.browser.find_element_by_id('sesion')
        botonSesion.click()

        label_usuario = self.browser.find_element_by_id('user')
        self.assertIn('USUARIO: CIENTIFICO', label_usuario.text)