def copy_file(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'w') as f2:
        for line in f1:
            f2.write(line + '\n')
if __name__ == "__main__":
    copy_file('input.txt', 'output.txt')
# make ur own text file
