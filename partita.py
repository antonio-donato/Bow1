import random

class partita:
    def __init__(self):
        self.lanci = [0, 0]
        self.extra_point = 0
        self.str_spare = [False, False]  # [0] - Strike; [1] - Spare

    def lancio(self, numero_lancio, restanti=10, raddoppio=False): # Se nei precedenti lanci ho fatto strike o spare, accantono il valore del piunteggio in extra point
        indice_lancio = numero_lancio
        birilli_restanti = restanti
        # birilli = random.randint(0, birilli_restanti)
        if birilli_restanti == 10:
            birilli = 10
        else:
            birilli = 0
        self.lanci[indice_lancio] = birilli
        if self.lanci[indice_lancio] == birilli_restanti:
            self.str_spare[indice_lancio] = True  # Strike/Spare in corrispondenza del tiro nel game
        if raddoppio:
            self.extra_point += birilli
        return self.lanci[indice_lancio]


class partitaFinale(partita):
    def __init__(self):
        super().__init__()
        self.lanci = [0, 0, 0]
        self.str_spare = [False, False, False]

