import sys

import adodbapi
import datetime

provider = ["prv", "Microsoft.ACE.OLEDB.12.0", "Microsoft.Jet.OLEDB.4.0"]

constr = "Provider=ihOLEDB.iHistorian.1;User Id=;Password="

# create the connection

con = adodbapi.connect(constr)

cursor = con.cursor()
ahora = datetime.datetime.now()
ahoraT = ahora.strftime("%Y/%m/%d %H:%M:%S")

cursor.execute("SELECT TagName, TimeStamp, Value, Quality FROM ihRawData WHERE TagName = DESKTOP-3PEVOMB.Ramp AND samplingmode=RawbyTime AND RowCount=1 AND timestamp>=Now-10s ORDER BY timestamp DESC",)
results=cursor.fetchall()
print(results[0])
PV=results[0]
print(PV[0])
for row in results:
    print(row)

print(str(ahoraT))