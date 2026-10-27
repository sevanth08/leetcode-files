"""
This is very good question (11.10.2026) 
we are given a group of anagrams we need to return the anagrams which are a anagrmam in a separate list

input = ["sin","pop","opp","ars"]
output = [ ["sin"] , ["pop","opp" , ["ars"] ]

just have a look sin and ars dint have any anagrams in tht group 

"""

# approach 1 (3120ms)
strs = list(map(str,input("enter the string in list: ").split()))
og_words = []
sorted_words = []
seen = {}
final_res = []
for i in strs:
    og_words.append(i)
    word = "".join(sorted(i))
    sorted_words.append(word)
for k in sorted_words:
    seen[k] = seen.get(k,0)+1
for key,values in seen.items():
    group = []
    for i in range(len(sorted_words)):
        if sorted_words[i] == key:
            group.append(og_words[i])
    final_res.append(group)
print(final_res)

print(seen)
# approach 2 (146ms)

'''strs = list(map(str,input("enter the string in list: ").split()))
seen = {}
for word in strs:
    key = "".join(sorted(word))
    if key not in seen:
        seen[key] = [] 
    seen[key].append(word)
print(seen)
print(list(seen.values()))'''
