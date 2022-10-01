# f in print before "" or '' are used to tell that we are taking values form a function
# lambda is a anonymous function
# to call a lambda function add () after the usually calling of the value from the key  eg- {person['networth']()}
# use pass if don't know what to write

def name(a,b):
    print(f'your name is {a} and age is {b}')

name("kru",6)


# to give default value to the varables in case of no input assign the value in the function like below
def name(a,b='10'):
    print(f'your name is {a} and age is {b}')

name("kru")# here not giving the value of b to run the default value
name("kru",8) # entering the value of b 

# named arguments --  the order of the input value dosen't matter
# if you give the variable name in the input and assign value to them 

name(b=4,a='yo')

'''
used for multiline comments

'''

