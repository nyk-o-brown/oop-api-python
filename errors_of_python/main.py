try:
    
    with open('moldovia.txt', 'r') as file:
        content = file.read()

except FileNotFoundError  :
    print("you file is non existant bitch")
    print("maketh dureth the fileth existeth")      
    
#finally:
    #with open('errors_of_python/moldovia.txt', 'r') as file:
        #content = file.read()
else:
    print("mate i could not find your file eh")        
            