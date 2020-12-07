import tkinter as tk
from tkinter import ttk
import time
import os
from TextfileIO import TextfileIO

##
tio = TextfileIO()
updated_flag=False
progress = "--"
items_count = 0
item_index = 0
assist_download_status = "completed" # processing/completed
##
all_removable_disks = []
g_verified_items_original = []
g_full_volume_labels = {}
##
from TextfileIO import TextfileIO
tio = TextfileIO()
json_dict = tio.get_json_dict("C1.conf.txt")
g_base_url=json_dict['g_base_url']
g_checklist=json_dict['g_checklist']
g_subpath=json_dict['g_subpath']
# g_base_url="http://192.168.56.102:9581/file/"
# g_checklist="sha256sum.txt"
# g_subpath="1009_udown\\u_FAT32"
g_password="48l7TIcGWxr0mZVhU1X3To."
g_output_folder="ZL:\\"
# g_cache_folder=".uDown_cache"


g_json_dict = tio.get_json_dict("C1.conf.txt")
###
import sys
# print(sys.argv[1:])
if "Post-processing enabled" not in g_json_dict:
    print("---> {}".format("Missing startup parameters"))
    sys.exit()
else:
    g_post_processing=g_json_dict["Post-processing enabled"]
    if not g_post_processing:
        print("---> {}".format("Parameter ID cannot be empty"))
        sys.exit()
    elif not "{} {}".format(g_post_processing, " ".join(sys.argv[1:])).strip().endswith(".nil .start"):
        print("{}".format("{} {}".format(g_post_processing, " ".join(sys.argv[1:]))))
        print("---> {}".format("Parameter identifies invalid"))
        sys.exit()
###
# print(g_json_dict)

g_base_url=g_json_dict["g_base_url"]
g_checklist=g_json_dict["g_checklist"]
g_subpath=g_json_dict["g_subpath"]
g_cache_folder=g_json_dict["g_cache_folder"]
g_verified=g_json_dict["g_verified"]
g_cached=g_json_dict["g_cached"]
g_text_field_delimiter=g_json_dict["g_text_field_delimiter"]
g_text_files_delimiter=g_json_dict["g_text_files_delimiter"]

g_frame_start_checking=g_json_dict["g_frame_start_checking"]
g_frame_title=g_json_dict["g_frame_title"]
g_frame_version=g_json_dict["g_frame_version"]
g_frame_width=g_json_dict["g_frame_width"]
g_frame_height=g_json_dict["g_frame_height"]
g_frame_button_font_size=g_json_dict["g_frame_button_font_size"]
g_frame_theme_disk_info_height=g_json_dict["g_frame_theme_disk_info_height"]
g_frame_border_thickness=g_json_dict["g_frame_border_thickness"]
g_frame_caption_thickness=g_json_dict["g_frame_caption_thickness"]
g_frame_caption_font_size=g_json_dict["g_frame_caption_font_size"]
g_frame_caption_fg=g_json_dict["g_frame_caption_fg"]
g_frame_caption_control_btn_font_size=g_json_dict["g_frame_caption_control_btn_font_size"]
g_frame_caption_control_btn_fg=g_json_dict["g_frame_caption_control_btn_fg"]

g_frame_theme_fg_title_bar=g_json_dict["g_frame_theme_fg_title_bar"]
g_frame_theme_bg_title_bar=g_json_dict["g_frame_theme_bg_title_bar"]
g_frame_theme_hlbg_control_btn_minimized=g_json_dict["g_frame_theme_hlbg_control_btn_minimized"]
g_frame_theme_hlbg_control_btn_closed=g_json_dict["g_frame_theme_hlbg_control_btn_closed"]
g_frame_theme_hlfg_button_mouse_up=g_json_dict["g_frame_theme_hlfg_button_mouse_up"]
g_frame_theme_hlfg_button_mouse_down=g_json_dict["g_frame_theme_hlfg_button_mouse_down"]
g_frame_theme_divider_border=g_json_dict["g_frame_theme_divider_border"]
g_frame_theme_icon_background=g_json_dict["g_frame_theme_icon_background"]
g_frame_theme_icon_size=g_json_dict["g_frame_theme_icon_size"]
g_frame_theme_icon_path=g_json_dict["g_frame_theme_icon_path"]
g_button_refresh_disks_text=g_json_dict["g_button_refresh_disks_text"]
g_button_update_packages_text=g_json_dict["g_button_update_packages_text"]
g_button_terminate_download_text=g_json_dict["g_button_terminate_download_text"]
g_button_query_text=g_json_dict["g_button_query_text"]
g_button_toggle_text=g_json_dict["g_button_toggle_text"]
g_label_update_progress_hori_gap=g_json_dict["g_label_update_progress_hori_gap"]
g_label_update_progress_font_size=g_json_dict["g_label_update_progress_font_size"]
g_label_update_progress_fg=g_json_dict["g_label_update_progress_fg"]
g_label_update_progress_tx_loading=g_json_dict["g_label_update_progress_tx_loading"]
g_label_update_progress_tx_writing=g_json_dict["g_label_update_progress_tx_writing"]
g_label_update_progress_tx_loaded=g_json_dict["g_label_update_progress_tx_loaded"]

g_label_drive_letter_prompt=g_json_dict["g_label_drive_letter_prompt"]
g_label_drive_letter_font_size=g_json_dict["g_label_drive_letter_font_size"]
g_label_empty_drive_letter_prompt=g_json_dict["g_label_empty_drive_letter_prompt"]
g_label_local_assets_grouping_prompt=g_json_dict["g_label_local_assets_grouping_prompt"]
g_label_cloud_assets_grouping_prompt=g_json_dict["g_label_cloud_assets_grouping_prompt"]

g_data_grouping_column_alias=g_json_dict["g_data_grouping_column_alias"]
g_data_grouping_column_width=g_json_dict["g_data_grouping_column_width"]
g_data_grouping_heading_align=g_json_dict["g_data_grouping_heading_align"]
g_data_grouping_column_align=g_json_dict["g_data_grouping_column_align"]
g_data_full_fields=g_json_dict["g_data_full_fields"]
g_data_search_fields=g_json_dict["g_data_search_fields"]
# g_data_filtered_fields=g_json_dict["g_data_filtered_fields"]
g_data_show_fields=g_json_dict["g_data_show_fields"]
g_data_filtered_fields = g_data_show_fields[:]
g_data_show_fields_alias=g_json_dict["g_data_show_fields_alias"]
g_data_show_fields_width=g_json_dict["g_data_show_fields_width"]
g_data_show_fields_align=g_json_dict["g_data_show_fields_align"]
g_data_show_heading_align=g_json_dict["g_data_show_heading_align"]
##
g_data_theme_bg_group=g_json_dict["g_data_theme_bg_group"]
g_data_theme_bg_slave=g_json_dict["g_data_theme_bg_slave"]
g_data_theme_bg_active=g_json_dict["g_data_theme_bg_active"]
g_data_theme_bg_parent=g_json_dict["g_data_theme_bg_parent"]
g_data_theme_bg_child=g_json_dict["g_data_theme_bg_child"]
g_data_theme_bg_normal=g_json_dict["g_data_theme_bg_normal"]
g_data_theme_bg_selected=g_json_dict["g_data_theme_bg_selected"]

g_data_theme_fg_group=g_json_dict["g_data_theme_fg_group"]
g_data_theme_fg_slave=g_json_dict["g_data_theme_fg_slave"]
g_data_theme_fg_active=g_json_dict["g_data_theme_fg_active"]
g_data_theme_fg_parent=g_json_dict["g_data_theme_fg_parent"]
g_data_theme_fg_child=g_json_dict["g_data_theme_fg_child"]
g_data_theme_fg_normal=g_json_dict["g_data_theme_fg_normal"]
g_data_theme_fg_selected=g_json_dict["g_data_theme_fg_selected"]

g_data_treeview_load_status_available=g_json_dict["g_data_treeview_load_status_available"]
g_data_treeview_load_status_loaded=g_json_dict["g_data_treeview_load_status_loaded"]
g_data_treeview_load_status_overwrite=g_json_dict["g_data_treeview_load_status_overwrite"]
g_data_treeview_load_status_original=g_json_dict["g_data_treeview_load_status_original"]

g_data_treeview_group_prefix=g_json_dict["g_data_treeview_group_prefix"]
g_data_treeview_parent_prefix=g_json_dict["g_data_treeview_parent_prefix"]
g_data_treeview_display_node_column=g_json_dict["g_data_treeview_display_node_column"]

####
x, y = 0, 0

zl_gap=12+g_frame_theme_icon_size

# zl_theme_error="#000000"
# zl_theme_warn="#000000"
# zl_theme_info="#0000ff"
# zl_theme_debug="#000000"

##
verified_items = []
stacked_items = {}
# full_fields = ['sha1_b64','packaged','update_mode','BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01','No_']
# filtered_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']
# show_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']
full_fields = g_data_full_fields[:]
filtered_fields = g_data_filtered_fields[:]
show_fields = g_data_show_fields[:]
show_fields_alias = g_data_show_fields_alias[:]
show_fields_width = g_data_show_fields_width[:]
show_fields_align = g_data_show_fields_align[:]
###

def startMove(event):
    global x, y
    # print(event.x_root, event.x, borderFrame.winfo_rootx())
    x = event.x
    y = event.y
def stopMove(event):
    global x, y
    x = None
    y = None
def moving(event):
    global x, y
    x_ = (event.x_root - x - (zl_gap))
    y_ = (event.y_root - y)
    root.geometry("+%s+%s" % (x_, y_))
    
def frame_mapped(e):
    # print(e)
    root.update_idletasks()
    root.overrideredirect(True)
    root.state('normal')

def minimize(event):
    root.update_idletasks()
    root.withdraw()
    root.overrideredirect(False)
    #root.state('withdrawn')
    root.state('iconic')

def exitProgram(event):
    root.withdraw()
    os._exit(0)

def hover(event):
    event.widget.config(bg=g_frame_theme_hlbg_control_btn_closed)
def unhover(event):
    event.widget.config(bg=g_frame_theme_bg_title_bar)
def hoverMin(event):
    event.widget.config(bg=g_frame_theme_hlbg_control_btn_minimized)
def unHoverMin(event):
    event.widget.config(bg=g_frame_theme_bg_title_bar)


root = tk.Tk()
removable_disk_selected = tk.StringVar()
var_update_progress = tk.StringVar()
var_query = tk.StringVar()
var_query.set(g_button_query_text)
var_assets_grouping_prompt = tk.StringVar()
# var_assets_grouping_prompt.set("{local_assets_grouping_prompt}{local_assets}{cloud_assets_grouping_prompt}{cloud_assets}".format(
#     local_assets_grouping_prompt=g_label_local_assets_grouping_prompt,local_assets=0,
#     cloud_assets_grouping_prompt=g_label_cloud_assets_grouping_prompt,cloud_assets="0/0"))

var_toggle = tk.StringVar()
var_toggle.set(g_button_toggle_text)
var_refresh_disks = tk.StringVar()
var_refresh_disks.set(g_button_refresh_disks_text)
var_update_packages = tk.StringVar()
var_update_packages.set(g_button_update_packages_text)

