#There may be times when we want to specify a type on to a variable.
#  This can be done with casting. Python is an object-orientated language, 
# and as such it uses classes to define data types, including its primitive types.
# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

#=============================================
# implicit conversion
# ============================================
# num_int = 123
# num_flo = 1.23
# num_new = num_int + num_flo
# print("datatype of num_int:",type(num_int))
# print("datatype of num_flo:",type(num_flo))
# print("Value of num_new:",num_new)
# print("datatype of num_new:",type(num_new))
#=============================================
# explicit conversion
#=============================================
num_int = 123
num_str = "456"
print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))
num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))
num_sum = num_int + num_str
print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))
