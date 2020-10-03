from tkinter import *
from datetime import datetime


def set_num():
	global timesnum
	times.config(text = str(timesnum))

def add_values():
	
	global timesnum, хачапури, джорджия, шашлык, фирминный, кахетинскй, бастурма, кебаб, салянка, харчо, чакапули
	global татариахни, чахохбили, чанахи, бозбаш, люля, царица, семга, курица, толма, оджахури, картошкагриб, джигит, джигиттел, джигитягн, баран
	global отбивная, мясогрибы, чашушули, отбивнаяинд, мужужи, хинкалисыр, хинкали, хинкалибаран, табак, фри, сыр, сыржаренный
	global овощная, лобио, баклажаны, баклажанырул, язык, кахети, капуста, морковь, свекла, ветчина, ермак, мясной, красавица
	global нежный, марина, греческий, цезарь, тбилиси

	timesnum += 1
	set_num()

	b1 = e1.get()
	хачапури += int(b1)

	b2 = e2.get()
	джорджия += int(b2)

	b3 = e3.get()
	шашлык += int(b3)

	b4 = e4.get()
	фирминный += int(b4)

	b5 = e5.get()
	кахетинскй += int(b5)

	b6 = e6.get()
	бастурма += int(b6)

	b7 = e7.get()
	кебаб += int(b7)

	b8 = e8.get()
	салянка += int(b8)

	b9 = e9.get()
	харчо += int(b9)

	b10 = e10.get()
	чакапули += int(b10)

	b11 = e11.get()
	татариахни += int(b11)

	b12 = e12.get()
	чахохбили += int(b12)

	b13 = e13.get()
	чанахи += int(b13)

	b14 = e14.get()
	бозбаш += int(b14)

	b15 = e15.get()
	люля += int(b15)

	b16 = e16.get()
	царица += int(b16)

	b17 = e17.get()
	семга += int(b17)

	b18 = e18.get()
	курица += int(b18)

	b19 = e19.get()
	толма += int(b19)

	b20 = e20.get()
	оджахури += int(b20)

	b21 = e21.get()
	картошкагриб += int(b21)

	b22 = e22.get()
	джигит += int(b22)

	b23 = e23.get()
	джигиттел += int(b23)

	b24 = e24.get()
	джигитягн += int(b24)

	b25 = e25.get()
	баран += int(b25)


#отбивная, мясогрибы, чашушули, отбивнаяинд, мужужи, хинкалисыр, хинкали, хинкалибаран, табак, фри, сыр, сыржаренный
	bs1 = es1.get()
	отбивная += int(bs1)

	bs2 = es2.get()
	мясогрибы += int(bs2)

	bs3 = es3.get()
	чашушули += int(bs3)

	bs4 = es4.get()
	отбивнаяинд += int(bs4)

	bs5 = es5.get()
	мужужи += int(bs5)

	bs6 = es6.get()
	хинкалисыр += int(bs6)

	bs7 = es7.get()
	хинкали += int(bs7)

	bs8 = es8.get()
	хинкалибаран += int(bs8)

	bs9 = es9.get()
	табак += int(bs9)

	bs10 = es10.get()
	фри += int(bs10)

	bs11 = es11.get()
	сыр += int(bs11)

	bs12 = es12.get()
	сыржаренный += int(bs12)

#овощная, лобио, баклажаны, баклажанырул, язык, кахети, капуста, морковь, свекла, ветчина, ермак, мясной, красавица
	bs13 = es13.get()
	овощная += int(bs13)

	bs14 = es14.get()
	лобио += int(bs14)

	bs15 = es15.get()
	баклажаны += int(bs15)

	bs16 = es16.get()
	баклажанырул += int(bs16)

	bs17 = es17.get()
	язык += int(bs17)

	bs18 = es18.get()
	кахети += int(bs18)

	bs19 = es19.get()
	капуста += int(bs19)

	bs20 = es20.get()
	морковь += int(bs20)

	bs21 = es21.get()
	свекла += int(bs21)

	bs22 = es22.get()
	ветчина += int(bs22)

	bs23 = es23.get()
	ермак += int(bs23)

	bs24 = es24.get()
	мясной += int(bs24)

	bs25 = es25.get()
	красавица += int(bs25)