var_volume_label = tk.StringVar()
var_volume_label.set(g_label_drive_letter_prompt)

root.title("{} {}".format(g_frame_title, g_frame_version))
root.geometry("{}x{}+0+0".format(g_frame_width, g_frame_height))
root.overrideredirect(True)

borderFrame = tk.Frame(root, width=g_frame_width, height=g_frame_height, bg=g_frame_theme_bg_title_bar, bd=g_frame_border_thickness)
borderFrame.pack_propagate(False)
borderFrame.pack(fill=tk.X)

# iconFrame = tk.Frame(borderFrame, width=zl_width, height=zl_frame_height-zl_gap/4, bg=g_frame_theme_bg_title_bar)
iconFrame = tk.Frame(borderFrame, width=g_frame_width, height=g_frame_caption_thickness, bg=g_frame_theme_bg_title_bar)
iconFrame.pack_propagate(False)
iconFrame.pack(fill=tk.X)

iconFrameLabel = tk.Label(iconFrame, bg=g_frame_theme_icon_background, bd=0)
iconFrameLabel.pack(side='left', padx=4)
import os
if os.path.exists(os.path.join(g_frame_theme_icon_path)):
    img = tk.PhotoImage(file=os.path.join(g_frame_theme_icon_path))
    iconFrameLabel.config(image=img) 

# holderFrame = tk.Frame(borderFrame, width=zl_width, height=zl_height-zl_frame_height, bg="grey62")
holderFrame = tk.Frame(borderFrame, width=g_frame_width, height=g_frame_height-g_frame_caption_thickness, bg=g_frame_theme_divider_border)
holderFrame.pack_propagate(False)
holderFrame.pack(fill=tk.BOTH, expand=1)

##
frameVT = tk.Frame(holderFrame, width=120, height=300, bg=None, bd=0)
frameVC = tk.Frame(holderFrame, width=320, height=45, bg=None, bd=0)
frameVB = tk.Frame(holderFrame, width=200, height=0, bg="#00bcd4", bd=0)
frameVT.pack(fill=tk.BOTH, ipadx=2)
frameVC.pack(fill=tk.BOTH, ipadx=2, pady=1)
frameVB.pack(fill=tk.BOTH, expand=1)

###
def get_el_C1Package_sha1(el_C1Package=""):
    global g_text_field_delimiter
    # el_C1Package = "{package_prefix}_{sha1_hexdigest}".format(
    #                         package_prefix = el_C1Package.split(g_text_field_delimiter)[0],
    #                         sha1_hexdigest = tio.get_hexdigest(plain_text=el_C1Package.split(g_text_field_delimiter)[0])[:7]
    #                     )
    el_C1Package = "{package_prefix}".format(
                            package_prefix = el_C1Package.split(g_text_field_delimiter)[0]
                        )
    return el_C1Package

def downloadfile(filename="", url="", chunk_size=1024):
    global progress
    import os
    import requests
    from sys import stdout
    import time

    global var_update_packages, g_button_update_packages_text, g_button_terminate_download_text
    # var_update_packages.set(g_button_update_packages_text)

    file_to_save = os.path.join(os.getcwd(), filename)  #获取当前路径
    print(file_to_save)

    response = requests.get(url, stream=True)
    if response.status_code==200:
        show = 0
        show2 = 0
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
                global progress, items_count, item_index
                progress = f"{show:.2%}"
                thr_update_progress()
                # time.sleep(0.1)
                
                # if var_update_packages.get()==g_button_update_packages_text:
                #     raise Exception("-- User terminated the download !")
                # global updated_flag
                # if not updated_flag:
                #     break
                
            print("\n-- End download")
    
    return response.status_code
def downloadfile_without_tips(filename="", url="", chunk_size=1024):
    global progress
    global assist_download_status
    import os
    import requests
    from sys import stdout
    import time

    global var_update_packages, g_button_update_packages_text, g_button_terminate_download_text
    # var_update_packages.set(g_button_update_packages_text)

    file_to_save = os.path.join(os.getcwd(), filename)  #获取当前路径
    print(file_to_save)

    response = requests.get(url, stream=True)
    if response.status_code==200:
        show = 0
        show2 = 0
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
                global progress, items_count, item_index
                progress = f"{show:.2%}"
                thr_update_progress()
                # time.sleep(0.1)
                if show == 1:
                    assist_download_status = "completed" # processing/completed
                else:
                    assist_download_status = "processing" # processing/completed
                
                # if var_update_packages.get()==g_button_update_packages_text:
                #     raise Exception("-- User terminated the download !")
            print("\n-- End download")
    
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

def download_checklist2(base_url="http://192.168.56.102:9581/file/", checklist="sample-sha256sum.txt", password="20201009", output_folder="E:\\1009_udown\\u_FAT32"):
    ## u_working_folder\downloads\temp
    print("-- Create download folder and temporary folder")
    backup_directories = [
        "downloads\\temp",
        output_folder,
        os.path.join(output_folder, g_cache_folder)
    ]
    create_backup_directories(backup_directories=backup_directories)
    hash_target_file = checklist
    hash_source_file = "{base_url}{checklist}".format(base_url=base_url,checklist=checklist)
    downloadfile(filename=hash_target_file, url=hash_source_file)
    ##
    # from TextfileIO import TextfileIO
    # tio = TextfileIO()
    old_entries=tio.read(os.path.join(output_folder, g_verified))
    new_entries=tio.read(hash_target_file)
    # rets=tio.read(hash_target_file)
    rets=get_diff_entries(old_entries, new_entries)
    return rets

def download_all_updates(base_url="http://192.168.56.102:9581/file/", checklist="sample-sha256sum.txt", password="20201009", output_folder="E:\\1009_udown\\u_FAT32"):
    global full_fields
    global g_cache_folder
    global g_cached
    global g_data_treeview_load_status_overwrite
    global g_text_field_delimiter
    global g_verified
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
        "downloads",
        # "downloads\\temp",
        output_folder,
        os.path.join(output_folder, g_cache_folder)
    ]
    create_backup_directories(backup_directories=backup_directories)
    hash_target_file = checklist
    hash_source_file = "{base_url}{checklist}".format(base_url=base_url,checklist=checklist)
    if not os.path.exists(hash_target_file):
        downloadfile(filename=hash_target_file, url=hash_source_file)
    ##
    # from TextfileIO import TextfileIO
    # tio = TextfileIO()
    old_entries=tio.read(os.path.join(output_folder, g_verified))
    new_entries=tio.read(hash_target_file)
    # rets=tio.read(hash_target_file)
    rets=get_diff_entries(old_entries, new_entries)

    target_files = []
    target_files_cache = []
    time_start_end_items = []
    # for rets_el in rets:
    for rets_el_index in range(len(rets)):
        rets_el = rets[rets_el_index]
        rets_el_dict = dict(zip(full_fields, rets_el.split(";")))
        ###
        global progress, items_count, item_index
        items_count=len(rets)
        item_index=rets_el_index
        thr_update_progress()

        print("-->{}<--".format(rets_el))
        if rets_el == "":
            continue
        # full_fields = ['sha1_b64','packaged','update_mode','BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01','No_']
        # filtered_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']
        # rets_el_sha1 = rets_el.split(";")[0]
        # rets_el_file = rets_el.split(";")[1]
        # rets_el_mode = rets_el.split(";")[2]
        rets_el_sha1 = rets_el_dict['sha1_b64']
        rets_el_file = rets_el_dict['packaged']
        rets_el_mode = rets_el_dict['update_mode']
        rets_el_C1Package = rets_el_dict['C1Package']
        if rets_el_C1Package == "":
            continue
        # print("-#1-->{}".format(rets_el_C1Package))
        rets_el_C1Package=get_el_C1Package_sha1(el_C1Package=rets_el_C1Package)
        # print("-#2-->{}".format(rets_el_C1Package))

        rets_el_Arg01 = rets_el_dict['Arg01']
        print("rets_el_Arg01: {}".format(rets_el_Arg01))

        rets_el_file_target = "downloads\\{}".format(rets_el_file)
        rets_el_file_source = "{base_url}{packaged_file}".format(base_url=base_url,packaged_file=rets_el_file)
        ###
        import time
        time_start = time.time()
        dl_rets=downloadfile(filename=rets_el_file_target, url=rets_el_file_source)
        time_end = time.time()
        time_start_end_items.append((rets_el_C1Package, format(time_end-time_start, ".7f")))
        ####
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
                target_files = [os.path.join(target_folder, diff_filenames_el) for diff_filenames_el in diff_filenames]
                target_files_cache = [os.path.join(target_folder, 
                        g_cache_folder, rets_el_C1Package, diff_filenames_el) for diff_filenames_el in diff_filenames]
                if rets_el_Arg01.split(g_text_field_delimiter)[0].lower().strip()==g_data_treeview_load_status_overwrite:
                    # target_files_cache = [os.path.join(target_folder, 
                    #     g_cache_folder, rets_el_C1Package, diff_filenames_el) for diff_filenames_el in diff_filenames]
                    ## 02、拷贝新的同名文件到对应的文件夹
                    ##
                    target_cached_file = os.path.join(target_folder, g_cache_folder, g_cached)
                    json_dict = tio.get_json_dict(target_cached_file)
                    json_dict[rets_el_C1Package] = {
                        'target_files': target_files,
                        'target_files_cache': target_files_cache,
                        'active': False,
                    }
                    tio.set_json_dict(target_cached_file,json_dict)
                    ###
                    print("json_dict: {}".format(json_dict))
                    for target_files_el_index in range(len(target_files_cache)):
                        target_files_el=target_files_cache[target_files_el_index]
                        if os.path.exists(target_files_el):
                            os.remove(target_files_el)
                        create_backup_directories(backup_directories=[os.path.dirname(target_files_el)])
                        shutil.copyfile(diff_filenames_src[target_files_el_index], target_files_el)
                    # pass
                    pass
                else:
                    # target_files = [os.path.join(target_folder, diff_filenames_el) for diff_filenames_el in diff_filenames]
                    # print("target_files: {}".format(target_files))
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
        ###
        tio.append(os.path.join(output_folder, g_verified), [rets_el])
        global verified_items
        verified_items.extend([rets_el])
        filter_all_cols_items(treeview, keywords="", verified_items=verified_items)
        print("--> {}".format(rets_el))
        
        ###
        # global progress, items_count, item_index
        items_count=len(rets)
        item_index=rets_el_index + 1
        thr_update_progress
    # import os
    # import shutil
    shutil.copyfile(hash_target_file, os.path.join(output_folder, g_verified))
    tio.write("downloads\\temp.txt",time_start_end_items)

