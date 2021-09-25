import mysql.connector

def insertBdd(unit_id,jsonObject):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database = "Unites"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id FROM automate where unit_id = %s and  num_automate = %s")
        myresult = mycursor.fetchone()
        print("result select :",myresult)
        # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


insertBdd(1)
