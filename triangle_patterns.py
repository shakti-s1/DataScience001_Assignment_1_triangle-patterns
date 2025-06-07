rows = 5

# Lower Triangular
print("Lower Triangular Pattern")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print()

# Upper Triangular
print("Upper Triangular Pattern")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print()

# Pyramid Pattern
print("Pyramid Pattern")
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Sample Output:
# Lower Triangular Pattern
# *
# **
# ***
# ****
# *****
#
# Upper Triangular Pattern
# *****
# ****
# ***
# **
# *
#
# Pyramid Pattern
#     *
#    ***
#   *****
#  *******
# *********

