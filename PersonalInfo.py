# Personal Information Manager - Week 1 Project

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
hobbies = input("Enter your hobbies (comma-separated): ")

# Convert hobbies into list
hobbies_list = [h.strip() for h in hobbies.split(",")]

print("\n====== PERSONAL INFORMATION ======")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"City    : {city}")
print("Hobbies : ", end="")

if hobbies_list:
    print(", ".join(hobbies_list))
else:
    print("None")

print("===================================\n")