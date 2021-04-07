from hashlib import sha256
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.chrome.options import Options


class Address(object):
    def __init__(self, pass_phrase, u_addy, c_addy, u_prk, c_prk, c_pbk, u_pbk):
        self.pass_phrase = pass_phrase
        self.u_addy = u_addy
        self.c_addy = c_addy
        self.c_prk = c_prk
        self.u_prk = u_prk
        self.c_pbk = c_pbk
        self.u_pbk = u_pbk
        self.status = None
        self.status2 = None

    def set_status(self, status):
        self.status = status

    def set_status2(self, status2):
        self.status2 = status2


def load_phrases():
    with open("phraselist.txt", "r") as f:
        phrases = f.read().splitlines()

    random.shuffle(phrases)  # Randomly shuffles phrase list

    # return phrases
    return phrases[0:10]  # Returns slice of 10 phrases


def save_objects(obj, filename):
    """
    :param obj: Address object list
    :param filename: Filename to save as
    :return: None
    """
    with open(filename, 'wb') as output:  # Saves address object list overwriting any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def wallet(elem, css_sel, phrases):
    addresses = list()

    elem.click()

    input_ = driver.find_element_by_css_selector(css_sel)

    for line in phrases:
        hashed_word = sha256(line.strip().encode('utf-8')).hexdigest()

        cursor = input_.is_enabled()

        if not cursor:
            continue

        actions = ActionChains(driver).move_to_element(input_)

        actions.send_keys(hashed_word)

        actions.send_keys(Keys.ENTER)

        actions.perform()

        add = driver.find_element_by_css_selector("#detailaddress.output").text
        add_comp = driver.find_element_by_css_selector("#detailaddresscomp.output").text

        pk = driver.find_element_by_css_selector("#detailprivwif").text
        pk_comp = driver.find_element_by_css_selector("#detailprivwifcomp").text

        pub_k = driver.find_element_by_css_selector("#detailpubkey.output.pubkeyhex").text
        comp_pub_k = driver.find_element_by_css_selector("span#detailpubkeycomp.output").text

        # actions.reset_actions()

        address = Address(line, add, add_comp, pk, pk_comp, comp_pub_k, pub_k)

        print()
        print(line)
        print(add)
        print(add_comp)
        print(pk_comp)
        print(comp_pub_k)
        print("=" * 50)

        addresses.append(address)

        actions = ActionChains(driver).move_to_element(input_)

        # actions.send_keys(Keys.CONTROL+"a")

        for i in range(65):
            actions.send_keys(Keys.BACK_SPACE)

        # actions.send_keys(Keys.DELETE)

        time.sleep(0.5)

        actions.perform()

    return addresses


if "__main__" in __name__:
    # options = Options()
    # options.headless = True

    driver = webdriver.Chrome()

    # print("Started WebDriver in headless mode")

    driver.get('https://www.bitaddress.org/')

    detail_wallet_css = "#detailwallet"

    details = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, detail_wallet_css)))

    phrase_list = load_phrases()

    addy = wallet(details, detail_wallet_css, phrase_list)

    save_objects(addy, "addresses.pickle")

    driver.quit()
