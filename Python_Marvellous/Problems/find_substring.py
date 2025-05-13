def count_substring(string, sub_string):
    index = string.find(sub_string)
        
    return index

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)