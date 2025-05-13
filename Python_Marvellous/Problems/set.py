def average(array):
    neew = set(array)
    n = 0
    for i in neew:
        n += i 
    return float(n/len(neew))
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)