## Part One: Getting started

#  Exercise 1 | Print Brothers Names in Order

print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print('Timo')
print("Tuomas\n")

# Exercise 2 | Print Row, row, row your boat properly

print("Row, row, row your boat, \n" \
"Gently down the stream.\n" \
"Merrily, merrily, merrily, merrily, \n" \
"Life is but a dream.")

# Exercise 3 | Write a program to calculate number of minute in a year

print("Number of minutes in a year:", 1 * 365 * 24 * 60)

# Exercise 4 | Printception

print('\nprint("Hello there!")')

## Part Two: Information from the user

#  Exercise 1 | Input from User Paul

name = input("\nWhat is your name? ")
print(name+ "\n" +  name)

# Exercise 2 | Name and Exclamation Marks

name = input("\nWhat is your name? ")
print("!"+name+"!"+name+"!")

# Exercise 3 | Name and address

name = input("Give name: ")
familyname =  input("Family name: ")
staddress = input("Street address: ")
citypostalcode = input("City and postal code: ")
print('\n' + name + " " + familyname + "\n" + staddress + "\n" + citypostalcode )

# Exercise 4 | Fix the code: Uterrances

partone = input("The 1st part: ")
parttwo = input("The 2nd part: ")
partthree = input("The 3rd part: ")

print(partone + "-" + parttwo + "-" + partthree + "!")

# Exercise 5 | Story

name = input("Please type in a name: ")
year = input("Please type in a year: ")

print(name + " is a valiant knight, born in the year " + year + ". One morning \n" + name + " woke up to an awful racket: a dragon was approaching the \nvillage. Only " + name + "could save the village's residents.")

## Part 3: More about variables

# Exercise 1 | Extra Space
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

# Changed the print commands to include f-string in them to print correctly
print(f"my name is {name}, I am {age} years old")
print("\nmy skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})")
print(f"\nI am looking for a job with a salary of {lower}-{upper} euros per month")

# Exercise 2 | Arithmetics

# numbers defined for arithmetic
x = 27
y = 15

# Addition, Subtraction, Multiplication, Division
add = print(f"{x} + {y} = {x + y}")
sub = print(f"{x} - {y} = {x - y}")
mult = print(f"{x} * {y} = {x * y}")
div = print(f"{x} / {y} = {x / y}")

# Exercise 3 | Fix the Code: Print a Single Line

# Fixing the way it prints so no line change occurs by adding end=""

print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)

## Part 4: Arithmetic Operations

# Exercise 1 | Times Five

# Learning about using the integer string and input
num = int(input("Please type in a number: "))
mult = print(f"{num} times 5 is {num * 5}")

# Exercise 2 | Name and Age

# Give name & year
name = input("What is your name? ")
year = int(input("Which year were you born? "))

# Print out desired statement about age and name
statement = print(f"Hi {name}, you will be {2021 - year} years old at the end of the year 2021")

# Exercise 3 | Seconds in a day

# Stores amount of days as integer
days = int(input("How many days? "))

# Prints out seconds with corresponding days given
seconds = print(f"Seconds in that many days: {days * 86400}")

# Exercise 4 | Fix the code:Product

# Creating a product variable for multiplication
product = 1

# Multiplying it by previously inputed number
product *= int(input("Please type in the first number: "))
product *= int(input("Please type in the second number: "))
product *= int(input("Please type in the third number: "))

# Prints out the product
print("The product is", product)

# Exercise 5 | Sum and Product

# Making inputs into integers for math later
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

# Prints out the addition and multiplication
print(f"The sum of the numbers: {num1 + num2}")
print(f"The product of the numbers: {num1 * num2}")

# Exercise 6 | Sum and Mean

num = 0
num += int(input("Number 1: "))
num += int(input("Number 2: "))
num += int(input("Number 3: "))
num += int(input("Number 4: "))

print(f"The sum of the numbers is {num} and the mean is {num/4}")

