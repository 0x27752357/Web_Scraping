import requests
import bs4 
import random


def Quotes(choice) :
    target = requests.get("https://www.goodreads.com/quotes/tag/" + choice )
    data_1 = bs4.BeautifulSoup(target.content , 'html.parser')
    data_2 = data_1.find('div' , attrs={"class" , "leftContainer"})
    data_3 = data_2.find_all('div' , attrs={"class" , "quoteText"})


    li = []
    for i in data_3 :
        li.append(i.text)
    
    print(random.choice(li))     
    
    
choice = input("Welcome \nPlease enter a keyword for your daily random quote : ")
Quotes(choice)
