import mysql.connector
import requests
from bs4 import BeautifulSoup


my_car = input().lower()

req = requests.get(
    "https://www.truecar.com/used-cars-for-sale/listings/" + my_car + "/"
)

soup = BeautifulSoup(req.text, "html.parser")
cards = soup.find_all("div", attrs={"class": "card"})

miless = []
count = 0

for card in cards:
    count += 1
    miles = card.find("div", attrs={"data-test": "vehicleMileage"})
    #  print(count,miles.text)
    miless.append(miles.text)

# print(miless)
pricess = []
count = 0

for card in cards:
    count += 1
    price = card.find("span", attrs={"data-test": "vehicleListingPriceAmount"})
    # print(count,price.text)
    pricess.append(price.text)
# print(pricess)

find_alles = []
for i in range(20):
    find_alles.append((pricess[i], miless[i]))

#########################################################################################$DATA BASE QUERY$###############################################################
cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
cursor = cnx.cursor()
cursor.execute("CREATE DATABASE %s" % my_car)
print("create database %s with successfuly" % my_car)
print("connection to database %s......." % my_car)
print("connect to database %s with successfuly" % my_car)

cn = mysql.connector.connect(
    user="root", password="", host="127.0.0.1", database="%s" % my_car
)
cursor = cn.cursor()

cursor.execute("CREATE TABLE cars (price varchar(100), miles varchar(100))")
print("Create Table cars with successfuly")

query = "INSERT INTO cars (price, miles) VALUES (%s, %s)"
cursor.executemany(query, find_alles)
cn.commit()
print(cursor.rowcount, "records inserted to cars")
cnx.close()
cn.close()
