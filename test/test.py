import sqlite3

with open(r'test\data.csv', 'r') as content:
    data = content.read()
    records=data.split('\n')
print(records)
db = sqlite3.connect(r'backend\\troski_system.db')
cursor = db.cursor()
for i in records:
    record=str(i).split(',')
    data = (record[0],record[3],record[1],record[2])
    cursor.execute('INSERT INTO tb_cars(number_plate,car_model,car_color,car_number) VALUES(?,?,?,?)',data)
db.commit()