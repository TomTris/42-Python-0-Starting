import sys

def	count_len(object:any)->int:
	count = 0
	for i in object:
		count += 1
	return count

def main():
	argv = sys.argv
	count = count_len(argv)
	if (count == 1):
		return 0
	if (count > 2):
		print("AssertionError: too many arguments")
		return 1
	try:
		number = int(argv[1])
		if (number % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except:
		print("AssertionError: is not a number")
		return 1

main()