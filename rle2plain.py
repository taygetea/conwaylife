import sys


length = 0
width = 0

filename = sys.argv[1]
with open(filename, 'r') as f:
    content = ""
    lines = []
    for line in f:
        if line.startswith("#"):
            print line
        elif line.startswith("x ="):
            parsed = filter(lambda x: x not in ",", line).split()
            length = parsed[5]
            width = parsed[2]
        else:
            content += line.strip()
    output = content.split("$")
for row in output:
    step = ""
    final = []
    for char in row:
        try:
            int(char)
            step += char
        except ValueError:
            step += char
            final.append(step)
            step = ""
print final
