
from model.orderModel import *


def orderController():

    while True:

        print("\n========== Order Management ==========")

        print("1. Add Order")
        print("2. Display All Orders")
        print("3. Search Order")
        print("4. Update Order")
        print("5. Delete Order")
        print("6. Back to Main Menu")

        ch = int(input("Enter Your Choice :: "))

        match ch:

            case 1:
                print("========== Add Order ==========")

                orderId = int(input("Enter Order ID :: "))
                customerId = int(input("Enter Customer ID :: "))
                productId = int(input("Enter Product ID :: "))
                orderDate = input("Enter Order Date (YYYY-MM-DD) :: ")
                orderQty = int(input("Enter Order Quantity :: "))

                addOrder(
                    orderId,
                    customerId,
                    productId,
                    orderDate,
                    orderQty
                )

            case 2:
                print("========== Display All Orders ==========")

                displayOrder()

            case 3:
                print("========== Search Order ==========")

                orderId = int(input("Enter Order ID to Search :: "))

                searchOrder(orderId)

            case 4:
                print("========== Update Order ==========")

                orderId = int(input("Enter Order ID to Update :: "))
                orderStatus = input("Enter Updated Order Status :: ")

                updateOrder(orderId, orderStatus)

            case 5:
                print("========== Delete Order ==========")

                orderId = int(input("Enter Order ID to Delete :: "))

                deleteOrder(orderId)

            case 6:
                break

            case _:
                print("Invalid Choice")
