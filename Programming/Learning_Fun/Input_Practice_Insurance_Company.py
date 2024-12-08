''' Create a python file that asks an insurance company the following inputs:


    Insurance company name

    Number of employees

    location (city, OR country, OR state)

    Lowest price for a policy

    The highest price for a policy

The output will consist of a prompt almost like an ad. For example:

"We are Company LLC located in India. Our 55 employees can help you find the policy that is right for you with policies ranging from $15 to $300 per month!" '''

name= input('Hello, What is the name of your company?: ')
#Name of Company Input

employees= input('How many employees are in your company?: ')
#Amount of employees input

location= input('What is the location of your company?(City, OR country, OR state): ')
#location input

lowest_price= input('What is the lowest price for your policy?: ')
#lowest price input

highest_price= input('What is the hightest price for your policy?: ')
#highest price input

print(f'Hello, welcome to {name}, we are an insurance company located in {location}. Our company has {employees} hard working employees. Our highest policy monthly rate is {highest_price}, and our lowest policy monthly rate is {lowest_price}. Thank you for your business.')