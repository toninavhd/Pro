def hyperfactorial(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0

    return n**n * hyperfactorial(n - 1)