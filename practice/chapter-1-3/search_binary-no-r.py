import random

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return False

if __name__ == "__main__":
    data = [random.randint(0, 100) for _ in range(10)]
    data.sort()
    print(data)
    target = int(input("What's number would you like to find?: "))
    print(binary_search(data, target))
