# 简单的屏幕抓取程序
# 假设你要从Python Job Board（http://python.org/jobs）提取招聘单位的名称和网站
# 可在类似于下面的链接中找到名称和URL：
# <a href="/jobs/1970/">Python Engineer</a>
# 使用urllib和re来提取所需的信息
from urllib.request import urlopen
import re
p = re.compile('<a herf="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('http://python.org/jobs').read().decode()
for url, name in p.findall(text):
    print('{} ({})'.format(name, url))
