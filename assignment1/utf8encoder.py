import sys

# Copy bits from one array to another in backward order
# from_index - index in copy_from array that identifies where to start the copy
# to_index - last index in copy_to array where a bit can be copied (Remember - This is going in reverse order)
def copybits(copy_from, copy_to, from_index, to_index):
	for x in range(10, to_index, -1):
		copy_to[x - 1] = copy_from[from_index - 1]
		from_index -= 1
		if from_index == 2:
			break
	return (copy_to, from_index)

# This is where it all begins
def main():
	input = sys.argv[1]
	with open(input, 'rb') as reader:
		with open("utf8encoder_out.txt", 'wb') as writer:
			byte = reader.read(2)
			while byte != "":
				decimal = 256 * ord(byte[0]) + ord(byte[1])
				binary = bin(decimal)
				print "Binary: " + binary
				print "Decimal: " + str(decimal)
				break

				if decimal < 128:
					char = chr(int(binary, 2))
					writer.write(char)
				
				elif decimal < 2048:
					bit_array1 = ['0'] * 10
					bit_array2 = ['0'] * 10
					bit_array1[1], bit_array2[1] = 'b', 'b'
					bit_array1[2], bit_array2[2] = '1', '1'
					bit_array1[3] = '1'

					num_bits = len(binary)
					bit_array2, num_bits = copybits(binary, bit_array2, num_bits, 4)
					if num_bits > 2:
						bit_array1, num_bits = copybits(binary, bit_array1, num_bits, 5)

					writer.write(chr(int(''.join(bit_array1), 2)))
					writer.write(chr(int(''.join(bit_array2), 2)))

				elif decimal < 65536:
					bit_array1 = ['0'] * 10
					bit_array2 = ['0'] * 10
					bit_array3 = ['0'] * 10
					bit_array1[1], bit_array2[1], bit_array3[1] = 'b', 'b', 'b'
					bit_array1[2], bit_array2[2], bit_array3[2] = '1', '1', '1'
					bit_array1[3], bit_array1[4] = '1', '1'

					num_bits = len(binary)
					bit_array3, num_bits = copybits(binary, bit_array3, num_bits, 4)
					if num_bits > 2:
						bit_array2, num_bits = copybits(binary, bit_array2, num_bits, 4)
						if num_bits > 2:
							bit_array1, num_bits = copybits(binary, bit_array1, num_bits, 6)

					writer.write(chr(int(''.join(bit_array1), 2)))
					writer.write(chr(int(''.join(bit_array2), 2)))
					writer.write(chr(int(''.join(bit_array3), 2)))

				byte = reader.read(2)


if __name__ == "__main__":
	main()
