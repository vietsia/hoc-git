def distance_from_zero(m):
	m=raw_input("nhap vao mot so: ")
	if type(m)==int or type(m)==float:
		return abs(m)
	else:
		return "Nope"