#нежный, марина, греческий, цезарь, тбилиси

	bt1 = et1.get()
	нежный += int(bt1)

	bt2 = et2.get()
	марина += int(bt2)

	bt3 = et3.get()
	греческий += int(bt3)

	bt4 = et4.get()
	цезарь += int(bt4)

	bt5 = et5.get()
	тбилиси += int(bt5)











	set_to_zero()
	print(салянка)


















def set_to_zero():
	for i in entrs:
		i.delete(0,END)
		i.insert(0, 0)


def get_values():
	# global салянка
	filename = "files/" + datetime.today().strftime('%Y-%m-%d-%H.%M.%S')
	filename += ".txt"
	text = ("\tКороче вот Твой результат\n\n\n"+"Xачапури: " + str(хачапури) + "\nДжорджия: " + str(джорджия) + "\nШашлык: " + str(шашлык) + "\nФирменный: " + str(фирминный) + "\nПо Кахетинскй: " + str(кахетинскй) +
	"\nБастурма: " + str(бастурма) + "\nКебаб: " + str(кебаб) + "\nСалянка: " + str(салянка) + "\nХарчо: " + str(харчо) + "\nЧакапули: " + str(чакапули) + "\nТатариахни: " + str(татариахни) + "\nЧахохбили: " + str(чахохбили) +
	"\nЧанахи: " + str(чанахи) + "\nБозбаш: " + str(бозбаш) + "\nЛюля: " + str(люля) + "\nЦарица: " + str(царица) + "\nСемга: " + str(семга) + "\nКурица: " + str(курица) + "\nТолма: " + str(толма) + "\nОджахури: " + str(оджахури) +
	"\nКартошка с грибами: " + str(картошкагриб) + "\nДжигит: " + str(джигит) + "\nДжигит Тел: " + str(джигиттел) + "\nДжигит Ягн: " + str(джигитягн) + "\nБаран: " + str(баран) + "\nОтбивная: " + str (отбивная) +
	"\nМясо с грибами: " + str(мясогрибы) + "\nЧашушули: " + str(чашушули) + "\nОтбивная индейка: " + str(отбивнаяинд) + "\nМужужи: " + str(мужужи) + "\nХинкали сыр: " + str(хинкалисыр) + "\nХинкали: " + str(хинкали) + "\nХинкали баран: " + str(хинкалибаран) + 
	"\nТабак: " + str(табак) + "\nФри: " + str(фри) + "\nСыр: " + str(сыр) + "\nСыр жаренный: " + str(сыржаренный) + "\nОвощная: " + str(овощная) + "\nЛобио: " + str(лобио) + "\nБаклажаны: " + str(баклажаны) + "\nБаклажаны Рул: " + str(баклажанырул) + 
	"\nЯзык: " + str(язык) + "\nКахети: " + str(кахети) + "\nКапуста: " + str(капуста) + "\nМорковь: " + str(морковь) + "\nСвекла: " + str(свекла) + "\nВетчина: " + str(ветчина) + "\nЕрмак: " + str(ермак) + "\nМясной: " + str(мясной) + "\nКрасавица: " + str(красавица) + 
	"\nНежный: " + str(нежный) + "\nМарина: " + str(марина) + "\nГреческий: " + str(греческий) + "\nЦезарь: " + str(цезарь) + "\nТбилиси: " + str(тбилиси))




	file = open(filename, "w")

	file.write(text)
	file.close()
	print(text)




# хачапури, джорджия, шашлык, фирминный, кахетинскй, бастурма, кебаб, салянка, харчо, чакапули
# татариахни, чахохбили, чанахи, бозбаш, люля, царица, семга, курица, толма, оджахури  

хачапури = 0
джорджия = 0
шашлык = 0
фирминный = 0
кахетинскй = 0
бастурма = 0
кебаб = 0
салянка = 0
харчо = 0
чакапули = 0
татариахни = 0
чахохбили = 0
чанахи = 0
бозбаш = 0
люля = 0
царица = 0
семга = 0
курица = 0 
толма = 0
оджахури = 0
#картошкагриб, джигит, джигиттел, джигитягн, баран
картошкагриб = 0
джигит = 0
джигиттел = 0
джигитягн = 0
баран = 0


