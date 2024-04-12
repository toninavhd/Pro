
# INTERVALO DE NUMEROS TENIENDO EN CUENTA LOS LIMITES.


def in_range(value: int, lower_limit: int, upper_limit: int, /) -> bool:
    if value >= lower_limit and value <= upper_limit:
        return True
    return False