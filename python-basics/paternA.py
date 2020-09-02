# rows = int(input("Enter Number of Rows: "))
# columns = int(input("Enter Number of Columns: "))
# print("Hollow Box Pattern with", rows, "rows and", columns, "columns")
#
# for i in range(0, rows):
#     for j in range(0, columns):
#         if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
#             print('*', end='  ')
#         else:
#             print(' ', end='  ')
#     print()


rows = int(input("Enter Number of Rows: "))
columns = int(input("Enter Number of Columns: "))
print("Hollow Box Pattern with", rows, "rows and", columns, "columns")

for i in range(0, rows):
    for j in range(0, columns):
        if i == 0 or i == 2 and  j == 1 and j==2:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()