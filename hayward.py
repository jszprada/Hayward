import math
from scipy.optimize import bisect

# Dane wejściowe
VAB = 16  # pojemność łącza AB w jednostkach przepływu (JP)
VAC = 23  # pojemność łącza AC w jednostkach przepływu (JP)
AAD = 15  # liczba erlangów ruchu spływającego na łącze AD
AAB = 20  # liczba erlangów ruchu na łączu AB
AAC = 30  # liczba erlangów ruchu na łączu AC

# Stała R - wymagana do obliczeń metodą Haywarda
R = AAD / (VAB + VAC)

def calc_Pb(VAD):
    A_tot = AAB + AAC
    numerator = A_tot * (1 - math.exp(-(VAB + VAC + VAD) / R))
    denominator = R * (VAB + VAC + VAD - (A_tot / R) * (1 - math.exp(-(R * (VAB + VAC + VAD)) / A_tot)))
    Pb = numerator / denominator
    return Pb

def find_VAD():
    return bisect(lambda VAD: calc_Pb(VAD) - 0.05, 1, 100)

# Obliczanie pojemności łącza alternatywnego VAD
VAD = find_VAD()

# Wynik
print(f"Pojemność łącza alternatywnego VAD: {VAD} JP")
