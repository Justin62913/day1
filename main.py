
with open('data.txt', 'r') as f:
    data = [line for line in f.read().strip().split('\n')]


elf_1 = 0
elf_2 = 0
elf_3 = 0
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > elf_1:
        elf_3 = elf_2
        elf_2 = elf_1
        elf_1 = count
    elif count > elf_2:
        elf_3 = elf_2
        elf_2 = count
    elif count > elf_3:
        elf_3 = count

print('The answer is: ', elf_1)
print('The 2nd answer is: ', elf_1+elf_2+elf_3)



