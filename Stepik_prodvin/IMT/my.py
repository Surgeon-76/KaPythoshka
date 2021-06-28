def ind_mas(m, r):
    imt = m / r**2
    if 18.5 <= imt <= 25: s = 'Оптимальная масса'
    elif imt < 18.5: s = 'Недостаточная масса'
    elif imt > 25: s = 'Избыточная масса'
    return s 

print(ind_mas(float(input()), float(input())))