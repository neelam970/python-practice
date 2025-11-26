# Create a dictionary to store details of a student (name, age, course) and print it.
student={"name":"neelam","age":23,"course":"Mca"}
print(student)
print(type(student))

# Access and print the value of a specific key (like "name").
student={"name":"neelam","age":23,"course":"Mca"}
print(student['name'])

# Add a new key-value pair "city": "Delhi" to the dictionary.
student={"name":"neelam","age":23,"course":"Mca"}
student["city"]="delhi"
print(student)

# Update the value of "age" to 25.
student={"name":"neelam","age":23,"course":"Mca"}
student['age']=21
print(student)

# Remove a specific key from the dictionary using pop().
student={"name":"neelam","age":23,"course":"Mca"}
student.pop("course")
print(student)

# Use len() to print the number of items in the dictionary.
student={"name":"neelam","age":23,"course":"Mca"}
student1=len({"name":"neelam","age":23,"course":"Mca"})
print(student1)

# Check if a particular key (like "name") exists in the dictionary using in.
student={"name":"neelam","age":23,"course":"Mca"}
if "name" in student:
    print("exists")
else:
    print("not exists")


    # Intermediate Level

# Create a dictionary and print all keys using .keys() method
student={"name":"neelam","age":23,"course":"Mca"}
print(student.keys())

# Print all values using .values().
student={"name":"neelam","age":23,"course":"Mca"}
print(student.values())

# Print all key-value pairs using .items().
student={"name":"neelam","age":23,"course":"Mca"}
print(student.items())

# Make a copy of a dictionary using .copy() and print both to show they are different objects.
dict_1={"name":"neelam","age":23,"course":"Mca"}
dict_2=dict_1.copy()
print(dict_1 is dict_2)

# Use get() to safely access a value for a key that might not exist.
student={"name":"neelam","age":23,"course":"Mca"}
print(student.get('city'))

# # Use a for loop to print each key and its corresponding value.
student={"name":"neelam","age":23,"course":"Mca"}
for key, value in student.items():
    print(key,":",value)

# # Create two dictionaries and merge them using .update().
dict_1={"name":"neelam","age":23,"course":"Mca"}
dict_2={"name":"komal","age":24,"course":"Mca","city":"patna"}
dict_1.update(dict_2)
print(dict_1)

# Write a program to find the key with the maximum value in a dictionary.
student = {"math": 90, "eng": 85, "science": 35}
print(max(student, key=student.get))   # Output: science


# # Write a program to count the frequency of each character in a string using a dictionary.
# dict_1={"name":"neelam","age":23,"course":"Mca"}
# print(dict_1.count("name"))

# Create a nested dictionary (e.g., student = {"name": "Neelam", "marks": {"math": 90, "eng": 85}}) and access inner values.
student={"name": "Neelam", "marks": {"math": 90, "eng": 85}}
print(student['marks'].values())

# Remove all items from a dictionary using .clear().
dict_1={"name":"neelam","age":23,"course":"Mca"}
dict_1.clear()
print(dict_1)

# Write a program to sum all values in a dictionary where values are numeric.
student={'a':3,'b':5,'c':9}
print(sum({'a':3,'b':5,'c':9}.values()))

# Write a Python program to convert two lists (keys and values) into a dictionary.
keys=['a','b','c','d']
values=[1,2,3,4]
result=dict(zip(keys,values))
print(result)