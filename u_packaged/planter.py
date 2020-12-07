if __name__ == "__main__":
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    command = "pyinstaller -F u_packer.py"
    tio.zlshell(command, print_msg=False)
    print("--> Packaged")
    import os
    import shutil
    dst_root = "u_store"
    if os.path.exists(dst_root):
        shutil.rmtree(dst_root)
    shutil.copytree("assets", "{}\\assets".format(dst_root))
    shutil.copytree("7z1900-extra", "{}\\7z1900-extra".format(dst_root))
    shutil.copy("dist\\u_packer.exe", dst_root)
    shutil.copy("C1.xlsx", dst_root)
    shutil.copy("local.conf.txt", dst_root)
    shutil.copy("start_console.bat", dst_root)
    print("--> Extracted")
    pass