data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = lambda data : sorted(data,reverse=True)
    print(result(data=data))
    
    result2 = sorted(data,reverse=True)
    print(result2)
