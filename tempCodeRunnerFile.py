def count_emma(statement):
    print("Given string: ",statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i : i+4] == 'Emma'
    return count

count = count_emma("Emma is a good developer. Emma is a writer")
print("Emma appeared ",count," times")
