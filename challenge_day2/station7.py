# Variables
a = 3
b = -1
c = 4
d = 7
e = 0.5

def solution_station7(expr: str):
    return eval(expr, {}, {"a": a, "b": b, "c": c, "d": d, "e": e})
