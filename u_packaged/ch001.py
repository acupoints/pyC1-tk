if __name__ == "__main__":
    from TextfileIO import TextfileIO
    tio = TextfileIO()
    json_dict = tio.get_json_dict("local.conf.txt")
    password=json_dict['g_password']
    print("--> {}".format(password))
    d1 = {
        "hello": "world",
        "Yes": True,
        "test_count": 81,
    }
    tio.set_json_dict("aaa.txt", d1)
    d2 = [
        {
            "name": "a1",
            "count": 9,
            "status": False,
        },
        {
            "name": "a2",
            "count": 11,
            "status": True,
        }
    ]
    tio.set_json_dict("aaa.txt", d2)
    pass