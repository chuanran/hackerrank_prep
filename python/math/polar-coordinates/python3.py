# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

if __name__ == "__main__":
    r, phi = cmath.polar(complex(input()))
    print(r)
    print(phi)
