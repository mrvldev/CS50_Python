def main():
    number = get_number()
    meow(3)

def get_number():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            break
    return n

def meow():
    for _ in range(n):
        print("Meow!")