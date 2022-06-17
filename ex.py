#Write your code below this line 👇
def prime_checker(number): 
   
    for i in range (2, number-1): 
        if number % i == 0: 
            indicator = 1
        else: 
            indicator = 0
    
    if indicator == 1: 
        print("It's a prime number.")
    else: 
        print("It's a prime number.")
            




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)