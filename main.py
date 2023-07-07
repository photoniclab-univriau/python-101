""""
entry points
"""

from lib import calc_fg

def main():

    m1 = 10
    m2 = 20
    r = 3

    computed_fg = calc_fg(m1, m2, r)
    print(computed_fg)

if __name__ == "__main__":
    main()


# REPL -> READ EVAL PRINT LOOP