from partita import partita
from partita import partitaFinale



def double(strike):
    if strike == 0:
        return False
    return True



if __name__ == '__main__':
    PARTITA_EXTRA = 9
    match = []                      # Lista contenente gli Oggetti "partita"
    ho_fatto_strike = 0             # può assumere il valore di 2 o 1 a seconda di uno STRIKE o di uno SPARE
    raddoppio = False               # quando la variabile ho_fatto_strike è > 0 raddoppio il punteggio del lancio

    for index in range(10):
        pin_restanti = 10

        if index != 9:
            match.append(partita())
        else:
            match.append(partitaFinale())

        raddoppio = double(ho_fatto_strike)
        if raddoppio:
            ho_fatto_strike -= 1

        tiro = match[index].lancio(0, pin_restanti, raddoppio)
        pin_restanti -= tiro
        # Strike
        if pin_restanti == 0:
            ho_fatto_strike = 2
            if index != 9:
                continue
            else:
                pin_restanti = 10

        raddoppio = double(ho_fatto_strike)
        if raddoppio:
            ho_fatto_strike -= 1

        tiro = match[index].lancio(1, pin_restanti, raddoppio)
        pin_restanti -= tiro

        if index == 9:
            if pin_restanti == 0:
                ho_fatto_strike = 1
                pin_restanti = 10

            raddoppio = double(ho_fatto_strike)
            if raddoppio:
                ho_fatto_strike -= 1

            if ho_fatto_strike > 0:
                tiro = match[index].lancio(2, pin_restanti, raddoppio)

        else:  # SPARE
            if pin_restanti == 0:
                ho_fatto_strike = 1

#  rappresentazione grafica
    punteggioTotaleIncrementale = 0
    for index in range(10):
        print(f"Risultati del lancio {index + 1}: \nTiri: {match[index].lanci}")
        if match[index].extra_point != 0: print(f"Extra punti: {match[index].extra_point}")
        if match[index].str_spare[0]:
            print("Hai fatto Strike!")
        if match[index].str_spare[1]:
            if index != 9:
                print("Hai fatto Spare!")
                continue
            elif match[index].str_spare[0]:
                print("Hai fatto Strike!")
            else:
                print("Hai fatto Spare!")

        if index == 9:
            if match[index].str_spare[2]:
                print("Hai fatto Strike!")

        for calcolo in match[index].lanci:
            punteggioTotaleIncrementale += calcolo

        punteggioTotaleIncrementale += match[index].extra_point

    print(f"\nPunteggio Finale: {punteggioTotaleIncrementale}")
