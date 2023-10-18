可以使用Python内置的configparser库来读取INI文件，然后将数据转换成JSON格式输出。

示例代码如下：

python
import configparser
import json

config = configparser.ConfigParser()
config.read('example.ini')

# 将配置文件的数据转换成字典
data = {}
for section in config.sections():
    data[section] = {}
    for option in config.options(section):
        data[section][option] = config.get(section, option)

# 将字典转换成JSON格式并输出
json_data = json.dumps(data, ensure_ascii=False)
print(json_data)
在这里，我们首先使用ConfigParser对象读取example.ini文件中的数据。然后，我们遍历所有的section和option，将它们转换成字典形式存储在data变量中。最后，我们使用json.dumps()函数将data变量转换成JSON格式，并将结果输出。

需要注意的是，json.dumps()函数的ensure_ascii参数默认为True，会将非ASCII字符（例如中文）转换成Unicode编码。若需要输出中文，需要将该参数设置为False。
