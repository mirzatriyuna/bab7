#masukkan nama file
fname = raw_input('Enter the file name: ')

if fname == 'na na boo boo':
   print 'NA NA BOO BOO TO YOU - You have been punkd!'
   exit()    
else:
   #pengecekan file eksis atau tidak
   try:
     fhand = open(fname)
   #jika tidak berhasil, print error
   except:
     print 'file cannot be opened:', fname
     exit()

   count = 0
   #menghitung banyaknya baris pada file tersebut
   for line in fhand:
      count = count + 1
   #menampilkan hasil bersama nama file
   print 'There were', count, 'subject line in', fname

