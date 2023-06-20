def add_atms(n, k, L):
    left = 1  # минимальное расстояние между банкоматами
    right = max(L)  # максимальное расстояние между банкоматами
    while left < right:
        mid = (left + right) // 2  # середина диапазона
        count = 0  # количество банкоматов, которые могут быть добавлены
        for i in range(n-1):
            count += (L[i] - 1) // mid  # количество банкоматов, которые могут быть добавлены между i и i+1
        if count > k:
            left = mid + 1
        else:
            right = mid

    result = []  # новые расстояния между банкоматами
    for i in range(n-1):
        result.append(L[i] // left)
        for j in range(1, (L[i] - 1) // left + 1):
            result.append(left)
    result.append(L[-1] // left)

    return result
