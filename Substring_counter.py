def count_substring(string, sub_string):
    #count = string.count(sub_string)
    pointer = 0
    count = 0
    for _ in range((len(string)-len(sub_string))+1):
        if string[pointer] == sub_string[0]:
            internal_pointer = 1
            internal_count = 1
            for _ in range(1, len(sub_string)):
                if string[pointer+internal_pointer] == sub_string[_]:
                    internal_pointer += 1
                    internal_count += 1
                else:
                    break
            if internal_count == len(sub_string):
                count += 1  
        pointer += 1
    return count

if __name__ == '__main__':
    string = input("Enter the string: ").strip()
    sub_string = input("Enter sub string: ").strip()
    
    count = count_substring(string, sub_string)
    print(f"Number of times \"{sub_string}\" occured is {count}")