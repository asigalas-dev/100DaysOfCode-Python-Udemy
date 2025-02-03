def calculate_love_score(name1, name2):
    combine_name = name1 + name2
    true = 0
    love = 0
    check1 = "true"
    check2 = "love"

    for letter_true in check1:
        for letter_name in combine_name.lower():
            if letter_true==letter_name:
                true += 1
    for letter_love in check2:
        for letter_name in combine_name.lower():
            if letter_love==letter_name:
                love += 1

    print(f"Your TRUE LOVE score is {true}{love}!")

print("Let's calculate your TRUE LOVE score!")
name1 = str(input("What is your full name?\n"))
name2 = str(input("What is the other person's name?\n"))

calculate_love_score(name1, name2)
