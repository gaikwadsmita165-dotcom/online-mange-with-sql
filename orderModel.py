
from config.db import mydb

mycursor = mydb.cursor()


# ================= ADD ORDER =================

def addOrder(orderId, customerId, productId, orderDate, orderQty):

    try:

        # Check Customer
        query = "SELECT customerId FROM customer WHERE customerId = %s"
        mycursor.execute(query, (customerId,))
        customerData = mycursor.fetchone()

        if customerData is None:
            print("Customer Does Not Exist")
            return

        # Check Product
        query = "SELECT productPrice, productQty FROM product WHERE productId = %s"
        mycursor.execute(query, (productId,))
        productData = mycursor.fetchone()

        if productData is None:
            print("Product Does Not Exist")
            return

        productPrice = productData[0]
        availableQty = productData[1]

        if orderQty <= 0 or orderQty > availableQty:
            print("Invalid Quantity or Insufficient Stock")
            return

        totalAmount = productPrice * orderQty

        # Insert Order
        query = """INSERT INTO orders
                   (orderId, customerId, productId, orderDate,
                    orderQty, totalAmount, orderStatus)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        value = (
            orderId,
            customerId,
            productId,
            orderDate,
            orderQty,
            totalAmount,
            "Pending"
        )

        mycursor.execute(query, value)

        # Update Product Stock
        query = """UPDATE product
                   SET productQty = productQty - %s
                   WHERE productId = %s"""

        mycursor.execute(query, (orderQty, productId))

        mydb.commit()

        print("Order Placed Successfully")
        print("Total Amount ::", totalAmount)

    except Exception as e:

        mydb.rollback()
        print("Error ::", e)


# ================= DISPLAY ALL ORDERS =================

def displayOrder():

    query = "SELECT * FROM orders"

    mycursor.execute(query)

    result = mycursor.fetchall()

    if len(result) == 0:

        print("No Orders Exist")

    else:

        for row in result:

            print("Order ID ::", row[0])
            print("Customer ID ::", row[1])
            print("Product ID ::", row[2])
            print("Order Date ::", row[3])
            print("Order Quantity ::", row[4])
            print("Total Amount ::", row[5])
            print("Order Status ::", row[6])
            print("=" * 30)


# ================= SEARCH ORDER =================

def searchOrder(orderId):

    query = "SELECT * FROM orders WHERE orderId = %s"

    mycursor.execute(query, (orderId,))

    result = mycursor.fetchone()

    if result:

        print("Order Found")

        print("Order ID ::", result[0])
        print("Customer ID ::", result[1])
        print("Product ID ::", result[2])
        print("Order Date ::", result[3])
        print("Order Quantity ::", result[4])
        print("Total Amount ::", result[5])
        print("Order Status ::", result[6])

    else:

        print("Order Not Found")


# ================= UPDATE ORDER =================

def updateOrder(orderId, orderStatus):

    query = """UPDATE orders
               SET orderStatus = %s
               WHERE orderId = %s"""

    mycursor.execute(query, (orderStatus, orderId))

    mydb.commit()

    if mycursor.rowcount > 0:

        print("Order Updated Successfully")

    else:

        print("Order Not Found or No Changes Made")


# ================= DELETE ORDER =================

def deleteOrder(orderId):

    try:

        # Check Payment Records
        query = "SELECT paymentId FROM payment WHERE orderId = %s"

        mycursor.execute(query, (orderId,))

        paymentData = mycursor.fetchone()

        if paymentData:

            print("Order Has Payment Records. Cannot Delete.")
            return

        # Get Product and Quantity
        query = """SELECT productId, orderQty
                   FROM orders
                   WHERE orderId = %s"""

        mycursor.execute(query, (orderId,))

        orderData = mycursor.fetchone()

        if orderData is None:

            print("Order Not Found")
            return

        productId = orderData[0]
        orderQty = orderData[1]

        # Restore Product Stock
        query = """UPDATE product
                   SET productQty = productQty + %s
                   WHERE productId = %s"""

        mycursor.execute(query, (orderQty, productId))

        # Delete Order
        query = "DELETE FROM orders WHERE orderId = %s"

        mycursor.execute(query, (orderId,))

        mydb.commit()

        print("Order Deleted Successfully")

    except Exception as e:

        mydb.rollback()
        print("Error ::", e)
