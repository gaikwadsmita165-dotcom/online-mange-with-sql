
from model.categoryModel import *


def categoryController():

    while True:

        print("\n========== Category Management ==========")

        print("1. Add Category")
        print("2. Display All Category")
        print("3. Search Category")
        print("4. Update Category")
        print("5. Delete Category")
        print("6. Back to Main Menu")

        ch = int(input("Enter Your Choice :: "))

        match ch:

            case 1:
                print("========== Add Category ==========")

                categoryId = int(input("Enter Category ID :: "))
                categoryName = input("Enter Category Name :: ")

                addCategory(categoryId, categoryName)

            case 2:
                print("========== Display All Category ==========")

                displayCategory()

            case 3:
                print("========== Search Category ==========")

                categoryId = int(input("Enter Category ID to Search :: "))

                searchCategory(categoryId)

            case 4:
                print("========== Update Category ==========")

                categoryId = int(input("Enter Category ID to Update :: "))
                categoryName = input("Enter Updated Category Name :: ")

                updateCategory(categoryId, categoryName)

            case 5:
                print("========== Delete Category ==========")

                categoryId = int(input("Enter Category ID to Delete :: "))

                deleteCategory(categoryId)

            case 6:
                break

            case _:
                print("Invalid Choice")
