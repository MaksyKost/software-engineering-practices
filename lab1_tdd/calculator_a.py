def Add(numbers):
    if numbers == "":
        return 0
    try:
        parts = numbers.split(",")
        return sum(int(x) for x in parts)
    except ValueError:
        raise ValueError("Bruh... are u serious?")