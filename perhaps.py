# Hiesenberg Uncertainity Principle



def calci(val, value):
    value = float(value)
    if val == "x":
        p = (5.2728 * (10**-35)/value)
        return p
    elif val == "p":
        x = (5.2728 * (10**-35)/value)
        return x
    else:
        return("Invalid Input")