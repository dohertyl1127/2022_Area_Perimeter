valid = False 
while not valid: 
    
    error = "Please enter a number ths is more than 0"

    try:

        response = float(input("Enter a number: ")) 
        
        if response > 0: 
            valid = True 
        
        else: 
            print(error)
            print() 
    
    except ValueError: 
        print(error)

        
