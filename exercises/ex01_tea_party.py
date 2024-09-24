"""The goal of this exercise is to practice decomposing a large program into subprograms,writing a function that calls other functions, and also writing a "main" function that helps the program's execution."""

__author__: str = "730765631"


def main_planner(guests: int) -> None:
    """The main_planner function helps to give all the details calculated by the other functions. This function calls other functions and prints their values based on the arguments given."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """This function calculates the total amount of teabags we need based on the number of people attending the tea party."""
    return people * 2


def treats(people: int) -> int:
    """this function calculates the total number of treats needed based on the amount of tea bags drank."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """this function calculates the cost based on the amount of tea bags and treats needed"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
