def Add(number):
    if number == "":
        return 0
    result = 0
    parts = number.split(",")
    for x in parts:
        if x == "":
            raise ValueError("Bad string!")
        result += int(x)
    return result

