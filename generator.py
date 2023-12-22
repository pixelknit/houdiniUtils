
def readTextLines(file_path):
    with open(file_path,"r") as file:
        lines = file.readlines()
        for line in lines:
            yield line

text_lines = readTextLines("python_poem.txt")

for i,line in enumerate(text_lines):
    if "20" in line:
        print("20 found in line: ", i)

