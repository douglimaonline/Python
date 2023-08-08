with open("file1.txt") as data_file1:
    file1 = data_file1.readlines()
with open("file2.txt") as data_file2:
    file2 = data_file2.readlines()
result = [int(num) for num in file1 if num in file2]
# Write your code above 👆

print(result)

