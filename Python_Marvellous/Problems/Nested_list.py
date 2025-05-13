def sort(list):
    
    n = len(list)
    for i in range(0,n):
        j = i+1
        while j<n and j > 0:
            if list[i][1] > list[j][1]:
                list[i],list[j] = list[j],list[i]
            j = j+1
                
    newlist = []
    
    for i in range(0,len(list)):
        if list[1][1] == list[i][1]:
            newlist.append(list[i][0])
        
        
    for i in range(0,len(newlist)):
        j = i+1
        while j<len(newlist) and j > 0:
            if newlist[i] > newlist[j]:
                newlist[i],newlist[j] = newlist[j],newlist[i]
            j = j+1
    
    for p in newlist:
        print(p)

    
    
def main():
    python_students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name,score])
        
    sort(python_students)
        
        
if __name__ == '__main__':
    main()