names = ['Henrique', 'Thales', 'Magdinha', 'Jubs', 'Bia', 'Bryan']

# for name in names:
#     if name.lower().startswith('b'):
#         print(name)

# TODO: Usar lambdas

def starts_with_b(text):
    return text[0].lower() == 'b'

print(list(filter(starts_with_b, names)))
print(*list(filter(starts_with_b, names)))
