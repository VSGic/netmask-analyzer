import math

def input_process(input_netmask):
	print(input_netmask)
	mask_parts = input_netmask.split('.', 4)
	x = mask_parts[3].count('/')
	if x == 0:
		just_address(mask_parts)
	else:
		address_and_mask(mask_parts)

def just_address(mask_parts):
	i = 3
	base_mask = 32
	mask = 1
	while i >= 0:
		x = 256 - int(mask_parts[i])
		if x ==  256:
			base_mask = base_mask - 8
			i = i - 1
		elif x == 1 and i == 3:
			i = -1
		elif x == 1 and i < 3:
		#	base_mask = base_mask - 8
			i = -1
		else:
			base_mask = base_mask - int(math.log2(x))
			i = -1
	print('Network mask is {0}'.format(base_mask))

def address_and_mask(mask_parts):
	mask_prep = mask_parts[3].split('/')
	mask = mask_prep[1]
	print('Network mask is {0}'.format(mask))
