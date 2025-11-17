def meow(n: int) -> str:
    """ Meow n times."""
    return "Meow!\n" * n

number: int  = int(input("Enter the number of meows: "))
meows: str = meow(number)
print(meows, end="")