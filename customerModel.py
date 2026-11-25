
from config.db import mydb

mycursor = mydb.cursor()


# ================= ADD CUSTOMER =================

def addCustomer(customerId, customerName, customerEmail, customerPhone, customerAddress):

    query = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s)"

    value = (customerId, customerName, customerEmail, customerPhone, customerAddress)

    mycursor.execute(query, value)

    mydb.commit()

    print("Customer Added Successfully")


# ================= DISPLAY ALL CUSTOMER =================

def displayCustomer():

    query = "SELECT * FROM customer"

    mycursor.execute(query)

    result = mycursor.fetchall()

    if len(result) == 0:

        print("No Customer Exists")

    else:

        for row in result:

            print("Customer ID ::", row[0])
            print("Customer Name ::", row[1])
            print("Customer Email ::", row[2])
            print("Customer Phone ::", row[3])
            print("Customer Address ::", row[4])
            print("=" * 30)


# ================= SEARCH CUSTOMER =================

def searchCustomer(customerId):

    query = "SELECT * FROM customer WHERE customerId = %s"

    value = (customerId,)

    mycursor.execute(query, value)

    result = mycursor.fetchone()

    if result:

        print("Customer Found")
        print("Customer ID ::", result[0])
        print("Customer Name ::", result[1])
        print("Customer Email ::", result[2])
        print("Customer Phone ::", result[3])
        print("Customer Address ::", result[4])

    else:

        print("Customer Not Found")


# ================= UPDATE CUSTOMER =================

def updateCustomer(customerId, customerName, customerEmail, customerPhone, customerAddress):

    query = """UPDATE customer
               SET customerName = %s,
                   customerEmail = %s,
                   customerPhone = %s,
                   customerAddress = %s
               WHERE customerId = %s"""

    value = (customerName, customerEmail, customerPhone, customerAddress, customerId)

    mycursor.execute(query, value)

    mydb.commit()

    if mycursor.rowcount > 0:

        print("Customer Updated Successfully")

    else:

        print("Customer Not Found or No Changes Made")


# ================= DELETE CUSTOMER =================

def deleteCustomer(customerId):

    query = "DELETE FROM customer WHERE customerId = %s"

    value = (customerId,)

    mycursor.execute(query, value)

    mydb.commit()

    if mycursor.rowcount > 0:

        print("Customer Deleted Successfully")

    else:

        print("Customer Not Found")