def download_all_updates2(base_url="http://192.168.56.102:9581/file/", checklist="sample-sha256sum.txt", password="20201009", output_folder="E:\\1009_udown\\u_FAT32"):
    global full_fields
    global g_cache_folder
    global g_cached
    global g_data_treeview_load_status_overwrite

    global g_verified
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
        "downloads",
        # "downloads\\temp",
        output_folder,
        os.path.join(output_folder, g_cache_folder)
    ]
    create_backup_directories(backup_directories=backup_directories)
    # hash_target_file = os.path.join("downloads", checklist)
    # hash_source_file = "{base_url}{checklist}".format(base_url=base_url,checklist=checklist)
    global g_base_url
    global g_checklist
    hash_target_file = os.path.join("downloads", g_checklist)
    if not os.path.exists(hash_target_file):
        # downloadfile(filename=hash_target_file, url=hash_source_file)
        from ArchiveIO import ArchiveIO
        aio = ArchiveIO()
        rets = aio.download(
            filename=g_checklist,
            url="{}{}".format(g_base_url, g_checklist),
            target_folder="downloads"
            )
        ###
    ##
    # from TextfileIO import TextfileIO
    # tio = TextfileIO()
    # hash_target_file = os.path.join("downloads", g_checklist)
    old_entries=tio.read(os.path.join(output_folder, g_verified))
    new_entries=tio.read(hash_target_file)
    # rets=tio.read(hash_target_file)
    rets=get_diff_entries(old_entries, new_entries)

    # thr_download(base_url=base_url, password=password, checklist=checklist, output_folder=output_folder, rets=rets)
    nothr_download(base_url=base_url, password=password, checklist=checklist, output_folder=output_folder, rets=rets)
    

def thr_download(base_url="", password="", checklist="", output_folder="", rets=[]):
    global full_fields
    global g_cache_folder
    global g_cached
    global g_data_treeview_load_status_overwrite

    global g_verified
    import os
    import shutil
    import zipfile
    from TextfileIO import TextfileIO
    ##
    # tio = TextfileIO()
    ###

    # target_files = []
    # target_files_cache = []
    # time_start_end_items = []
    # for rets_el in rets:
    for rets_el_index in range(len(rets)):
        rets_el = rets[rets_el_index]
        rets_el_dict = dict(zip(full_fields, rets_el.split(";")))
        ###
        global progress, items_count, item_index
        # items_count=len(rets)
        # item_index=rets_el_index
        # thr_update_progress()

        print("-->{}<--".format(rets_el))
        if rets_el == "":
            continue
        # full_fields = ['sha1_b64','packaged','update_mode','BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01','No_']
        # filtered_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']
        # rets_el_sha1 = rets_el_dict['sha1_b64']
        rets_el_file = rets_el_dict['packaged']
        # rets_el_mode = rets_el_dict['update_mode']
        rets_el_C1Package = rets_el_dict['C1Package']
        if rets_el_C1Package == "":
            continue
        rets_el_C1Package=get_el_C1Package_sha1(el_C1Package=rets_el_C1Package)

        rets_el_Arg01 = rets_el_dict['Arg01']
        print("rets_el_Arg01: {}".format(rets_el_Arg01))

        rets_el_file_target = "downloads\\{}".format(rets_el_file)
        rets_el_file_source = "{base_url}{packaged_file}".format(base_url=base_url,packaged_file=rets_el_file)
        ###
        # import time
        # time_start = time.time()
        # print("-->{}\n-->{}".format(rets_el_file_target,rets_el_file_source))
        ###
        # dl_rets=
        downloadfile_without_tips(filename=rets_el_file_target, url=rets_el_file_source)
        # if not os.path.exists(rets_el_file_target):
        # else:
        #     dl_rets=200
        ####

def nothr_download(base_url="", password="", checklist="", output_folder="", rets=[]):
    global full_fields
    global g_cache_folder
    global g_cached
    global g_data_treeview_load_status_overwrite
    ##
    global g_verified
    import os
    import shutil
    import zipfile
    ##
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    ###

    # target_files = []
    # target_files_cache = []
    time_start_end_items = []
    ###
    # target_folder = output_folder
    # target_cached_file = os.path.join(target_folder, g_cache_folder, g_cached)
    # json_dict = tio.get_json_dict(target_cached_file)

    ###
    global progress, items_count, item_index
    # items_count=0
    # item_index=0
    global updated_flag
    ####
    for rets_el_index in range(len(rets)):
        if not updated_flag:
            break
        rets_el = rets[rets_el_index]
        rets_el_dict = dict(zip(full_fields, rets_el.split(";")))
        ###
        items_count=len(rets)
        item_index=rets_el_index + 1
        thr_update_progress()

        print("-->{}<--".format(rets_el))
        if rets_el == "":
            continue
        # full_fields = ['sha1_b64','packaged','update_mode','BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01','No_']
        # filtered_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']
        rets_el_sha1 = rets_el_dict['sha1_b64']
        rets_el_file = rets_el_dict['packaged']
        rets_el_mode = rets_el_dict['update_mode']
        rets_el_C1Package = rets_el_dict['C1Package']
        if rets_el_C1Package == "":
            continue
        rets_el_C1Package=get_el_C1Package_sha1(el_C1Package=rets_el_C1Package)

        rets_el_Arg01 = rets_el_dict['Arg01']
        print("rets_el_Arg01: {}".format(rets_el_Arg01))

        rets_el_file_target = "downloads\\{}".format(rets_el_file)
        rets_el_file_source = "{base_url}{packaged_file}".format(base_url=base_url,packaged_file=rets_el_file)
        ###
        import time
        time_start = time.time()
        print("-->{}\n-->{}".format(rets_el_file_target,rets_el_file_source))
        ###
        if not os.path.exists(rets_el_file_target):
            dl_rets=downloadfile(filename=rets_el_file_target, url=rets_el_file_source)
        else:
            dl_rets=200
        ####

        time_end = time.time()
        time_start_end_items.append((rets_el_C1Package, format(time_end-time_start, ".7f")))
        ####
        if dl_rets == 200:
            print("-- Download completed")
            sha1 = tio.getSHA1(rets_el_file_target)
            print("sha1-old: {}".format(sha1))
            print("sha1-new: {}".format(rets_el_sha1))
            # 解包方式2，自定义
            from ArchiveIO import ArchiveIO
            aio = ArchiveIO()
            # zip_files = aio.top_files(target_folder="downloads", allowed_suffixes=[".zip"])
            zip_files = [rets_el_file_target]
            aio.unzip_plugin(
                zip_files=zip_files,
                password=password,
                # target_folder=os.path.join(g_output_folder, g_cache_folder),
                target_folder=os.path.join(output_folder, g_cache_folder),
                packaged=True
                )
            if sha1==rets_el_sha1:
                ## 哈希暂不校验
                ###

                ####

                old_filenames = get_all_filenames("downloads\\temp\\_{}".format(rets_el_mode))
                print("--> old_filenames: {}".format(old_filenames))
                # temp_dir=os.path.join(output_folder, g_cache_folder, rets_el_C1Package)
                # tio.zlshell("7z1900-extra\\7za.exe x -o{temp_dir} {zip_file} -p{pwd} -aos".format(
                #     temp_dir=temp_dir, zip_file=rets_el_file_target,pwd=password))
                #####################################################
                ####

                # diff_filenames = get_all_filenames(temp_dir)
                # target_folder = output_folder
                # # import os
                # # import shutil
                # target_files = [os.path.join(target_folder, diff_filenames_el) for diff_filenames_el in diff_filenames]
                # target_files_cache = [os.path.join(target_folder, 
                #         g_cache_folder, rets_el_C1Package, diff_filenames_el) for diff_filenames_el in diff_filenames]
                # ###
                # target_cached_file = os.path.join(target_folder, g_cache_folder, g_cached)
                # json_dict = tio.get_json_dict(target_cached_file)
                # json_dict[rets_el_C1Package] = {
                #     'target_files': target_files,
                #     'temp_cache_folder': temp_dir,
                #     'target_files_cache': target_files_cache,
                #     'active': False,
                #     'type': rets_el_Arg01.split(g_text_field_delimiter)[0].lower().strip(),
                #     'zip_file': os.path.abspath(rets_el_file_target),
                # }
                # tio.set_json_dict(target_cached_file,json_dict)
                ###
                # print("json_dict: {}".format(json_dict))
                pass

            else:
                print("-- File may be tampered with")
            # # 删除临时文件及压缩包
            # clear_cache_files("downloads")
        elif dl_rets == 404:
            print("-- File not found")
        

