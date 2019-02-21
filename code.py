
if __name__ == "__main__":

    import os
    import re

    # 打开txtNew.txt，提取文档内所有foerId，生成list
    txtNew = open('txtNew.txt', 'r')

    resultNew = re.findall('<a.*? data-user_id="(.*?)">', txtNew.read())
    if resultNew:
        print(resultNew)
    print(len(resultNew))

    txtNew.close()

    # 打开txtOld.txt，提取文档内所有foerId，生成list
    txtOld = open('txtOld.txt', 'r')

    resultOld = re.findall('<a.*? data-user_id="(.*?)">', txtOld.read())
    if resultOld:
        print(resultOld)
    print(len(resultOld))

    txtOld.close()

    # 比较txtNew和txtOld两个list，并生成txtResult.txt
    result = []

    # 在txtNew不在txtOld，newfoer
    count = 0
    result.append('newfoerId:' + '\n')
    for id in resultNew:
        if resultNew[count] not in resultOld:
            print("newfoerId:" + str(resultNew[count]))
            result.append('https://www.pixiv.net/member.php?id=')
            result.append(str(resultNew[count]) + '\n')
        count += 1

    # 在txtOld不在txtNew，unfoer
    count = 0
    result.append('unfoerId:' + '\n')
    for id in resultOld:
        if resultOld[count] not in resultNew:
            print("unfoerId:" + str(resultOld[count]))
            result.append('https://www.pixiv.net/member.php?id=')
            result.append(str(resultOld[count]) + '\n')
        count += 1

    # 生成txtResult
    txtResult = open('txtResult.txt', 'w')
    txtResult.write(''.join(result))
    txtResult.close()

    # 删掉txtOld，改txtNew名字为txtOld
    module_path = os.path.dirname(__file__)
    pathNew = module_path + '/txtNew.txt'
    pathOld = module_path + '/txtOld.txt'
    os.remove(pathOld)
    os.rename(pathNew, 'txtOld.txt')