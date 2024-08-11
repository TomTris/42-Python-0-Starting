def NULL_not_found(object : any)->int:
	if (object.__class__.__name__ == "NoneType"):
		print("Nothing:", object, object.__class__)
	elif (object.__class__.__name__ == "float"):
		print("Cheese:", object, object.__class__)
	elif (object.__class__ == int):
		print("Zero:", object, object.__class__)
	elif (object.__class__.__name__ == "str" and object == ""):
		print("Empty:", object, object.__class__)
	elif (object.__class__ == bool):
		print("Fake: ", object, object.__class__)
	else:
		print("Type not Found")
	return 1