def download_main(base_url="http://192.168.56.102:9581/file/", 
        checklist="sample-sha256sum.txt", password="20201009", output_folder="E:\\1009_udown\\u_FAT32"):
    global var_update_progress,var_assets_grouping_prompt
    global var_update_packages
    global g_button_update_packages_text, g_button_terminate_download_text
    # var_update_packages.set(g_button_update_packages_text)
    global tk
    global button_query
    # global button_update_packages
    global button_toggle
    ## 禁用
    button_query['state'] = tk.DISABLED
    # button_update_packages['state'] = tk.DISABLED
    button_toggle['state'] = tk.DISABLED
    try:
        # download_all_updates(base_url=base_url, checklist=checklist, password=password, output_folder=output_folder)
        download_all_updates2(base_url=base_url, checklist=checklist, password=password, output_folder=output_folder)

    except Exception as ex:
        print(ex)
        print("--> Remote resource is not accessible")
    finally:
        print("--> The download task processing process is completed")
        # var_update_progress.set("{g_label_update_progress_tx_loaded}".format(g_label_update_progress_tx_loaded=g_label_update_progress_tx_loaded))
        # var_update_progress.set(var_assets_grouping_prompt.get())
        var_update_packages.set(g_button_update_packages_text)

        global item_index
        global items_count
        print("## item_index: {}, items_count: {}".format(item_index, items_count))
        item_index=0
        items_count=0
        # ## 仅更新状态指示
        # thr_update_progress()

        ## 生成json
        import os
        import shutil
        from TextfileIO import TextfileIO
        tio = TextfileIO()
        from UtilitiesIO import UtilitiesIO
        uio = UtilitiesIO()
        # checklist="sample-sha256sum.txt"
        # hash_target_file=checklist
        hash_target_file=os.path.join("downloads", g_checklist)
        g_cached_file=os.path.join("downloads", g_cached)
        # old_entries=tio.read(os.path.join(output_folder, g_verified))
        new_entries=tio.read(hash_target_file)
        # global g_output_folder
        # global g_cache_folder
        # global g_text_field_delimiter
        # global g_cached
        # global g_data_full_fields
        uio.convert(entries=new_entries,
            g_cached=os.path.join("downloads", g_cached),
            g_output_folder=g_output_folder,
            g_cache_folder=g_cache_folder,
            g_text_field_delimiter=g_text_field_delimiter,
            g_data_full_fields=g_data_full_fields,
            downloads="downloads")
        ## 备份两个文件
        import os
        import shutil
        if not os.path.exists(os.path.join(g_output_folder, g_cache_folder)):
            os.makedirs(os.path.join(g_output_folder, g_cache_folder))
        shutil.copy(hash_target_file, os.path.join(g_output_folder, g_cache_folder, g_checklist))
        # shutil.copy(g_cached_file, os.path.join(g_output_folder, g_cache_folder, g_cached))
        my_cached_dict_file = os.path.join(g_output_folder, g_cache_folder, g_cached)
        # if not os.path.exists(my_cached_dict_file):
        #     shutil.copy(g_cached_file, my_cached_dict_file)
        old_cached_active=get_cached_active(cached_file=my_cached_dict_file)
        shutil.copy(g_cached_file, my_cached_dict_file)
        set_cached_active(cached_file=my_cached_dict_file, cached_active = old_cached_active)
        ##
        # shutil.copy(hash_target_file, os.path.join(g_output_folder, hash_target_file))

        # ## 刷新列表
        # global treeview
        # local_load(treeview)
        # var_update_packages.set(g_button_update_packages_text)

        # ###
        # # global g_output_folder
        # # global g_cache_folder, g_cached
        # import os
        # import shutil
        # target_folder = g_output_folder
        # target_cached_file = os.path.join(target_folder, g_cache_folder, g_cached)
        # json_dict = tio.get_json_dict(target_cached_file)
        # print("-200->{}".format(target_cached_file))
        # ### try004
        # ## 01 单命令解压，完成后进入下一步
        # # zip_file="{}\\*.zip".format(os.path.abspath("downloads"))
        # # cmd_contents = "7z1900-extra\\7za.exe x -o{temp_dir} {zip_file} -p{pwd} -aoa".format(
        # #         temp_dir=os.path.join(g_output_folder, g_cache_folder), zip_file=zip_file, pwd=password)
        # # print("--->cmd_contents:\n{}\n<---".format(cmd_contents))
        # # tio.zlshell(cmd_contents)
        # # # 解包方式2，自定义
        # # from ArchiveIO import ArchiveIO
        # # aio = ArchiveIO()
        # # zip_files = aio.top_files(target_folder="downloads", allowed_suffixes=[".zip"])
        # # aio.unzip_plugin(
        # #     zip_files=zip_files,
        # #     password=password,
        # #     target_folder=os.path.join(g_output_folder, g_cache_folder),
        # #     packaged=True
        # #     )

        # ## 02 遍历字典，检查指定目录下的所有文件的绝对路径，连同目标文件的绝对路径一同写回配置
        
        # ####

        # for _, json_dict_elv in json_dict.items():
        #     el_target_files = json_dict_elv["target_files"]
        #     el_temp_cache_folder = json_dict_elv["temp_cache_folder"]
        #     el_target_files_cache = json_dict_elv["target_files_cache"]
        #     # el_zip_file = json_dict_elv["zip_file"]

        #     # ### try003
        #     # tio.zlshell("7z1900-extra\\7za.exe x -o{temp_dir} {zip_file} -p{pwd} -aos".format(
        #     #     temp_dir=el_temp_cache_folder, zip_file=el_zip_file, pwd=password))

        #     # ##
        #     # diff_filenames = get_all_filenames(el_temp_cache_folder)
        #     # target_folder = output_folder
        #     # # import shutil
        #     # # import os
        #     # el_target_files = [os.path.join(target_folder, diff_filenames_el) for diff_filenames_el in diff_filenames]
        #     # print("--->el_target_files:{}".format(el_target_files))

        #     # ###
        #     # el_target_files_cache = [os.path.join(target_folder, el_temp_cache_folder, diff_filenames_el) for diff_filenames_el in diff_filenames]
        #     # print("--->el_target_files_cache:{}".format(el_target_files_cache))
        #     # ####

        #     # el_active = json_dict_elv["active"]
        #     el_type = json_dict_elv["type"]
        #     if el_type != "overwrite":
        #         for item_el_index in range(len(el_target_files_cache)):
        #             item_el_source = el_target_files_cache[item_el_index]
        #             item_el_target = el_target_files[item_el_index]
        #             ## 移动每一个缓存的文件
        #             if os.path.exists(item_el_source):
        #                 shutil.move(item_el_source, item_el_target)
        #         ## 移除临时缓存文件夹
        #         if os.path.exists(el_temp_cache_folder):
        #             shutil.rmtree(el_temp_cache_folder)
                

        # # target_files=json_dict[rets_el_C1Package]['target_files']
        # # target_files_cache=json_dict[rets_el_C1Package]['target_files_cache']
        # # active=json_dict[rets_el_C1Package]['active']

        # var_update_packages.set(g_button_update_packages_text)
        
        check_leaks()
        ## 刷新列表
        global treeview
        local_load(treeview)
        ## 仅更新状态指示
        thr_update_progress()
        
        # var_update_packages.set(g_button_update_packages_text)
        # var_update_progress.set(var_assets_grouping_prompt.get())

        ## 解除禁用
        button_query['state'] = tk.NORMAL
        # button_update_packages['state'] = tk.NORMAL
        button_toggle['state'] = tk.NORMAL
####

###
def get_cached_active(cached_file=""):
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    cached_active = {}
    try:
        json_dict=tio.get_json_dict(cached_file)
        for k,v in json_dict.items():
            if json_dict[k]["active"] is True:
                # cached_active[k]=True
                cached_active[k]=v["active"]
    except Exception as ex:
        print("**{}".format(ex))
    return cached_active

def set_cached_active(cached_file="", cached_active = {}):
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    json_dict=tio.get_json_dict(cached_file)
    for k,v in cached_active.items():
        json_dict[k]["active"] = v
        # cached_file[k]["active"] = True
    tio.set_json_dict(cached_file, json_dict)
####
def remove_all_cols_items(comp):
    x=comp.get_children()
    for item in x:
        comp.delete(item)

def preprocessing(cols_items=[]):
    global full_fields
    global filtered_fields
    stacked_items = {}

    # cols_items = verified_items[:]
    filtered_items = []
    for _, cols_items_el in enumerate(cols_items):
        # full_fields = ['sha1_b64','packaged','update_mode','BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01','No_']
        # filtered_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']
        cols_dict = dict(zip(full_fields, cols_items_el))
        # comp.insert('', i, values=cols_items_el)
        # print(cols_dict)
        filtered_columns = []
        for filtered_fields_el in filtered_fields:
            filtered_columns.append(cols_dict[filtered_fields_el])
        ##
        filtered_items.append(filtered_columns)

        ## Stacked items
        el_CrisisBIOS = cols_dict['CrisisBIOS'].split(g_text_field_delimiter)[0]
        if el_CrisisBIOS not in stacked_items:
            stacked_items[el_CrisisBIOS]=[cols_dict['C1Package']]
        else:
            stacked_items[el_CrisisBIOS].append(cols_dict['C1Package'])
    
    return filtered_items, stacked_items

def open_nodes(nodes):
    global treeview
    for node in nodes.values():
        treeview.item(node, open=True)

def filter_all_cols_items(comp, keywords="", verified_items=[], continued=False):
    global g_output_folder
    # global treeview
    global button_query
    global full_fields
    global g_data_search_fields
    global filtered_fields
    global stacked_items
    # global var_query
    global g_button_query_text
    ##
    global g_cache_folder
    global g_cached
    # global g_output_folder
    # global filtered_fields
    global g_data_theme_bg_group
    global g_data_theme_bg_slave
    global g_data_theme_bg_active
    global g_data_theme_bg_parent
    global g_data_theme_bg_child
    global g_data_theme_bg_normal
    
    global g_data_theme_fg_group
    global g_data_theme_fg_slave
    global g_data_theme_fg_active
    global g_data_theme_fg_parent
    global g_data_theme_fg_child
    global g_data_theme_fg_normal

    global g_data_treeview_load_status_available
    global g_data_treeview_load_status_overwrite
    global g_text_field_delimiter
    global g_verified
    import os
    import shutil
    from TextfileIO import TextfileIO
    ##
    tio = TextfileIO()
    ###

    ##
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    if len(verified_items)==0:
        ###
        verified_items = tio.read(os.path.join(g_output_folder, g_verified))
        ##
        global g_verified_items_original
        global var_assets_grouping_prompt
        g_verified_items_original = verified_items[:]
        var_assets_grouping_prompt.set("{local_assets_grouping_prompt}{local_assets}{cloud_assets_grouping_prompt}{cloud_assets}".format(
        local_assets_grouping_prompt=g_label_local_assets_grouping_prompt,local_assets=len(g_verified_items_original),
        # cloud_assets_grouping_prompt=g_label_cloud_assets_grouping_prompt,cloud_assets="0/0")
        cloud_assets_grouping_prompt=g_label_cloud_assets_grouping_prompt,cloud_assets="0")
        )
    # if keywords!="":
    #     verified_items = [verified_items_el for verified_items_el in verified_items 
    #         if keywords in "{}".format(verified_items_el).lower()]
    #     # print("verified_items: {}".format(verified_items))

    # verified_items = [verified_items_el.split(";")[::-1] for verified_items_el in verified_items]
    verified_items = [verified_items_el.split(";")[:] for verified_items_el in verified_items]
    ## Stacked items
    stacked_items = {}
    _, stacked_items = preprocessing(cols_items=verified_items[:])
    if keywords!="":
        verified_items_new = []
        for verified_items_el in verified_items:
            verified_items_el_dict = dict(zip(full_fields, verified_items_el))
            # print("-##-->{}".format(verified_items_el_dict))
            search_fields = []
            for g_data_search_fields_el in g_data_search_fields:
                if g_data_search_fields_el in verified_items_el_dict:
                    search_fields.append(verified_items_el_dict[g_data_search_fields_el])
            if keywords.lower() in ";".join(search_fields).lower():
                verified_items_new.append(verified_items_el)
        verified_items = verified_items_new[:]
        # verified_items = [verified_items_el for verified_items_el in verified_items 
        #     if keywords.lower() in ";".join(verified_items_el).lower()]
    filtered_items, _ = preprocessing(cols_items=verified_items[:])
    ###
    if not continued:
        remove_all_cols_items(comp)
    # button_query.configure(text="Query({})".format(len(verified_items)))
    global var_query
    var_query.set("{}({})".format(g_button_query_text, len(verified_items)))
    
    # cols_items = verified_items[:]
    # filtered_items, stacked_items = preprocessing(cols_items=verified_items[:])
    # print("stacked_items: {}".format(stacked_items))

    ## 01
    import copy
    stacked_items_tmp = {}
    stacked_items_new = copy.deepcopy(stacked_items)
    for k, v in stacked_items_new.items():
        k_new = k.lower()
        if k_new in stacked_items_tmp:
            stacked_items_tmp[k_new]=stacked_items_tmp[k_new]+v
        else:
            stacked_items_tmp[k_new]=v
    stacked_items = copy.deepcopy(stacked_items_tmp)
    ##
    target_folder = g_output_folder
    target_cached_file = os.path.join(target_folder, g_cache_folder, g_cached)
    json_dict = tio.get_json_dict(target_cached_file)
    ###

    group_nodes = {}
    all_group_position = {}
    # group_nodes_el_count = 0

    group_position_default = "end"
    group_position = group_position_default
    for filtered_items_el_index in range(len(filtered_items)):
        filtered_items_el = filtered_items[filtered_items_el_index]
        filtered_columns = filtered_items_el[:]
        # full_fields = ['sha1_b64','packaged','update_mode','BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01','No_']
        # filtered_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']

        cols_dict = dict(zip(filtered_fields, filtered_columns))
        rets_el_C1Package=cols_dict['C1Package']
        rets_el_Arg01=cols_dict['Arg01']
        rets_el_C1Package=get_el_C1Package_sha1(el_C1Package=rets_el_C1Package)
        active_el = None
        if rets_el_C1Package in json_dict:
            active_el=json_dict[rets_el_C1Package]
            # print("-active_el-->{}".format(active_el))
                
        item_deep = len(cols_dict['PN'].split(g_text_field_delimiter))
        group_node=''
        alternative_text = cols_dict['CrisisBIOS'].split(g_text_field_delimiter)[0]
        alternative_text_tips = alternative_text

        ## 02
        alternative_text=alternative_text.lower()

        ## 直接加载条目
        # comp.insert('', 'end', text=alternative_text_tips, values=filtered_columns, tags=('parent',))
        ## 展开条目包含所有子项
        # tags_active = 'slave' if not active_el or not active_el['active'] else 'active'
        ####
        ############################################
        if not active_el:
            tags_active = 'normal'
        elif active_el['active']:
                tags_active = 'active'
        else:
            tags_active = 'slave'

        # print("-->stacked_items\n{}\n<---".format(stacked_items))
        # print("-->{} --- {}".format(alternative_text, g_data_treeview_load_status_overwrite in rets_el_Arg01))
        # if len(stacked_items[alternative_text])>1 or g_data_treeview_load_status_overwrite in rets_el_Arg01:
        if len(stacked_items_tmp[alternative_text])>1 or g_data_treeview_load_status_overwrite in rets_el_Arg01:
            if alternative_text not in group_nodes:
                group_node=comp.insert('', '0', text="{} {}".format(g_data_treeview_group_prefix, alternative_text_tips), values=[""]*len(filtered_columns), tags=('group',))
                group_nodes[alternative_text]=group_node
                group_position=comp.index(group_node)
            else:
                group_node=group_nodes[alternative_text]
                group_position=comp.index(group_node)
            
            # ##
            # if alternative_text not in group_nodes:
            #     group_nodes[alternative_text]=group_nodes_el_count
            # else:
            #     group_position=group_nodes[alternative_text]
            ##
            all_group_position[alternative_text] = group_position
        ## 仅有一个文件
        else:
            group_position = group_position_default
        
        ## 合并条目的处理
        if g_data_treeview_display_node_column is True:
            group_node = ""
            if group_position != "end":
                group_position = group_position + 1
            parent_node=comp.insert(group_node, group_position, text="{} {}".format(g_data_treeview_parent_prefix, alternative_text_tips), values=[""]*len(filtered_columns), tags=('parent',))
        
        parent_node = ""
        for item_deep_index in range(item_deep):
            filtered_columns_item = [filtered_columns_el.split(g_text_field_delimiter)[item_deep_index] for filtered_columns_el in filtered_columns]
            filtered_columns_item_dict = dict(zip(filtered_fields, filtered_columns_item))

            if group_position != "end":
                group_position = group_position + 1
            comp.insert(parent_node, group_position, text='{} --> {}'.format(alternative_text_tips, filtered_columns_item_dict["MT"]), values=filtered_columns_item, tags=('child' if g_data_treeview_load_status_available in rets_el_Arg01 else tags_active,))
            
            # ##
            # if alternative_text in group_nodes:
            #     group_nodes[alternative_text]=group_nodes_el_count

        ####
        ############################################


    # comp.tag_configure('parent', background='#e91e63', foreground="white")
    comp.tag_configure('group', background=g_data_theme_bg_group, foreground=g_data_theme_fg_group)
    comp.tag_configure('slave', background=g_data_theme_bg_slave, foreground=g_data_theme_fg_slave)
    comp.tag_configure('active', background=g_data_theme_bg_active, foreground=g_data_theme_fg_active)
    comp.tag_configure('parent', background=g_data_theme_bg_parent, foreground=g_data_theme_fg_parent)
    comp.tag_configure('child', background=g_data_theme_bg_child, foreground=g_data_theme_fg_child)
    comp.tag_configure('normal', background=g_data_theme_bg_normal, foreground=g_data_theme_fg_normal)
    comp.tag_configure('selected', background=g_data_theme_bg_selected, foreground=g_data_theme_fg_selected)
    # comp.tag_configure('normal', background='blue', font=("Century Gothic", '10', 'bold'), foreground="white")
    print("--> Data refresh is called")
    modify_treeview_state()
    # open_nodes(group_nodes)
    print("-->all_group_position\n{}\n<---".format(all_group_position))