#отбивная, мясогрибы, чашушули, отбивнаяинд, мужужи, хинкалисыр, хинкали, хинкалибаран, табак, фри, сыр, сыржаренный
#овощная, лобио, баклажаны, баклажанырул, язык, кахети, капуста, морковь, свекла, ветчина, ермак, мясной, красавица
#нежный, марина, греческий, цезарь, тбилиси

отбивная = 0
мясогрибы = 0
чашушули = 0
отбивнаяинд = 0
мужужи = 0
хинкалисыр = 0
хинкали = 0
хинкалибаран = 0
табак = 0
фри = 0
сыр = 0
сыржаренный = 0
овощная = 0
лобио = 0
баклажаны = 0
баклажанырул = 0
язык = 0
кахети = 0
капуста = 0
морковь = 0
свекла = 0
ветчина = 0
ермак = 0
мясной = 0
красавица = 0
нежный = 0
марина = 0
греческий = 0
цезарь = 0
тбилиси = 0

timesnum = 0








root = Tk()
root.geometry("1200x800")
root.config(bg = "black")
frame = Frame(root)
frame.place(x = 10, y = 10)

secframe = Frame(root)
secframe.place(x = 240, y = 10)

thframe  = Frame(root)
thframe.place(x = 470, y = 10)


times = Label(root, font="Times 30 italic bold" ,text = str(timesnum))
times.place(x = 1140, y = 20)


butt_frame = Frame(root)
butt_frame.place(x = 950, y = 730)
butt_frame.config(bg = "gray")

ret = Button(butt_frame, width = 10, height = 4, text = "Вернуть", state = DISABLED)
ret.pack(side = "left", padx = 2)


add = Button(butt_frame, width = 10, height = 4, text = "Добавить", command = add_values)
add.pack(side = "left", padx = 2)



finish = Button(butt_frame, width = 10, height = 4, text = "Подсчет", command = get_values)
finish.pack(side = "left", padx = 2)



l1 = Label(frame, width = 20, text = "Хачапури: ", anchor='e')
l1.grid(row = 0, column = 0, padx=2, pady=2)
e1 = Entry(frame, width = 10)
e1.grid(row = 0, column = 1, padx=2, pady=2)

l2 = Label(frame, width = 20, text = "Джорджия: ", anchor='e')
l2.grid(row = 1, column = 0, padx=2, pady=2)
e2 = Entry(frame, width = 10)
e2.grid(row = 1, column = 1, padx=2, pady=2)

l3 = Label(frame, width = 20, text = "Шашлык: ", anchor='e')
l3.grid(row = 2, column = 0, padx=2, pady=2)
e3 = Entry(frame, width = 10)
e3.grid(row = 2, column = 1, padx=2, pady=2)

l4 = Label(frame, width = 20, text = "Фирменный: ", anchor='e')
l4.grid(row = 3, column = 0, padx=2, pady=2)
e4 = Entry(frame, width = 10)
e4.grid(row = 3, column = 1, padx=2, pady=2)

l5 = Label(frame, width = 20, text = "По Кахетинскй: ", anchor='e')
l5.grid(row = 4, column = 0, padx=2, pady=2)
e5 = Entry(frame, width = 10)
e5.grid(row = 4, column = 1, padx=2, pady=2)

l6 = Label(frame, width = 20, text = "Бастурма: ", anchor='e')
l6.grid(row = 5, column = 0, padx=2, pady=2)
e6 = Entry(frame, width = 10)
e6.grid(row = 5, column = 1, padx=2, pady=2)

l7 = Label(frame, width = 20, text = "Кебаб: ", anchor='e')
l7.grid(row = 6, column = 0, padx=2, pady=2)
e7 = Entry(frame, width = 10)
e7.grid(row = 6, column = 1, padx=2, pady=2)

