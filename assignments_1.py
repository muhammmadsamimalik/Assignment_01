
print("Name: Muhammad Sami\nFather:\nDOB 26/12/2006")

name = "Muhammad Sami"
age3 = 18
height = 164
education = "Matriculation"
city = "Karachi"
goal = "cloud data engineer"
print(f"MY name is {name}. I am {age3} years old. My height is {height}. I have done {education}. I live in {city}. my goal is to become a {goal}.")

a = 10 
b = 13

# arithmetic

print(a + b)
print(a - b)    
print(a * b)
print(a / b)
print(a % b)    
print(a ** b)

# comparison

print(a == b)
print(a != b)       
print(a > b)
print(a < b)        
print(a >= b)
print(a <= b)   

# assignmen

a += b 
print(a)
a -= b      
print(a)
a *= b
print(a)        
a /= b
print(a)    
a %= b  
print(a)    
a **= b
print(a)    


# logical

c = True
d = False       
print(c and d)
print(c or d)       
print(not c)    
print(not d)


english = 78
islamiyat = 85
math = 90   

obtained_marks = english + islamiyat + math
total_marks = 300   
percentage = (obtained_marks / total_marks) * 100
print("Percentage:", percentage)


years = int(input("Your year of services: "))
if years  >= 5:
    salary = int(input("Your salary: "))
    bonus = (5 / 100) * salary
    print("Your bonus is:", bonus)
else:
    print("No bonus, since your service is 5 years or less.")


age2 = int(input("Enter your age:"))
if age2 >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


number = int(input("Enter a number: "))          
if number % 2 == 0:
    print("The number is even.")    
else:
    print("The number is odd.")

number2 = int(input("Enter a number: "))
if number2 % 7 == 0:
    print("The number is divisible by 7.")
else:   
    print("The number is not divisible by 7.")  


number3 = int(input("Enter a number: "))
if number3 % 5 == 0:
    print("hello")
else:
    print("bye")    

number4 = int(input("Enter a number: "))
last_digit = number4 % 10 
print("The last digit is:", last_digit)

length = int(input("Enter length"))
breadth = int(input("Enter breadth"))
if length == breadth:
    print("It is a square")
else:
    print("It is a rectangle")

val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))   
if val1 > val2:
    print(f"{val1} is greater")
elif val2 > val1:
    print(f"{val2} is greater")
else:
    print("chala jaaa bhai")

unit = int(input("How many units you want to buy:"))
cost1 = unit * 100
if cost1 > 1000:
    discount = cost1 *0.10
    cost1 -= discount
    print(f"your total cost after discount is {cost1}")
else:
    print(f"your total cost is {cost1}")

marks = int(input("Enter your marks: "))
if marks >= 80:
    print("A")
elif 60 <= marks < 80:
        print("B")
elif 50 <= marks < 60:
        print("C")
elif 45 <= marks < 50:
        print("D")
elif 25 <= marks < 45:
        print("E")
else:
    print("F")

classes_attended = int(input("Enter number of classes attended: "))
total_classes = int(input("Enter total number of classes: ")) 
cause = (input("do you have a medical cause? ('Y or N'): ")).upper()
percentage = (classes_attended / total_classes) * 100
print(f"Your attendance percentage is: {percentage}%")
if percentage >= 75: 
    print("You are allowed to sit in the exam.")
elif cause == "Y":
        print("You are allowed to sit in the exam.")
else:   
    print("You are not allowed to sit in the exam.")


leapyear = int(input("Enter a year: "))
if leapyear % 400 == 0:
        print(f"{leapyear} is a leap year.") 
elif leapyear % 100 == 0:
        print(f"{leapyear} is not a leap year.") 
elif leapyear % 4 == 0:
    print(f"{leapyear} is a leap year.")   
  
else:
    print(f"{leapyear} is not a leap year.")


age = int(input("Enter your age: "))
gender = input("Enter your gender (M or F): ").upper()
martial_status = input("Enter your marital status (Y or N): ").upper()
if gender == "F":
    print("You can work in urban areas only.")  
elif gender == "M" and 20 <= age <= 40:
        print("You can work anywhere.") 
elif gender == "M" and 40 < age <= 60:
        print("You can work in urban areas only.")  

else:
    print("ERROR")
    

keunit = int(input("Enter the number of units :"))
if keunit <= 100:
    print("no charges")
elif keunit <= 200:
        cost = keunit * 5
        print(f"your total cost is {cost}")
elif keunit > 200:
    cost = keunit * 10 
    print (f"your total cost is {cost}")
    
person1 = int(input("Enter age of person 1: "))
person2 = int(input("Enter age of person 2: "))
person3 = int(input("Enter age of person 3: "))

oldest = max(person1, person2, person3)
youngest = min(person1, person2, person3)

print(f"The oldest age is {oldest}")
print(f"The youngest age is {youngest}")




    
    



