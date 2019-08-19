# hanya seorang pelajar yang belajar python
# https://github.com/skeleton45

import os,sys
os.system("clear")

print "\033[32;1mwww.affan45.site"
print (' ')
print ("\033[31;1m   *********    ********")
print ("   *  A    *    *  A   *")
print ("   *    R  *    *   R  *")
print ("   *********    *******")
print ("   *       *    * *")
print ("   *       *    *  *")
print ("   *       *    *    ***")
print ("\n   \033[33;1m     [x] IP Class & SUBNETMASK Finder Tool [x]")
print (" \n\033[32;1m  [1] Start IP & SUBNETMASK Finder\n  [2] Fungsi dan Penjelasan")

p = int(input("\n[>>>] Pilihanmu > "))

if p == 1:
	print ("\n\033[39;1m   [>>>] IP Class Finder [<<<]")
	a = str(raw_input("\n\033[32;1m[>>>] Masukan IP Address > "))
	
	if a <= "127.999.999.999":
		print "\n  \033[33;1m       	[!] KETEMU GAN [!]"
		print "\n\033[39;1m   [>>>] IP Address: " , a
		print "   [>>>] SUBNETMASK: 255.0.0.0"
		print "   [>>>] IP Class: A"
		
	elif a <= "191.999.999.999":
		print "\n  \033[33;1m       	[!] KETEMU GAN [!]"
		print "\n \033[39;1m  [>>>] IP Address: " , a
		print "   [>>>] SUBNETMASK: 255.255.0.0"
		print "   [>>>] IP Class: B"
		
	elif a <= "223.999.999.999":
		print "\n  \033[33;1m       	[!] KETEMU GAN [!]"
		print "\n\033[39;1m   [>>>] IP Address: " , a
		print "   [>>>] SUBNETMASK: 255.255.255.0"
		print "   [>>>] IP Class: C"
	else: os.system("exit()")
if p == 2:
	os.system("clear")
	print "\033[32;1mwww.affan45.site"
	print (' ')
	print ("\033[31;1m   *********    ********")
	print ("   *  A    *    *  A   *")
	print ("   *    R  *    *   R  *")
	print ("   *********    *******")
	print ("   *       *    * *")
	print ("   *       *    *  *")
	print ("   *       *    *    ***")
	print ("\n   \033[33;1m     [x] IP Class & SUBNETMASK Finder Tool [x]")
	print ("\n\033[39;1m[?] Apasih kegunaan tool/alat ini? Alat ini berfungsi untuk mencari 'Class IP & SUBNETMASK' dengan menggunakan alamat IP atau IP Address.\n\n[!] Contoh IP Adress: \n   [1] 116.22.177.1\n   [2] 192.168.1.12\n   [3] 222.167.22.11")
	plh = raw_input("\n[?] Sudah paham? jika sudah ketik y untuk kembali ke menu > ")
	if plh == "y":
		os.system("exit()")
		os.system("python2 ipsubnet.py")
