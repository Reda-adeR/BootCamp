str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
str = str.split(", ")
print("Number of manufactureres : ", len(str))

str = sorted(str, reverse=True)

print("Manufactureres at reverse order : ", ", ".join(str))

have_o = 0
havnt_i = 0

for s in str:
    if "o" in s:
        have_o += 1
    if "i" not in s:
        havnt_i += 1
print("Number of manufacturers that have 'o' : ", have_o)
print("Number of manufacturers that don't have 'i' : ", havnt_i)

str = [
    "Honda", 
    "Volkswagen", 
    "Toyota", 
    "Ford Motor", 
    "Honda", 
    "Chevrolet", 
    "Toyota"]
str = set(str)
print("Unique ", len(str), " manufacturers : ", ",".join(str))

str = sorted(str)

for i in range(len(str)):
    str[i] = str[i][::-1]
    
print("Manufacturers in reverse order : ", ",".join(str))