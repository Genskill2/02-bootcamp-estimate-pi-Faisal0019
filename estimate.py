import math

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

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
	@@ -15,8 +34,8 @@ def test_high_iters(self):

class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)

        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

	@@ -26,7 +45,6 @@ def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


if __name__ == "__main__":
    unittest.main()
