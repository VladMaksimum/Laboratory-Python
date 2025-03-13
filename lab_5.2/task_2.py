from pathlib import Path

dirpath = Path(input("dirpath = "))
files = input("files = ").split()


if not dirpath.exists():
    dirpath = Path.cwd
files_in_dirpath = list(dirpath.glob("*"))

if files != []:
    Path("lab_5.2/in_dir.txt").touch()
    Path("lab_5.2/out_dir.txt").touch()

    inf = open("lab_5.2/in_dir.txt",'w')
    outf = open("lab_5.2/out_dir.txt",'w')
    inl = []
    outl = []

    for file in files:
        file_path = Path(f"{dirpath.name}/{file}")
        if file_path.exists():
            inf.write(f"{file}\n")
            inl.append(file)
        else:
            outf.write(f"{file}\n")
            outl.append(file)


    print("Files in directory: ", inl)
    print("Files out of directory: ", outl)

    inf.close()
    outf.close()
else:
    size = 0
    len = 0
    for file in files_in_dirpath:
        size+=file.stat().st_size
        len+=1

    print("In dirpath ", len, " files.")
    print("Size of dirpath = ", size, " байт")