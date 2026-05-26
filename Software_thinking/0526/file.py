import os

dir1 = input("첫 번째 디렉토리 이름: ")
dir2 = input("두 번째 디렉토리 이름: ")

path1 = os.path.join(os.getcwd(), dir1)
path2 = os.path.join(os.getcwd(), dir2)

if not os.path.isdir(path1):
    print(f"{dir1} 디렉토리가 존재하지 않습니다.")
    exit()

if not os.path.isdir(path2):
    print(f"{dir2} 디렉토리가 존재하지 않습니다.")
    exit()

files1 = sorted([
    f for f in os.listdir(path1)
    if os.path.isfile(os.path.join(path1, f))
])

files2 = sorted([
    f for f in os.listdir(path2)
    if os.path.isfile(os.path.join(path2, f))
])


if len(files1) != len(files2):
    print("파일 개수가 다릅니다.")
    exit()

print("파일 개수는 같습니다.\n")

if files1 != files2:
    print("파일 이름이 다릅니다.")
    print(files1)
    print(files2)
    exit()

print("파일 이름이 같습니다.\n")

all_same = True

for file_name in files1:
    file1 = os.path.join(path1, file_name)
    file2 = os.path.join(path2, file_name)

    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)

    if size1 != size2:
        print(f"[크기 다름] {file_name}")
        all_same = False
        continue


    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        content1 = f1.read()
        content2 = f2.read()

    if content1 == content2:
        print(f"[같음] {file_name}")
    else:
        print(f"[내용 다름] {file_name}")
        all_same = False

if all_same:
    print("\n두 디렉토리의 파일이 모두 동일합니다.")
else:
    print("\n두 디렉토리의 파일에 차이가 있습니다")