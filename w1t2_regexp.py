def calculate(data, findall):
	matches = findall(r'([abc])([+-]?=)([abc]?)([+-]?\d*)')
	for var1, sign, var2, num in matches:
		new_value = data.get(var2, 0) + int(num or 0)
		if sign == '=':
			data[var1] = new_value
		else:
			data[var1] += new_value if '+' in sign else -new_value
	
	return data 