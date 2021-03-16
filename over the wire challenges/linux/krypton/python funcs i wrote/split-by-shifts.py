import sys

string1 = ""

key_length = int(sys.argv[2])
shift = int(sys.argv[3])
with open(sys.argv[1]) as fh:
    lines =fh.readlines()
for line in lines:
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    for index in range(shift, len(line)):
        if index % key_length == shift:
            string1 += line[index]
print(string1)