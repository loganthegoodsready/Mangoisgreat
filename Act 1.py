# Lab task 1:
age = float(input("How old is your dog in human years? "))
if age == 2:
    print("Your dog is", 21, "years old")
elif age > 2:
    print("Your dog is", (age-2)*4 + 21, "years old")
elif age <= 1:
    print("your dog is a puppy")
elif age >1 and age <2:
    print("your dog is an adolescent")

# else statement N/A
