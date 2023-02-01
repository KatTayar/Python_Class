#Exercise 3: Write a program called SoftwareSales.py for the following problem. “A software company sells a package that retails for $99. Quantity discounts are given according to the following table:  

 #   Quantity                    Discount

           #   10 – 19                  20%

           #   20 – 49                 30%

           #   50 – 99                 40%

           #   100 or more 50%

#Write a program that asks the user to enter the number of packages purchased. The program should then display the amount of discount (if any) and the total amount of the purchase after the discount.” For example, if the user entered 24, the program would print:

 #  'You purchased 24 packages resulting in a discount of $712.8'

 #  'Your total payment after discount is $1663.2'

#Problem adapted from Gaddis textbook Programming Exercise 4.8

def software_sales():
    price = 99
    packages = int(input("Enter the number of packages purchased: "))
    if packages >= 10 and packages <= 19:
        discount = 0.2
    elif packages >= 20 and packages <= 49:
        discount = 0.3
    elif packages >= 50 and packages <= 99:
        discount = 0.4
    elif packages >= 100:
        discount = 0.5
    else:
        discount = 0
    discount_amount = price * packages * discount
    total = price * packages - discount_amount
    print(f"You purchased {packages} packages resulting in a discount of ${discount_amount:.2f}")
    print(f"Your total payment after discount is ${total:.2f}")

software_sales()
