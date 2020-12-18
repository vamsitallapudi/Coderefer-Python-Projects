# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# def printWeird(n):
#     if n%2==1:
#         print("Weird")
#     elif n%2 == 0:
#         if n in range(2,5):
#             print("Not Weird")
#         elif n in range(6,20):
#             print("Weird")
#         elif n > 20:
#             print("Not Weird")

# python program to print below average marks
marks = [100, 76, 45, 28, 52, 17, 83]
below_average = list(filter(lambda x : x<35, marks))
print(below_average)