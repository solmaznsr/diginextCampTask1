from collections import defaultdict

def Anagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)
    
    return list(anagrams.values())

input_strs = input("Enter strings: ").split()
output = Anagrams(input_strs)
print("Grouped anagrams:", output)
