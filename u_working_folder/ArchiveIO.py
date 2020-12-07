class ArchiveIO():
    def print_ArchiveIO(self):
        print("--> {}".format("print_ArchiveIO"))
    
    def download(self, filename="", url="", target_folder="", chunk_size=1024):
        import os
        import requests
        from sys import stdout
        import time
        ###
        from TextfileIO import TextfileIO
        tio = TextfileIO()
        ####
        
        if target_folder == "":
            file_to_save = os.path.join(os.getcwd(), filename)
        else:
            file_to_save = os.path.join(target_folder, filename)

        print(file_to_save)
        tio.mkpaths([file_to_save])

        response = requests.get(url, stream=True)
        if response.status_code==200:
            show = 0
            show2 = 0
            # binary mode doesn't take an encoding argument
            with open(file_to_save, "wb") as f:
                # f.write(response.content)
                filesize = response.headers["Content-Length"]
                times = int(filesize) // chunk_size
                if times>0:
                    show = 1 / times
                    show2 = 1 / times
                start = 1

                for chunk in response.iter_content(chunk_size):
                    f.write(chunk)
                    if start <= times:
                        stdout.write(f"-- progress: {show:.2%}\n")
                        start += 1
                        show += show2
                    else:
                        stdout.write("-- progress: 100%")
                        show = 1
                    ###
                    self.progress = f"{show:.2%}"
                print("\n-- End download")
        
        return response.status_code

    def unzip_customized(self, zip_files=[], password="", target_folder="", packaged=False):
        import os
        import zipfile
        import time
        time_begin = time.time()
        for zip_files_el in zip_files:
            time_start = time.time()
            basename = os.path.basename(zip_files_el)
            basename_fore = os.path.splitext(basename)[0]
            basename_back = os.path.splitext(basename)[1]
            print(basename)
            print(basename_fore)
            print(basename_back)
            target_folder_new=os.path.join(target_folder)
            if packaged is True:
                target_folder_new=os.path.join(target_folder, basename_fore)
            
            # import zipfile
            daemons = zipfile.ZipFile(zip_files_el)#文件的路径与文件名
            daemons_nl = daemons.namelist() # 得到压缩包里所有文件
            for daemons_nl_el in daemons_nl:
                daemons.extract(daemons_nl_el, target_folder_new, pwd=password.encode("utf-8")) # 循环解压文件到指定目录
            daemons.close() # 关闭文件，必须有，释放内存
            time_end = time.time()
            expired = format(time_end-time_start, ".7f")
            print("--> {} {}".format(expired, zip_files_el))
        # pass
        time_end = time.time()
        expired = format(time_end-time_begin, ".7f")
        print("--> {} {}".format(expired, "--Summary--"))

    def unzip_plugin(self, zip_files=[], password="", target_folder="", packaged=False):
        import os
        from TextfileIO import TextfileIO
        tio = TextfileIO()
        for zip_files_el in zip_files:
            basename = os.path.basename(zip_files_el)
            basename_fore = os.path.splitext(basename)[0]
            basename_back = os.path.splitext(basename)[1]
            print(basename)
            print(basename_fore)
            print(basename_back)
            target_folder_new=os.path.join(target_folder)
            if packaged is True:
                target_folder_new=os.path.join(target_folder, basename_fore)

            ## -aoa overwrite -aos skip
            ## e (release), x (full path release)
            cmd_contents = "7z1900-extra\\7za.exe e -o{target_folder} {zip_files_el} -p{password} -aoa".format(
                    target_folder=target_folder_new,
                    zip_files_el=zip_files_el,
                    password=password
                    )
            print("--->cmd_contents:\n{}\n<---".format(cmd_contents))
            tio.zlshell(cmd_contents)
        # pass
    
    ### The following functions return (abso_paths, rela_paths)
    def top_files(self, target_folder="", allowed_suffixes=[".zip"]):
        import os
        allowed_files = []
        allowed_suffixes_new = [allowed_suffixes_el.lower() for allowed_suffixes_el in allowed_suffixes]
        for root, _, files in os.walk(os.path.join(target_folder)):  
            # print(root) #当前目录路径  
            # print(dirs) #当前路径下所有子目录  
            # print(files) #当前路径下所有非目录子文件  
            for files_el in files:
                if os.path.splitext(files_el)[1].lower() in allowed_suffixes_new or len(allowed_suffixes)==0:
                    allowed_files.append(os.path.join(root, files_el))
            break

        return allowed_files

    def nesting_files(self):
        pass
    def top_folders(self):
        pass
    def some_has(self, src=[], dst=[]):
        rets = False
        if len(dst)>0:
            for src_el in src:
                if src_el in dst:
                    rets = True
                    break
        else:
            rets = False
        return rets
    def any_has(self, src=[], dst=[]):
        rets = True
        if len(dst)>0:
            for src_el in src:
                if src_el not in dst:
                    rets = False
                    break
        else:
            rets = False
        return rets
    ####
    

if __name__ == "__main__":
    from ArchiveIO import ArchiveIO
    aio = ArchiveIO()
    # rets = aio.download(
    #     filename="0QCN30WW.zip",
    #     url="http://seservice.lenovo.com/static_file/C1_Depository/0QCN30WW.zip",
    #     target_folder="download2"
    #     )
    # print(rets)
    # rets = aio.download(
    #     filename="0UCN25WW.zip",
    #     url="http://seservice.lenovo.com/static_file/C1_Depository/0UCN25WW.zip",
    #     target_folder="download2"
    #     )
    # print(rets)
    # rets = aio.download(
    #     filename="1YCN40WW.zip",
    #     url="http://seservice.lenovo.com/static_file/C1_Depository/1YCN40WW.zip",
    #     target_folder="download2"
    #     )
    # print(rets)
    # rets = aio.download(
    #     filename="sha256sum.txt",
    #     url="http://seservice.lenovo.com/static_file/C1_Depository/sha256sum.txt",
    #     target_folder="download2"
    #     )
    # print(rets)
    # aio.unzip_plugin(
    #     zip_files=["download2\\0QCN30WW.zip",
    #     "download2\\0UCN25WW.zip"],
    #     password="48l7TIcGWxr0mZVhU1X3To.",
    #     # target_folder="download2\\temp2",
    #     target_folder="E:\\.C1_Store",
    #     packaged=True
    #     )

    # aio.unzip_customized(
    #     zip_files=["download2\\0QCN30WW.zip",
    #     "download2\\0UCN25WW.zip"],
    #     password="48l7TIcGWxr0mZVhU1X3To.",
    #     # target_folder="download2\\temp2",
    #     target_folder="E:\\.C1_Store",
    #     packaged=True
    #     )

    # zip_files = aio.top_files(target_folder="downloads")
    # print("--> zip_files: {}".format(zip_files))

    ##
    rets = aio.any_has(src=[12,8,1,17],dst=[8,12,17,6])
    print("--> rets: {}".format(rets))
    pass