import pandas as pd
import requests
from bs4 import BeautifulSoup

names = ["Asylum Demon","Stray Demon","Taurus Demon","Capra Demon","Bell Gargoyles", "Gaping Dragon","Chaos Witch Quelaag","Moonlight Butterfly","Great Grey Wolf Sif","Iron Golem","Dark Sun Gwyndolin","Dragon Slayer Ornstein and Executioner Smough","Crossbreed Priscilla","Seath the Scaleless","Pinwheel","Gravelord Nito","Four Kings","Ceaseless Discharge","Demon Firesage","Centipede Demon","Bed of Chaos","Gwyn, Lord of Cinder"]
local = ["Undead Asylum","Undead Asylum", "Undead Burg", "Undead Burg", "Undead Burg","The Depths","Blighttown","Darkroot Garden","Darkroot Garden","Sen's Fortress","Anor Londo","Anor Londo","Painted World of Ariamis","Crystal Cave","The Catacombs","Tomb of the Giants","New Londo Ruins","Demon Ruins","Demon Ruins","Demon Ruins","Lost Izalith","Kiln of the First Flame"]
# para veloz 1 = sim 0 = nao
veloz = [0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1]
weakness = ["none","none","magic","fire","none","fire","lightning","fire","none","none","light","none","fire","magic","lightning","lightning","lightning","magic","none","magic","none","none"]
resintance = ["none","magic","none","none","none","magic","fire","magic","magic","fire","magic","light","magic","magic","magic","none","none","fire","fire","fire","fire","none"]

def comparaMap(boss):
    maps = {"Undead Asylum","Undead Burg","Parish","Undead Burg/Parish", "The Depths", "Blighttown","Quelaag's Domain","Darkroot Garden","Sen's Fortress","Anor Londo","Painted World of Ariamis","The Duke's Archives","Crystal Cave","The Catacombs","New Londo Ruins","Demon Ruins","Lost Izalith","Kiln of the First Flame"}

    if boss in maps:
        return  True

    return False

# URL do site com informações desejada
#url = 'https://darksouls.fandom.com/wiki/Boss'

# Realizar a solicitação GET para obter o conteúdo da página
#response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
#if response.status_code == 200:
 #   soup = BeautifulSoup(response.text, 'html.parser')
  #  div = soup.find_all('a')

   # for element in div:
    #    if comparaMap(element.text):
     #       actual_map = element
      #      while actual_map and comparaMap(actual_map.find_next('a').text) == False:
       #        names.append(boss_name.text)
        #        print(boss_name.text)
         #       local.append(element.text)
          #      actual_map = actual_map.find_next('a')
           #     if element.text == "Kiln of the First Flame" and boss_name == "Gwyn, Lord of Cinder":
            #        break

#else:
 #   print('Falha ao acessar o site')

dicionario = {
    'Nomes' : names,
    'Locais' : local,
    "Velocidade": veloz,
    "Fraqueza": weakness,
    "Resistente": resintance
}
print(len(names))
print(len(local))
print(len(resintance))
print(len(veloz))
print(len(weakness))
tabela = pd.DataFrame(dicionario)
tabela.to_csv("bosses_csv", index=True)
print(tabela)
