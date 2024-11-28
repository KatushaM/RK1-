
def print_result(outer_func):
    def inner_func(*args, **kwargs):
        result = outer_func(*args, **kwargs)
        print(outer_func.__name__)
        if isinstance(result, list):
            print(*result, sep='\n')
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        return result
    return inner_func

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
    
    
