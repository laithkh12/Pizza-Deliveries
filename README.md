# 🍕 Python Pizza Deliveries

Welcome to the **Python Pizza Deliveries** program! This interactive script allows users to customize their pizza orders by selecting the size, adding pepperoni, and opting for extra cheese. The program then calculates the total cost of the order.

---

## 📋 Features

- **Customizable Pizza Size**: Choose from small, medium, or large pizzas.
- **Add Pepperoni**: Decide whether to include pepperoni with additional costs.
- **Extra Cheese Option**: Add extra cheese for a small additional fee.
- **Total Bill Calculation**: The program computes the final bill based on the user's choices.

---

## 🔍 Code Overview

The program prompts the user for their pizza preferences and calculates the total cost based on their selections. Below is a breakdown of how it works:

1. **Size Selection**: User inputs pizza size (S, M, or L) and the program sets a base price.
2. **Pepperoni Option**: If the user wants pepperoni, the program adds the corresponding cost based on the selected size.
3. **Extra Cheese**: If requested, an additional cost is added for extra cheese.
4. **Final Bill**: The total bill is displayed at the end.

### Code Snippet

```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N.\n")
extraCheese = input("Do you want extra cheese? Y or N.\n")

# Calculate the bill based on size choice
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print("Please Choose one of the following: S, M or L")

# Add to the bill based on pepperoni choice
if pepperoni == "Y":
    if size == 'S':
        bill += 2
    elif size == 'M':
        bill += 3
    elif size == 'L':
        bill += 4

# Add to the bill based on extra cheese choice
if extraCheese == 'Y':
    bill += 1

print(f'Your final bill is: {bill}$')
```

## 📋 Usage Instructions
1. Clone the Repository:
```bash
git clone https://github.com/your-username/python-pizza-deliveries
cd python-pizza-deliveries
```
2. Run the Program: Execute the script in a Python environment:
```bash
python pizza_delivery.py
```
3. Follow the Prompts:
  - Input the size of the pizza (S, M, or L).
  - Indicate if you want pepperoni and extra cheese (Y or N).
  - The program will output your final bill.

## 💡 Example Output
```bash
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L:
M
Do you want pepperoni on your pizza? Y or N.
Y
Do you want extra cheese? Y or N.
N
Your final bill is: 23$
```

## ⚙️ Customization
  Feel free to modify the prices, add new options, or enhance the functionality of the pizza delivery system!

## 📜 License
  This project is licensed under the MIT License. See the LICENSE file for details.


Enjoy your pizza! 🍕✨
