import os
import json
import requests as req
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Travel:

    def search_aviatickets(self):
        pass

    def search_hostels(self):
        pass

    def get_iata(self, first_city, second_city):
        a = 5
        link = f'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{a}%20в%20{a}'

    def create_pdf(self):
        pass

    def save_to_database(self):
        pass