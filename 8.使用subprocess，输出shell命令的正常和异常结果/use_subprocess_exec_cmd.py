在Python中执行Shell命令并获取Shell返回结果，您可以使用`subprocess`模块。下面是一个示例代码：

python
import subprocess

# 执行Shell命令
command = "ls -l"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# 获取Shell返回结果
output = result.stdout
error = result.stderr

# 打印输出结果
print("Output:", output)
print("Error:", error)
在上面的示例中，我们使用`subprocess.run()`函数执行Shell命令，并使用`capture_output=True`参数来捕获命令的输出结果。`text=True`参数用于将输出结果以文本形式返回。`stdout`属性包含命令的标准输出，`stderr`属性包含命令的标准错误输出。

您可以根据需要调整`command`变量的值来执行不同的Shell命令。然后，可以通过`result.stdout`和`result.stderr`来获取输出结果。最后，您可以使用`print()`函数打印输出结果。
