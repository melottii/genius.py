from random import randint
import os

def game(): #Jogo
    number_list = []
    while True:
        os.system('cls')
        new_number = randint(0, 9)
        number_list.append(new_number)
        print("O novo numero eh:", new_number)
        response = list(map(int, input("Digite a sequencia completa: ")))
        if number_list != response:
            break
    return len(number_list)-1


def bests_scores(this_game_highest_score, all_games_highest_score): #prints
    print()
    print(f'{this_game_highest_score[0]}, seu maior score foi: {this_game_highest_score[1]}')
    print(f'O maior ranking desse jogo foi do(a) {all_games_highest_score[0]}, com: {all_games_highest_score[1]} pontos')


def set_score(name, max_score): #ranking
    ranking_file = open('data.txt', 'r+')
    ranking_score = ranking_file.readline()
    ranking_file.seek(0)
    ranking_score = ranking_score.split(",")
    if len(ranking_score) == 0 or max_score > int(ranking_score[1]):
        highest_score = [name, max_score]
        ranking_file.write(f'{highest_score[0]}, {highest_score[1]}')
    else:
        highest_score = [ranking_score[0], ranking_score[1]]
    ranking_file.close()
    return highest_score


def main():
    name = input('Seu nome: ')
    score_list = []
    while True:
        score_list.append(game())
        if input('Jogar novamente? S (Sim) ou Pressione qualquer tecla (Não): ').upper() != 'S':
            break
    this_game_highest_score = [name, max(score_list)]
    all_games_highest_score = set_score(name, max(score_list))
    bests_scores(this_game_highest_score, all_games_highest_score)


main()
