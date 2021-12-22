from guitar import Guitar

def main():
    guitars = []

    print("My Guitar")
    name = input("Name : ")
    while name != "":
        year = int(input("Year : "))
        cost = float(input("Cost : "))
        guitars_added = Guitar(name, year, cost)
        guitars.append(guitars_added)
        print(f"{guitars_added} added.")
        name = input("Name : ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars : ")
        for i, guitar in enumerate(guitars):
            vintage_string= ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(f"Guitar {i+1} : {guitar.name} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    else :
        print("No guitars :( Quick, go and buy one")

main()


