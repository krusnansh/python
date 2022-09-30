# dictionary {key:value}  are ordered in python
# f in print before "" or '' are used to tell that we are taking values form a function
# lambda is a anonymous function
# to call a lambda function add () after the usually calling of the value from the key  eg- {person['networth']()}

def introducer():   # def is used to define a function

    person = {
        'name':'krusnansh',
        'age':'19',
        'college':'jims',
        'assets':100,
        'debt':50,
        'networth': lambda: person['assets'] - person['debt']

}
    print(f"my name is {person['name']},i am {person['age']} years old and currently studying in {person['college']} and a networth of {person['networth']()} ")

#   print(person.values())   #  print all the values 
 #   print(person.keys())        # print all the key
  #  print(list(person.values()))    # print all the value as a list


    # dictonary and lists are mutable
    #person['name']='aj'
    #print(person['name'])

introducer()  # calling the function