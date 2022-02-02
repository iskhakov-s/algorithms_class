class Student:
    def __init__(self, name, id=0):
        self.name = name
        self.id = id

    def __str__(self):
        return f'Student: {self.name}, {self.id}'


def linear_search(arr, keyid):
    """
    arr - list of Students
    keyid - int
    
    Returns the index of the Student in arr whose id matches keyid, -1 if not found
    """
    
    for i, student in enumerate(arr):
        if student.id == keyid:
            return i
    return -1


def binary_search(arr, keyid):
    """
    arr - list of Students, sorted in increasing order by id
    keyid - int
    
    Returns the index of the Student in arr whose id matches keyid, -1 if not found
    """
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (high+low)//2
        id_ = arr[mid].id
        if id_ == keyid:
            return mid
        elif id_ < keyid:
            low = mid + 1
        else:
            high = mid - 1
        
    
    return -1


def main():
    lst = [Student(name, id**2) for id, name in enumerate("ABCDEFG")]
    #uncomment to see students:
    #for s in lst: print(s)
    print(linear_search(lst, 3)) #should be -1
    print(linear_search(lst, 4)) #should be 2
    print(binary_search(lst, 3)) #should be -1
    print(binary_search(lst, 4)) #should be 2


if __name__ == '__main__':
    main()
