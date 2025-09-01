import david, isar, pija,  norina, karolina, dan
team_name = "RiseNShine"


def team_intro():
    print(f"This is team {team_name}, we are:")
    print(isar.name())
    print(david.david())
    print(karolina.karolina())
    print(norina.norina())
    print(pija.name())
    print(dan.dan())



team_intro()


## Below is the bonus challenge.
## three acts 1 paragraph each person per act, work with a partner and fix spelling mistakes

def story():
    print("\nOur story begins...\n")
    print(pija.act1())
    print(karolina.act1())
    print(norina.act1())
    print(david.act1())
    print(isar.act1())
    print(dan.act1())
    print("\nThe story continues...\n")
    print(pija.act2())
    print(karolina.act2())
    print(norina.act2())
    print(david.act2())
    print(isar.act2())
    print(dan.act2())
    print("\nThe story concludes...\n")
    print(pija.act3())
    print(karolina.act3())
    print(norina.act3())
    print(david.act3())
    print(isar.act3())
    print(dan.act3())

story()