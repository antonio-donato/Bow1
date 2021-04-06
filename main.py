import random


class partita:
    def __init__(self):
        self.lanci = [0, 0]
        self.str_spare = [False, False]  # [0] - Strike; [1] - Spare

    def lancio(self, numero_lancio, restanti=10):
        indice_lancio = numero_lancio
        birilli_restanti = restanti
        self.lanci[indice_lancio] = random.randint(0, birilli_restanti)
        if self.lanci[indice_lancio] == birilli_restanti:
            self.str_spare[indice_lancio] = True  # Strike/Spare in corrispondenza del tiro nel game
        return self.lanci[indice_lancio]


class partitaFinale(partita):
    def __init__(self):
        super().__init__()
        self.lanci = [0, 0, 0]
        self.str_spare = [False, False, False]


if __name__ == '__main__':
    match = []
    punteggioTotaleIncrementale = 0

    for index in range(10):
        pin_restanti = 10
        tiro = 0

        if index != 9:
            match.append(partita())
        else:
            match.append(partitaFinale())

        # print(type(match[index]))
        tiro = match[index].lancio(0)
        pin_restanti -= tiro
        # Strike
        if pin_restanti == 0:
            continue

        tiro = match[index].lancio(1, pin_restanti)

    for index in range(10):
        print(f"Risultati del lancio {index + 1}: \nTiri: {match[index].lanci}")
        if match[index].str_spare[0]:
            print("Hai fatto Strike!")
        if match[index].str_spare[1]:
            print("Hai fatto Spare!")
