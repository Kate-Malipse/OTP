import allure
import pytest
import time
import requests
from page.mainPage import MainPage


# helper
def print_dictionary(dictionary: dict) -> str:
    rows = ""
    for (key, value) in dictionary.items():
        rows += f"{key}: {value}\n"

    return rows


class TestsMainPage:

    @allure.title("Check footer title")
    def test_page_footer_title(self, driver):
        main_page = MainPage(driver)
        with allure.step("open main page"):
            main_page.go_to_main_page()

        with allure.step("verify footer title"):
            assert main_page.footer_title() == 'Официальный портал Мэра и Правительства Москвы'

    @allure.title("Check that page links return 200")
    def test_link_request_return_200(self, driver):
        failed_requests = dict()
        main_page = MainPage(driver)

        with allure.step("open main page"):
            main_page.go_to_main_page()

        with allure.step("create link list"):
            link_list = main_page.find_all_links()

        with allure.step("check that request to all links on a page return 200"):
            for link in link_list:
                r = requests.get(link, timeout=5)
                if r.status_code != 200:
                    failed_requests[link] = r.status_code
            assert bool(failed_requests) is False, f'Failed requests:\n{print_dictionary(failed_requests)}'

    @allure.title("Check the address bar after following the link")
    def test_links_follow_to_correct_url(self, driver):
        incorrect_urls = dict()
        main_page = MainPage(driver)

        with allure.step("open main page"):
            main_page.go_to_main_page()

        with allure.step("create link list"):
            link_list = main_page.find_all_links()

        with allure.step("check current url after following the link"):
            for link in link_list:
                main_page.follow_the_link(link)
                if link != driver.current_url:
                    incorrect_urls[link] = driver.current_url
            assert bool(incorrect_urls) is False, f'Incorrect following:\n{print_dictionary(incorrect_urls)}'
