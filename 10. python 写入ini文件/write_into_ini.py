在Python中写入.ini文件，我们可以使用configparser库。下面是一个简单的示例：


from configparser import ConfigParser
 
# 创建一个ConfigParser对象
config = ConfigParser()
 
# 使用一个有序字典来存储我们的配置
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
 
with open('example.ini', 'w') as configfile:
    # 写入到文件
    config.write(configfile)
在这个例子中，我们创建了一个ConfigParser对象，并且添加了一些配置到一个名为'DEFAULT'的section里。然后我们打开一个名为'example.ini'的文件（如果该文件不存在，Python会自动创建它），并使用config.write()方法将配置写入到文件。

这将会生成一个.ini文件如下：

[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
