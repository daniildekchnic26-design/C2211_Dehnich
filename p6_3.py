try:
    print("start code")
    print(10 / 0)
    print("No errors")
except (NameError, ZeroDivisionError):
    print("We nave Error")

print("code after capsule")