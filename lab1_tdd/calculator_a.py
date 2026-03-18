def Add(numbers):
    if numbers == "":
        return 0

    parts = numbers.split(",")
    return sum(int(x) for x in parts)