l8 = Label(frame, width = 20, text = "Салянка: ", anchor='e')
l8.grid(row = 7, column = 0, padx=2, pady=2)
e8 = Entry(frame, width = 10)
e8.grid(row = 7, column = 1, padx=2, pady=2)

l9 = Label(frame, width = 20, text = "Харчо: ", anchor='e')
l9.grid(row = 8, column = 0, padx=2, pady=2)
e9 = Entry(frame, width = 10)
e9.grid(row = 8, column = 1, padx=2, pady=2)

l10 = Label(frame, width = 20, text = "Чакапули: ", anchor='e')
l10.grid(row = 9, column = 0, padx=2, pady=2)
e10 = Entry(frame, width = 10)
e10.grid(row = 9, column = 1, padx=2, pady=2)

l11 = Label(frame, width = 20, text = "Татариахни: ", anchor='e')
l11.grid(row = 10, column = 0, padx=2, pady=2)
e11 = Entry(frame, width = 10)
e11.grid(row = 10, column = 1, padx=2, pady=2)

l12 = Label(frame, width = 20, text = "Чахохбили: ", anchor='e')
l12.grid(row = 11, column = 0, padx=2, pady=2)
e12 = Entry(frame, width = 10)
e12.grid(row = 11, column = 1, padx=2, pady=2)

l13 = Label(frame, width = 20, text = "Чанахи: ", anchor='e')
l13.grid(row = 12, column = 0, padx=2, pady=2)
e13 = Entry(frame, width = 10)
e13.grid(row = 12, column = 1, padx=2, pady=2)

l14 = Label(frame, width = 20, text = "Бозбаш: ", anchor='e')
l14.grid(row = 13, column = 0, padx=2, pady=2)
e14 = Entry(frame, width = 10)
e14.grid(row = 13, column = 1, padx=2, pady=2)

l15 = Label(frame, width = 20, text = "Люля: ", anchor='e')
l15.grid(row = 14, column = 0, padx=2, pady=2)
e15 = Entry(frame, width = 10)
e15.grid(row = 14, column = 1, padx=2, pady=2)

l16 = Label(frame, width = 20, text = "Царица: ", anchor='e')
l16.grid(row = 15, column = 0, padx=2, pady=2)
e16 = Entry(frame, width = 10)
e16.grid(row = 15, column = 1, padx=2, pady=2)

l17 = Label(frame, width = 20, text = "Семга: ", anchor='e')
l17.grid(row = 16, column = 0, padx=2, pady=2)
e17 = Entry(frame, width = 10)
e17.grid(row = 16, column = 1, padx=2, pady=2)

l18 = Label(frame, width = 20, text = "Курица: ", anchor='e')
l18.grid(row = 17, column = 0, padx=2, pady=2)
e18 = Entry(frame, width = 10)
e18.grid(row = 17, column = 1, padx=2, pady=2)

l19 = Label(frame, width = 20, text = "Толма: ", anchor='e')
l19.grid(row = 18, column = 0, padx=2, pady=2)
e19 = Entry(frame, width = 10)
e19.grid(row = 18, column = 1, padx=2, pady=2)

l20 = Label(frame, width = 20, text = "Оджахури: ", anchor='e')
l20.grid(row = 19, column = 0, padx=2, pady=2)
e20 = Entry(frame, width = 10)
e20.grid(row = 19, column = 1, padx=2, pady=2)

l21 = Label(frame, width = 20, text = "Картошка с грибами: ", anchor='e')
l21.grid(row = 20, column = 0, padx=2, pady=2)
e21 = Entry(frame, width = 10)
e21.grid(row = 20, column = 1, padx=2, pady=2)

l22 = Label(frame, width = 20, text = "Джигит: ", anchor='e')
l22.grid(row = 21, column = 0, padx=2, pady=2)
e22 = Entry(frame, width = 10)
e22.grid(row = 21, column = 1, padx=2, pady=2)

l23 = Label(frame, width = 20, text = "Джигит Тел: ", anchor='e')
l23.grid(row = 22, column = 0, padx=2, pady=2)
e23 = Entry(frame, width = 10)
e23.grid(row = 22, column = 1, padx=2, pady=2)

