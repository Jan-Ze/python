def leicheng(number):
    if number > 1:
        return number * leicheng(number - 1)
    else:
        return 1
def leijia(number):
    if number > 1:
        return number + leijia(number-1)
    else:
        return 1
    