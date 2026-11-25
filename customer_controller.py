
from model.customerModel import *


def customerController():

    while True:

        print("\n========== Customer Management ==========")

        print("1. Add Customer")
        print("2. Display All Customer")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back to Main Menu")

        ch = int(input("Enter Your Choice :: "))

        match ch:

            case 1:
                print("========== Add Customer ==========")

                customerId = int(input("Enter Customer ID :: "))
                customerName = input("Enter Customer Name :: ")
                customerEmail = input("Enter Customer Email :: ")
                customerPhone = input("Enter Customer Phone :: ")
                customerAddress = input("Enter Customer Address :: ")

                addCustomer(
                    customerId,
                    customerName,
                    customerEmail,
                    customerPhone,
                    customerAddress
                )

            case 2:
                print("========== Display All Customer ==========")

                displayCustomer()

            case 3:
                print("========== Search Customer ==========")

                customerId = int(input("Enter Customer ID to Search :: "))

                searchCustomer(customerId)

            case 4:
                print("========== Update Customer ==========")

                customerId = int(input("Enter Customer ID to Update :: "))
                customerName = input("Enter Updated Customer Name :: ")
                customerEmail = input("Enter Updated Email :: ")
                customerPhone = input("Enter Updated Phone :: ")
                customerAddress = input("Enter Updated Address :: ")

                updateCustomer(
                    customerId,
                    customerName,
                    customerEmail,
                    customerPhone,
                    customerAddress
                )

            case 5:
                print("========== Delete Customer ==========")

                customerId = int(input("Enter Customer ID to Delete :: "))

                deleteCustomer(customerId)

            case 6:
                break

            case _:
                print("Invalid Choice")
