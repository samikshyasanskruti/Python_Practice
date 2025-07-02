def display_by_index(countries):
    index = int(input("Enter an index (0-4): "))
    if 0 <= index < len(countries):
        print("Country at index", index, "is", countries[index])
    else:
        print("Invalid index.")
if __name__ == "__main__":
    countries = ("India", "USA", "Germany", "Japan", "Australia")
    display_by_index(countries)
