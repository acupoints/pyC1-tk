
if __name__ == "__main__":
    import sys
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    files = sys.argv[1:]
    for files_el in files:
        sha1=tio.getSHA1(files_el)
        print("{};{}".format(sha1, files_el))
    pass