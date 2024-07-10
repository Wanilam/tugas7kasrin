import mysql.connector

def create_record(id, nama, no_telepon):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="toko_laptop"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO pelanggan (id, nama, no_telepon) VALUES ( %s, %s, %s)"
    val = (id, nama, no_telepon)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()