def wallis():

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
