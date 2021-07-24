lst = [1,4,3,5,6,2,8,7,10,9]
lst.sort()
first = 0
last = len(lst)-1
mid = (first + last) // 2
item = int(input("введите номер который хотите найти"))
found = False
while(first <= last and not found):
	mid = (first + last) // 2
	if lst[mid] == item:
		print("это {mid}")
		found = True
	else:
		if item < lst[mid]:
			last = mid - 1
		else:
			first = mid + 1
if found == False:
	print("не найдено")