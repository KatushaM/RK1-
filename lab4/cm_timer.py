import time
from time import sleep
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"time: {self.end_time - self.start_time}")

@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"time: {end_time - start_time}")

def main():
    print("cm1:")
    with cm_timer_1():
        sleep(0.5)

    print("\ncm2:")
    with cm_timer_2():
        sleep(0.5)

if __name__ == "__main__":
    main()
