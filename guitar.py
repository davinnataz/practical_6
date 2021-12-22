current_year = 2021
vintage = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name= name
        self.year = year
        self.cost = cost

    def get_age(self):
        return current_year - self.year

    def is_vintage(self):
        if self.get_age() < vintage:
            return False
        else :
            return True

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year
