def add_to(num):
    """Recursively adds from 1 to num"""

    # base case
    if num == 1:
        return 1
    
    # recursive case:
    else:
        return num + add_to(num - 1)

print(add_to(8))