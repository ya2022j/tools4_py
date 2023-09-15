如果你想将列表 ["d1", "d2", "d3"] 中的元素作为节名，遍历写入 INI 文件，可以使用以下 Python 代码：

from configparser import ConfigParser

config = ConfigParser()

sections = ["d1", "d2", "d3"]

for section in sections:
    config.add_section(section)
    config.set(section, 'key1', 'value1')
    config.set(section, 'key2', 'value2')

with open('example.ini', 'w') as f:
    config.write(f)

一定要把with语句放到for循环之外，一次性写入才能解决写入的问题
在上述代码中，首先创建了一个 ConfigParser 对象。然后，使用 add_section() 方法将列表中的元素作为节名添加到 INI 文件中。接下来，使用 set() 方法设置键和值。最后，使用 write() 方法将配置写入 INI 文件。

这样，你就可以将列表中的元素作为节名遍历写入 INI 文件了。如果你想要添加更多的键和值，只需要在循环中使用 set() 方法即可。
