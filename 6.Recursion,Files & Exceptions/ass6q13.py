def compute_price_per_unit(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        weights = list(map(float, f1.readlines()))
        costs = list(map(float, f2.readlines()))
        for w, c in zip(weights, costs):
            if w != 0:
                out.write(f"{c / w:.2f}\n")
            else:
                out.write("Infinity\n")
if __name__ == "__main__":
    compute_price_per_unit('weights.txt', 'costs.txt', 'output.txt')
# use own text file
