from src.functions import sum_even_numbers
# from viewer.mainwindow import App
import random

def main():

    qyantitu = random.randint(1, 100000)
    left = -20000
    right = 20000
    array = [random.randint(left, right) for _ in range(qyantitu)]
    summ_event_numbers = sum_even_numbers(array)
    print(f'Numbers of elements {qyantitu}')
    print(summ_event_numbers)
    print('='*20)



if __name__ == '__main__':
    main()


