import urllib.request
import json
import random
import mysql.connector
from mysql.connector import errorcode
from datetime import date

num = random.randint(0,100)

URL = "https://jsonplaceholder.typicode.com/todos/{0}".format(num)

response = urllib.request.urlopen(URL)

response = response.read()

json = json.loads(response)

frase = json["title"]

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='augusto08'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

mycursor = conn.cursor()

mycursor.execute("USE `jogoteca`;")

insert = ("INSERT INTO frases (Data,Frase) "
       "VALUES (%s, %s)"
       )

data = (date.today(), frase)

mycursor.execute(insert, data)
conn.commit()

print("Frase numero {0} adicionada ao banco!".format(num))


