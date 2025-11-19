# Divide Village Using Fences
n = int(input())
v = input().strip()

# Rule 1: If two H's are consecutive, impossible
if "HH" in v:
    print("NO")
else:
    print("YES")
    # Replace all dots with B to maximize fences
    print(v.replace(".", "B"))
