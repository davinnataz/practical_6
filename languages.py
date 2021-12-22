from programming_language import ProgrammingLanguange

def main():
    ruby = ProgrammingLanguange("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguange("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguange("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)
    print()
    print()
    language_name = [ruby, python, visual_basic]
    print("The dynamically typed languages are : ")
    for i in language_name:
        if i.is_dynamic():
            print(i.name)

main()