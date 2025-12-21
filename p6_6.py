try:
    print("start code")
    print(10/0)
    print("No errors")
except NameError:
    print("We nave an error")
else:
    print("No priblem")
finally:
    print("Fin code")