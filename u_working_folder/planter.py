if __name__ == "__main__":
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    
    import os
    import shutil
    entry_base_name = "C1_Sres"
    dst_root = "{}_store".format(entry_base_name)
    ##
    command = "pyinstaller -F -i C1.ico {}.py".format(entry_base_name)
    tio.zlshell(command, print_msg=False)
    print("--> Packaged")
    ##
    if not os.path.exists(dst_root):
        os.makedirs(dst_root)
    else:
        if not os.path.isdir(dst_root):
            os.makedirs(dst_root)
        else:
            del_list = os.listdir(dst_root)
            for f in del_list:
                file_path = os.path.join(dst_root, f)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
    ##
    # shutil.copytree("assets", "{}\\assets".format(dst_root))
    shutil.copytree("7z1900-extra", "{}\\7z1900-extra".format(dst_root))
    shutil.copy("dist\\{}.exe".format(entry_base_name), dst_root)
    shutil.copy("C1.exe", dst_root)
    # shutil.copy("C1.xlsx", dst_root)
    shutil.copy("C1.conf.txt", dst_root)
    # shutil.copy("main.png", dst_root)
    shutil.copy("C1.png", dst_root)
    ##
    bat_contents = [
        "@echo off &&cls && color a",
        "{}.exe".format(entry_base_name),
        "echo.",
        "echo Press any key to exit",
        "pause>nul",
    ]
    # bat_contents = "\n".join(bat_contents)
    tio.write("start_{}.bat".format(entry_base_name), bat_contents)
    ###
    shutil.copy("start_{}.bat".format(entry_base_name), dst_root)
    print("--> Extracted")
    pass