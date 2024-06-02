def int_to_32bit_binary(n):
    # Get the binary representation of the integer, remove the '0b' prefix, and pad with leading zeroes to 32 bits
    binary_representation = format(n if n >= 0 else (1 << 32) + n, '032b')
    return binary_representation
l=[1,2,4,5]
k=3
for i in l:
    print(int_to_32bit_binary(i))

print("\nk=\n"+int_to_32bit_binary(k))
# |4-3|=1