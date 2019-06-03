import os
import zipfile

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)       
    else:
        print('This is not zip')
unzip_file(a,b)//

#zip_src:是zip文件的全路径
 
#dst_dir：是要解压到的目的文件夹
