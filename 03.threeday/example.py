# 思考题:
# ips = {'192.168.123.10': 34, '12.34.56.78': 12, '90.12.34.56': 19}
# 对上方的字典进行排序 -> 根据值进行排序;

# 从access_log中读取ip地址, 并统计每个ip访问的次数, 且提取出排名前十的IP地址;
with open(file="access_log", mode='r') as log:
    ips = {}
    for lines in log.readlines():
        if lines.split()[0] in ips.keys():
            ips[lines.split()[0]] += 1
        else:
            ips.setdefault(lines.split()[0], 1)
    print(ips)

# 请统计出网站的PV量及UV量; -> 就是在access_log中统计出接受过多少次访问?和有多少个不同的ip访问


# 练习题:
# 1. 如何获取到文件的行数? 请用代码表示

# 2. 请统计出threekingdom.txt中"刘备","曹操","关羽","郭嘉"各出现的次数

# 3. 请统计出threekingdom.txt中"青龙偃月刀","丈八蛇矛","雌雄双股剑","方天画戟"各出现的次数

# 4. 请统计出access_log中,(200, 404, 502, 504)状态码出现的次数;
