
try:
    x = 10/0
except ZeroDivisionError:
    print("Error there is division by zero in ur code")
else:
    print("Ur code is running successfully")
finally:
    print("Proceed to next step")

