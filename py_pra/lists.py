#lists [arrays] in python
#methods eg- list.method() vs function eg- print()

fruits = ['apple','banana','orange']
print(fruits)
fruits.append('pineapple')      #  .append() - add the string at the end of the string  - a method
print(fruits)

#   indexing   gives a single value of the specified index
print(fruits[0])  
print(fruits[-1])   # negative numbers give index from the end or backwards
print(fruits[0:4:2])  # 0:4:2 here 2 is step (to skip some things)(works in negative)
print(fruits[::-1])   # can revers a list of arrays
# slicing

print(fruits[0:2])  # 0 is included and 2 is not included
#   -------------------check it----------------
#  print(fruits[0:-1])  
#   or
# print(fruits[0:len(fruits)-1])    # len() is a function

print('hi i am checking'[0:10])   # works on strings


 