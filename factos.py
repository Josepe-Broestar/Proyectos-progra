def factorial(factor):
  f = 1
  cont_factor = factor
  while cont_factor > 0:
    f = f * cont_factor
    cont_factor -= 1
  return f

print(factorial(5))