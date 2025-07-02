def functionGrowth():
    print("N\tlogN\tN^2\tN^3\t2^N")
    import math
    for N in [2**i for i in range(4, 12)]:
        print(f"{N}\t{math.log(N):.2f}\t{N**2}\t{N**3}\t{2**N}")
if __name__ == "__main__":
    functionGrowth()
