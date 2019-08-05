# ZIP

# Zipping
print("ZIP")
name = ["A", "B", "C", "D"] 
_id = [1, 2, 3, 4] 
score = [40, 50, 60, 70]

res = list(zip(_id, name, score))
print(res)

# Unzipping
n, i, s = zip(*res)
print(n)
print(i)
print(s)


# ENUMERATE
print("\nENUMERATE")
string = "python"
  
# creating enumerate objects 
obj1 = enumerate(name) 
obj2 = enumerate(string) 
  
print("Type:", type(obj1))
print(list(obj1))
  
# changing start index to 100 from 0 
print(list(enumerate(string,100)))


# Importing functions from other files
print("\nIMPORTING FUNCTIONS FROM OTHER FILES")
from func_demo import add

add(10, 20)