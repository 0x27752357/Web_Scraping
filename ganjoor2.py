import requests
import bs4

def Molana_DivanShams_Ghazal() :
    Choice = input("Pick a number between [1,2303] : ")

    link = requests.get("https://ganjoor.net/moulavi/shams/ghazalsh/sh" + Choice)

    data_a = bs4.BeautifulSoup(link.content , 'html.parser')

    data_b = data_a.find('div' , attrs={"class" ,"poem"})

    data_c = data_b.find_all('div' , attrs={"class" , "b"})

    for i in data_c :
        print(i.text)
    

def Molana_Masnavi_Daftars() :
    Choice = input("Pick a daftar : ")
    Choice_2 = input("Pick your number : ")
    
    link = requests.get("https://ganjoor.net/moulavi/masnavi/daftar" + Choice + "/sh" + Choice_2)

    data_a = bs4.BeautifulSoup(link.content , 'html.parser')

    data_b = data_a.find('div' , attrs={"class" ,"poem"})

    data_c = data_b.find_all('div' , attrs={"class" , "b"})

    for i in data_c :
        print(i.text)
        


def Saadi_Divan_Ghazaliat() :
    Choice_2 = input("Pick your number : ")
    
    link = requests.get("https://ganjoor.net/saadi/divan/ghazals/sh"+ Choice_2)

    data_a = bs4.BeautifulSoup(link.content , 'html.parser')

    data_b = data_a.find('div' , attrs={"class" ,"poem"})

    data_c = data_b.find_all('div' , attrs={"class" , "b"})

    for i in data_c :
        print(i.text)
        


def Saadi_Bostan_Niayesh() :
    Choice = input("Pick a Bob : ")
    Choice_2 = input("Pick your number : ")
    
    link = requests.get("https://ganjoor.net/saadi/boostan/bab" + Choice + "/sh" + Choice_2)

    data_a = bs4.BeautifulSoup(link.content , 'html.parser')

    data_b = data_a.find('div' , attrs={"class" ,"poem"})

    data_c = data_b.find_all('div' , attrs={"class" , "b"})

    for i in data_c :
        print(i.text)
        
def Hafez_Divan_Ghazaliat() :
    Choice_2 = input("Pick your number [1,495] : ")
    
    link = requests.get("https://ganjoor.net/hafez/ghazal/sh"+ Choice_2)

    data_a = bs4.BeautifulSoup(link.content , 'html.parser')

    data_b = data_a.find('div' , attrs={"class" ,"poem"})

    data_c = data_b.find_all('div' , attrs={"class" , "b"})

    for i in data_c :
        print(i.text)
        
