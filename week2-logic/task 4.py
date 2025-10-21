def pyramid_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def diamond_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def hollow_square(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example calls
print("Pyramid Pattern:")
pyramid_pattern(5)

print("\nInverted Pyramid:")
inverted_pyramid(5)

print("\nDiamond Pattern:")
diamond_pattern(5)

print("\nNumber Triangle:")
number_triangle(5)

print("\nHollow Square:")
hollow_square(5)
