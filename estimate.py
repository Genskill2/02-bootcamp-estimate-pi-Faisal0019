def wallis():
    print("Wallis\n======")
    iterations = 1000000
    numerator = 2.0
    denominator = 1.0
    pi = 1.0

    for i in range(1, iterations + 1):
        pi*= (numerator / denominator)
        if (i%2) == 1:
            denominator+= 2.0
        else:
            numerator+= 2.0

    pi*= 2.0

    print_as_text(pi) 

    
    import random as r
import math as m

inside = 0
overall = 100000

for i in range(0, overall):
  x2 = r.random()**2
  y2 = r.random()**2
    if m.sqrt(x2 + y2) < 1.0:
      inside += 1

pi = (float(inside) / total) * 4

print(pi)
