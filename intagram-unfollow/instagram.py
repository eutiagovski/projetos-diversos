import json
from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = "SEU_USUARIO_OU_EMAIL"
passwd = 'SUA_SENHA'

url = "https://www.instagram.com"

def getInsta():
    print("Iniciando navegador")
    global driver

    driver = webdriver.Firefox()
    driver.get(url)

    sleep(5)
    return True

def logaFacebook():
    driver.find_element_by_class_name('KPnG0').click()
    driver.implicitly_wait(5)
    elem = driver.find_element_by_name('email')
    elem.send_keys(user)
    elem = driver.find_element_by_name('pass')
    elem.send_keys(passwd)
    elem.send_keys(Keys.RETURN)

    sleep(5)
    return True

def logaInsta():
    elem = driver.find_element_by_name('username')
    elem.send_keys(user)
    elem = driver.find_element_by_name('password')
    elem.send_keys(passwd)
    elem.send_keys(Keys.RETURN)

    sleep(5)
    return True

def carregaSeguidores():
    driver.find_elements_by_class_name('Y8-fY ')[1].click()
    
    try:
        carregarMais = driver.find_element_by_class_name('oMwYe')

        while carregarMais:
            carregarMais = driver.find_element_by_class_name('oMwYe')
            carregarMais.click()
            sleep(2)
            
    except:
        pass
    
    global listaMeusSeguidores
    seguidores = driver.find_elements_by_xpath("//div[@class='d7ByH']//span")

    try:
        bk = open('listaSeguidores.txt', 'r')
        bk = json.load(bk)
        listaMeusSeguidores = bk
    
    except:
        listaMeusSeguidores = []

    for i in seguidores:
        t = i.text
        if t not in listaMeusSeguidores:
            listaMeusSeguidores.append(t)
    
    driver.find_element_by_xpath('//div[@class="WaOAr"]//button').click()

    print(f"\nForam encontrados {len(listaMeusSeguidores)} seguidores..")
    
    return True

seguidoresApagados = []

def deletaNaoSeguidor():
    counter = 0
    limite = 10

    global seguidoresApagados

    if driver.current_url != url:
            driver.get("https://www.instagram.com/eutiagovski/")
            
    while True:
        try:
            driver.find_elements_by_class_name('Y8-fY ')[2].click()
        except:
            pass
        carregarMais = driver.find_element_by_class_name('oMwYe')
        carregarMais.click()
        sleep(2)

        d = driver.find_element_by_class_name('PZuss')
        i = d.find_elements_by_tag_name('li')

        for p in i:
            if p.find_element_by_tag_name("button").text == 'Seguindo':
                if p.find_element_by_class_name('d7ByH').text not in listaMeusSeguidores:
                        p.find_element_by_class_name('Pkbci').click()
                        sleep(1)
                        driver.find_element_by_xpath("//div[@class='_1XyCr']//div[@class='mt3GC']//button").click()
                        seguidoresApagados.append(p.find_element_by_class_name('d7ByH').text)
                        sleep(1)
                        counter += 1
                        if counter >= limite:
                            driver.find_element_by_xpath('//div[@class="WaOAr"]//button').click()
                            counter = 0
                            break

def getProfile():
    user = driver.find_element_by_class_name('gmFkV').text
    userUrl = "https://www.instagram.com/"+user+"/"
    driver.get(userUrl)
    sleep(2)
    return True




# Se você for entrar com intagram, comente a linha logaFacebook e descomente a linha logaInsta

getInsta()
#if logaInsta():
if logaFacebook():
    if getProfile():
        if carregaSeguidores():
            deletaNaoSeguidor()