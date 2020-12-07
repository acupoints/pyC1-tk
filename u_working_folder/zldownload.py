def downloadfile(filename="", url="", chunk_size=1024):
    import os
    import requests
    from sys import stdout
    import time

    file_to_save = os.path.join(os.getcwd(), filename)  #获取当前路径
    print(file_to_save)

    response = requests.get(url, stream=True)
    if response.status_code==200:
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
                    # stdout.write(f"下载进度: {show:.2%}\n")
                    start += 1
                    show += show2
                else:
                    stdout.write("下载进度: 100%")
                # time.sleep(0.1)
            print("\n结束下载")
    
    return response.status_code

def get_all_filenames(source_folder, use_internal_path=True):
    all_filenames = []
    import os
    # for root, dirs, files in os.walk(source_folder):
    for root, _, files in os.walk(source_folder):
        # print("root: {}".format(root))
        # print("dirs: {}".format(dirs))
        for files_el in files:
            internal_path = os.path.join(root, files_el)
            if use_internal_path:
                # print("--{}".format(internal_path))
                internal_path = internal_path.split(source_folder)[1]
                internal_path = internal_path.lstrip("\\")
                # print("--{}".format(internal_path))
            all_filenames.append(internal_path)
            
    return all_filenames
def get_diff_filenames(old_filenames, new_filenames, base_dir=""):
    import os
    diff_filenames = []
    for new_filenames_el in new_filenames:
        if new_filenames_el not in old_filenames:
            diff_filenames.append(new_filenames_el)
    return [os.path.join(base_dir, diff_filenames_el) for diff_filenames_el in diff_filenames]
def get_diff_entries(old_entries, new_entries, base_dir=""):
    import os
    diff_entries = []
    for new_entries_el in new_entries:
        if new_entries_el not in old_entries:
            diff_entries.append(new_entries_el)
    return [os.path.join(base_dir, diff_entries_el) for diff_entries_el in diff_entries]
