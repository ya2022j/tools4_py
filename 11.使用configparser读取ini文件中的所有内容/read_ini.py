要使用ConfigParser库来读取INI文件的内容。首先，需要导入ConfigParser类。然后，使用该类创建一个ConfigParser对象，并使用其read()方法来读取INI文件。

以下是读取INI文件内容的示例代码：

python
from configparser import ConfigParser

# 创建ConfigParser对象
config = ConfigParser()

# 读取INI文件
config.read('your_file.ini')

# 获取INI文件中的所有节
sections = config.sections()
print('所有节:', sections)

# 获取指定节中的所有选项和值
for section in sections:
    options = config.options(section)
    for option in options:
        value = config.get(section, option)
        print(f'{section} - {option}: {value}')
在上述示例中，首先创建了一个ConfigParser对象，然后使用read()方法将INI文件加载到该对象中。接下来，可以使用sections()方法获取INI文件中的所有节，并循环遍历每个节。对于每个节，可以使用options()方法获取该节中的所有选项，并再次循环遍历每个选项。最后，通过get()方法获取选项的值，并进行打印输出。

请确保将示例代码中的your_file.ini替换为实际的INI文件路径。
