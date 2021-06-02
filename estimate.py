def wallis(dublets):
    products = 1
    multiplier - 2
    for dublet in range(dublet):
        pterm = (multiplier)/(multiplier-1)
        nterm = (multiplier)/(multiplier+1)
        products *= pterm*nterm
        multiplier +=2
    return products*2
    print(wallis(100000))
    print('Estimate of PI: ')