l24 = Label(frame, width = 20, text = "Джигит Ягн: ", anchor='e')
l24.grid(row = 23, column = 0, padx=2, pady=2)
e24 = Entry(frame, width = 10)
e24.grid(row = 23, column = 1, padx=2, pady=2)

l25 = Label(frame, width = 20, text = "Баран: ", anchor='e')
l25.grid(row = 24, column = 0, padx=2, pady=2)
e25 = Entry(frame, width = 10)
e25.grid(row = 24, column = 1, padx=2, pady=2)



ls1 = Label(secframe, width = 20, text = "Отбивная: ", anchor='e')
ls1.grid(row = 0, column = 0, padx=2, pady=2)
es1 = Entry(secframe, width = 10)
es1.grid(row = 0, column = 1, padx=2, pady=2)

ls2 = Label(secframe, width = 20, text = "Мясо с грибами: ", anchor='e')
ls2.grid(row = 1, column = 0, padx=2, pady=2)
es2 = Entry(secframe, width = 10)
es2.grid(row = 1, column = 1, padx=2, pady=2)

ls3 = Label(secframe, width = 20, text = "Чашушули: ", anchor='e')
ls3.grid(row = 2, column = 0, padx=2, pady=2)
es3 = Entry(secframe, width = 10)
es3.grid(row = 2, column = 1, padx=2, pady=2)

ls4 = Label(secframe, width = 20, text = "Отбивная индейка: ", anchor='e')
ls4.grid(row = 3, column = 0, padx=2, pady=2)
es4 = Entry(secframe, width = 10)
es4.grid(row = 3, column = 1, padx=2, pady=2)

ls5 = Label(secframe, width = 20, text = "Мужужи: ", anchor='e')
ls5.grid(row = 4, column = 0, padx=2, pady=2)
es5 = Entry(secframe, width = 10)
es5.grid(row = 4, column = 1, padx=2, pady=2)

ls6 = Label(secframe, width = 20, text = "Хинкали сыр: ", anchor='e')
ls6.grid(row = 5, column = 0, padx=2, pady=2)
es6 = Entry(secframe, width = 10)
es6.grid(row = 5, column = 1, padx=2, pady=2)

ls7 = Label(secframe, width = 20, text = "Хинкали: ", anchor='e')
ls7.grid(row = 6, column = 0, padx=2, pady=2)
es7 = Entry(secframe, width = 10)
es7.grid(row = 6, column = 1, padx=2, pady=2)

ls8 = Label(secframe, width = 20, text = "Хинкали баран: ", anchor='e')
ls8.grid(row = 7, column = 0, padx=2, pady=2)
es8 = Entry(secframe, width = 10)
es8.grid(row = 7, column = 1, padx=2, pady=2)

ls9 = Label(secframe, width = 20, text = "Табак: ", anchor='e')
ls9.grid(row = 8, column = 0, padx=2, pady=2)
es9 = Entry(secframe, width = 10)
es9.grid(row = 8, column = 1, padx=2, pady=2)

ls10 = Label(secframe, width = 20, text = "Фри: ", anchor='e')
ls10.grid(row = 9, column = 0, padx=2, pady=2)
es10 = Entry(secframe, width = 10)
es10.grid(row = 9, column = 1, padx=2, pady=2)

ls11 = Label(secframe, width = 20, text = "Сыр: ", anchor='e')
ls11.grid(row = 10, column = 0, padx=2, pady=2)
es11 = Entry(secframe, width = 10)
es11.grid(row = 10, column = 1, padx=2, pady=2)

ls12 = Label(secframe, width = 20, text = "Сыр жаренный: ", anchor='e')
ls12.grid(row = 11, column = 0, padx=2, pady=2)
es12 = Entry(secframe, width = 10)
es12.grid(row = 11, column = 1, padx=2, pady=2)

ls13 = Label(secframe, width = 20, text = "Овощная: ", anchor='e')
ls13.grid(row = 12, column = 0, padx=2, pady=2)
es13 = Entry(secframe, width = 10)
es13.grid(row = 12, column = 1, padx=2, pady=2)

