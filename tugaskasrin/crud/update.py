
import mysql.connector

def update_record(id,  nama, no_telepon ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="toko_laptop"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE pelanggan SET id = %s, nama = %s, no_telepon = %s WHERE id = %s"
        val = (id, nama, no_telepon, id)
        print("Executing SQL:", sql % val)  
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()


