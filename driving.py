country = input("請問您是哪國人: ")
age = input("請輸入年齡:　")
age = int(age)
if country == "台灣":
	if age >= 18:
		print("你可以考照")
	else:
		print("你不可以考照")