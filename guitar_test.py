from guitar import Guitar

def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 900)

    print(guitar)
    print(other)

    print()

    print(f"{guitar.name} get_age() -  Expected 99. Got {guitar.get_age()}")
    print(f"{other.name} get_age() -  Expected 8. Got {other.get_age()}")

    print()

    print(f"{guitar.name} is_vintage -  Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage -  Expected False. Got {other.is_vintage()}")

    print()
    fifty_years_old_guitar = Guitar("50 years old Guitar", 1971, 11000)
    print(fifty_years_old_guitar)
    print()
    print (f"{fifty_years_old_guitar.name} get_age() -  Expected 50. Got {fifty_years_old_guitar.get_age()}")
    print()
    print(f"{fifty_years_old_guitar.name} is_vintage -  Expected True. Got {fifty_years_old_guitar.is_vintage()}")



main()