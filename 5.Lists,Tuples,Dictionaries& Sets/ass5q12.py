def display_countries(countries):
    print("Countries:", countries)
    selected = input("Enter the name of a country from the list: ")
    if selected in countries:
        print("Index of", selected, "is", countries.index(selected))
    else:
        print("Country not in the list.")
if __name__ == "__main__":
    countries = ("India", "USA", "Germany", "Japan", "Australia")
    display_countries(countries)
