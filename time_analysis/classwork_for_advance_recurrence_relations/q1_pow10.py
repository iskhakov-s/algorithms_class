def pow10(exp):
    if exp == 0:
        return 1
    else:
        return 10 * pow10(exp - 1)

def fast_pow10(exp):
    if exp == 0:
        return 1
    else:
        num = fast_pow10(exp // 2)
        if exp % 2 == 0:
            return num * num
        else:
            return 10 * num * num

