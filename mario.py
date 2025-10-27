def main():
   n = int(input("Enter the size of the square: "))
   print_square(n)

def print_square(size):
    for i in range(size):
        print('#' * size)      
main()    