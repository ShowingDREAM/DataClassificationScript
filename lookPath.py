import os

def all_path(dirname):

    result = []#���е��ļ�

    for maindir, subdir, file_name_list in os.walk(dirname):

        print("1:",maindir) #��ǰ��Ŀ¼
        print("2:",subdir) #��ǰ��Ŀ¼�µ�����Ŀ¼
        print("3:",file_name_list)  #��ǰ��Ŀ¼�µ������ļ�

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#�ϲ���һ������·��
            result.append(apath)

    return result

print(all_path("E:\myTest"))
