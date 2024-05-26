import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
           "q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F",
           "G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",
           "W","X","Y","Z"]
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','~']

print("Welcome to the password generator ")
num_letter = int(input("How many letters you want in your password : "))
num_number = int(input("How many number you want in your password : "))
num_symbol = int(input("How many symbol you want in your password : "))
# ezy_level
# password= ""
# for char in range(1,num_letter + 1):
#     rand_char = random.choice(letters)
#     password += rand_char
# for num in range(1,num_number+1):
#     rand_num = random.choice(numbers)
#     password += str(rand_num)
# for sym in range(1,num_symbol+1):
#     rand_sym = random.choice(symbols)
#     password += rand_sym
# print(password)

# hard level

password= []
final = ""
for char in range(1,num_letter + 1):
    rand_char = random.choice(letters)
    password.append(rand_char) 
for num in range(1,num_number+1):
    rand_num = random.choice(numbers)
    password.append(rand_num)
for sym in range(1,num_symbol+1):
    rand_sym = random.choice(symbols)   
    password.append(rand_sym)
for pascode in password:
    rand_pass = str(random.choice(password))
    final += rand_pass
print(final)