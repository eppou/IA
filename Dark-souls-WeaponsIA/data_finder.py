import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

#listas para informaçoes das armas
nomes = []
reqS = []
reqD = []
reqI = []
reqF = []
tipos = []
danoP = []
bloqP = []
danoM = []
bloqM = []
danoF = []
bloqF = []
danoR = []
pesos = []

def getRequirements(html,count):
    pattern = r'\d+"."*\d+?|-'

    # Encontra todas as correspondências dentro da string HTML
    matches = re.findall(pattern, html)

    if count == 1:
        reqFor = matches
        reqS.append(reqFor)
        return True
    if count == 2:
        reqDex = matches
        reqD.append(reqDex)
        return  True
    if count == 3:
        reqInt = matches
        reqI.append(reqInt)
        return  True
    if count == 4:
        reqFe = matches
        reqF.append(reqFe)
        return True
    return False

def getAtributes(html,count):
    # Define uma expressão regular para encontrar números ou "-"
    pattern = r'-?(\d+(\.\d+)?)|-'

    # Encontra todas as correspondências dentro da string HTML
    matches = re.findall(pattern, html)

    if count == 1:
        phDMG = matches
        danoP.append(phDMG)
        return  True
    if count == 2:
        phBLQ = matches
        bloqP.append(phBLQ)
        return  True
    if count == 3:
        mgDMg = matches
        danoM.append(mgDMg)
        return  True
    if count == 4:
        mgBLQ = matches
        bloqM.append(mgBLQ)
        return  True
    if count == 5:
        frDMG = matches
        danoF.append(frDMG)
        return  True
    if count == 6:
        frBLQ = matches
        bloqF.append(frBLQ)
        return  True
    if count == 7:
        lgDMG = matches
        danoR.append(lgDMG)
        return  True
    if count == 8:
        weight = matches
        pesos.append(weight)
        return  True
    return False


def getInfoTable(request_info):
    soup_info = BeautifulSoup(response_info.text, 'html.parser')

    div_atributes = soup_info.find('table', class_='wiki_table')
    td_tags = div_atributes.find_all(lambda tag: tag.name == 'td' and tag.get('colspan') == '5')
    count = 1
    count2 = 1
    for td_tag in td_tags:
        inputado = td_tag.text

        if getAtributes(inputado,count):
            count = count + 1

    td_tags2 = div_atributes.find_all(lambda tag: tag.name == 'td' and tag.get('colspan') == '4')

    for td_tag2 in td_tags2:
        inputado = td_tag2.text

        if getRequirements(inputado,count2):
            count2 = count2 + 1

def getType(request_info):
    soup_info = BeautifulSoup(response_info.text, 'html.parser')

    div_atributes = soup_info.find_all('a', class_='wiki_link')
    type = div_atributes.text

def createDataFrame():
    del nomes[14]
    print(nomes)
    print(len(danoP))
    print(len(reqS))
    print(len(reqD))
    print(len(reqF))
    print(len(reqI))
    print(len(danoM))
    print(len(danoR))
    print(len(danoF))
    print(len(bloqF))
    print(len(bloqM))
    print(len(bloqP))
    print(len(pesos))
    data = {
    'Nome': nomes,
    'Requerimento Força': reqS,
    'Requerimento Int': reqI,
    'Requerimento Fe': reqF,
    'Requerimento Des': reqD,
    'Dano fisico': danoP,
    'Dano fogo': danoF,
    'Dano raio': danoR,
    'Dano magico': danoM,
    'Defesa Fogo': bloqP,
    'Defesa Magica': bloqM,
    'Defesa Elementar': bloqF,
    'Peso': pesos
    }

    df_armas = pd.DataFrame(data)
    df_armas.to_csv("exemplo_csv",index=True)
    print(df_armas)

# URL do site com informações sobre armas
url = 'https://darksouls.wiki.fextralife.com/Weapons'
# Realizar a solicitação GET para obter o conteúdo da página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analisar o conteúdo da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todas as divs com a classe "col-xs-6 col-sm-2"
    divs_armas = soup.find_all('div', class_='col-xs-6 col-sm-2')

    # Iterar sobre as divs das armas
    for div_arma in divs_armas:
        # Encontrar a tag <br> dentro da div para obter o nome da arma
        br_tag = div_arma.find('br')

        # Se a tag <br> for encontrada, obter o nome da arma
        if br_tag:
            nome_arma = br_tag.nextSibling.strip()

            # Encontrar o link <a> dentro da div para acessar informações adicionais
            link_arma = div_arma.find('a', class_='wiki_link')

            # Se o link for encontrado, seguir o link e acessar a página para obter mais informações
            if link_arma:
                link_arma_url = link_arma['href']  # Obtém o valor do atributo 'href' do link
                # Construir a URL completa para a página de informações adicionais (pode variar dependendo do site)
                print(link_arma_url)
                pagina_info_url = f'https://darksouls.wiki.fextralife.com/{link_arma_url}'

                # Realizar uma nova solicitação GET para acessar a página de informações adicionais
                response_info = requests.get(pagina_info_url)

                # Verificar se a solicitação foi bem-sucedida
                if response_info.status_code == 200:
                    nomes.append(nome_arma)
                    print(nome_arma)
                    # Analisar o conteúdo da página de informações adicionais
                    getInfoTable(response_info)
                    #getType(response_info)
                else:
                    print("erro ao validar site da arma")

        # Imprimir uma linha em branco entre as informações das armas

    createDataFrame()

else:
    print('Falha ao acessar o site')