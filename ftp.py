from ftplib import FTP

ftp=FTP()
ftp.connect("111.229.14.128", 21)
ftp.login('ftpusr','ogms')
# ftp.cwd('pub')
f=open('test.js','rb')
ftp.storbinary("STOR"+'te.js',f) 
f.close()

ftp.quit()