def button_query_OnClicked():
    global treeview
    keywords=entry_search.get()
    print("{}".format(keywords))
    remove_all_cols_items(treeview)
    filter_all_cols_items(treeview, keywords=keywords, verified_items=verified_items)
    # entry_search.delete(0, 'end')

def thr_copyfile(src="",dst=""):
    import os
    import shutil
    create_backup_directories(backup_directories=[os.path.dirname(src)])
    shutil.copyfile(src, dst)
    print("--->复制文件完成")

def onClicked_button_toggle():
    print("--> onClicked_button_toggle")
    global treeview
    global g_cached
    global stacked_items
    ##
    global g_cache_folder
    global g_cached
    global g_output_folder
    global filtered_fields
    global g_text_field_delimiter
    import os
    import shutil
    from TextfileIO import TextfileIO
    ##
    tio = TextfileIO()
    ###

    # ## 01
    # import copy
    # stacked_items_tmp = {}
    # stacked_items_new = copy.deepcopy(stacked_items)
    # for k, v in stacked_items_new.items():
    #     k_new = k.lower()
    #     if k_new in stacked_items_tmp:
    #         stacked_items_tmp[k_new]=stacked_items_tmp[k_new]+v
    #     else:
    #         stacked_items_tmp[k_new]=v
    # ##

    for item in treeview.selection():
        item_text = treeview.item(item,"text")
        item_values = treeview.item(item,"values")
        
        print("-Toggle- {} -Toggle- {}".format(item_text, item_values[0]))
        ##
        # full_fields = ['sha1_b64','packaged','update_mode','BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01','No_']
        # filtered_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']
        item_values_dict = dict(zip(filtered_fields, item_values))
        rets_el_C1Package = item_values_dict['C1Package']
        rets_el_CrisisBIOS = item_values_dict['CrisisBIOS']
        if rets_el_C1Package == "":
            continue
        print("-rets_el_C1Package-->\n{}\n<---".format(rets_el_C1Package))
        rets_el_C1Package=get_el_C1Package_sha1(el_C1Package=rets_el_C1Package)

        ###
        # available_packages = stacked_items[item_text.split(g_text_field_delimiter)[0]]
        # print("--->\n{}\n<---".format(stacked_items))
        # print("--->\n{}\n<---".format(rets_el_CrisisBIOS.split(g_text_field_delimiter)[0]))
        
        ## 03组
        # available_packages = stacked_items[rets_el_CrisisBIOS.split(g_text_field_delimiter)[0]]
        available_packages = stacked_items[rets_el_CrisisBIOS.split(g_text_field_delimiter)[0].lower()]
        print("available_packages: {}".format(available_packages))
        if len(available_packages)>0:
            target_folder = g_output_folder
            target_cached_file = os.path.join(target_folder, g_cache_folder, g_cached)
            print("修改文件:{}".format(target_cached_file))
            
            json_dict = tio.get_json_dict(target_cached_file)
            target_files=json_dict[rets_el_C1Package]['target_files']
            target_files_cache=json_dict[rets_el_C1Package]['target_files_cache']
            active=json_dict[rets_el_C1Package]['active']

            ###
            import time
            time_start=time.time()
            print("修改，刷新前")
            ################################################################

            if active is True:
                ## <删除> 列表中的所有文件
                for target_files_el_index in range(len(target_files)):
                    target_files_el=target_files[target_files_el_index]
                    if os.path.exists(target_files_el):
                        os.remove(target_files_el)
                    # create_backup_directories(backup_directories=[os.path.dirname(target_files_el)])
                    # shutil.copyfile(diff_filenames_src[target_files_el_index], target_files_el)
                    # pass
                ## 设置状态为 <未启用>
                json_dict[rets_el_C1Package]['active'] = False
                pass
                ################################################################
                print("修改，刷新后1")
                time_end=time.time()
                print('totally cost',time_end-time_start)
                time_start=time_end
            else:
                ## <拷贝>列表中的所有文件
                for target_files_el_index in range(len(target_files_cache)):
                    target_files_el=target_files_cache[target_files_el_index]
                    print("target_files_el: --> {}".format(target_files_el))
                    # if os.path.exists(target_files_el):
                    #     os.remove(target_files_el)
                    # create_backup_directories(backup_directories=[os.path.dirname(target_files_el)])
                    # shutil.copyfile(target_files_el, target_files[target_files_el_index])
                    ## 启动线程下载文件
                    import threading
                    threading.Thread(target=thr_copyfile, 
                        kwargs=dict(src=target_files_el
                        , dst=target_files[target_files_el_index]
                        )).start()
                    # pass
                ## 设置状态为 <启用>
                json_dict[rets_el_C1Package]['active'] = True
                pass
                ################################################################
                print("修改，刷新后2")
                time_end=time.time()
                print('totally cost',time_end-time_start)
                time_start=time_end
            ### 处理其它的包，不能被同时选中
            for available_packages_el in available_packages:
                available_packages_el=get_el_C1Package_sha1(el_C1Package=available_packages_el)
                if available_packages_el!=rets_el_C1Package:
                    json_dict[available_packages_el]['active'] = False

            tio.set_json_dict(target_cached_file,json_dict)
            ################################################################
            print("修改，刷新后3")
            time_end=time.time()
            print('totally cost',time_end-time_start)

    print("stacked_items: {}".format(len(stacked_items)))
    
    ###
    button_query_OnClicked()
    
    

# relief must be flat, groove, raised, ridge, solid, or sunken
button_toggle=tk.Button(frameVC, font=("Arial", g_frame_button_font_size), width=16, textvariable=var_toggle, text="Toggle", relief="groove", fg=g_frame_theme_hlbg_control_btn_minimized, command=onClicked_button_toggle)
button_toggle.pack(side='right', pady=2, padx=2)


button_update_packages=tk.Button(frameVC, font=("Arial", g_frame_button_font_size), width=16, textvariable=var_update_packages, text="Update packages", relief="groove", fg=g_frame_theme_hlfg_button_mouse_up, activeforeground=g_frame_theme_hlfg_button_mouse_down)
# button_update_packages.pack(side='left', fill=tk.Y, pady=2, padx=2)
# button_update_packages.pack(side='left', pady=2, padx=2)
button_update_packages.pack(side='right', pady=2, padx=2)

# button_query=tk.Button(frameVC, font=("Arial", g_frame_button_font_size), width=16, textvariable=var_query, text="Search", relief="groove", fg=g_frame_theme_hlbg_control_btn_minimized, command=button_query_OnClicked)
button_query=tk.Button(frameVC, font=("Arial", g_frame_button_font_size), width=16, text=g_button_query_text, relief="groove", fg=g_frame_theme_hlbg_control_btn_minimized, command=button_query_OnClicked)
button_query.pack(side='right', pady=2, padx=2)

# label_query = tk.Label(frameVC, relief="flat", textvariable=var_assets_grouping_prompt, 
#     text="{local_assets_grouping_prompt}{local_assets}{cloud_assets_grouping_prompt}{cloud_assets}".format(
#     local_assets_grouping_prompt=g_label_local_assets_grouping_prompt,local_assets=12,
#     cloud_assets_grouping_prompt=g_label_cloud_assets_grouping_prompt,cloud_assets=200))
# label_query.pack(side='left', fill=tk.Y, pady=2, padx=2)

