
class Pares():

    @staticmethod
    def pares_que_suman_n(n):
        pares = []
        if n <= 10**6:
            for a in range(1, n):
                b = n - a
                if b > 0:
                    pares.append((a, b))
        return pares