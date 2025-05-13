def main():
    list1 = []
    for i in range(int(input())):
        inputs = input().split()
        
        cmd = inputs[0].lower()
        
        if cmd == "insert":
            list1.insert(int(inputs[1]),int(inputs[2]))
        
        elif cmd == "print":
            print(list1)
            
        elif cmd == "remove":
            list1.remove(int(inputs[1]))
            
        elif cmd == "append":
            list1.append(int(inputs[1]))
            
        elif cmd == "sort":
            list1.sort()
            
        elif cmd == "pop":
            list1.pop()
            
        else :
            list1.reverse()
                  

    
if __name__ == "__main__":
    main()