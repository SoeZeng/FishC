def FileWrite(FileName):
    f = open(FileName,'w')
    print("请输入内容，单独输入':w'保存退出：")
    while True:
        content = input()
        if content != ':w':
            f.write(content+'\n')
        else:
            break
    f.close()
    
FileName = input("请输入文件名：")
FileWrite(FileName)

    