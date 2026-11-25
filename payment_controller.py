
from model.paymentModel import *


def paymentController():

    while True:

        print("\n========== Payment Management ==========")

        print("1. Add Payment")
        print("2. Display All Payments")
        print("3. Search Payment")
        print("4. Update Payment")
        print("5. Delete Payment")
        print("6. Back to Main Menu")

        ch = int(input("Enter Your Choice :: "))

        match ch:

            case 1:
                print("========== Add Payment ==========")

                paymentId = int(input("Enter Payment ID :: "))
                orderId = int(input("Enter Order ID :: "))
                paymentMethod = input("Enter Payment Method (UPI/Card/Cash) :: ")
                paymentAmount = float(input("Enter Payment Amount :: "))

                addPayment(
                    paymentId,
                    orderId,
                    paymentMethod,
                    paymentAmount
                )

            case 2:
                print("========== Display All Payments ==========")

                displayPayment()

            case 3:
                print("========== Search Payment ==========")

                paymentId = int(input("Enter Payment ID to Search :: "))

                searchPayment(paymentId)

            case 4:
                print("========== Update Payment ==========")

                paymentId = int(input("Enter Payment ID to Update :: "))
                paymentStatus = input("Enter Updated Payment Status :: ")

                updatePayment(paymentId, paymentStatus)

            case 5:
                print("========== Delete Payment ==========")

                paymentId = int(input("Enter Payment ID to Delete :: "))

                deletePayment(paymentId)

            case 6:
                break

            case _:
                print("Invalid Choice")
