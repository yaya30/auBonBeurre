import mariadb
def insertBdd(unit_id):
    try:
        mydb = mariadb.connect(
            host="mariadb",
            user="root",
            port=3309,
            password="root",
            database = "Unites"
        )
        mycursor = mydb.cursor()
        mycursor.execute("show databases;")
        myresult = mycursor.fetchone()
        print("result select :",myresult)
        # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        
    except mariadb.Error as err:
        print("Something went wrong: {}".format(err))


insertBdd(1)
