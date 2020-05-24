
def to_count():
    with open(file_name, encoding='utf-8') as f:
        data = f.read()
        print(data.split('。'))
    with open(key_path, encoding='utf-8') as f:
        key_list = f.readlines()
    with open(to_path + r'\to_' + file_name.split('\\')[-1], 'w+', encoding='utf-8') as fp:
        for key in key_list:
            key = key.strip()
            # print('%s %s' % (keyword, weight))
            fp.write('%s %s' % (key, data.count(key)))
            sen_num = len(data.split('。'))
            fp.write(' %d' % sen_num)
            percent=data.count(key)*10000/sen_num
            fp.write(' %d\n' % percent)
            words_num = len(data.split())
    print('over')


# 要读取的目标文件
file_name = r'D:\Pycharm\上海16年.txt'
# 要统计的关键词
key_path = r'D:\Pycharm\keywords.txt'
# 要输出的文件夹
to_path = r'D:\Pycharm'
to_count()

