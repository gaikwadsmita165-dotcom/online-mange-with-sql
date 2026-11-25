
from config.db import mydb

mycursor = mydb.cursor()


# ================= ADD CATEGORY =================

def addCategory(categoryId, categoryName):

    query = "INSERT INTO category VALUES (%s, %s)"

    value = (categoryId, categoryName)

    mycursor.execute(query, value)

    mydb.commit()

    print("Category Added Successfully")


# ================= DISPLAY ALL CATEGORY =================

def displayCategory():

    query = "SELECT * FROM category"

    mycursor.execute(query)

    result = mycursor.fetchall()

    for row in result:

        print("Category ID ::", row[0])
        print("Category Name ::", row[1])
        print("=" * 30)


# ================= SEARCH CATEGORY =================

def searchCategory(categoryId):

    query = "SELECT * FROM category WHERE categoryId = %s"

    value = (categoryId,)

    mycursor.execute(query, value)

    result = mycursor.fetchone()

    if result:

        print("Category Found")
        print("Category ID ::", result[0])
        print("Category Name ::", result[1])

    else:

        print("Category Not Found")


# ================= UPDATE CATEGORY =================

def updateCategory(categoryId, categoryName):

    query = "UPDATE category SET categoryName = %s WHERE categoryId = %s"

    value = (categoryName, categoryId)

    mycursor.execute(query, value)

    mydb.commit()

    if mycursor.rowcount > 0:

        print("Category Updated Successfully")

    else:

        print("Category Not Found")


# ================= DELETE CATEGORY =================

def deleteCategory(categoryId):

    query = "DELETE FROM category WHERE categoryId = %s"

    value = (categoryId,)

    mycursor.execute(query, value)

    mydb.commit()

    if mycursor.rowcount > 0:

        print("Category Deleted Successfully")

    else:

        print("Category Not Found")
