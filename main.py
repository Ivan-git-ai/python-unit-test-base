def min_of_three_vars(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
        
def main():
    print(min_of_threee_vars(-3,10,100))
    
if __name__ == "__main__":
    main()
