def longestConsecutive(nums):
    if not nums:
        return []

    num_set = set(nums)
    l_str = 0
    l_seq = []

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            curr_str = 1
            curr_seq = [num]

            while current_num + 1 in num_set:
                current_num += 1
                curr_str += 1
                curr_seq.append(current_num)

            if curr_str > l_str:
                l_str = curr_str
                l_seq = curr_seq

    return l_seq

input_nums = input("Enter a sequence of numbers: ").split()
input_nums = list(map(int, input_nums)) 
output = longestConsecutive(input_nums)
print(f"دنباله: {output}")
