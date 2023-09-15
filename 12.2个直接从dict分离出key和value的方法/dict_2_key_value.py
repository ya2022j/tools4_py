
# 如何在 Python 中将字典转换为字符串  https://www.zadmei.com/rhzpzjzd-2.html
dict_data = {'name': 'Tom'}
def dict_to_string1(dict_data):

    key_item,value_item = ''.join([f'{key}:{value}' for key, value in dict_data.items()]).split(":")
    return key_item,value_item

k,v = dict_to_string1(dict_data)
print(k,v)


method2

dict_data = {'name': 'Tom', 'age': 20, 'gender': 'male'}
str_data = '{name}:{age}:{gender}'.format(**dict_data)

print(str_data)
