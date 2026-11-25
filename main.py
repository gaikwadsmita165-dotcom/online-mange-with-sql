
from controller.category_controller import categoryController
from controller.product_controller import productController
from controller.customer_controller import customerController
from controller.order_controller import orderController
from controller.payment_controller import paymentController


while True:

    print("\n========== Online Shopping Management System ==========")

    print("1. Product Management")
    print("2. Customer Management")
    print("3. Category Management")
    print("4. Order Management")
    print("5. Payment Management")
    print("6. Exit")

    choice = int(input("Hey User, Please Enter Your Choice :: "))

    match choice:

        case 1:
            productController()

        case 2:
            customerController()

        case 3:
            categoryController()

        case 4:
            orderController()

        case 5:
            paymentController()

        case 6:
            print("Thank You For Using Online Shopping Management System!")
            break

        case _:
            print("Invalid Choice")



