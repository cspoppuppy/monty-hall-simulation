import numpy as np
import random


def num_to_percent(num):
    return "{:.2f}".format(num*100)


def print_message(func):
    def inner(num_of_games):
        res = func(num_of_games)
        print('*'*100)
        print(
            f'{num_of_games} games \n \
            probability of winning with original choice: \
            {num_to_percent(res)}%, \n \
            probability of winning by switching choice: \
            {num_to_percent(1-res)}%'
        )
        return res
    return inner


def behind_chosen_door():
    behind_doors = [0, 0, 1]  # 0 represents goat, 1 represents car
    np.random.shuffle(behind_doors)  # shuffle randomly
    chosen_door = random.randint(0, 2)  # choose a door randomly
    return behind_doors[chosen_door]  # return what's behind the door


@print_message
def winning_probability(num_of_games):
    chosen_contents = [behind_chosen_door() for i in range(num_of_games)]
    return sum(chosen_contents)/num_of_games


if __name__ == '__main__':
    winning_probability(num_of_games=100)
    winning_probability(num_of_games=1000)
    winning_probability(num_of_games=10000)
