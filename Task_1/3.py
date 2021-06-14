storage = {
    'Joe': 1430000,
    'Soda': 590000,
    'Diz': 272000,
    'Medaed': 220000,
    'Quantum': 4500000
}

# Сложность O(n**2) - квадратичная

sorted_values_1 = sorted(storage.values(), reverse=True)   # O(nlogn) - линейно-логарифмическая
sorted_storage_1 = {}                                      # O(1) - константная

count = 0                                                   # O(1) - константная
for i in sorted_values_1:                                   # O(n) - линейная
    if count > 2:                                           # O(1) - константная
        break                                               # O(1) - константная
    count += 1                                              # O(1) - константная
    for j in storage.keys():                               # O(n) - линейная
        if storage[j] == i:                                # O(1) - константная
            sorted_storage_1[j] = storage[j]              # O(1) - константная
            break                                           # O(1) - константная

print(sorted_storage_1)                                    # O(n) - линейная

# Сложность O(n*logn) - линейно-логарифмическая

sorted_keys_2 = sorted(storage, key=storage.get, reverse=True)    # O(nlogn) - линейно-логарифмическая
sorted_storage_2 = {}                                              # O(1) - константная
count = 0                                                           # O(1) - константная
for i in sorted_keys_2:                                             # O(n) - линейная
    if count > 2:                                                   # O(1) - константная
        break                                                       # O(1) - константная
    count += 1                                                      # O(1) - константная
    sorted_storage_2[i] = storage[i]                              # O(1) - константная

print(sorted_storage_2)                                            # O(n) - линейная

# Самое эффективное решение под номером 2, так как его сложность линейно-логарифмическая. Она занимает гораздо меньше времени, чем квадратичная.