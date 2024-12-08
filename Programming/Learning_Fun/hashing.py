import bcrypt


pw= 'Password123' 

# bcrypt function to hash password. first encode to bytes, then add salt, then decode
hashed= bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode() 


given = input('Please enter a password: ')

if bcrypt.checkpw(given.encode(), hashed.encode()): #boolean returns true or false. 
    print('Access Granted')
else:
    print('Access Denied')