entry_search=tk.Entry(frameVC, relief="solid", show=None, width=35, bg=None,
    selectbackground ="#000000",selectforeground="#00bcd4",font = ('Helvetica', '12', 'normal'))
entry_search.pack(side='left', fill=tk.BOTH, expand=1, pady=2, padx=2)

def onKeyReturn(event=None):
    # print("--> You pressed enter")
    button_query_OnClicked()

entry_search.bind('<Return>', onKeyReturn)


# button_add=tk.Button(frameVC, text="Add", relief="groove", fg=zl_theme_bg)
# button_add.pack(side='right')

close = tk.Label(root, font=("Arial", g_frame_caption_control_btn_font_size), bg=g_frame_theme_bg_title_bar, fg=g_frame_caption_control_btn_fg , anchor=tk.CENTER, text="X", cursor="hand2")
close.place(x=(g_frame_width-40-g_frame_border_thickness), y=0+g_frame_border_thickness, width=40, height=g_frame_caption_thickness-g_frame_border_thickness*2)

min = tk.Label(root, font=("Arial", g_frame_caption_control_btn_font_size), bg=g_frame_theme_bg_title_bar, fg=g_frame_caption_control_btn_fg , anchor=tk.CENTER, text="_", cursor="hand2")
min.place(x=(g_frame_width-40-g_frame_border_thickness)-40, y=0+g_frame_border_thickness, width=40, height=g_frame_caption_thickness-g_frame_border_thickness*2)

caption = tk.Label(root, font=("Arial", g_frame_caption_font_size), bg=g_frame_theme_bg_title_bar, fg=g_frame_caption_fg , anchor=tk.W, text=root.title(), cursor="hand2")
caption.place(x=zl_gap, y=0+g_frame_border_thickness, width=(g_frame_width-40-g_frame_border_thickness)-40-(zl_gap), height=g_frame_caption_thickness-g_frame_border_thickness*2)
caption.pack_propagate(False)


min.bind("<Enter>", hoverMin)
min.bind("<Leave>", unHoverMin)
min.bind("<Button-1>", minimize)
close.bind("<Enter>", hover)
close.bind("<Leave>", unhover)
close.bind("<Button-1>", exitProgram)

borderFrame.bind("<Button-1>", startMove)
borderFrame.bind("<ButtonRelease-1>", stopMove)
borderFrame.bind("<B1-Motion>", moving)
borderFrame.bind("<Map>", frame_mapped)

caption.bind("<Button-1>", startMove)
caption.bind("<ButtonRelease-1>", stopMove)
caption.bind("<B1-Motion>", moving)
caption.bind("<Map>", frame_mapped)


  
# label text for title 
# fat32_items_type=ttk.Label(frameVT, text = "FAT32", 
#           background = None, foreground ="#aabbcc", font = ("Times New Roman", 45)) 
# fat32_items_type.pack(side='left')

frameDiskInfo = tk.Frame(frameVT, width=0, height=g_frame_theme_disk_info_height, bg=None, bd=0)
frameDiskInfo.pack(side='left')

# fat32_items_label=ttk.Label(frameVT, text = "Please choose a fat32 u disk:", 
#           font = ("Times New Roman", 10))
# fat32_items_label.pack(side='top', anchor='nw', padx = 10) 

def combobox_modified(event):
    # global treeview
    # remove_all_cols_items(treeview)
    # filter_all_cols_items(treeview, keywords="", verified_items=[])
    print("{}chkChanged".format("--"*32))
    spliced_disk()

def spliced_disk():
    global fat32_items
    global g_output_folder
    global g_subpath
    import os
    print("fat32_items.get() --> {}".format(fat32_items.get()))
    print("gletter(fat32_items.get()) --> {}".format(gletter(fat32_items.get())))
    # lasted_output_folder=g_output_folder
    g_output_folder = os.path.join(gletter(fat32_items.get()), g_subpath)
    # g_output_folder=removable_disk_selected.get()
    print("--> g_output_folder: {}".format(g_output_folder))
    print("Update to {}".format(gletter(fat32_items.get())))
    global var_volume_label
    # volume_label = get_volume_label(drive_letter=g_output_folder, default_volume_label="--")
    volume_label = get_volume_label(drive_letter=g_output_folder)
    var_volume_label.set(volume_label)
    ## 单击刷列表
    # all_removable_disks = list(g_full_volume_labels.keys())
    # ###
    # if lasted_output_folder!=g_output_folder or len(all_removable_disks)==1:
    print("<-- 已切换目录，正在刷新")
    global treeview
    remove_all_cols_items(treeview)
    ## 启动线程下载文件
    import threading
    threading.Thread(target=thr_visibilityChanged).start()

##
# relief must be flat, groove, raised, ridge, solid, or sunken
# label_volume_label=tk.Label(frameVT, font=("Arial", g_label_drive_letter_font_size), textvariable = var_volume_label, text="Refresh disks", relief="flat", anchor="w")
# label_volume_label.pack(side='top', fill=tk.X, pady=2, padx=2)

# Combobox creation 
fat32_items = ttk.Combobox(frameVT, width=18, textvariable = removable_disk_selected, font=("Arial", g_frame_button_font_size), state='readonly') 
fat32_items.bind('<<ComboboxSelected>>', combobox_modified)
fat32_items.pack(side='left', padx = 2)

##
def zlshell(command, print_msg=True):
    import os
    sh_rets = os.popen(command)
    lines = sh_rets.readlines()

    valid_lines = []
    for lines_el in lines:
        el = lines_el.strip()
        if el:
            valid_lines.append(el)
            if print_msg:
                print("-->{}--".format(el))
    return valid_lines

def gletter(volume_label_key):
    global g_full_volume_labels
    drive_letter=""
    if volume_label_key in g_full_volume_labels:
        drive_letter = g_full_volume_labels[volume_label_key]
    return drive_letter

def get_full_volume_labels():
    all_removable_disks=get_all_removable_disks()
    disks_dict = {}
    for all_removable_disks_el in all_removable_disks:
        # volume_label = get_volume_label(drive_letter=all_removable_disks_el, default_volume_label="--")
        volume_label = get_volume_label(drive_letter=all_removable_disks_el)
        volume_label_key = "{} ({})".format(volume_label,all_removable_disks_el)
        disks_dict[volume_label_key] = all_removable_disks_el
    return disks_dict

def get_volume_label(drive_letter="C:", default_volume_label="Removable Disk"):
    volume_label = zlshell("WMIC LOGICALDISK WHERE NAME='{drive_letter}' GET VOLUMENAME".format(drive_letter=drive_letter[:2]), print_msg=False)
    if len(volume_label)>1:
        volume_label = volume_label[1]
    else:
        volume_label = default_volume_label
    return volume_label

def get_all_removable_disks():
    all_removable_disks = []
    disks = zlshell("WMIC LOGICALDISK GET DEVICEID, DESCRIPTION", print_msg=False)
    for disks_el in disks:
        if ('Removable Disk' in disks_el) or ('可移动磁盘' in disks_el) :
            all_removable_disks.append(disks_el.strip()[-2:])
    
    all_removable_disks = ["{}\\".format(all_removable_disks_el[-2:]) for all_removable_disks_el in all_removable_disks]

    return all_removable_disks
###


def thr_update_progress():
    global label_update_progress
    global progress, items_count, item_index
    global removable_disk_selected
    global var_update_progress
    
    global g_verified_items_original
    global var_assets_grouping_prompt
    
    
    if progress=="100.00%":
        ## 显示 100.00% 时的提示
        global g_label_update_progress_tx_writing
        # var_update_progress.set("{progress} {item_index}/{items_count} {g_label_update_progress_tx_loading}".format(
        #         progress=g_label_update_progress_tx_writing, items_count=items_count, item_index=item_index, g_label_update_progress_tx_loading=g_label_update_progress_tx_loading))
        var_update_progress.set("{progress} {local_key}{local_value}{cloud_key}{item_index}/{items_count}".format(
                progress=progress
                , item_index=item_index
                , items_count=items_count
                # , g_label_update_progress_tx_loading=g_label_update_progress_tx_loading
                , local_key=g_label_local_assets_grouping_prompt
                , local_value=len(g_verified_items_original)+item_index
                , cloud_key=g_label_cloud_assets_grouping_prompt
                # , cloud_value="{items_count}".format(items_count=items_count)
                )
            )
    else:
        ## 显示 00.00%-99.99% 时的提示
        # if progress!="--":
        #     var_update_progress.set("{progress} {item_index}/{items_count} {g_label_update_progress_tx_loading}".format(
        #             progress=progress, items_count=items_count, item_index=item_index, g_label_update_progress_tx_loading=g_label_update_progress_tx_loading))
        if progress!="--":
            var_update_progress.set("{progress} {local_key}{local_value}{cloud_key}{item_index}/{items_count}".format(
                    progress=progress
                    , item_index=item_index
                    , items_count=items_count
                    # , g_label_update_progress_tx_loading=g_label_update_progress_tx_loading
                    , local_key=g_label_local_assets_grouping_prompt
                    , local_value=len(g_verified_items_original)+item_index
                    , cloud_key=g_label_cloud_assets_grouping_prompt
                    # , cloud_value="{items_count}".format(items_count=items_count)
                    )
                )

        # if item_index == 0 and items_count == 0:
        #     var_update_progress.set(var_assets_grouping_prompt.get())
    
    
    ## 显示另一种提示 local 32; cloud 15
    # if progress=="--":
    #     var_update_progress.set("{local_assets_grouping_prompt}{local_assets}{cloud_assets_grouping_prompt}{cloud_assets}".format(
    #     local_assets_grouping_prompt=g_label_local_assets_grouping_prompt,local_assets=len(g_verified_items_original)+item_index,
    #     cloud_assets_grouping_prompt=g_label_cloud_assets_grouping_prompt,cloud_assets="{items_count}".format(items_count=items_count)
    #     ))
    if progress=="--":
        var_update_progress.set("{progress} {local_key}{local_value}{cloud_key}{item_index}/{items_count}".format(
                progress=""
                , item_index=item_index
                , items_count=items_count
                # , g_label_update_progress_tx_loading=g_label_update_progress_tx_loading
                , local_key=g_label_local_assets_grouping_prompt
                , local_value=len(g_verified_items_original)+item_index
                , cloud_key=g_label_cloud_assets_grouping_prompt
                # , cloud_value="{items_count}".format(items_count=items_count)
                )
            )
    

