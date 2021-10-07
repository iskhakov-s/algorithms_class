def bottles_of_beer(n: int):
    """[prints the "Bottles of Beer" song for n bottles of beer]

    Args:
        n (int): [initial bottle count]
    """
    for i in range(n+1, -1, -1):
        print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
        if i == 0:
            print(f'Go to the store and buy some more, {n} bottles of beer on the wall...')
        else:
            print(f'Take one down, pass it around, {i-1} bottles of beer on the wall...')
            
def main():
    bottles_of_beer(5)

if __name__ == '__main__':
    main()
            