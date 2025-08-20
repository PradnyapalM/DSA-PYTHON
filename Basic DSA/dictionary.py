# DAY 18

"""
Map(in c,c++ and Java)
Hashmap is nothing but the Dictionary in Python
1.If we want to represent the group of objects as key-value pair
then we should go for dictionary.(roll_no-name, ip_add-Domain name)
2.Duplicate keys are not allowed but duplicate values are allowed
3.Hetrogenious objects are allowed for both keys and values.
4.Insertion order is not preserved.
5.Dictionary are Mutable.
6.Dictionary are Dynamic.
7.Indexing or slicing ar not applicable.
"""

#  Topic How to create Dictionary in 

# d = {} 
# d = dict()
#  We are creating empty dict we can add entries as follows
# d[100] = "Akash"
# d[200] = "Atul"
# d[300] = "Ajay"

# print(d) #{100: 'Akash', 200: 'Atul', 300: 'Ajay'}

"""
syntax:--> d[key] = value
d={key:value}
"""

# Topic How to access data from dictionary
# ans--> we can access data by using keys

# data={100: 'Akash', 200: 'Atul', 300: 'Ajay'}

# print(data[300]) #Ajay
# print(data[200]) #Atul

# Note:-- If the specefied key is not available the it gives error
# print(data[800]) #KeyError:

# Q Check whether the key is present or not in the dictionay
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay'}
# print(data)
# if 400 in data:
#     print(data[400]) # Ajay
# else:
#     print("Value is not avaiable in the data")

# Topic How to update the dictionary
"""
d[key] = Value
1.If the key is not available then a new entry will be added to
the dictionary with the specified key-value pairs.
2.If the key is already avilable then old value will be
replaced with new value
"""
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay'}

# print(data)
# data[400] = "Aman"
# print(data) #{100: 'Akash', 200: 'Atul', 300: 'Ajay', 400: 'Aman'}
# data[100] = "Mia"
# print(data) #{100: 'Mia', 200: 'Atul', 300: 'Ajay', 400: 'Aman'}


# Topic how to delete elements from the dictionary
"""
syntax:--> del d[key]
If delete entry associated with the specified key. If the key is not 
available then will get the value error.
"""
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay'}
# print(data) #{100: 'Akash', 200: 'Atul', 300: 'Ajay'}

# del data[100]
# print(data) #{200: 'Atul', 300: 'Ajay'}

# del data[400]
# print(data) #KeyError


#  Topic Important function of Dictionary

# 1> dict()--> To create a dictionary
# d = dict() #--> create empty dictionary

# 2 len()--> Returns the no of items in the dict.
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay'}
# print(len(data)) #3

# 3 clear()--> Clear all the elements (syntax d.clear())
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay'}
# print(data)
# print(data.clear())#None

# Q What is value associated of 100?
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay'}
# # print(data[100]) #Akash
# print(data.get(100)) #New Method (VVV__IMP) #Akash
# # It returns a NULL or NONE if value is not present
# print(data.get(500)) #None

# 4. pop()--> It removes the key value and return corrosponding value
#  data.pop(key)
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay'}
# print(data)
# print(data.pop(300)) #Ajay
# print(data) #{100: 'Akash', 200: 'Atul'}

# 5. popitems():- It will delete lasy key-value item from dictionary
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay',500:"Shyam"}
# print(data)
# print(data.popitem())#(500, 'Shyam')
# print(data) #{100: 'Akash', 200: 'Atul', 300: 'Ajay'}

# 6. keys():--> It will returns all the keys associated with dict
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay',500:"Shyam"}
# print(data)
# print(data.keys()) #dict_keys([100, 200, 300, 500]
# for k in data.keys():
#     print(f"key-->{k}")

# 7. values():--> It will returns all the values associated with dict
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay',500:"Shyam"}
# print(data)
# print(data.values()) #dict_values(['Akash', 'Atul', 'Ajay', 'Shyam'])
# for val in data.values():
#     print(f"Values-->{val}")

# 8 items()--> It returns list of tuple representing the key-value pairs
# [(k,v),(k,v)]
# data={100: 'Akash', 200: 'Atul', 300: 'Ajay',500:"Shyam"}
# print(data)
# print(data.items()) #dict_items([(100, 'Akash'), (200, 'Atul'), (300, 'Ajay'), (500, 'Shyam')])

# for key, val in data.items():
#     print(f"key-->{key}---value-->{val}")

"""
key-->100---value-->Akash
key-->200---value-->Atul
key-->300---value-->Ajay
key-->500---value-->Shyam
"""

# Q WAP to take dictionary i/p from keyboard and print sum of values.

# data = eval(input("Enter some dictionary: "))
# print(data)
# sum_out = sum(data.values())
# print(sum_out)










