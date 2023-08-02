import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="jban",
    passwd ="",
    database="pos"
    )
if db.is_connected():
    print("MYSQL CONNECTED")