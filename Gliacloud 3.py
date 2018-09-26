
def multiplesSum(n):

    def sum(num):
        return ((num + (n // num * num)) * (n // num)) / 2

    return int(sum(3) + sum(5) - sum(15))


print(multiplesSum(1000))
