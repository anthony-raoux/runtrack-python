import string

alphabet_lower=string.ascii_lowercase

print(alphabet_lower)

reverse_lower=list(reversed(alphabet_lower))
for item in reverse_lower:
    print(item, end="")