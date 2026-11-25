
from config.db import mydb

mycursor = mydb.cursor()


# ================= ADD PRODUCT =================

def addProduct(productId, productName, productPrice, productQty, categoryId):

    query = "INSERT INTO product VALUES (%s, %s, %s, %s, %s)"

    value = (productId, productName, productPrice, productQty, categoryId)

    mycursor.execute(query, value)

    mydb.commit()

    print("Product Added Successfully")


# ================= DISPLAY ALL PRODUCT =================

def displayProduct():

    query = "SELECT * FROM product"

    mycursor.execute(query)

    result = mycursor.fetchall()

    if len(result) == 0:
        print("No Product Exists")

    else:
        for row in result:

            print("Product ID ::", row[0])
            print("Product Name ::", row[1])
            print("Product Price ::", row[2])
            print("Product Quantity ::", row[3])
            print("Category ID ::", row[4])
            print("=" * 30)


# ================= SEARCH PRODUCT =================

def searchProduct(productId):

    query = "SELECT * FROM product WHERE productId = %s"

    value = (productId,)

    mycursor.execute(query, value)

    result = mycursor.fetchone()

    if result:

        print("Product Found")
        print("Product ID ::", result[0])
        print("Product Name ::", result[1])
        print("Product Price ::", result[2])
        print("Product Quantity ::", result[3])
        print("Category ID ::", result[4])

    else:
        print("Product Not Found")


# ================= UPDATE PRODUCT =================

def updateProduct(productId, productName, productPrice, productQty, categoryId):

    query = """UPDATE product
               SET productName = %s,
                   productPrice = %s,
                   productQty = %s,
                   categoryId = %s
               WHERE productId = %s"""

    value = (productName, productPrice, productQty, categoryId, productId)

    mycursor.execute(query, value)

    mydb.commit()

    if mycursor.rowcount > 0:
        print("Product Updated Successfully")

    else:
        print("Product Not Found or No Changes Made")


# ================= DELETE PRODUCT =================

def deleteProduct(productId):

    query = "DELETE FROM product WHERE productId = %s"

    value = (productId,)

    mycursor.execute(query, value)

    mydb.commit()

    if mycursor.rowcount > 0:
        print("Product Deleted Successfully")

    else:
        print("Product Not Found")
