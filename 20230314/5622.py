chr = input()
list_input = []

time = 0

phone = [['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'], ['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]
for i in chr:
    list_input.append(i)

def get_index(phone, n):
    for idx1, i in enumerate(phone):
        for idx2, j in enumerate(i):
            if j == n:
                return idx1
    return None
for i in list_input:
    time += get_index(phone, i)

print(time)

