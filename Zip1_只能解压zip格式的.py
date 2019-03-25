import zipfile
import tarfile
import os
import shutil
from glob import glob
import sys

Address=sys.argv[1]
Pos_unzip=sys.argv[2]
Type=sys.argv[3]


def un_zip(filename):
	zip_file = zipfile.ZipFile(filename)
	a_name=zip_file.namelist()
	if (filename.find(".zip")) > -1:
		zip_file = zipfile.ZipFile(filename)
		a_name=zip_file.namelist()
	if (filename.find(".tar")) > -1:
		zip_file = tarfile.open(filename)
		a_name=zip_file.getnames()
		#zip_file=zipfile.getnames()
	for names in a_name:
		if (names.find(Type)) > -1:
			try:
				zip_file.extract(names,Pos_unzip)
			except:
				print(filename+" X_Fail")
				pass
	print (filename+" V_Done")
def all_path(dirname):
    substr = dirname.rfind("\\")
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            #print("."+apath[substr:])
            Pos_zip = "."+apath[substr:]
            files = glob(Pos_zip)
            for file_name in files:
                un_zip(file_name)
all_path(Address)
print("\n========All File has finished================")
