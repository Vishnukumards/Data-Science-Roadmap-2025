import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "8983"
)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE if not exists votingdatabase")

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "8983",
    database ="votingdatabase"
)
mycursor = db.cursor()
mycursor.execute("""create table if not exists voter_data (Voterid int,voter_name varchar(50),voter_number BIGINT,voter_address varchar(200)) """)
print("TABLE CREATED")

mycursor = db.cursor()
mycursor.execute(
    "INSERT INTO votingdatabase.voter_data (Voterid ,voter_name,voter_number,voter_address) VALUES(%s,%s,%s,%s)",(128845,"RAJ",9952468985,"Hari har pg hennur road, bengalurur,56004"))
db.commit()
print("Table data added ")

mycursor = db.cursor()
mycursor.execute("SELECT * FROM votingdatabase.voter_data")
for i in mycursor.fetchall():
    print(i)
    

mycursor = db.cursor()
mycursor.execute("SELECT voter_name,Voterid FROM votingdatabase.voter_data")
for i in mycursor.fetchall():
    print(i)
