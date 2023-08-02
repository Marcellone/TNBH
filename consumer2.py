import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
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

# login al sito
def login_to_website(username, password):
    print("Connessione in corso...")
    service = Service(executable_path='C:/Users/Utente/Desktop/script/chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Rimuove la print di DevTools
    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://timcomunica.timbusiness.it')
    login_button = driver.find_element(By.XPATH, '//*[@id="pulsanteAccedi"]/a')
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="utenteAccedi"]/input')))
    username_input.send_keys(username)
    password_input = driver.find_element(By.XPATH, '//*[@id="passAccedi"]/input')
    password_input.send_keys(password)
    login_button.click()
    time.sleep(12)  # Wait for login to complete
    print("Connessione effettuata!")

    return driver

# Funzione per navigare alla pagina SEDI
def navigate_to_sedi(driver):
    sedi_button = driver.find_element(By.XPATH, '//*[@id="row"]/div[1]/div/div[1]/a[2]')
    sedi_button.click()
    time.sleep(3)

# Funzione per fare clic sul bottone per il Settore
def click_settore_button(driver):
    settore_button = driver.find_element(By.XPATH, '//*[@id="2"]/td[4]/button')
    settore_button.click()
    time.sleep(3)

# Funzione per fare clic sul sottomenu per gli Utenti
def click_utenti_submenu(driver, wait):
    hover_menu = driver.find_element(By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[2]/span')
    ActionChains(driver).move_to_element(hover_menu).perform()
    utenti_submenu = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[2]/ul/li[2]/a')))
    utenti_submenu.click()
    time.sleep(3)

# Funzione per fare clic sul bottone dell'telefono con l'ID specificato dall'utente
def click_telefono_button(driver, sede_id):
    telefono_button = driver.find_element(By.XPATH, f'//*[@id="{sede_id}"]/td[4]/button')
    telefono_button.click()
    time.sleep(3)

# Funzione per fare clic sul sottomenu per l'elemento selezionato
def click_sottomenu_elemento(driver, wait):
    hover_menu_tendina = driver.find_element(By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[4]/span')
    ActionChains(driver).move_to_element(hover_menu_tendina).perform()
    sottomenu_elemento = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[4]/ul/li[2]/span')))
    ActionChains(driver).move_to_element(sottomenu_elemento).perform()
    elemento_selezionato = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menuBarConfigura"]/ul/li[4]/ul/li[2]/ul/li[3]/a')))
    elemento_selezionato.click()
    time.sleep(3)

# Funzione per aggiungere un nuovo elemento
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
    ActionChains(driver).click().perform()  # Clicca su un punto qualsiasi
    time.sleep(3)

def get_username():
    try:
        with open(get_absolute_path('username.txt'), "r") as username_file:
            username = username_file.readline().strip()
            if len(username) > 0:
                return username
    except FileNotFoundError:
        pass

    return None

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

    # Stampa le linee una alla volta per creare l'effetto di animazione
    for line in welcome_message:
        print(line)
        time.sleep(0.1)

    print(created_by)

# Funzione principale del programma
def main():
    
    print_animated_welcome()
    
    # Controlla se l'username è già presente nel file
    username = get_username()
    if not username:
        username = input("Inserisci il tuo username: ")
        save_username = input("Vuoi salvare l'username? (s/n): ").lower()
        if save_username == 's':
            with open(get_absolute_path('username.txt'), "r") as username_file:
                username_file.write(username)
    
    password = get_user_input("Inserisci la tua password: ")
    sede_id = input("Inserisci l'ID del telefono che desideri modificare: ")

    driver = login_to_website(username, password)
    wait = WebDriverWait(driver, 10)  # Creazione dell'oggetto wait

    with open(get_absolute_path('ciesse.csv'), 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Salta la prima riga dell'intestazione

        navigate_to_sedi(driver)
        click_settore_button(driver)
        click_utenti_submenu(driver, wait)
        click_telefono_button(driver, sede_id)
        click_sottomenu_elemento(driver, wait)

        file.seek(0)

        for row in reader:
            if len(row) >= 4:
                numero_telefono = row[2]
                nome = row[3]
                add_new_element(driver, wait, numero_telefono, nome)  # Passaggio di wait come parametro
                print("Elemento aggiunto correttamente!")

    driver.quit()

if __name__ == "__main__":
    main()
