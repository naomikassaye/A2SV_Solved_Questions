def split_and_join(line):
    res = line.split(" ")
    result = "-".join(res)  
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
