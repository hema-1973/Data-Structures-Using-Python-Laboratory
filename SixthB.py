from collections import deque

s = input("Enter a string: ")

clean = ""
for ch in s:
    if ch.isalnum():
        clean += ch.lower()

d = deque(clean)

palindrome = True

while len(d) > 1:
    if d.popleft() != d.pop():
        palindrome = False
        break

if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