def button_update_packages_OnClicked(event):
    # print("button_update_packages_OnClicked")
    global updated_flag
    updated_flag = not updated_flag
    print("updated_flag: {}".format(updated_flag))
    global g_base_url, g_checklist, g_password, g_output_folder
    global fat32_items
    if gletter(fat32_items.get())=="":
        global var_update_progress
        global g_label_empty_drive_letter_prompt
        var_update_progress.set(g_label_empty_drive_letter_prompt)
        return

    global verified_items
    global stacked_items

    global var_update_packages, g_button_update_packages_text, g_button_terminate_download_text
    if var_update_packages.get()==g_button_update_packages_text:
        var_update_packages.set(g_button_terminate_download_text)
        ## 按钮显示 Stop
        verified_items = []
        stacked_items = {}
        
        ## 启动线程下载文件
        import threading
        thr_update_progress()
        threading.Thread(target=download_main, 
            kwargs=dict(base_url=g_base_url
            , checklist=g_checklist
            , password=g_password
            , output_folder=g_output_folder
            # , output_folder=os.path.join(g_output_folder, g_subpath)
            )).start()
        # download_main(base_url=base_url, 
        #     checklist=checklist, password=password, output_folder=output_folder)
        filter_all_cols_items(treeview, keywords="", verified_items=[])
    else:
        var_update_packages.set(g_button_update_packages_text)
        ## 按钮显示 Update


button_update_packages.bind("<Button-1>", button_update_packages_OnClicked)

##
label_update_progress_hori_gap=ttk.Label(frameVT, text = "", 
          background = None, foreground = None, font = ("Times New Roman", g_label_update_progress_font_size)) 
label_update_progress_hori_gap.pack(side='right', padx=g_label_update_progress_hori_gap)
###
label_update_progress=ttk.Label(frameVT, textvariable=var_update_progress, text = "", 
          background = None, foreground =g_label_update_progress_fg, font = ("Times New Roman", g_label_update_progress_font_size)) 
label_update_progress.pack(side='right')


# filtered_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']
# filtered_fields = ['BIOSID','C1Package','PN','MT','CrisisBIOS','Arg01']
# columns=("BHChecksum", "C1Package", "UpdateMode", "PN", "MT")[::-1]

# treeview=ttk.Treeview(frameVB, height=18, show="headings", columns=columns)
# treeview=ttk.Treeview(frameVB, height=18, show="tree", columns=columns)
# treeview=ttk.Treeview(frameVB, height=18, show="tree headings", columns=show_fields)
treeview=ttk.Treeview(frameVB, height=18, show="tree headings" if g_data_treeview_display_node_column is True else "headings", columns=show_fields)

def modify_treeview_state():
    global treeview
    global g_data_treeview_load_status_available
    global g_data_treeview_load_status_loaded
    global g_data_treeview_load_status_overwrite
    global g_data_treeview_load_status_original
    global g_data_show_fields

    items = treeview.get_children()
    for items_el in items:

        tags = treeview.item(items_el, "tags")
        values = treeview.item(items_el, "values")
        items_el_dict = dict(zip(g_data_show_fields, values))
        items_el_Arg01 = items_el_dict["Arg01"]
        # print("tags1: {}".format(tags))
        # print("values1: {}".format(values[-1]))
        if g_data_treeview_load_status_overwrite in items_el_Arg01:
            values=list(values)
            values[-1]=g_data_treeview_load_status_available
            if "active" in tags:
                values[-1]=g_data_treeview_load_status_loaded
            treeview.item(items_el, values=values)
        elif g_data_treeview_load_status_original in items_el_Arg01:
            values=list(values)
            values[-1]=g_data_treeview_load_status_loaded
            treeview.item(items_el, values=values)

def onDoubleClicked_treeview(event):
    print("--> onDoubleClicked_treeview")
    global treeview
    item = treeview.identify('item', event.x, event.y)
    print("you clicked on", treeview.item(item, "text"))
    print("you clicked on", treeview.item(item, "tags"))

def onClicked_treeview(event):
    # print("--> onClicked_treeview")
    # global treeview
    global button_toggle
    global g_data_treeview_load_status_available

    for item in treeview.selection():
        item_text = treeview.item(item,"text")
        item_values = treeview.item(item,"values")
        item_tags = treeview.item(item, "tags")
        item_index = treeview.index(item)
        print("<-- {} -text-> {} -Arg01-> {} -tags-> {} -C1Package-> {}".format(item_index, item_text, item_values[-1:], item_tags, item_values[:1]))

        if g_data_treeview_load_status_available in item_values[-1:]:
            button_toggle.config(state=tk.NORMAL)
        else:
            button_toggle.config(state=tk.DISABLED)
    pass
 
treeview.bind('<ButtonRelease-1>', onClicked_treeview)
treeview.bind("<Double-1>", onDoubleClicked_treeview)

treeview.heading('#0', text=g_data_grouping_column_alias, anchor=g_data_grouping_heading_align)
treeview.column('#0', width=g_data_grouping_column_width, anchor=g_data_grouping_column_align)

for show_fields_el_index in range(len(show_fields)):
    show_fields_el = show_fields[show_fields_el_index]
    treeview.heading(show_fields_el, text=g_data_show_fields_alias[show_fields_el_index], anchor=g_data_show_heading_align[show_fields_el_index])
    treeview.column(show_fields_el, width=show_fields_width[show_fields_el_index], anchor=g_data_show_fields_align[show_fields_el_index])

vsb = ttk.Scrollbar(frameVB, orient="vertical", command=treeview.yview)
vsb.pack(side='right', fill='y')
hsb = ttk.Scrollbar(frameVB, orient="horizontal", command=treeview.xview)
hsb.pack(side='bottom',fill='x')

treeview.configure(xscrollcommand=hsb.set)
treeview.configure(yscrollcommand=vsb.set)
treeview.pack(fill=tk.BOTH, expand=1)


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def local_load(comp):
    filter_all_cols_items(comp, keywords="", verified_items=[])
# ###
# local_load(treeview)

center(root)

def download_checklist():
    import os
    import shutil
    hash_target_file = os.path.join("downloads", g_checklist)
    bak=hash_target_file+".bak"
    ## 启动时下载一个校验文件
    from ArchiveIO import ArchiveIO
    aio = ArchiveIO()
    rets = aio.download(
        filename=g_checklist,
        url="{}{}".format(g_base_url, g_checklist),
        target_folder="downloads"
        )
    ###

    if rets==200:
        if os.path.exists(hash_target_file):
            print("下载后，从配置生成json，同时拷贝一次两个文件，并生成备份")
            ## 拷贝文件
            # shutil.copy(hash_target_file, target_checklist_file)
            ## 生成json配置
            ## 生成json
            import os
            import shutil
            from TextfileIO import TextfileIO
            tio = TextfileIO()
            from UtilitiesIO import UtilitiesIO
            uio = UtilitiesIO()
            # checklist="sample-sha256sum.txt"
            # hash_target_file=g_checklist
            hash_target_file=os.path.join("downloads", g_checklist)
            g_cached_file=os.path.join("downloads", g_cached)
            # old_entries=tio.read(os.path.join(output_folder, g_verified))
            new_entries=tio.read(hash_target_file)
            # global g_output_folder
            # global g_cache_folder
            # global g_text_field_delimiter
            # global g_cached
            # global g_data_full_fields
            uio.convert(entries=new_entries,
                g_cached=os.path.join("downloads", g_cached),
                g_output_folder=g_output_folder,
                g_cache_folder=g_cache_folder,
                g_text_field_delimiter=g_text_field_delimiter,
                g_data_full_fields=g_data_full_fields,
                downloads="downloads")
            ## 备份两个文件
            import os
            import shutil
            if not os.path.exists(os.path.join(g_output_folder, g_cache_folder)):
                os.makedirs(os.path.join(g_output_folder, g_cache_folder))
            shutil.copy(hash_target_file, os.path.join(g_output_folder, g_cache_folder, g_checklist))
            # shutil.copy(g_cached_file, os.path.join(g_output_folder, g_cache_folder, g_cached))
            my_cached_dict_file = os.path.join(g_output_folder, g_cache_folder, g_cached)
            # if not os.path.exists(my_cached_dict_file):
            #     shutil.copy(g_cached_file, my_cached_dict_file)
            old_cached_active=get_cached_active(cached_file=my_cached_dict_file)
            shutil.copy(g_cached_file, my_cached_dict_file)
            set_cached_active(cached_file=my_cached_dict_file, cached_active = old_cached_active)
            ##
            shutil.copy(hash_target_file, hash_target_file+".bak")
            if os.path.exists(g_cached_file):
                os.remove(g_cached_file)
            print("{}".format(hash_target_file+".bak"))
        #################################################
    else:
        print("文件不存在，尝试下载后的配置生成拷贝无法完成，下载异常")

