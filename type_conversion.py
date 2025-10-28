
birth_year = input("Your birth year : ")
birth_year = int(birth_year)
age = 2025 - birth_year
print(age)

# int() => converts the string to input
print(int(birth_year))
# float() => converts the string to float
print(float(birth_year))
# int() => converts the string to input
print(bool(birth_year))
#type() => prints the type of variable
print(type(birth_year))

#what if a i want to convert an integer to string ?
#str()=> convets the other type to string
salary = 200000
salary = str(salary)
print(type(salary))

#assignment 03
# ask a user their weight(in pounds) , convert it to kg and print in termianl

user_weight = input('Please enter your weight(in pounds): ')

user_weight = float(user_weight) * 0.453592 #one catch part is => you need to convert type while making operation. here , the string must need to convert to float

print('Your weight in kilo gram : ' + str(user_weight)) # another catch is you just can con-cotanate string with string by '+' . not integer with string.