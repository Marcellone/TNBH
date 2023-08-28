import csv
import time
import os
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import getpass

def get_absolute_path(filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, filename)

def get_user_input(prompt):
    try:
        return getpass.getpass(prompt)
    except Exception as error:
        print("Errore nell'input:", error)
        return None

def get_chromedriver_path():
    if platform.system() == 'Windows':
        return get_absolute_path('chromedriver.exe')
    elif platform.system() == 'Linux':
        return 'chromedriver'
    elif platform.system() == 'Darwin':
        return get_absolute_path('chromedriver')
    else:
        raise Exception("Sistema operativo non supportato.")
    
# def get_csv_path(fname):
#     if platform.system() == 'Windows':
#         return get_absolute_path('chromedriver.exe')
#     elif platform.system() == 'Linux':
#         return 'chromedriver'
#     elif platform.system() == 'Darwin':
#         return get_absolute_path('chromedriver')
#     else:
#         raise Exception("Sistema operativo non supportato.")

def login_to_website(username, password):
    print("Connessione in corso...")
    chromedriver_path = get_chromedriver_path()
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://timcomunica.timbusiness.it')
    login_button = driver.find_element(By.XPATH, '//*[@id="pulsanteAccedi"]/a')
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="utenteAccedi"]/input')))
    username_input.send_keys(username)
    password_input = driver.find_element(By.XPATH, '//*[@id="passAccedi"]/input')
    password_input.send_keys(password)
    login_button.click()
    time.sleep(12)
    print("Connessione effettuata!")

    return driver

def main_menu():
    print("╔════════════════════════════════╗")
    print("║       MENU PRINCIPALE          ║")
    print("╠════════════════════════════════╣")
    print("║ 1. Aggiungi elemento           ║")
    print("║ 2. Elimina elementi            ║")
    print("╚════════════════════════════════╝")
    choice = input("Inserisci il numero corrispondente all'opzione desiderata: ")
    return choice


def delete_element(driver):
    while True:
        try:
            delete_button = driver.find_element(By.XPATH, '//*[@id="1"]/td[5]/button/img')
            delete_button.click()

            alert = driver.switch_to.alert
            alert.accept()

            time.sleep(2)
            driver.find_element(By.XPATH, '//body').click()
            ActionChains(driver).click().perform()
            time.sleep(1)
        except NoSuchElementException:
            print("Eliminazione completata")
            break

def navigate_to_sedi(driver):
    sedi_button = driver.find_element(By.XPATH, '//*[@id="row"]/div[1]/div/div[1]/a[2]')
    sedi_button.click()
    time.sleep(3)

def click_settore_button(id_sede ,driver):
    settore_button = driver.find_element(By.XPATH, f'//*[@id="{id_sede}"]/td[4]/button')
    settore_button.click()
    time.sleep(3)

def click_utenti_submenu(driver, wait):
    hover_menu = driver.find_element(By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[2]/span')
    ActionChains(driver).move_to_element(hover_menu).perform()
    utenti_submenu = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[2]/ul/li[2]/a')))
    utenti_submenu.click()
    time.sleep(3)

def click_telefono_button(driver, id_centralino):
    telefono_button = driver.find_element(By.XPATH, f'//*[@id="{id_centralino}"]/td[4]/button')
    telefono_button.click()
    time.sleep(3)

def click_sottomenu_elemento(driver, wait):
    hover_menu_tendina = driver.find_element(By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[4]/span')
    ActionChains(driver).move_to_element(hover_menu_tendina).perform()
    sottomenu_elemento = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[4]/ul/li[2]/span')))
    ActionChains(driver).move_to_element(sottomenu_elemento).perform()
    elemento_selezionato = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[4]/ul/li[2]/ul/li[3]/a')))
    elemento_selezionato.click()
    time.sleep(3)

def add_new_element(driver, wait, numero_telefono, nome):
    add_button = driver.find_element(By.XPATH, '//*[@id="speed_dial_100_add"]')
    add_button.click()
    time.sleep(3)
    input_numero_telefono = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="phoneNumber"]')))
    input_numero_telefono.send_keys(numero_telefono)
    input_nome = driver.find_element(By.XPATH, '//*[@id="description"]')
    input_nome.send_keys(nome)
    add_speed_dial_button = driver.find_element(By.XPATH, '//*[@id="add_speed_dial_100"]')
    add_speed_dial_button.click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//body').click()
    ActionChains(driver).click().perform()
    time.sleep(3)

def create_username_file_if_not_exists():
    username_file_path = get_absolute_path('username.txt')
    if not os.path.exists(username_file_path):
        with open(username_file_path, "w"):
            pass

def get_username():
    create_username_file_if_not_exists()
    try:
        with open(get_absolute_path('username.txt'), "r") as username_file:
            username = username_file.readline().strip()
            if len(username) > 0:
                return username
    except FileNotFoundError:
        pass

    return None

def get_csv_file():
    csv_file = input("Inserisci il nome del file CSV (inserisci solo il nome, senza percorsi): ")
    return get_absolute_path(csv_file+'.csv')

def print_animated_welcome():
    welcome_message = [
        "████████╗███╗░░██╗██████╗░██╗░░██╗",
        "╚══██╔══╝████╗░██║██╔══██╗██║░░██║",
        "░░░██║░░░██╔██╗██║██████╦╝███████║",
        "░░░██║░░░██║╚████║██╔══██╗██╔══██║",
        "░░░██║░░░██║░╚███║██████╦╝██║░░██║",
        "░░░╚═╝░░░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝"
    ]
    created_by = "Created by wiryale - LinkedIn: https://it.linkedin.com/in/alessandro-marcellino"

    for line in welcome_message:
        print(line)
        time.sleep(0.1)

    print(created_by)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_console()
        print_animated_welcome()

        # Ottieni l'username salvato o richiedilo all'utente
        username = get_username()
        if not username:
            username = input("Inserisci il tuo username: ")
            save_username = input("Vuoi salvare l'username? (s/n): ").lower()
            if save_username == 's':
                with open(get_absolute_path('username.txt'), "w") as username_file:
                    username_file.write(username)

        password = get_user_input("Inserisci la tua password: ")
        id_sede = input("Inserisci l'ID della sede che desideri modificare: ")
        id_centralino = input("Inserisci l'ID del telefono che desideri modificare: ")

        driver = login_to_website(username, password)
        wait = WebDriverWait(driver, 10)

        choice = main_menu()
        if choice == '1':
            # Aggiunta di elementi
            csv_file = get_csv_file()

            with open(csv_file, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)

                navigate_to_sedi(driver)
                click_settore_button(id_sede ,driver)
                click_utenti_submenu(driver, wait)
                click_telefono_button(driver, id_centralino)
                click_sottomenu_elemento(driver, wait)

                file.seek(0)

                for row in reader:
                    if len(row) >= 4:
                        numero_telefono = row[2]
                        nome = row[3]
                        add_new_element(driver, wait, numero_telefono, nome)
                        print("Elemento aggiunto correttamente!")

        elif choice == '2':
            # Eliminazione di elementi
            navigate_to_sedi(driver)
            click_settore_button(id_sede, driver)
            click_utenti_submenu(driver, wait)
            click_telefono_button(driver, id_centralino)
            click_sottomenu_elemento(driver, wait)
            time.sleep(1)
            delete_element(driver)
        else:
            print("Opzione non valida o terminata.")

        driver.quit()

        # Pausa prima di tornare al menu iniziale
        input("Premi Enter per tornare al menu principale...")

if __name__ == "__main__":
    main()
