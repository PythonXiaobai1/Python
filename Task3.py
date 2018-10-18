"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。


第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
"""第一部分：
    被班加罗尔地区固话拨打的所有电话"""
all_dict = []
for element in calls:
	key = element[0]
	value = element[1]
	if key[0:5] == "(080)":
		all_dict.append(value)

"""被呼叫电话的区号和前缀"""

called_list = []
for a in all_dict:
	if a[0:3] == "140":
		called_list.append(a[0:3])
	elif a[0] == "(":
		b = a.index(")")
		called_list.append(a[1:b])
	elif a[0] =="7" or a[0] == "8" or a[0] == "9":
		called_list.append(a[0:4])
	else:
		continue

new_called_list = sorted(set(called_list))

print("The numbers called by people in Bangalore have codes:")
for a in new_called_list:
	print(a)

"""第二部分
   班加罗尔固话打往班加罗尔的电话所占比例"""
counts = 0
for i in all_dict:
	if i[0:5] == "(080)":
		counts += 1


percentage = round((counts / len(all_dict)) * 100 , 2)
print("{}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))