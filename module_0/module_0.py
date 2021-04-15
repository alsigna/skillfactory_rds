import numpy as np

# random number from 0 to MAX_NUMBER for guessing
MAX_NUMBER = 100
# how many times to test algorithm
ITERATION_COUNT = 10000


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, MAX_NUMBER + 1, size=(ITERATION_COUNT))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v3(number):
    """Custom algorithm for guessing random number.

    Args:
        number (int): Number to guess

    Returns:
        int: Number of attempts
    """
    count = 1
    predict = int(MAX_NUMBER / 2)
    step = int(predict / 2) + int(predict % 2 > 0)

    while number != predict:
        count += 1
        if number > predict:
            predict += step
        elif number < predict:
            predict -= step
        step = int(step / 2) + int(step % 2 > 0)

    return count


def game_core_v4(number):
    """Guessing based on Binary Search.

    Args:
        number (int): Number to guess

    Returns:
        int: Number of attempts
    """
    left = 0
    right = MAX_NUMBER + 1
    count = 1
    predict = MAX_NUMBER // 2

    while number != predict:
        count += 1
        if predict < number:
            left = predict
        else:
            right = predict
        predict = (left + right) // 2

    return count


if __name__ == "__main__":
    score_game(game_core_v3)
    score_game(game_core_v4)
