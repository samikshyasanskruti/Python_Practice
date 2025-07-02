def find_pythagorean_triples(limit=100):
    triples = []
    for a in range(1, limit):
        for b in range(a, limit):
            c_sq = a*a + b*b
            c = int(c_sq ** 0.5)
            if c < limit and c*c == c_sq:
                triples.append((a, b, c))
    return triples
if __name__ == "__main__":
    print(find_pythagorean_triples())
