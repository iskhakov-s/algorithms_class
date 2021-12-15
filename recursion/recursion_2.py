def double(string):
    if len(string) == 0:
        return ''
    return string[0] * 2 + double(string[1:])
    

def is_palindrome(string):
    if len(string) <= 1:
        return True
    return (string[0] == string[-1]) and is_palindrome(string[1:-1])


def count_vowels(string):
    if len(string) == 0:
        return 0
    is_vowel = string[0] in 'aeiou'
    return (1 if is_vowel else 0) + count_vowels(string[1:])


def multiply(num1, num2):
    if num2 == 0:
        return 0
    return num1 + multiply(num1, num2-1)


if __name__ == '__main__':
    print(double('cake')) # should be 'ccaakkee'
    print(double('banana')) # should be 'bbaannaannaa'
    print(double('g')) # should be 'gg'

    print(is_palindrome('noon')) # should be True
    print(is_palindrome('starts')) # should be False
    print(is_palindrome('onion')) # should be False
    print(is_palindrome('v')) # should be True

    print(count_vowels('rhythm')) # should be 0
    print(count_vowels('area')) # should be 3
    print(count_vowels('gnomon')) # should be 2

    print(multiply(3, 5)) # should be 15
    print(multiply(0, 4)) # should be 0
    print(multiply(2, 1)) # should be 2
