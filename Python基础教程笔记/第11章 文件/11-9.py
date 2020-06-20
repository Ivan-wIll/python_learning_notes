def process(string):
    print('Processing:', string)

    
with open('somefile.txt') as f: 
    for char in f.read():
        process(char)
