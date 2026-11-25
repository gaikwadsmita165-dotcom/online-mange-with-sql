
from config.db import mydb

mycursor = mydb.cursor()


# ================= ADD PAYMENT =================

def addPayment(paymentId, orderId, paymentMethod, paymentAmount):

    try:

        # Check Payment ID
        query = "SELECT paymentId FROM payment WHERE paymentId = %s"
        mycursor.execute(query, (paymentId,))

        if mycursor.fetchone():
            print("Payment ID Already Exists")
            return

        # Check Order
        query = """SELECT totalAmount
                   FROM orders
                   WHERE orderId = %s"""

        mycursor.execute(query, (orderId,))

        orderData = mycursor.fetchone()

        if orderData is None:
            print("Order Does Not Exist")
            return

        totalAmount = float(orderData[0])

        # Check Payment Amount
        if paymentAmount != totalAmount:
            print("Payment Amount Does Not Match Order Total")
            return

        query = """INSERT INTO payment
                   (paymentId, orderId, paymentMethod,
                    paymentAmount, paymentStatus)
                   VALUES (%s, %s, %s, %s, %s)"""

        value = (
            paymentId,
            orderId,
            paymentMethod,
            paymentAmount,
            "Success"
        )

        mycursor.execute(query, value)

        mydb.commit()

        print("Payment Added Successfully")
        print("Payment Status :: Success")

    except Exception as e:

        mydb.rollback()
        print("Error ::", e)


# ================= DISPLAY ALL PAYMENTS =================

def displayPayment():

    query = "SELECT * FROM payment"

    mycursor.execute(query)

    result = mycursor.fetchall()

    if len(result) == 0:

        print("No Payments Exist")

    else:

        for row in result:

            print("Payment ID ::", row[0])
            print("Order ID ::", row[1])
            print("Payment Method ::", row[2])
            print("Payment Amount ::", row[3])
            print("Payment Status ::", row[4])
            print("=" * 30)


# ================= SEARCH PAYMENT =================

def searchPayment(paymentId):

    query = "SELECT * FROM payment WHERE paymentId = %s"

    mycursor.execute(query, (paymentId,))

    result = mycursor.fetchone()

    if result:

        print("Payment Found")

        print("Payment ID ::", result[0])
        print("Order ID ::", result[1])
        print("Payment Method ::", result[2])
        print("Payment Amount ::", result[3])
        print("Payment Status ::", result[4])

    else:

        print("Payment Not Found")


# ================= UPDATE PAYMENT =================

def updatePayment(paymentId, paymentStatus):

    query = """UPDATE payment
               SET paymentStatus = %s
               WHERE paymentId = %s"""

    mycursor.execute(query, (paymentStatus, paymentId))

    mydb.commit()

    if mycursor.rowcount > 0:

        print("Payment Updated Successfully")

    else:

        print("Payment Not Found or No Changes Made")


# ================= DELETE PAYMENT =================

def deletePayment(paymentId):

    query = "DELETE FROM payment WHERE paymentId = %s"

    mycursor.execute(query, (paymentId,))

    mydb.commit()

    if mycursor.rowcount > 0:

        print("Payment Deleted Successfully")

    else:

        print("Payment Not Found")
