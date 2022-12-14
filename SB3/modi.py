import sqlite3


cn = sqlite3.Connection("DataBase/banquito.db")
cursor = cn.cursor()
Lis_PS = ['f7d4edae-79b1-11ed-8b46-be0d8dc753b1', '12345678', 'Marlon', 'Durand', 'Caracuzma',
          'marlon@gmail.com', '2002-02-02', '987654321', 'MOVIS', '21200290', '654321', 'A', 'plataforma']
cursor.executemany(
    "INSERT INTO personal VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", [Lis_PS])
print("SUCCESS")

cn.commit()
cn.close()
