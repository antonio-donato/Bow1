import random


class partita():
    def __init__(self):
        self.lanci = [0, 0]
        self.str_spare = [False, False]  # [0] - Strike; [1] - Spare

    def lancio(self, remain_pins=10):
        self.remain_pins = remain_pins
        tiro = random.randint(1, self.remain_pins)
        return tiro

    def lancio1(self, restanti=10):
        self.restanti = restanti
        self.lanci[0] = self.lancio(self.restanti)
        if self.lanci[0] == self.restanti:
            self.str_spare[0] = True  # Strike
        return self.lanci[0]

    def lancio2(self, restanti=10):
        self.restanti = restanti
        self.lanci[1] = self.lancio(self.restanti)
        if self.lanci[1] == self.restanti:
            self.str_spare[1] = True  # Spare
        return self.lanci[1]


class partitaFinale(partita):
    def __init__(self):
        super().__init__()
        self.lanci = [0, 0, 0]
        self.str_spare = [False, False, False]

    def lancio3(self, restanti=10):
        self.restanti = restanti
        self.lanci[2] = self.lancio(self.restanti)
        if self.lanci[2] == self.restanti:
            self.str_spare[2] = True  #......
        return self.lanci[2]


def randomizza():
    tiro = random.randint(1, 10)
    print(tiro)


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
        tiro = match[index].lancio1()
        pin_restanti -= tiro
        # Strike
        if pin_restanti == 0:
            continue

        tiro = match[index].lancio2(pin_restanti)

    for index in range(10):
        print(f"Risultati del lancio {index + 1}: \nTiri: {match[index].lanci}")
        if match[index].str_spare[0]:
            print("Hai fatto Strike!")
        if match[index].str_spare[1]:
            print("Hai fatto Spare!")
