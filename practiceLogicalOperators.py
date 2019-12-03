'''
Created on Dec 1, 2019

@author: ITAUser
'''
print("AND") 

a = True and True 

print(a) 
#True 

a = True and False 

print(a) 
#False , both sides of the 'and' need to be the same 

a = False and False 

print(a) 
#False bc both sides of a are going to be false 




print("OR")

a = True or True  

print(a) 
#true bc both have to be true 

a = True or False
#returns true bc only one side is needed to be true 
print(a) 

a = False or False 
#false, neither side is true 
print(a) 

print("NOT")

a = not False 

print(a) 
#true 

a = not True 

print(a) 
#False bc it is not true  


print("COMPARISONS")

a = 4 == 5 and 5 == 5 

print(a) 
#false          #true 
#overall is false because one is false using and 

a = 5 == 5 and 5 == 5 

print(a) 
#true          #true 
#true bc both are true using 'and' rules


a = 4 == 5 or 5 == 5 

print(a) 
#false           #true 
#overall is true bc 'or' only needs one side to be true 

a = 5 == 5 or 5 == 5 

print(a) 
#true          #true 
#overall true 


a = 4 == 5 or 4 == 5 

print(a) 
#false        #false 
#both are false, for 'or' u need one to be true 


print("NOT")

a = not 4 == 5 
#       False 
print(a) 
#final answer is "True" because it is NOT FALSE 