print("Welcome to the online store! Let's start shopping!")
shopping_cart_item = []
shopping_cart_price = []

checker = "Y"

while checker == "Y":
    item = input ("Please Enter the name of the item: ")
    while item == "":
        item = input ("INVALID INPUT!, Please Enter the name of the item: ")
    price = float(input("Please enter the price of the item: "))
    while price <= 0:
        price = float(
            input("INVALID INPUT!, Please Enter the price of the item:"))
    
    shopping_cart_item.append(item)
    shopping_cart_price.append(price)

    print(f"{item} was added to your shopping cart.")
    checker = input("\nDo you want to add another item? (Y/N): ")


total = 0
print("\nItem List: ")

for items in shopping_cart_item:
    print(f"1. {items}")

for total_price in shopping_cart_price:
    total = total + total_price

print(f"\nThank you afor shopping with us! Your total cost is ${total}")