ls14 = Label(secframe, width = 20, text = "Лобио: ", anchor='e')
ls14.grid(row = 13, column = 0, padx=2, pady=2)
es14 = Entry(secframe, width = 10)
es14.grid(row = 13, column = 1, padx=2, pady=2)

ls15 = Label(secframe, width = 20, text = "Баклажаны: ", anchor='e')
ls15.grid(row = 14, column = 0, padx=2, pady=2)
es15 = Entry(secframe, width = 10)
es15.grid(row = 14, column = 1, padx=2, pady=2)

ls16 = Label(secframe, width = 20, text = "Баклажаны Рул: ", anchor='e')
ls16.grid(row = 15, column = 0, padx=2, pady=2)
es16 = Entry(secframe, width = 10)
es16.grid(row = 15, column = 1, padx=2, pady=2)

ls17 = Label(secframe, width = 20, text = "Язык: ", anchor='e')
ls17.grid(row = 16, column = 0, padx=2, pady=2)
es17 = Entry(secframe, width = 10)
es17.grid(row = 16, column = 1, padx=2, pady=2)

ls18 = Label(secframe, width = 20, text = "Кахети: ", anchor='e')
ls18.grid(row = 17, column = 0, padx=2, pady=2)
es18 = Entry(secframe, width = 10)
es18.grid(row = 17, column = 1, padx=2, pady=2)

ls19 = Label(secframe, width = 20, text = "Капуста: ", anchor='e')
ls19.grid(row = 18, column = 0, padx=2, pady=2)
es19 = Entry(secframe, width = 10)
es19.grid(row = 18, column = 1, padx=2, pady=2)

ls20 = Label(secframe, width = 20, text = "Морковь: ", anchor='e')
ls20.grid(row = 19, column = 0, padx=2, pady=2)
es20 = Entry(secframe, width = 10)
es20.grid(row = 19, column = 1, padx=2, pady=2)

ls21 = Label(secframe, width = 20, text = "Свекла: ", anchor='e')
ls21.grid(row = 20, column = 0, padx=2, pady=2)
es21 = Entry(secframe, width = 10)
es21.grid(row = 20, column = 1, padx=2, pady=2)

ls22 = Label(secframe, width = 20, text = "Ветчина: ", anchor='e')
ls22.grid(row = 21, column = 0, padx=2, pady=2)
es22 = Entry(secframe, width = 10)
es22.grid(row = 21, column = 1, padx=2, pady=2)

ls23 = Label(secframe, width = 20, text = "Ермак: ", anchor='e')
ls23.grid(row = 22, column = 0, padx=2, pady=2)
es23 = Entry(secframe, width = 10)
es23.grid(row = 22, column = 1, padx=2, pady=2)

ls24 = Label(secframe, width = 20, text = "Мясной: ", anchor='e')
ls24.grid(row = 23, column = 0, padx=2, pady=2)
es24 = Entry(secframe, width = 10)
es24.grid(row = 23, column = 1, padx=2, pady=2)

ls25 = Label(secframe, width = 20, text = "Красавица: ", anchor='e')
ls25.grid(row = 24, column = 0, padx=2, pady=2)
es25 = Entry(secframe, width = 10)
es25.grid(row = 24, column = 1, padx=2, pady=2)

lt1 = Label(thframe, width = 20, text = "Нежный: ", anchor='e')
lt1.grid(row = 0, column = 0, padx=2, pady=2)
et1 = Entry(thframe, width = 10)
et1.grid(row = 0, column = 1, padx=2, pady=2)

lt2 = Label(thframe, width = 20, text = "Марина: ", anchor='e')
lt2.grid(row = 1, column = 0, padx=2, pady=2)
et2 = Entry(thframe, width = 10)
et2.grid(row = 1, column = 1, padx=2, pady=2)

lt3 = Label(thframe, width = 20, text = "Греческий: ", anchor='e')
lt3.grid(row = 2, column = 0, padx=2, pady=2)
et3 = Entry(thframe, width = 10)
et3.grid(row = 2, column = 1, padx=2, pady=2)

