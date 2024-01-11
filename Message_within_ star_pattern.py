message = input("Enter the message: ")
words = message.split()
m = len(words)+2
n = max(len(word) for word in words)+2 

for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            print("*", end="")
        elif i - 1 < len(words) and j - 1 < len(words[i - 1]):
            print(words[i - 1][j - 1], end="")
        else:
            print(" ", end="")
    print()