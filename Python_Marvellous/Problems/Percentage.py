def avg(student_marks):
    k,n=0.0,0.0
    for i in student_marks:

        k += i
        n += 1.0
    d = k/n
    return f"{d:.2f}"

def main():
    n =int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(avg(student_marks[query_name]))

if __name__ == '__main__':
    main()
