# def isSubsequence(s, t):
#     ascending = []
#     for char in s:
#         map(t.find, char)

def isSubsequence(s, t):
    ascending = list(map(t.find, s))
    print(ascending)
    return False if -1 in ascending else sorted(ascending) == ascending and len(set(ascending)) == len(ascending)

print(isSubsequence('abc', 'abcdabdab')) # True
print(isSubsequence('abc', 'ahbgdc')) # True
print(isSubsequence('axc', 'ahbgdc')) # False
print(isSubsequence('', 'ahbgdc')) # True
print(isSubsequence('abc', '')) # False
print(isSubsequence('b', 'c')) # False
print(isSubsequence("aaaaaa", "bbaaaa")) # False
print(isSubsequence("ab", "baab")) # True