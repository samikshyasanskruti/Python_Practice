def star(amount):
    for i in range(10-len(amount)):
        amount='*'+amount
    return amount
def main():
    print(star("123"))
if __name__=="__main__":
    main()