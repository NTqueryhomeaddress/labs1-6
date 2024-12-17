import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exp_type, exp_value, traceback):
        end_time = time.time()
        print(f"time: {end_time - self.start_time:.2f} сек")

@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"time: {end_time - start_time:.2f} сек")

if __name__ == "__main__":
    print("Тестирование cm_timer_1:")
    with cm_timer_1():
        time.sleep(2)

    print("\nТестирование cm_timer_2:")
    with cm_timer_2():
        time.sleep(3)
