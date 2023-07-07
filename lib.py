def calc_fg(m1, m2, r):
    # G = 6.672*10^-1
    G = 6.672e-11
    fg = G * ((m1*m2)/r**2)
    return fg
    