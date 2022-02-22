#Imprime los tags del historian

from sqlite3 import Row
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
ListaDeTags = {"Tags": 0}
i=0
for row in results:
    #print(row[0])
    NumTag ="Tag_" + str(i)
    ListaDeTags[NumTag] = row[0]
    i=i+1
ListaDeTags["Tags"]=i

print(ListaDeTags)    