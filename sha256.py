import hashlib

f = open('C:\\After\\TheTypeOf_PDF4\\3a8f94ac5b0dd3c19fd51e79512f632a.pdf','rb')

sh = hashlib.sha256()
sh.update(f.read())
print sh.hexdigest()

f.close()
