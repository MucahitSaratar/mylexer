import os
class sablon:
	def __init__(self):
		self.ds = "a"
		self.dsayi = 0
		self.acilis = "section .data\n\t{}\n\nsection .text\n"
		self.kapanis = "\n\tmov eax, 1\n\txor ebx, ebx\n\tint 80h\n"
		self.uyku = "\n\tmov dword [saniye], {}\n\tmov dword [nanosaniye], 0\n\tmov eax, 162\n\tmov ebx, forsleep\n\tmov ecx, 0\n\tint 80h\n"
		self.yaz = "\n\tmov eax,4\n\tmov ebx, 1\n\tmov ecx, {}\n\tmov edx, {}\n\tint 80h\n"
		self.ana = ""

	def default_in(self):
		return self.acilis

	def default_out(self):
		return self.kapanis

	def sleep(self, uzunluk):
		if "forsleep" not in self.acilis:
			self.acilis = self.acilis.format("{}\n\tforsleep:\n\t\tsaniye: dd 0\n\t\tnanosaniye: dd 0\n")
		self.ana += self.uyku.format(uzunluk)
		self.ana

	def ekranayaz(self, metin, son):
		if son == 1:
			metin += "\", 10,\""
		elif son == 0:
			pass
		else:
			print "bu yazdigim ilk derleme hata ayiklama blogu, hayirli ugurlu olsun"
			exit(3)
		self.acilis = self.acilis.format("{}\n\tmetin"+self.ds+": db \""+metin+"\"\n\tmetin"+self.ds+"_l: equ $-metin"+self.ds+"\n")
		bir, iki = "metin"+self.ds, "metin"+self.ds+"_l"
		self.ana += self.yaz.format(bir, iki)
		self.ds += "a"


	def save(self, isim):
		op = open(isim.replace(".muco", ".asm"), "w+")
		op.write(self.net())
		op.close()


	def cmd(self, co):
		os.system(co)


	def run(self, isim):
		saf = isim.split(".")[0]
		olu = saf+".o"
		k1 = "nasm -f elf -o {} {}".format(olu, isim)
		k2 = "ld -m elf_i386 -o {} {}".format(saf, olu)
		k3 = "./" + saf
		self.cmd(k1)
		self.cmd(k2)
		self.cmd(k3)

	def net(self):
		return self.acilis.replace("{}", "")+self.ana+self.kapanis

a = sablon()
a.sleep(2)
a.ekranayaz("iki saniye ", 0)
a.sleep(3)
a.ekranayaz("uc saniye", 1)
a.save("lemoco.muco")
a.run("lemoco.asm")
