#-*- coding: cp1254 -*-
import random
import time
print u"\nAdın ne?"
ad = raw_input(":")
print "\nPeki, ",ad,u" hadi seninle bir oyun oynayalım ben 1 ile 1000 arasında bir sayı tutuyorum.\n"
while True:
	print u"\ntahmin et bakalım\n"
	sa=random.randrange(1,1000)
	ts=1

	while True: 
		ta=input(":")
		if sa>ta:
			print u"\nyükselt\n"
			ts=ts+1
		elif sa<ta:
			print u"\nalçalt\n"
			ts=ts+1
		elif sa==ta:
			print u"\ndoğru tahmin\n"
			ts=ts+1
			if ts > 10 and ts <=15:
				print ts,u"\n tahminde bildin. Fena değilsin.\n"
			elif ts >15 and ts<=20:
				print ts,u"\n tahminde bildin. Kötü bir skor.\n"
			elif ts > 20:	
				print ts,u"\n tahminde bildin. Eminim daha kötü yapanlarda vardır. Boşver.\n"
				
			else:
				print ts,u"\n tahminde bildin. Süpersin.\n"
			break
	raw_input()
	print ""
	print u"\nŞimdi sıra bende hadi Sen 1 ile 1000 arasında bir sayı tut ben bileyim.\n"
	print ""
	raw_input()
	print u"\ntahminimi azaltmam gerekirse 'a' ya yükseltmem gerekirse 'y' ye \n"
	print ""
	raw_input()
	print u"\ntahminim doğru ise 'd' ye basman yeterli.\n"
	print ""
	raw_input()
	print u"\nSayı Tut\n"
	time.sleep(2)
	a=1
	b=1000
	ts2=1
	while True:
		try:
			sa2=random.randrange(a,b)
			while True:
				print sa2
				th=raw_input(":")
				if th == "y":
					a=sa2+1
					ts2=ts2+1
					break
				elif th == "a":
					b =sa2
					ts2=ts2+1
					break
				elif th == "d":
					print ts2,u"\n tahminde bildim.\n"
					if ts2>ts:
						print u"\nbeni geçtin aferin sana.\n" 
					elif ts2<ts:
						print u"\nseni geçtim ezik oooooooooooooooo.\n"
					elif ts2==ts:
						print u"\nskorlar eşit hadi bakalım.\n"
					break
				else:
					print u"\ntahminimi azaltmam gerekirse 'a' ya arttırmam gerekirse 'y' ye \n"
					print u"\ntahminim doğru ise 'd' ye basman gerekli.\n"
		except:
			print u"Hile yapıyosun"
			break
		
			

			
	print u"Bir daha oynamak istiyorsan 'y' ye basman yeterli"
	yeni = raw_input(":")
	if yeni != "y":
		print u"\nSeninle çok hoş vakit geçirdim. Teşekkür ederim\n"
		print u"\nTekrar oynamak istersen ben buradayım.\n"
		time.sleep(3)
		quit()