# Exercise 7 | Food Expenditure

# Storing data into variables for later use
times = int(input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch? "))
grocery = float(input("How much money do you spend on groceries in a week? "))

print(f"Average food expenditure:")
print(f"Daily: {(grocery + lunch* times)/7} euros")
print(f"Weekly: {(times * lunch) + grocery} euros")

# Exercise 8 | Students in Groups

students = int(input("How many students on the course? "))
group = int(input("Desired group size? "))
size = int(-(-students // group))

print(f"Number of groups formed: {size}")

## Part 5: Conditional Statements

# Exercise 1 | Orwell

num = int(input("Please type in a number: "))
orwell = 1984

if num == orwell:
    print("Orwell")

# Exercise 2 | Absolute Value

num = int(input("Please type in a number: "))

if num > 0:
    print(f"The absolute value of this number is {num}")

if num < 0:
    print(f"The absolute value of this number is {-1*num}")

if num == 0:
    print(f"The absolute vlaue of this number is {num}")

# Exercise 3 | Soup or No Soup

name = input("Please tell me your name: ")

if name == ("Jerry"):
    print("Next please!")

if name != ("Jerry"):
    num = (int(input("How many portions of soup? ")))
    print(f"The total cost is {num * 5.9}")
    print("Next please!")

# Exercise 4 | Order of Magnitude

num = int(input("Please type in a number: "))

if num < 1000:
    print("This number is smaller than 1000")
    if num < 100:
        print("This number is smaller than 100")
        if num < 10:
            print("This number is smaller than 10")
print("Thank you!")

# Exercise 5 | Calculator

num1 = int(input("Number 1: "))
num2 = int(input('Number 2: '))
op = input("Operation: ")

# Creating Boolean statements for when user gives input
add = (op == "add")
sub = (op == "subtract")
mult = (op == "multiply")

# If statements that check and see if boolean statements are true and then execute the code
if add == True:
    print(f"{num1} + {num2} = {num1 + num2}")
if sub == True:
    print(f"{num1} - {num2} = {num1 - num2}")
if mult == True:
    print(f"{num1} * {num2} = {num1 * num2}")

# Exercise 6 | Temperatures

fahr = int(input("Please type in a temperature (F): "))

#Convert F into C
cels = (fahr - 32)*(5/9)

# Print out conversion
print(f"{fahr} degrees Fahrenheit equals {cels} degrees Celsius")

# Boolean statement to see if celsius conversion is lower than 0
brr = (cels < 0)


if brr == True:
    print("Brr! It's cold in here!")

# Exercise 7 | Daily Wages

# Make a float becayse hours may not be int
hour = float(input("Hourly wage:"))
worked = int(input('Hours worked:'))

# ask for the day to then be checked in boolean
day = input("Day of the week:")

# boolean for specifically sunday
sun = (day == "Sunday")

# If statements for specific day
if sun == True:
    print(f"Daily wages: {hour*worked*2} euros")

if sun == False:
    print(f"Daily wages: {hour*worked} euros")

# Exercise 8 | Loyalty Bonus
points = int(input("How many points are on your card? "))

# Had to fix the error by creating this boolean
percent = (points < 100)

if percent == True:
    points *= 1.1
    print("Your bonus is 10 %")

if percent == False:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

# Exercise 9 | What to Wear Tomorrow

temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no):")

cond = (rain == "yes")

print("Wear jeans and a T-shirt")

if temp <= 20:
    print("I recommend a jumper as well")
if temp <= 10:
    print("Take a jacket with you")
if temp <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if cond == True:
    print("Don't forget your umbrella!")

# Exercise 10 | Solving a Quadratic Equation
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

# To use exponents use "**"
x1 = float((-b + sqrt(b**2 - 4*a*c))/(2*a))
x2 = float((-b - sqrt(b**2 - 4*a*c))/(2*a))

print(f"The roots are {x1} and {x2}")