lt4 = Label(thframe, width = 20, text = "Цезарь: ", anchor='e')
lt4.grid(row = 3, column = 0, padx=2, pady=2)
et4 = Entry(thframe, width = 10)
et4.grid(row = 3, column = 1, padx=2, pady=2)

lt5 = Label(thframe, width = 20, text = "Тбилиси: ", anchor='e')
lt5.grid(row = 4, column = 0, padx=2, pady=2)
et5 = Entry(thframe, width = 10)
et5.grid(row = 4, column = 1, padx=2, pady=2)




lt6 = Label(thframe, width = 20, text = "Чача Гиоргоба: ", anchor='e')
lt6.grid(row = 5, column = 0, padx=2, pady=2)
et6 = Entry(thframe, width = 10)
et6.grid(row = 5, column = 1, padx=2, pady=2)

lt7 = Label(thframe, width = 20, text = "Водка Белуга: ", anchor='e')
lt7.grid(row = 6, column = 0, padx=2, pady=2)
et7 = Entry(thframe, width = 10)
et7.grid(row = 6, column = 1, padx=2, pady=2)

lt8 = Label(thframe, width = 20, text = "Водка Финляндия: ", anchor='e')
lt8.grid(row = 7, column = 0, padx=2, pady=2)
et8 = Entry(thframe, width = 10)
et8.grid(row = 7, column = 1, padx=2, pady=2)

lt9 = Label(thframe, width = 20, text = "Водка Абсолют: ", anchor='e')
lt9.grid(row = 8, column = 0, padx=2, pady=2)
et9 = Entry(thframe, width = 10)
et9.grid(row = 8, column = 1, padx=2, pady=2)

lt10 = Label(thframe, width = 20, text = "Водка Царская Золотая: ", anchor='e')
lt10.grid(row = 9, column = 0, padx=2, pady=2)
et10 = Entry(thframe, width = 10)
et10.grid(row = 9, column = 1, padx=2, pady=2)

lt11 = Label(thframe, width = 20, text = "Водка Русский Стандарт: ", anchor='e')
lt11.grid(row = 10, column = 0, padx=2, pady=2)
et11 = Entry(thframe, width = 10)
et11.grid(row = 10, column = 1, padx=2, pady=2)

lt12 = Label(thframe, width = 20, text = "Водка Парламент: ", anchor='e')
lt12.grid(row = 11, column = 0, padx=2, pady=2)
et12 = Entry(thframe, width = 10)
et12.grid(row = 11, column = 1, padx=2, pady=2)

lt13 = Label(thframe, width = 20, text = "Водка Хортица: ", anchor='e')
lt13.grid(row = 12, column = 0, padx=2, pady=2)
et13 = Entry(thframe, width = 10)
et13.grid(row = 12, column = 1, padx=2, pady=2)

lt14 = Label(thframe, width = 20, text = "Водка Журавли: ", anchor='e')
lt14.grid(row = 13, column = 0, padx=2, pady=2)
et14 = Entry(thframe, width = 10)
et14.grid(row = 13, column = 1, padx=2, pady=2)

lt15 = Label(thframe, width = 20, text = "Водка Губернский Стан: ", anchor='e')
lt15.grid(row = 14, column = 0, padx=2, pady=2)
et15 = Entry(thframe, width = 10)
et15.grid(row = 14, column = 1, padx=2, pady=2)

lt16 = Label(thframe, width = 20, text = "Водка Зеленая Марка: ", anchor='e')
lt16.grid(row = 15, column = 0, padx=2, pady=2)
et16 = Entry(thframe, width = 10)
et16.grid(row = 15, column = 1, padx=2, pady=2)

lt17 = Label(thframe, width = 20, text = "Водка Белая Березка: ", anchor='e')
lt17.grid(row = 16, column = 0, padx=2, pady=2)
et17 = Entry(thframe, width = 10)
et17.grid(row = 16, column = 1, padx=2, pady=2)
















entrs = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, es1, es2, es3, es4, es5, es6, es7, es8, es9, es10, es11, es12, es13, es14, es15, es16, es17, es18, es19, es20, es21, es22, es23, es24, es25, et1, et2, et3, et4, et5]

set_to_zero()
root.mainloop()