def Add(number):
    if number == "":
        return 0

    return sum(int(x) for x in number.split(","))
        