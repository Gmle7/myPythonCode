import math


def quadratic(a, b, c):
    drt = b * b - 4 * a * c
    if drt >= 0:
        return (-b + math.sqrt(drt)) / (2 * a), (-b - math.sqrt(drt)) / (2 * a)
    else:
        return 0


print(quadratic(2, 7, 5))
