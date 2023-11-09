number = int(input("Gimmy a number greater than 100 plz…: "))
threshold = 100

while number <= threshold:
	print(str(number) + " is less than 100, dummy. Try again… I’ve got all day…")
	number = int(input("Gimmy a number greater than 100 plz…: "))

print(str(number) + " is greater than 100! Good work.")