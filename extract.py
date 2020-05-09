#import mysql.connector
import pymysql
import os
from PIL import Image
import base64
mydb =  pymysql.connect("localhost","ephmuya","5141","fingerdata" )
my_database = mydb.cursor()
sql_statement = "SELECT SubjectId,Template FROM subjects"
my_database.execute(sql_statement)
output = my_database.fetchall()
Thisfolder = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(Thisfolder, "pictures")
for x in output:
    name = str(x[0])

    picture = os.path.join(folder, "{names}.png".format(names=name))
    with open(picture, 'wb') as file:
        try:
            decoded = base64.decodebytes(x[1])
            #print(decoded)
            file.write(x[1])
            print(name + ": Success")
            file.close

        except Exception as e:

            print(name+" :" +str(e))



