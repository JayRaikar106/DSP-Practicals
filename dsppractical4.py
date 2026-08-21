#tuple operations
t = (10, 20, 30, 40)
print ("Tuple element:", t[1])

#set operations
s = {1, 2, 3, 4}
s.add(5)
s. remove(2)
print("set:",s)

#Dictionary operations
student = {"name" : "amit", "age" : 20, "marks": 85}

#Accesing values
print("name:", student["name"])

#updating values
student["marks"] = 90

#addding new keys
student["city"] = "Nagpur"

#Deleting key
del student["age"]

print("updating Dictionary:", student)

#Built in functions
print("Dictionary keys:", student.keys())
print("Dictionary values:", student.values())
print("Dictionary items:", student.items())