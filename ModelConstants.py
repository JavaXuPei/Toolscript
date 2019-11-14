import os
import sys


def formatter(src: str, firstUpper: bool = True):
    """
    将下划线分隔的名字,转换为驼峰模式
    :param src:
    :param firstUpper: 转换后的首字母是否指定大写(如
    :return:
    """
    arr = src.split('_')
    res = ''
    for i in arr:
        res = res + i[0].upper() + i[1:]

    if not firstUpper:
        res = res[0].lower() + res[1:]
    return res


def formatterFalse(src: str, firstUpper: bool = False):
    """
    将下划线分隔的名字,转换为驼峰模式
    :param src:
    :param firstUpper: 转换后的首字母是否指定大写(如
    :return:
    """
    arr = src.split('_')
    res = ''
    for i in arr:
        res = res + i[0].upper() + i[1:]

    if not firstUpper:
        res = res[0].lower() + res[1:]
    return res


print(r"正在生成", sys.argv[1])
# urls = "C:\\Users\\bjy\\Desktop\\a.txt"
urls = sys.argv[1]
file = open(urls, 'r', encoding='UTF-8')
content = file.read().split("\n")
message = []
index = 0
one = ""
pwd = os.getcwd()
# 读取前5行的注释 保存到数组
annotation = [content[0], content[1], content[2], content[3], content[4], content[5]]
del content[0:6]
for val in content:
    print(val)
# 表名位第7行
titleName = content[0]
# 创建目录
os.mkdir(titleName.replace("_", ""))
# 文件读取
for val in content:
    if index == 1:
        one = val
        msg = "public static final String %s_TABLE_NAME = \"%s\"" % (val.upper(), val) + ";"
        message.append(msg)
        index = index + 1
    else:
        msg = "public static final String %s_%s_PROPERTY= \"%s\"" % (one.upper(), val.upper(), val) + ";"
        message.append(msg)
        index = index + 1
file.close()

# 文件写入
fout = open(pwd + os.sep + titleName.replace("_", "") + os.sep + "数据plus.txt", 'w', encoding='utf8')
for i in message:
    fout.write(i + "\n")

fout.write("\n")
# for val in content:
fout.write("public " + formatter(titleName) + "Entity" + "(" + formatter(titleName) + " " + formatterFalse(
    titleName) + ")" + "{" + "\n")
fout.write("\t" + "super(" + formatterFalse(titleName) + ");" + "\n")
for val in content:
    fout.write("\t" + "this." + formatterFalse(val) + " = " + formatterFalse(titleName) + ".get" + formatter(
        val) + "();" + "\n")
fout.write("}")
fout.write("\n")

fout.write("\t" + "@Override" + "\n")
fout.write("\t" + "public " + formatter(titleName) + " " + "toData() {" + "\n")
fout.write("\t\t" + formatter(titleName) + " " + formatterFalse(titleName) + " = " + "new " + formatter(
    titleName) + "();" + "\n")
fout.write("\t\t" + "super.toData(" + formatterFalse(titleName) + ");" + "\n")
for val in content:
    fout.write("\t\t" + formatterFalse(titleName) + ".set" + formatter(val) + "(" + formatterFalse(val) + ");" + "\n")
fout.write("\t\t" + "return " + formatter(val) + ";" + "\n")
fout.write("}" + "\n")
fout.close()

# JpaDao 文件
file = open(pwd + os.sep + "JpaUserDao", 'r')
JpaDao = file.read().split("\n")
h3 = JpaDao[2]
JpaDao[2] = h3.format(formatter(titleName))

h5 = JpaDao[5]
JpaDao[5] = h5.format(formatter(titleName),
                      formatter(titleName).replace(formatter(titleName)[0:1], formatter(titleName)[0:1].lower(), 1))

h7 = JpaDao[7]
JpaDao[7] = h7.format(formatter(titleName))

h9 = JpaDao[9]
JpaDao[9] = h9.format(formatter(titleName))

h12 = JpaDao[12]
JpaDao[12] = h12.format(formatter(titleName))

h14 = JpaDao[14]
JpaDao[14] = h14.format(formatter(titleName),
                        formatter(titleName).replace(formatter(titleName)[0:1], formatter(titleName)[0:1].lower(),
                                                     1))

JpaDao_ = open(
    pwd + os.sep + titleName.replace("_", "") + os.sep + "Jpa" + formatter(titleName) + "Dao.java", 'w',
    encoding='utf8')
for i in annotation:
    JpaDao_.write(i + "\n")
for i in JpaDao:
    JpaDao_.write(i + "\n")
JpaDao_.close()

# Dao层
Daofile = open(pwd + os.sep + "UserDao", 'r')
Dao = Daofile.read().split("\n")
Daoh0 = Dao[0]
Dao[0] = Daoh0.format(formatter(titleName), formatter(titleName))
Dao_ = open(pwd + os.sep + titleName.replace("_", "") + os.sep + formatter(titleName) + "Dao.java", 'w',
            encoding='utf8')
for i in annotation:
    Dao_.write(i + "\n")
for i in Dao:
    Dao_.write(i + "\n")
Dao_.close()

# Repository层
Repositoryfile = open(pwd + os.sep + "UserRepository", 'r')
Repository = Repositoryfile.read().split("\n")
Repositoryh0 = Repository[1]
Repository[1] = Repositoryh0.format(formatter(titleName), formatter(titleName))
Repository_ = open(
    pwd + os.sep + titleName.replace("_", "") + os.sep + formatter(titleName) + "Repository.java", 'w',
    encoding='utf8')
for i in annotation:
    Repository_.write(i + "\n")
for i in Repository:
    Repository_.write(i + "\n")
Repository_.close()

# Service 层
Servicefile = open(pwd + os.sep + "UserService", 'r')
Service = Servicefile.read().split("\n")
Serviceh0 = Service[0]
Service[0] = Serviceh0.format(formatter(titleName))
Service_ = open(pwd + os.sep + titleName.replace("_", "") + os.sep + formatter(titleName) + "Service.java",
                'w', encoding='utf8')
for i in annotation:
    Service_.write(i + "\n")
for i in Service:
    Service_.write(i + "\n")
Service_.close()

# ServiceImpl 层
ServiceImplfile = open(pwd + os.sep + "UserServiceImpl", 'r')
ServiceImpl = ServiceImplfile.read().split("\n")
Serviceh0 = ServiceImpl[2]
ServiceImpl[2] = Serviceh0.format(formatter(titleName), formatter(titleName))
ServiceImpl_ = open(
    pwd + os.sep + titleName.replace("_", "") + os.sep + formatter(titleName) + "ServiceImpl.java", 'w',
    encoding='utf8')
for i in annotation:
    ServiceImpl_.write(i + "\n")
for i in ServiceImpl:
    ServiceImpl_.write(i + "\n")
ServiceImpl_.close()
print("成功!!!!")
