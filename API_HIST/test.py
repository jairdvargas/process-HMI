#Imprime los tags del historian

import sys
import adodbapi

#Codigo de prueba

provider = ["prv", "Microsoft.ACE.OLEDB.12.0", "Microsoft.Jet.OLEDB.4.0"]

constr = "Provider=ihOLEDB.iHistorian.1;User Id=;Password="

# create the connection

con = adodbapi.connect(constr)

cursor = con.cursor()
cursor.execute("SELECT TagName FROM ihTags",)
results=cursor.fetchall()

for row in results:
    print(row)