class Divisor:
    def __init__(self, number):
        self.value = number
        self.divs = self.__find_div(number)

    @staticmethod
    def __find_div(n):
        divs_list = [1, n]
        for i in range(2, int(n ** 0.5 + 1)):
            if i * i == n:
                divs_list.append(i)
            elif n % i == 0:
                divs_list.append(i)
                divs_list.append(n // i)
        return sorted(divs_list)

    def is_simple(self):
        if len(self.divs) == 2:
            return True
        return False
