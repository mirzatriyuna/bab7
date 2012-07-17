#meminta user memasukkan nama file
fname = raw_input('Enter the file name: ')
#pengecekan file
try:
   fname = open(fname)
#jika tidak ada maka tampilkan pesan
except:
   print 'error open file:', fname
   exit()

#mengubah semua huruf menjadi kapital
for line in fname:
    print line.upper()
