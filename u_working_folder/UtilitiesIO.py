class UtilitiesIO():
    def print_UtilitiesIO(self):
        print("--> {}".format("print_UtilitiesIO"))

    def dedup_split(self, files=[], files_delimiter="~>"):
        files_split=[]
        for files_el in files:
            files_split.extend(files_el.split(files_delimiter))
        files_dedup=[]
        for files_split_el in files_split:
            if files_split_el not in files_dedup:
                files_dedup.append(files_split_el)
        return files_dedup[:]

    def convert(self, entries=[],
        g_output_folder="F:\\aaa", g_cached="a.json", g_cache_folder=".C1_Store", g_text_field_delimiter="==",
        g_data_full_fields=["sha1_b64","packaged","update_mode","BIOSID","C1Package","PN","MT","CrisisBIOS","Arg01","No_"],
        downloads="downloads"):
        import os
        from TextfileIO import TextfileIO
        tio = TextfileIO()
        ##
        json_dict = {}
        for entries_el in entries:
            entries_el_dict = dict(zip(g_data_full_fields, entries_el.split(";")))
            el_Arg01 = entries_el_dict["Arg01"]
            el_CrisisBIOS = entries_el_dict["CrisisBIOS"]
            el_C1Package = entries_el_dict["C1Package"]
            el_C1Package = el_C1Package.split(g_text_field_delimiter)[0]
            ##
            target_files=el_CrisisBIOS.split(g_text_field_delimiter)
            target_files=self.dedup_split(files=target_files,files_delimiter="~>")
            target_files=[
                os.path.join(g_output_folder, target_files_el)
                for target_files_el in target_files]
            temp_cache_folder=os.path.join(g_output_folder, g_cache_folder, el_C1Package)

            target_files_cache=el_CrisisBIOS.split(g_text_field_delimiter)
            target_files_cache=self.dedup_split(files=target_files_cache,files_delimiter="~>")
            target_files_cache=[
                os.path.join(g_output_folder, g_cache_folder, el_C1Package, target_files_cache_el) 
                for target_files_cache_el in target_files_cache]
            temp_cache_folder=os.path.abspath(temp_cache_folder)

            json_dict[el_C1Package] = {
                'target_files': target_files,
                'temp_cache_folder': temp_cache_folder,
                'target_files_cache': target_files_cache,
                'active': False,
                'type': el_Arg01.split(g_text_field_delimiter)[0].lower().strip(),
                'zip_file': "{}.zip".format(os.path.abspath(os.path.join(downloads, el_C1Package))),
            }
            # print("-- {}".format(json_dict[el_C1Package]))
        tio.set_json_dict(g_cached, json_dict)

if __name__ == "__main__":
    uio = UtilitiesIO()
    entries=[
        "qWvlOEMbNThTmvBSWD52C2gnCvY=;0QCN30WW.zip;recommended;0QCN;0QCN30WW;Lenovo B50-50;80S2;0Q_Crisis.fd;original;10",
        "0N/WgcKWQ3m/F7iQgunakOoY13Y=;0RCN35WW.zip;recommended;0RCN;0RCN35WW;Lenovo B71-80;80RJ;0R_Crisis.bin;original;11",
        "M+Nw296eiUxyU/mPvFxtqGiFx0Q=;8YCN31WW.zip;recommended;8YCN==8YCN;8YCN31WW==8YCN31WW;Lenovo V130-14IKB==Lenovo WEI5-14IKB;81HQ==81ME;ELMV2_6L.bin~>ELMV2_8L.bin==ELMV2_6L.bin~>ELMV2_8L.bin;original==original;423==424",
    ]
    # g_output_folder="F:\\aaa"
    g_output_folder="E:\\aaa"
    g_cache_folder=".C1_Store"
    g_text_field_delimiter="=="
    g_cached="a.json"
    g_data_full_fields=["sha1_b64","packaged","update_mode","BIOSID","C1Package","PN","MT","CrisisBIOS","Arg01","No_"]
    downloads="downloads"

    ##
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    checklist="sha256sum.txt"
    hash_target_file=checklist
    # old_entries=tio.read(os.path.join(output_folder, g_verified))
    new_entries=tio.read(hash_target_file)
    new_entries=entries[-1:]

    uio.convert(entries=new_entries,
        g_cached="a.json",
        g_output_folder=g_output_folder,
        g_cache_folder=g_cache_folder,
        g_text_field_delimiter=g_text_field_delimiter,
        g_data_full_fields=g_data_full_fields,
        downloads="downloads")

    pass