
data = [10,20,30,41,50,61,71,81,90]
def main():
    i = 0
    while i < len(data):
        if data[i]%2 != 0 and data[i+1]%2 != 0 and  data[i+2]%2 !=0:
            print(data[i],data[i+1],data[i+2])
            print(True)
        i += 1
        
if __name__ == "__main__":
    main()