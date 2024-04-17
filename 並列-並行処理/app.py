from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def func_1(x):
    for n in range(3):
        time.sleep(2)
        # print(f'func_1 - {n}  ({x})')
        return f'func_1 - {n}  ({x})'
    
def func_2(x, y):
    for n in range(3):
        time.sleep(1)
        print(f'func_2 - {n}  ({x}, {y})')
    
def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        for arg in ["A", "B", "C", "D"]:
            res = executor.map(func_1, arg)
            print(res, arg)

        # executor.submit(func_2)

if __name__ == "__main__":
    main()