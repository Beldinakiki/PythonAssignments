# Function to calculate discount if less than 20% 
def calculate_discount(price,discount_percent):
    if discount_percent <= 20:
        discount = price * (discount_percent / 100)
        discounted_price = price - discount
        return discounted_price
    else:
        return price

# Prompt user to enter price and discount percentage
price = int(input("Enter the total price:"))
discount_percent = int(input("Enter the discount percentage:"))
#Apply function 
discounted_price = calculate_discount(price,discount_percent)
print("The final price is: ", discounted_price)