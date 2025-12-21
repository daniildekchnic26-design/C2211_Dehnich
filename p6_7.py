def cheker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry, we can't work with {type(var_1)}, we need class str")
    else:
        return var_1


    f_var = 10
    cheker(f_var)
