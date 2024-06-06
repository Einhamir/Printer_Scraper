import pandas as pd

from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path


def get_printer_ip(urls_path):

    #file_printers = Path(r"C:\Users\mr344c\Documents\Python Scripts\LA_XARP\urls.txt")
    file_printers = Path(urls_path)
                         
    if file_printers.exists():
        print ("\n Archivo de lectura encontrado.")
        with open(file_printers,"r",) as i:
            list_printers = i.readlines()

        return list_printers
        
    

urls_path = input("Introduce la ubicación del archivo de lectura.\n\n")
printers = get_printer_ip(urls_path)

# url = "file:///C:/Users/mr344c/Documents/Python%20Scripts/LA_XARP/webnew.html"
# page = urlopen(url)
# html = page.read().decode("utf-8")
webs=[]
series =[]
nombres =[]
modelos =[]
ubicaciones =[]

ctrl_ix = 0

for p in printers:

    try:
        url = p.strip()
        page = urlopen(url)
        html = page.read().decode("utf-8")

        soup = BeautifulSoup(html, "html5lib")
    except:
        webs.append(url)
        series.append('WEB-ERROR')
        nombres.append('WEB-ERROR')
        modelos.append('WEB-ERROR')
        ubicaciones.append('WEB-ERROR')
    else:

        coll_td = soup.find_all('td')
        if (len(coll_td)> 0):
            webs.append(url)
            if (coll_td[0].get_text() == ''):
                ctrl_ix = 0
                for td in range (1,12):
                
                    if (td % 2) == 0:
                        
                        ctrl_ix = ctrl_ix +1
                        
                        if ctrl_ix == 1:
                            series.append(coll_td[td].get_text())
                            
                        if ctrl_ix == 2:    
                            nombres.append(coll_td[td].get_text())
                        if ctrl_ix == 3:
                            modelos.append(coll_td[td].get_text())
                        if ctrl_ix == 4:
                            ubicaciones.append(coll_td[td].get_text())
            else:
                ctrl_ix = 0
                for td in range (1,12):
                
                    if (td % 2) != 0:
                        
                        ctrl_ix = ctrl_ix +1
                        
                        if ctrl_ix == 1:
                            series.append(coll_td[td].get_text())
                            
                        if ctrl_ix == 2:    
                            nombres.append(coll_td[td].get_text())
                        if ctrl_ix == 3:
                            modelos.append(coll_td[td].get_text())
                        if ctrl_ix == 4:
                            ubicaciones.append(coll_td[td].get_text())
        else:
            webs.append(url)
            series.append('TD-ERROR')
            nombres.append('TD-ERROR')
            modelos.append('TD-ERROR')
            ubicaciones.append('TD-ERROR')
            

# print(series)
# print(nombres)
# print(modelos)
# print(ubicaciones)

dict_csv = {"IP":webs,"SERIE":series,"NOMBRE":nombres,"MODELO":modelos,"UBICACION":ubicaciones}

df = pd.DataFrame(dict_csv)

##csv_path = input("Introduce la carpeta donde guardar el CSV.\n")
                 
#df.to_csv(r"C:\Users\mr344c\Documents\Python Scripts\LA_XARP\printer_info.csv",sep="|",index=False)
print(r"Guardando archivo como .... C:\printer_info.csv")

df.to_csv(r"C:\printer_info.csv",sep="|",index=False)