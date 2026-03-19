def Add(numbers):
    try:
        if numbers == "":
            return 0
        numbers = numbers.replace("\n", ",")
        num = numbers.split(",")
        s = 0
        for i in num:
            s += int(i)     
            
        return s
    
    except ValueError:
        raise ValueError("Please provide proper value")
    
    

    