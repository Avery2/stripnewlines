# print("paste input here: ", end="")
import sys
lines = '\n'.join(sys.stdin.readlines())
# ! remove newlines
new_lines = lines.replace("\n", " ").replace("  ", " ")

print(len(new_lines))

# ! add newlines
# new_lines = lines.replace("\n", "\n\n").replace("  ", " ")
print(new_lines)
