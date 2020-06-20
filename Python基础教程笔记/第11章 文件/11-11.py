import fileinput


def process(string):
    print('Processing:', string)


for line in fileinput.input('somefile.txt'):
    process(line)
    
