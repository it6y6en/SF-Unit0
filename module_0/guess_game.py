import numpy as np

def game_core_v3(number):
    '''Берём середину угадываемого отрезка np.mean(predict_space)
       и каждый неудачный раз обрезаем сверху или снизу отрезок до нового значения середины'''
    count = 1
    predict_space = [1,101] #может передаваться как аргумент функции
    predict = int(np.mean(predict_space)) #первая попытка будет 50
    while number != predict:
        count+=1
        if number > predict:
            predict_space[0] = predict
            predict = int(np.mean(predict_space))
        elif number < predict:
            predict_space[1] = predict
            predict = int(np.mean(predict_space))
    return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)