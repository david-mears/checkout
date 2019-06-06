class Shop():
    PRICES = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }
    
    def checkout(self, basket):
        total = 0
        basket = list(str(basket))
        for item in basket:
            if item not in list(self.PRICES.keys()):
                return -1
        while basket.count('A') >= 3:
            basket.remove('A')
            basket.remove('A')
            basket.remove('A')
            total += 130
        while basket.count('B') >= 2:
            basket.remove('B')
            basket.remove('B')
            total += 45
        for item in basket:
            total += self.PRICES[item]
        return total
