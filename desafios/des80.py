nums= []
i = j = 0


for c in range(0,5):
    num = int(input(f"Informe o {c+1} valor"))
    nums.append(num)

    i = -1
    j =0

    if nums[j] < nums[i]:
        nums.insert(i, j)
        nums.remove(j)

    i += 1
    j += 1

print(nums)
