import csv
import time

import PIL.ImageShow
from bs4 import BeautifulSoup

from pykeyboard import PyKeyboard
from pymouse import *
import pyperclip

import pytesseract
from PIL import ImageGrab

# get text from screen
def get_text_from_screen():
    image = ImageGrab.grab()
    text = pytesseract.image_to_string(image,lang='chi_sim')
    print(text)
    print("***********************")
    text = text.split("\n")
    telephone = ""
    email = ""
    type = ""
    for i in text:
        i = str(i).replace(" ","")
        if(i.__contains__("白")):
            telephone = i.split("白")[1]
        elif(i.__contains__("机")):
            telephone = i.split("机")[1]
        elif(i.__contains__("性质")):
            type = i.split("性质")[1]
        elif(i.__contains__("箱")):
            email = i.split("箱")[1]

    return telephone,email,type

with open("/Users/alexhan/Desktop/people.txt",'r') as f:
    soup = BeautifulSoup(f, "html.parser")
    tt = soup.findAll("h4")
    pos = soup.findAll("p")
    people = tt.__str__()[1:-1].split(",")
    companies = pos.__str__()[1:-1].split(",")

    name = []
    comp = []
    position = []
    for i in range(616):
        people[i] = people[i][people[i].find(">")+1:-12].split("<span>")
        companies[i] = companies[i][companies[i].find(">")+1:-4]
        name.append(people[i][0])
        position.append(people[i][1])
        comp.append(companies[i])


#     with open("/Users/alexhan/Desktop/people.csv",'w') as csvfile:
#         writer = csv.writer(csvfile)
#         for i in range(616):
#             writer.writerow([name[i],position[i],comp[i]])

m = PyMouse()
k = PyKeyboard()

search = [1395.12890625, 96.05078125]
pleaseInput = [1330,96.05078125]
card = [673.6015625, 252.71875]
ret = [239.09765625, 877.01171875]

telephone = []
email = []
type = []

# imitate mouse clicking
time.sleep(5)
for i in range(0,616):
    print(i)
    pyperclip.copy(name[i])

    m.click(pleaseInput[0],pleaseInput[1])
    time.sleep(0.5)
    k.press_key('command')
    k.press_key('a')
    k.release_key('a')

    k.press_key('v')
    k.release_key('v')
    k.release_key('command')

    m.click(search[0],search[1])

    time.sleep(3)
    m.click(card[0],card[1])

    time.sleep(3)

    result = get_text_from_screen()
    telephone.append(result[0])
    email.append(result[1])
    type.append(result[2])

    m.click(ret[0],ret[1])

    with open("/Users/alexhan/Desktop/crawler.csv", 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name[i], position[i], comp[i], type[i], telephone[i], email[i]])

    time.sleep(5)