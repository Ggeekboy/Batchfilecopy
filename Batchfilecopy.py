import os, shutil

searchdir = 'G:/tl/官方补丁/Material/Icons/'
aimsdir = 'G:/tl/整理补丁/Material/'
filename = 'F:/python/file.txt'


# searchdir = input("请输入要查找的目录：")
# aimsdir = input("请输入目标目录：")
# filename= input("请输入要查找的文件列表(文件导入方式):")
def search_file(start_dir, target):
    os.chdir(start_dir)  # 切换到用户输入的路径

    for each_file in set(os.listdir(os.curdir)):  #遍历目录下的文件
        if each_file in target: #如果文件名等于被遍历的文件名则返回
            # print(os.getcwd()+each_file)
            result = os.getcwd() + "\\" + each_file
            return result
        if os.path.isdir(each_file):  #判断文件是不是目录，如果是则进行递归调用遍历
            search_file(each_file, target)
            os.chdir(os.pardir)


def copysearch_file(searchdir, aimsdir, filename):
    with open(filename) as file_obj:  #打开文件
        for file in file_obj: #遍历文件内容
            isfile = search_file(searchdir, file.strip()) #调用搜索文件函数
            if isfile: #如果遍历出来的文件存在，则进行下一步操作
                aimsfile = aimsdir + file
                aimsfile=aimsfile.strip()
                fileexists=os.path.exists(aimsfile) 
                if fileexists:#判断目标文件是否存在
                    print("文件存在不复制:{}".format(aimsfile))
                    continue
                print("开始复制文件{} 到 {}".format(isfile, aimsfile))
                shutil.copy(isfile,aimsdir)
            else:
                print("没有找到文件:{}".format(file))


copysearch_file(searchdir, aimsdir, filename)