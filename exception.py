age = int(input("Enter Your Age : "))

try:
    if age<10 or age>18:
        # raise ValueError("You are not eligible , your age must be between 10-18")
        print("you are not eligible")
    else:
        print("Welcome to the club")
except Exception as Err:
    print(f"an error occures as {Err}")

print("The Club will start soon")