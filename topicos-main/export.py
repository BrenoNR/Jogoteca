import zipfile

import mysql.connector
from mysql.connector import errorcode
import zipfile as zip
import os
import json

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

mycursor = conn.cursor(dictionary=True)

mycursor.execute("USE jogoteca")

mycursor.execute('''SELECT *
FROM jogos''')

select = mycursor.fetchall()

with open("export.json", "w") as outfile:
    json.dump(select, outfile)

zip_file = zip.ZipFile('Export.zip', "w")
zip_file.write('export.json', compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()

os.remove("export.json")