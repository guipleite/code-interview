# Question 5.7 - Cracking the Coding Interview

def swap_odd_even_bits(x: int) -> int:

    bi = "{0:b}".format(x)

    even_mask = []
    odd_mask = []

    for i in range(len(bi)):
        if i%2 == 0:
            even_mask.append('0')
            odd_mask.append('1')
        else:
            even_mask.append('1')
            odd_mask.append('0')

    even_mask = int(''.join(even_mask),2)
    odd_mask  = int(''.join(odd_mask),2)

    even_masked = x & even_mask
    odd_masked  = x & odd_mask

    merged = (odd_masked >> 1) | (even_masked << 1)

    return merged

print(swap_odd_even_bits(1431655765))