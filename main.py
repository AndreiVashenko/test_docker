from pathlib import Path

if __name__ == '__main__':
    print('PyCharm')
    #path_new_dir = Path(".\temp\os.txt")
    #path_new_dir = Path("C://temp_os/os.txt")
    #path_new_dir = Path("./temp/py.txt")
    #path_new_dir = Path("./temp/os.txt")
    path_new_dir1 = Path("./temp_os.txt")
    path_new_dir2 = Path("./temp/temp_os.txt")
    path_new_dir3 = Path("./temp/py.txt")

    #path_new_dir.mkdir()
    print(path_new_dir1.exists())
    print(path_new_dir2.exists())
    print(path_new_dir3.exists())

    ss = input("enter any word")
