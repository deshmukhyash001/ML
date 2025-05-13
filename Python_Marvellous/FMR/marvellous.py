def filterX(Task,Values):
    Result = []
    
    for i in Values:
        if Task(i) == True:
            Result.append(i)
        
    return Result

def mapX(Task,Values):
    Result = []
    
    for i in Values:
        Result.append(Task(i))
        
    return Result

def reduceX(Task,Values):
    Result = 0
    
    for i in Values:
        Result = Task(Result,i)
        
    return Result
