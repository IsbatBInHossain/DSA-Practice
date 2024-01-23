class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefix_product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1] 
        else:
            self.prefix_product.append(self.prefix_product[-1] * num)
        self.nums.append(num)

    def getProduct(self, k: int) -> int:
        m = len(self.prefix_product)
        if k >= m:
            return 0
        return self.prefix_product[-1] // self.prefix_product[m - k- 1]