def clear_cache_files(source_folder):
    import os
    import shutil
    del_list = os.listdir(source_folder)
    for f in del_list:
        file_path = os.path.join(source_folder, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("--> {}".format(file_path))
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def create_backup_directories(backup_directories=[]):
        import os
        streamDirectories=backup_directories[:]
        for streamDirectories_el in streamDirectories:
            if not os.path.exists(streamDirectories_el):
                os.makedirs(streamDirectories_el)
                print("--- Create stream folder {}".format(streamDirectories_el))

def download_all_updates(base_url="http://192.168.56.102:9581/file/", 
        checklist="sample-sha256sum.txt", 
        password="20201009", output_folder="E:\\1009_udown\\u_FAT32"):
    import os
    import shutil
    import zipfile
    from TextfileIO import TextfileIO
    ##
    tio = TextfileIO()
    ###

    ## u_working_folder\downloads\temp
    print("-- Create download folder and temporary folder")
    backup_directories = [
        "downloads\\temp",
        output_folder,
    ]
    create_backup_directories(backup_directories=backup_directories)
    hash_target_file = checklist
    hash_source_file = "{base_url}{checklist}".format(base_url=base_url,checklist=checklist)
    downloadfile(filename=hash_target_file, url=hash_source_file)
    ##
    # from TextfileIO import TextfileIO
    # tio = TextfileIO()
    old_entries=tio.read(os.path.join(output_folder,"verified.txt"))
    new_entries=tio.read(hash_target_file)
    # rets=tio.read(hash_target_file)
    rets=get_diff_entries(old_entries, new_entries)

    for rets_el in rets:
        print("-->{}<--".format(rets_el))
        if rets_el == "":
            continue
        rets_el_sha1 = rets_el.split(";")[0]
        rets_el_file = rets_el.split(";")[1]
        rets_el_mode = rets_el.split(";")[2]
        rets_el_file_target = "downloads\\{}".format(rets_el_file)
        rets_el_file_source = "{base_url}{packaged_file}".format(base_url=base_url,packaged_file=rets_el_file)
        dl_rets=downloadfile(filename=rets_el_file_target, url=rets_el_file_source)
        if dl_rets == 200:
            print("-- Download completed")
            sha1 = tio.getSHA1(rets_el_file_target)
            if sha1==rets_el_sha1:
                # import zipfile
                daemons = zipfile.ZipFile(rets_el_file_target)#文件的路径与文件名
                daemons_nl = daemons.namelist() # 得到压缩包里所有文件
                old_filenames = get_all_filenames("downloads\\temp\\_{}".format(rets_el_mode))
                print("--> old_filenames: {}".format(old_filenames))
                for daemons_nl_el in daemons_nl:
                    # daemons.extract(daemons_nl_el, "downloads\\temp", pwd="20201009".encode("utf-8")) # 循环解压文件到指定目录
                    daemons.extract(daemons_nl_el, "downloads\\temp\\_{}".format(rets_el_mode), pwd=password.encode("utf-8")) # 循环解压文件到指定目录
                        
                daemons.close() # 关闭文件，必须有，释放内存
                new_filenames = get_all_filenames("downloads\\temp\\_{}".format(rets_el_mode))
                print("--> new_filenames: {}".format(new_filenames))
                old_filenames = []
                diff_filenames = get_diff_filenames(old_filenames, new_filenames, base_dir="")
                diff_filenames_src = get_diff_filenames(old_filenames, new_filenames, 
                    base_dir="downloads\\temp\\_{}".format(rets_el_mode))
                print("--> diff_filenames: {}".format(diff_filenames))
                ## 拷贝临时文件，mode=>deprecated同名删除，mode=>recommended同名覆盖
                ## 01、删除同名文件
                # target_folder = "E:\\1009_udown\\u_FAT32"
                target_folder = output_folder
                # import os
                # import shutil
                target_files = [os.path.join(target_folder,diff_filenames_el) for diff_filenames_el in diff_filenames]
                print("target_files: {}".format(target_files))
                if rets_el_mode=="recommended":
                    ## 02、拷贝新的同名文件到对应的文件夹
                    for target_files_el_index in range(len(target_files)):
                        target_files_el=target_files[target_files_el_index]
                        if os.path.exists(target_files_el):
                            os.remove(target_files_el)
                        create_backup_directories(backup_directories=[os.path.dirname(target_files_el)])
                        shutil.copyfile(diff_filenames_src[target_files_el_index], target_files_el)
                    # pass
                    pass
                elif rets_el_mode=="deprecated":
                    ## 03、啥也不做
                    for target_files_el_index in range(len(target_files)):
                        target_files_el=target_files[target_files_el_index]
                        if os.path.exists(target_files_el):
                            os.remove(target_files_el)
                        # create_backup_directories(backup_directories=[os.path.dirname(target_files_el)])
                        # shutil.copyfile(diff_filenames_src[target_files_el_index], target_files_el)
                    # pass
                    pass

            else:
                print("-- File may be tampered with")
            # # 删除临时文件及压缩包
            clear_cache_files("downloads")
        elif dl_rets == 404:
            print("-- File not found")

    # import os
    # import shutil
    shutil.copyfile(hash_target_file, os.path.join(output_folder,"verified.txt"))
def download_main():
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    json_dict = tio.get_json_dict("u.conf.txt")
    base_url=json_dict['g_base_url']
    checklist=json_dict['g_checklist']
    # subpath=json_dict['g_subpath']
    # base_url="http://192.168.56.102:9581/file/"
    # checklist="sha256sum.txt"

    password="48l7TIcGWxr0mZVhU1X3To."
    output_folder="E:\\1009_udown\\u_FAT32"

    try:
        download_all_updates(base_url=base_url, checklist=checklist, password=password, output_folder=output_folder)
    except Exception as ex:
        print(ex)
        print("--> Remote resource is not accessible")
    finally:
        print("--> The download task processing process is completed")


if __name__ == "__main__":
    download_main()
    # pass