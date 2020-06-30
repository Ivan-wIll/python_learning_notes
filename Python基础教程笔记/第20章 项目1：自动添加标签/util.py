# 一个文本块生成器


# 在文件末尾添加一个空行
def lines(file):
    for line in file:
        yield line
    yield '\n'


# 收集空行前的所有行并将它们返回，然后重复这样的操作
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
