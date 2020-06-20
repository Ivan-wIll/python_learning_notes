def process(string):
    print('Processing:', string)


with open('somefile.txt') as f: 
    char = f.read(1) 
    while char: 
        process(char) 
        char = f.read(1)