def check_leaks():
    import os
    import shutil
    from ArchiveIO import ArchiveIO
    aio = ArchiveIO()
    print("--<{}>".format(g_output_folder))
    print("--<{}>".format(":" in g_output_folder))
    if ":" not in g_output_folder:
        print("## 未找到可移动磁盘，可以尝试刷新磁盘列表")
        return
    # file_checker()
    # def file_checker():
    #     pass
    ## 从缓存获取数据，检查缓存目录和目标目录，重新生成校验文件
    # old_entries=tio.read(os.path.join(output_folder, g_verified))
    # last_entries=tio.read(g_checklist)
    # json_dict=tio.get_json_dict(g_cached)
    # print("--->os.path.join(g_output_folder, g_checklist):{}".format(os.path.join(g_output_folder, g_cache_folder, g_checklist)))
    last_entries=tio.read(os.path.join(g_output_folder, g_cache_folder, g_checklist))
    json_dict=tio.get_json_dict(os.path.join(g_output_folder, g_cache_folder, g_cached))
    # "g_data_full_fields": ["sha1_b64","packaged","update_mode","BIOSID","C1Package","PN","MT","CrisisBIOS","Arg01","No_"],
    import os
    import shutil
    lst_C1_verified = []
    user_files = aio.top_files(target_folder=g_output_folder, allowed_suffixes=[])
    print("user_files(U-disk):{}".format(user_files))
    free_folders = []
    for last_entries_el in last_entries:
        # print("last_entries_el:{}".format(last_entries_el))
        last_entries_el_dict = dict(zip(g_data_full_fields, last_entries_el.split(";")))
        # print("last_entries_el_dict:{}".format(last_entries_el_dict))
        el_key_C1Package = last_entries_el_dict["C1Package"].split(g_text_field_delimiter)[0]
        # if el_key_C1Package not in json_dict:
        #     continue
        if el_key_C1Package not in json_dict:
            continue
        el_dict=json_dict[el_key_C1Package]
        target_files=el_dict["target_files"]
        temp_cache_folder=el_dict["temp_cache_folder"]
        target_files_cache=el_dict["target_files_cache"]
        target_files=el_dict["target_files"]
        el_active=el_dict["active"]
        el_type=el_dict["type"]
        # el_zip_file=el_dict["zip_file"]
        ##
        ######################################################################
        missed_cache_precheck = False
        # if not aio.some_has(src=target_files, dst=user_files):
        if not aio.any_has(src=target_files, dst=user_files) \
            and (el_type=="original" or (el_type=="overwrite" and el_active is True)):
            ## 缓存文件不存在或不完整，删除缓存目录并跳过
            ## 检查缓存是否完整
            for target_files_cache_el in target_files_cache:
                if not os.path.exists(target_files_cache_el):
                    missed_cache_precheck = True
                    break
            ## 缓存完整时要进行拷贝操作，并恢复标识
            if missed_cache_precheck:
                if os.path.exists(temp_cache_folder):
                    shutil.rmtree(temp_cache_folder)
                # print("--> 跳过")
                continue
        else:
            print("--> {} --> 检查".format(el_key_C1Package))
        ##
        ######################################################################
        # if el_key_C1Package!="0YCN26WW":
        # if el_key_C1Package!="0KCN36WW":
        # if el_key_C1Package!="0TCN14WW":
        # if el_key_C1Package not in ["0YCN26WW", "2QCN20WW", "2TCN37WW", "2UCN10WW"]:
        #     continue
        
        missed = False
        missed_cache = False
        for target_files_el in target_files:
            if not os.path.exists(target_files_el):
                ## 只要有一个文件缺失，就设置标识，并不退出循环不再检查
                missed = True
                break
        if el_type=="overwrite":
            missed = True
        ## 文件缺失时
        if missed:
            ## 检查缓存是否完整
            for target_files_cache_el in target_files_cache:
                if not os.path.exists(target_files_cache_el):
                    missed_cache = True
                    break
            ## 缓存完整时要进行拷贝操作，并恢复标识
            if not missed_cache:
                ## 可以拷贝缓存
                ##
                # lst_C1_verified.append(last_entries_el)
                ###
                #######################################################
                if el_type=="original" or (el_type=="overwrite" and el_active is True):
                    for target_files_el_index in range(len(target_files)):
                        target_files_el_dst = target_files[target_files_el_index]
                        target_files_el_src = target_files_cache[target_files_el_index]
                        if el_type=="original":
                            shutil.move(target_files_el_src, target_files_el_dst)
                        elif el_type=="overwrite" and el_active is True:
                            shutil.copyfile(target_files_el_src, target_files_el_dst)

                    
                    if el_type=="original":
                        if os.path.exists(temp_cache_folder):
                            # shutil.rmtree(temp_cache_folder)
                            free_folders.append(temp_cache_folder)
                ####
                ## 修复完成，重置状态
                missed = False
                lst_C1_verified.append(last_entries_el)
            else:
                # ## 检查压缩包是否可用
                # if os.path.exists(el_zip_file):
                #     ## 压缩包存在，可以选解压再拷贝
                #     ## 先解压
                #     from ArchiveIO import ArchiveIO
                #     aio = ArchiveIO()
                #     aio.unzip_plugin(
                #         zip_files=[el_zip_file],
                #         password=g_password,
                #         target_folder=os.path.join(g_output_folder, g_cache_folder),
                #         packaged=True
                #         )
                #     ## 再拷贝
                #     ###
                #     #######################################################
                #     if el_type=="original" or (el_type=="overwrite" and el_active is True):
                #         for target_files_el_index in range(len(target_files)):
                #             target_files_el_dst = target_files[target_files_el_index]
                #             target_files_el_src = target_files_cache[target_files_el_index]
                #             shutil.copyfile(target_files_el_src, target_files_el_dst)
                #         pass
                #     ####
                #     ## 修复完成，重置状态
                #     missed = False
                #     missed_cache = False

                ## overwrite缓存不完整
                if el_type=="overwrite":
                        if os.path.exists(temp_cache_folder):
                            # shutil.rmtree(temp_cache_folder)
                            free_folders.append(temp_cache_folder)
                pass
        else:
            ## 文件未丢失或已补回，添加一条可用记录用于显示在列表中
            ## 当前记录追加到验证文件中
            ## last_entries_el -> C1_verified.txt
            ##
            ## 检查缓存是否完整
            missed_cache = False
            for target_files_cache_el in target_files_cache:
                if not os.path.exists(target_files_cache_el):
                    missed_cache = True
                    break
            ## 缓存完整时要进行拷贝操作，并恢复标识
            if not missed_cache:
                ## 可以拷贝缓存
                ##
                # lst_C1_verified.append(last_entries_el)
                ###
                #######################################################
                if el_type=="original":
                    for target_files_el_index in range(len(target_files)):
                        target_files_el_dst = target_files[target_files_el_index]
                        target_files_el_src = target_files_cache[target_files_el_index]
                        if el_type=="original":
                            shutil.move(target_files_el_src, target_files_el_dst)
                        # elif el_type=="overwrite" and el_active is True:
                        #     shutil.copyfile(target_files_el_src, target_files_el_dst)
                    
                    if el_type=="original":
                        if os.path.exists(temp_cache_folder):
                            # shutil.rmtree(temp_cache_folder)
                            free_folders.append(temp_cache_folder)

                    ####
            lst_C1_verified.append(last_entries_el)
            
            pass
    # print("lst_C1_verified:{}".format(lst_C1_verified))
    tio.write(os.path.join(g_output_folder, g_verified), lst_C1_verified)
    ## 删除所有空目录
    # print("暂停2秒")
    # import time
    # time.sleep(2)
    # print("开始删除空目录")
    for free_folders_el in free_folders:
        shutil.rmtree(free_folders_el)
    ## 设置需要更新的条目数量
    # from TextfileIO import TextfileIO
    # tio = TextfileIO()
    hash_target_file = os.path.join("downloads", g_checklist)
    old_entries=tio.read(os.path.join(g_output_folder, g_verified))
    print("<-- {}".format(os.path.join(g_output_folder, g_verified)))
    new_entries=tio.read(hash_target_file)
    # rets=tio.read(hash_target_file)
    rets=get_diff_entries(old_entries, new_entries)
    global items_count
    items_count=len(rets)
    print("###可以更新{}个包".format(items_count))

# download_checklist()

# check_leaks()
# # thr_update_progress()
# ###
# local_load(treeview)
# thr_update_progress()

# root.attributes('-topmost', True)

def thr_visibilityChanged():
    global var_update_progress
    global g_frame_start_checking
    var_update_progress.set(g_frame_start_checking)
    
    global tk
    global button_query
    global button_update_packages
    global button_toggle
    ## 禁用
    button_query['state'] = tk.DISABLED
    button_update_packages['state'] = tk.DISABLED
    button_toggle['state'] = tk.DISABLED

    download_checklist()

    check_leaks()
    # thr_update_progress()
    ###
    local_load(treeview)
    thr_update_progress()
    
    ## 解除禁用
    button_query['state'] = tk.NORMAL
    button_update_packages['state'] = tk.NORMAL
    button_toggle['state'] = tk.NORMAL

def visibilityChanged(event):
    print("界面出现")
    # your code here
    root.unbind('<Visibility>') # only call `callback` the first time `root` becomes visible
    print("解除绑定")
    ## 启动线程下载文件
    import threading
    threading.Thread(target=thr_visibilityChanged).start()


##
# relief must be flat, groove, raised, ridge, solid, or sunken
button_refresh_disks=tk.Button(frameVT, font=("Arial", g_frame_button_font_size), textvariable=var_refresh_disks, text="Refresh disks", relief="groove", fg=g_frame_theme_hlfg_button_mouse_up, activeforeground=g_frame_theme_hlfg_button_mouse_down)
# button_refresh_disks.pack(side='left', fill=tk.Y, pady=2, padx=2)
button_refresh_disks.pack(side='left', pady=2, padx=2)

# button_update_packages=tk.Button(frameVT, font=("Arial", g_frame_button_font_size), textvariable=var_update_packages, text="Update packages", relief="groove", fg=g_frame_theme_hlfg_button_mouse_up, activeforeground=g_frame_theme_hlfg_button_mouse_down)
# # button_update_packages.pack(side='left', fill=tk.Y, pady=2, padx=2)
# button_update_packages.pack(side='left', pady=2, padx=2)

def button_refresh_disks_OnClicked(event):
    print("button_refresh_disks_OnClicked")
    global all_removable_disks
    global fat32_items
    # all_removable_disks = get_all_removable_disks()
    global g_full_volume_labels
    g_full_volume_labels = get_full_volume_labels()
    all_removable_disks = list(g_full_volume_labels.keys())
    print("all_removable_disks:{}".format(all_removable_disks))
    fat32_items['values'] = all_removable_disks[:]
    if len(all_removable_disks)>0 and gletter(fat32_items.get())=="":
        if fat32_items.get() not in all_removable_disks:
            fat32_items.current(0)
    ##
    print("{}btnClicked".format("--"*32))
    spliced_disk()
    

button_refresh_disks.bind("<Button-1>", button_refresh_disks_OnClicked)

button_refresh_disks_OnClicked(None)

## 拷贝配置文件到缓存文件夹
#################################################
import shutil
hash_target_file = os.path.join("downloads", g_checklist)
# target_checklist_file = os.path.join(g_output_folder, g_cache_folder, g_checklist)
# target_cached_file = os.path.join(g_output_folder, g_cache_folder, g_cached)
bak=hash_target_file+".bak"
if os.path.exists(bak):
    print("从备份恢复")
    shutil.copy(bak, hash_target_file)
else:
    print("备份尚不存在")
if os.path.exists(hash_target_file):
    print("下载前，从配置生成json，同时拷贝一次两个文件，并生成备份")
    ## 拷贝文件
    # shutil.copy(hash_target_file, target_checklist_file)
    ## 生成json配置
    ## 生成json
    import os
    import shutil
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    from UtilitiesIO import UtilitiesIO
    uio = UtilitiesIO()
    # checklist="sample-sha256sum.txt"
    # hash_target_file=g_checklist
    hash_target_file=os.path.join("downloads", g_checklist)
    g_cached_file=os.path.join("downloads", g_cached)
    # old_entries=tio.read(os.path.join(output_folder, g_verified))
    new_entries=tio.read(hash_target_file)
    # global g_output_folder
    # global g_cache_folder
    # global g_text_field_delimiter
    # global g_cached
    # global g_data_full_fields
    uio.convert(entries=new_entries,
        g_cached=os.path.join("downloads", g_cached),
        g_output_folder=g_output_folder,
        g_cache_folder=g_cache_folder,
        g_text_field_delimiter=g_text_field_delimiter,
        g_data_full_fields=g_data_full_fields,
        downloads="downloads")
    ## 备份两个文件
    import os
    import shutil
    if not os.path.exists(os.path.join(g_output_folder, g_cache_folder)):
        os.makedirs(os.path.join(g_output_folder, g_cache_folder))
    shutil.copy(hash_target_file, os.path.join(g_output_folder, g_cache_folder, g_checklist))
    # shutil.copy(g_cached_file, os.path.join(g_output_folder, g_cache_folder, g_cached))
    my_cached_dict_file = os.path.join(g_output_folder, g_cache_folder, g_cached)
    # if not os.path.exists(my_cached_dict_file):
    #     shutil.copy(g_cached_file, my_cached_dict_file)
    old_cached_active=get_cached_active(cached_file=my_cached_dict_file)
    shutil.copy(g_cached_file, my_cached_dict_file)
    print("<-- 状态 -- {}".format(old_cached_active))
    set_cached_active(cached_file=my_cached_dict_file, cached_active = old_cached_active)
    ##
    shutil.copy(hash_target_file, hash_target_file+".bak")
    os.remove(g_cached_file)
else:
    print("文件不存在，下载前的配置生成拷贝无法完成")
#################################################


root.bind('<Visibility>', visibilityChanged) # call `callback` whenever `root` becomes visible
root.mainloop()