
from model.productModel import *


def productController():

    while True:

        print("\n========== Product Management ==========")

        print("1. Add Product")
        print("2. Display All Product")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")

        ch = int(input("Enter Your Choice :: "))

        match ch:

            case 1:
                print("========== Add Product ==========")

                productId = int(input("Enter Product ID :: "))
                productName = input("Enter Product Name :: ")
                productPrice = float(input("Enter Product Price :: "))
                productQty = int(input("Enter Product Quantity :: "))
                categoryId = int(input("Enter Category ID :: "))

                addProduct(productId, productName, productPrice, productQty, categoryId)

            case 2:
                print("========== Display All Product ==========")

                displayProduct()

            case 3:
                print("========== Search Product ==========")

                productId = int(input("Enter Product ID to Search :: "))

                searchProduct(productId)

            case 4:
                print("========== Update Product ==========")

                productId = int(input("Enter Product ID to Update :: "))
                productName = input("Enter Updated Product Name :: ")
                productPrice = float(input("Enter Updated Product Price :: "))
                productQty = int(input("Enter Updated Product Quantity :: "))
                categoryId = int(input("Enter Updated Category ID :: "))

                updateProduct(productId, productName, productPrice, productQty, categoryId)

            case 5:
                print("========== Delete Product ==========")

                productId = int(input("Enter Product ID to Delete :: "))

                deleteProduct(productId)

            case 6:
                break

            case _:
                print("Invalid Choice")
