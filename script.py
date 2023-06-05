import os

path = "dataset_atributos/color"
f = open("catalog.txt", "w")

all_paths = []
for i in os.listdir(path):
    # print(os.path.join(path,i))
    for j in os.listdir(os.path.join(path,i)):
        print(os.path.join(path, i, j))
        f.write(os.path.join(path, i, j))
        f.write("\n")
        # all_paths.append(os.path.join(path, i, j))
print(len(all_paths))
# print(all_paths)

f.close()