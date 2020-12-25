import os
import json
import requests as req
import time
from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.firefox.options import *
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class Travel:
    tickets = []
    hotels = []

    def __init__(self, origin, destination, or_date, des_date):
        self.origin = origin
        self.destination = destination
        self.or_date = or_date
        self.des_date = des_date

    def search_aviatickets(self):
        origin_iata, destination_iata = self.__get_iata()
        origin_date = self.__refactor_date(self.or_date)
        destination_date = self.__refactor_date(self.des_date)
        print(f'{origin_date}, {destination_date}')
        link = f'https://www.aviasales.ru/search/{origin_iata}{origin_date}{destination_iata}{destination_date}1'
        opts = Options()
        opts.set_headless()
        assert opts.headless
        browser = webdriver.Firefox(options=opts)
        browser.get(link)
        try:
            WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.CLASS_NAME, "show-more-products")))
        except Exception as e:
            print(e)
            browser.close()
        # btn = browser.find_element_by_class_name("show-more-products")
        # try:
        #     btn = btn.find_element_by_tag_name("button")
        #     ActionChains(browser).move_to_element(btn).click()
        # except Exception as e:
        #     print(e)
        time.sleep(5)
        data = self.__parse_tickets(browser.find_elements_by_class_name("ticket-desktop"))
        browser.close()
        self.tickets = data

    def search_hostels(self):
        self.hotels = [{"inf": "Отель найден"}]

    def __parse_tickets(self, parent):
        data = []
        times = []
        cmpies = ""
        str_date = ""
        for el in parent:
            company = el.find_elements_by_class_name("ticket-carrier__img")
            origin_time = el.find_elements_by_css_selector(".segment-route__time")
            date = el.find_elements_by_css_selector(".segment-route__date")
            buy_button = el.find_element_by_class_name("buy-button__price").text.replace("\u2009", "").replace("₽", " руб.")
            link = el.find_element_by_class_name("buy-button__button").get_attribute("href")
            for clck in origin_time:
                times.append(clck.text)
            for i, d in enumerate(date):
                str_date += times[i] + " " + d.text + "/"
            str_date = str_date.split("/")
            for cmp in company:
                cmpies += cmp.get_attribute("alt") + "/"
            data.append({"price": buy_button, "fromOrigin": {"originTime": str_date[0], "destinationTime": str_date[1]},
                         "company": cmpies, "fromDestination": {"originTime": str_date[2], "destinationTime": str_date[3]},
                         "link": link})
            times = []
            cmpies = ""
            str_date = ""
        return data

    def __get_iata(self):
        link = f'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{self.origin}%20в%20{self.destination}'
        response = req.get(link).json()
        try:
            origin_iata = response["origin"]["iata"]
            destination_iata = response["destination"]["iata"]
            return (origin_iata, destination_iata)
        except Exception as e:
            print(f"Произошла ошибка.\n{e}")

    def __refactor_date(self, date):
        result = str(date).split("-")
        print(result)
        return f'{result[2]}{result[1]}'

    def __create_pdf(self):
        pass

    def __save_to_database(self):
        pass
