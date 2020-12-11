P = float(input('Enter the principal: '))
R = float(input('Enter the rate%: '))
T = float(input('Enter the time: '))

val1 = (1+(R/100))
# A = P(math.pow(val1, T))
A = P*(val1**T)
CI = A-P 
print(f'AMOUNT = {A}')
print(f'CI = {CI}')