from selenium.webdriver.common.by import By
from base.Base import BasePage
import allure


class Locators:
    FOOTER_TITLE = (By.CLASS_NAME, 'Footer_title__1d0CK')


class MainPage(BasePage):

    @allure.step("find text inside footer title element")
    def footer_title(self) -> str:
        footer = self.find_element(Locators.FOOTER_TITLE)
        return footer.text

    @allure.step("find all links on a page")
    def find_all_links(self) -> set[str]:
        link_list = set()

        with allure.step("find all 'a' html tag"):
            links = self.driver.find_elements_by_tag_name('a')

        with allure.step("find 'href' attribute for links and remove links with '#'"):
            for link in links:
                href = link.get_attribute('href')
                if href.find('#') == -1:
                    link_list.add(href)
        return link_list

    @allure.step("follow the link")
    def follow_the_link(self, link: str):
        self.driver.get(link)
