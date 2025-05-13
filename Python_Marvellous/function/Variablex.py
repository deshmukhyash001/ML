def display(*A):
    type(A)
    print(A)
    

def main():
    display(10,12,23,34)
    display(10,12,23,34,33)
    display(10,12,23)
    display(23)
    display()

    
if __name__ == "__main__":
    main()