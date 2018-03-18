# implementation of Dictionary Data type:
student={'name':'hemant','rollNumber':77,'courses':['Math','Chemistry','Physics']}
print(student)
print(student['name'])
print(student.keys())
print(student.values())
print(student.items())

print(student.get('hobby','Not Found'))

student['name']='Harry'
print(student)

# Trying loops in Dictionary:
for keys in student:
    print(keys)
print('============================================')
for values in student:
    print(values)    
print('------------------------------------------')

for keys,value in student.items():
    print(keys,value)

 
    
    
    







