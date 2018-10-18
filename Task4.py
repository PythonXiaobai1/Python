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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
call_1 = []
call_2 = []
call_3 = []
call_4 = []
tele_list = []

for a in texts:
	call_1.append(a[0])
	call_2.append(a[1])
for b in calls:
	call_3.append(b[0])
	call_4.append(b[1])
for i in call_3:
	if i not in call_1 and i not in call_2 and i not in call_4:
		tele_list.append(i)

new_tele_list = sorted(set(tele_list))

print("These numbers could be telemarketers: ")
for i in new_tele_list:
	print(i)







