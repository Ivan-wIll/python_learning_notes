def process(string):
    print('Processing:', string)

    
with open('somefile.txt') as f:
    for line in f.readlines():
        process(line)
