scores,ms = [],[]

for i in range(int(input("Enter no. of students"))):
    name = input()
    score = float(input)
    ms.append([name,score])
    scores.append(score)
    
sl = (sorted(set(scores)))[1]

for i,j in sorted(ms):
    if j == sl:
        print(i)
        
print(ms)

'''
take input sa[erately -> name, score
store                 -> ms = [name,score], scores = score
create set of scores 
sort set in ascending -> sl = scores[1]

for loop on alphabetically sorted ms 
    -> check in ms[x][1] == sl
        -> print(ms[x][0])

'''