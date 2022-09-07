# Ask the user for their name 
username = input("what is your name? ") 
print()
# Ask the user for their favourite interger 
fav_num = int(input("what is your favourite interger? ")) 
print()
# Double, halve and square the number
double = fav_num * 2
halved = fav_num / 2 
squared = fav_num * fav_num 

# Greet the user 
print("hi {}, your favourite number is {}".format(username, fav_num))
print()
# output the result of doubling, 
# halving and squaring their favourite number 
print("double {} is {}".format(fav_num, double)) 
print()
print("half {} is {}".format(fav_num, halved)) 
print()
print("{} squared is {}".format(fav_num, squared))
print()