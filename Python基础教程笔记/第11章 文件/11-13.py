def process(string):
    print('Processing:', string)


for line in open('somefile.txt'): 
    process(line)
    
