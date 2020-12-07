
def get_all_packages(max_count=None):
    import pandas as pd

    df=pd.read_excel('C1.xlsx', sheet_name=0, usecols=None)
    fields = df.columns.values.tolist()
    fields = [fields_el.replace(".", "_") for fields_el in fields]
    items = df.values

    all_packages = {}
    for items_el_index in range(len(items)):
        if max_count is None or max_count <= 0:
            pass
        else:
            if items_el_index > max_count:
                break

        items_el = items[items_el_index]
        items_el_dict = dict(zip(fields, items_el))
        # print(items_el_dict)
        el_key = items_el_dict["C1Package"]
        if not el_key in all_packages:
            all_packages[el_key] = [items_el_dict]
        else:
            all_packages[el_key].append(items_el_dict)
        pass

    return all_packages

def pack_folders(cmder="7z1900-extra\\7za.exe",
    options="a", 
    target_file="output\\pw.zip", 
    source_folder="assets\\001-dir", 
    password="-p20201009"):
    # 7z1900-extra\7za.exe a output\pw.zip assets\001-dir\* -p20201009
    import os
    from TextfileIO import TextfileIO
    tio = TextfileIO()

    working_dir = os.getcwd()
    g_cmder = os.path.abspath(cmder)
    g_target_file = os.path.abspath(target_file)
    command = "{cmder} {options} {target_file} {source_folder} {password}".format(
        cmder = g_cmder, 
        options = options, 
        target_file = g_target_file, 
        source_folder = "*", 
        password = password
    )
    # print("command: {}".format(command))
    if os.path.exists(g_target_file):
        os.remove(g_target_file)

    os.chdir(source_folder)
    tio.zlshell(command, print_msg=False)
    os.chdir(working_dir)

def get_all_folders(target_folder):
    import os
    all_folders = []
    for root, dirs, _ in os.walk(target_folder):  
        for dirs_el in dirs:
            all_folders.append((os.path.join(root, dirs_el),dirs_el))
        break
    return all_folders
def get_merge_fields(all_packages={}, keywords=""):
    # BIOSID/C1Package/PN/MT/CrisisBIOS/Arg01/No_
    merge_fields=";".join(["","","","","","",""])
    if keywords in all_packages:
        els = all_packages[keywords]
        ## fields
        BIOSID = "==".join([str(el["BIOSID"]) for el in els])
        C1Package = "==".join([str(el["C1Package"]) for el in els])
        PN = "==".join([str(el["PN"]) for el in els])
        MT = "==".join([str(el["MT"]) for el in els])
        CrisisBIOS = "==".join([str(el["CrisisBIOS"]) for el in els])
        Arg01 = "==".join([str(el["Arg01"]) for el in els])
        No_ = "==".join([str(el["No_"]) for el in els])
        ## merge fields
        merge_fields = ";".join([BIOSID,C1Package,PN,MT,CrisisBIOS,Arg01,No_])

    return merge_fields

def generate_sha256sum(password="-p20201009"):
    from TextfileIO import TextfileIO
    tio = TextfileIO()

    all_packages = get_all_packages(max_count=None)
    # print(len(all_packages.keys()))
    
    all_folders = get_all_folders("assets")
    sha256sum_items = []
    for all_folders_el in all_folders:
        # print("--> all_folders_el: {}".format(all_folders_el))
        pack_folders(cmder="7z1900-extra\\7za.exe",
            options="a", 
            target_file="output\{}.zip".format(all_folders_el[1]), 
            source_folder="{}".format(all_folders_el[0]), 
            password=password)
        files_el = "output\{}.zip".format(all_folders_el[1])
        files_el2 = "{}.zip".format(all_folders_el[1])
        sha1=tio.getSHA1(files_el)
        mfs = get_merge_fields(all_packages=all_packages, keywords=all_folders_el[1])
        sha256sum_items_el = "{};{};recommended;{}".format(sha1, files_el2, mfs)
        print(sha256sum_items_el)
        sha256sum_items.append(sha256sum_items_el)
    
    ## Generate configuration file 
    tio.write("output\sha256sum.txt", contents=sha256sum_items)


if __name__ == "__main__":
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    json_dict = tio.get_json_dict("local.conf.txt")
    password=json_dict['g_password']
    generate_sha256sum(password="-p{}".format(password))
    pass