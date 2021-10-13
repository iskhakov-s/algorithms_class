def boring(num):
    if num <= 1:
        return 1
    else:
        return num + boring(num // 2)

print(boring(12))
