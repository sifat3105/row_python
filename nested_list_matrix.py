row_1 = ['💰','💰','💰']
row_2 = ['💰','💰','💰']
row_3 = ['💰','💰','💰']
matrix = [row_1,row_2,row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

position = input("enter the position whore you wont hide money: ")
row_index = int(position[0])-1
column_index = int(position[1])-1

secected_row = matrix[row_index]
secected_row[column_index] = '❎'

print(f"{row_1}\n{row_2}\n{row_3}")