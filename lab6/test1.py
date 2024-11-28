import random

def gen_random(num_count, begin, end):
    if not isinstance(num_count, int) or num_count <= 0:
        return []  
    if not isinstance(begin, int) or not isinstance(end, int) or begin > end:
        raise ValueError("Неверные входные параметры: begin и end должны быть целыми числами, и begin <= end")
    return [random.randint(begin, end) for _ in range(num_count)]


def format_output(numbers):
    return ", ".join(map(str, numbers))


def main():
    try:
        random_numbers = gen_random(12, 1, 100)
        print(format_output(random_numbers))
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "main":
    main()
