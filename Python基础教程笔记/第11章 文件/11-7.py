def process(string):
    print('Processing:', string)


with open(r'D:\python 3.8.2\somefile.txt') as f:  
    while True:
        char = f.read(1)
        if not char: break
        process(char) 
        
