with open("m.txt") as f:
    content = f.readlines()
    line_count = len(content)
    word_count = sum(len(line.split()) for line in content)
    
    print("Lines:", line_count)
    print("Words:", word_count)