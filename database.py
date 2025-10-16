import sqlite3

db=sqlite3.connect("databaseTest.db")

cursor=db.cursor()

# db_path = os.path.join(os.getcwd(), "databaseTest.db")
# db = sqlite3.connect(db_path)
cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
    title text,
    genre text,
    lengh float,
    rewiews text
)
""")

# cursor.execute("INSERT INTO movies values('ratatuj','family', 2 , 9.2)")
# cursor.execute("SELECT, title, genre FROM movies")
# cursor.execute("DELETE FROM movies WHERE rowid >= 2 AND rowid <= 5")аш туй не прописувати where тоїсть условіє то оно просто удалит значенія із усіх полєй в 
cursor.execute("UPDATE movies SET rewiews =6.9, lengh=3 WHERE genre ='fantasy'")
cursor.execute("SELECT rowid, * FROM movies WHERE rewiews >6 ORDER BY rowid DESC")
# <> се знак для обозначенія не равності в язикови SQL
print(cursor.fetchall())
items=cursor.fetchall()

# print(cursor.fetchmany(5)[4][1])
# print(cursor.fetchone()[1])
# for el in items:
#     print(el[1] + "\n"+ el[4])
db.commit()
db.close()