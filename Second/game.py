from tkinter import * 
import hashlib 
import time
from random import randint
from math import sqrt


def exitG(window):
	window.destroy()


def check():
	global nick, nickname, password2, fhealth, score, money, bul_speed, ammount_bull, first_ab, second_ab, speed_of_game
	nickname = ex_login.get()
	password = ex_pass.get()

	text = "users/" + nickname + ".txt"
	file = open(text)
	info = file.read()
	file.close()
	info = info.split()
	nick = info[0]
	password2 =  info[1]
	hashed_pass = hashlib.md5(password.encode()).hexdigest()

	if (nickname == nick) and (hashed_pass == password2):
		fhealth = info[2]
		score = info[3]
		money = info[4]
		bul_speed = info[5]
		ammount_bull = info[6]
		speed_of_game = info[7]

		go_into.destroy()
		register.destroy()
		menu()
















def reg():
	nickname = cre_login.get()
	password = cre_pass.get()
	hashed_pass = hashlib.md5(password.encode()).hexdigest()
	file = open("users/nicknames.txt")
	nicks = file.read().split()


	if (password == "") or (nickname == "") or (nickname in nicks):
# I need to add some worrning here!
		cre_login.delete(0, "end")
		cre_pass.delete(0, "end")

	else:

		name = "users/" + nickname + ".txt"
		file = open(name, "w")
		# 0) nick, 1) pass, 2) healt, 3) score, 4) money, 5) speed of bullet, 6) ammount of bullet, 7) speed of game 
		text = nickname + "\n" + str(hashed_pass) + "\n" + "100" + "\n" + "0" "\n" + "0" + "\n" + "4" + "\n" + "3" + "\n" + "4000"  
		file.write(text)
		file.close()
		file = open("users/nicknames.txt", "a")
		text_v2 = nickname + "\n" 
		file.write(text_v2)
		file.close()
		registerv2.destroy()



def sign_in():
	global ex_login, ex_pass, go_into

	go_into = Toplevel()

	ws = go_into.winfo_screenwidth()
	hs = go_into.winfo_screenheight()
	go_into.geometry(("%dx%d" % (ws,hs)))
	go_into.attributes('-fullscreen', True)
	label = Label(go_into, bg ="#012", width = "200", height = "200")
	label.pack(fill = "x")

	frame = Frame(go_into, bg = "#012")
	frame.place(x = "700", y ="360")

	l_log = Label(frame, text = "Enter your nickname",font=("Courier", 20), fg = "white", bg = "gray")
	l_log.grid(row = 0, column = 0, padx = 2, pady = 2)
	ex_login = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white")
	ex_login.grid(row = 0, column = 1)

	l_pass = Label(frame, text = "Enter your password",font=("Courier", 20), fg = "white", bg = "gray")
	l_pass.grid(row = 1, column = 0, padx = 2, pady = 2)
	ex_pass = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white", show = "*")
	ex_pass.grid(row = 1, column = 1, pady = 20)

	button = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign In", font=("Courier", 20), fg = "white", command = check)
	button.grid(row = 2, columnspan = 2 , pady = 2)

	button = Button(frame, bg ="grey", width = "20", height = "2", text = "Go back", font=("Courier", 20), fg = "white", command = lambda: exitG(go_into))
	button.grid(row = 3, columnspan = 2 , pady = 2)

	go_into.mainloop()


def sign_up():
	global cre_login, cre_pass, registerv2
	registerv2 = Toplevel()
	ws = registerv2.winfo_screenwidth()
	hs = registerv2.winfo_screenheight()
	registerv2.geometry(("%dx%d" % (ws,hs)))
	registerv2.attributes('-fullscreen', True)
	label = Label(registerv2, bg ="#012", width = "200", height = "200")
	label.pack(fill = "x")

	frame = Frame(registerv2, bg = "#012")
	frame.place(x = "700", y ="360")

	label1 = Label(frame, text = "Enter your nickname",font=("Courier", 20), fg = "white", bg = "gray")
	label1.grid(row = 0, column = 0, padx = 2, pady = 2)

	cre_login = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white")
	cre_login.grid(row = 0, column = 1)

	label2 = Label(frame, text = "Enter your password",font=("Courier", 20), fg = "white", bg = "gray")
	label2.grid(row = 1, column = 0, padx = 2, pady = 2)

	cre_pass = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white", show = "*")
	cre_pass.grid(row = 1, column = 1, pady = 20)

	button = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign Up", font=("Courier", 20), fg = "white", command = reg)
	button.grid(row = 2, columnspan = 2 ,pady = 2)
	button = Button(frame, bg ="grey", width = "20", height = "2", text = "Go back", font=("Courier", 20), fg = "white", command = lambda: exitG(registerv2))
	button.grid(row = 3, columnspan = 2 , pady = 2)
	registerv2.mainloop()

def put_enemy():
	enemy_2 = c.create_image(100, 700 , image = sec_enemy)

	enemy_3 = c.create_image(1200, 50, image = third_enemy)

	c.after(100, put_enemy)




def bestiary():
	global c, sec_enemy, third_enemy


	bestiary = Toplevel()
	ws = bestiary.winfo_screenwidth()
	hs = bestiary.winfo_screenheight()
	nhs = hs - 120
	third_enemy = PhotoImage(file = "images/second_enemy.png")
	sec_enemy = PhotoImage(file = "images/enemy.png")
	bestiary.geometry(("%dx%d" % (ws,hs)))
	bestiary.attributes('-fullscreen', True)
	c = Canvas(bestiary, height = nhs, width = ws, bg = "black")

	c.create_oval(25, 25, 100, 100, fill = "#631c1c")

	c.create_text(300, 25 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Name: 'The Evil Meteorite'")
	c.create_text(300, 55 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Appears: score < 20")
	c.create_text(300, 85 ,fill="#f4eb13" ,font="Times 20 italic bold",text="DMG: 15")
	c.create_text(300, 115 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Gain exp: 1")
	c.create_text(300, 145 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Gain money: 20$")

	c.create_text(450, 650 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Name: 'The Evil Meteorite'")
	c.create_text(450, 680 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Appears: score >= 20 and score < 80")
	c.create_text(450, 710 ,fill="#f4eb13" ,font="Times 20 italic bold",text="DMG: 25")
	c.create_text(450, 740 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Gain exp: 5")
	c.create_text(450, 770 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Gain money: 60$")

	c.create_text(1500, 50 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Name: 'The Evil Meteorite'")
	c.create_text(1500, 80 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Appears: score >= 80 and score < 200")
	c.create_text(1500, 110 ,fill="#f4eb13" ,font="Times 20 italic bold",text="DMG: 30")
	c.create_text(1500, 140 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Gain exp: 10")
	c.create_text(1500, 170 ,fill="#f4eb13" ,font="Times 20 italic bold",text="Gain money: 80$")
	c.pack()

	put_enemy()




	exbutton = Button(bestiary, height = 5, width = 15, text = "Exit", font=("Courier", 44), bg = "grey", command = lambda: exitG(bestiary))
	exbutton.pack(side = "right")
	motivation = Label(bestiary, height = 5, font = ("Courier", 20), width = 90, text = "The best way of winning is learning about enemies first", bg = "gray")
	motivation.pack(side = "right", padx = 10)
	bestiary.mainloop()




def menu():
	global menu
	name = nick
	menu = Tk()
	ws = menu.winfo_screenwidth()
	hs = menu.winfo_screenheight()
	menu.geometry(("%dx%d" % (ws,hs)))
	menu.attributes('-fullscreen', True)
	label = Label(menu, bg ="#012", width = "200", height = "200")
	label.pack(side = "top", fill = "x")
	text = "Welcome to the Game\n" + name
	welcome = Label(menu, bg ="#012", text = text, font=("Courier", 44), fg = "white")
	welcome.place(x =ws/3 - 30, y = "130")
	frame = Frame(menu, bg = "#012")
	frame.place(x = ws/2 - 150, y ="360")
	new_game = Button(frame, bg ="grey", width = "20", height = "2", text = "Start the game!", font=("Courier", 20), fg = "white", command = start)
	new_game.grid(row = 0, column = 0, pady = 2)
	continue_game = Button(frame, bg ="grey", width = "20", height = "2", text = "Continue", font=("Courier", 20), fg = "white", state = DISABLED)
	continue_game.grid(row = 1, column = 0, pady = 2)
	button3 = Button(frame, bg ="grey", width = "20", height = "2", text = "Bestiary", font=("Courier", 20), fg = "white", command = bestiary)
	button3.grid(row = 2, column = 0, pady = 2)
	button4 = Button(frame, bg ="grey", width = "20", height = "2", text = "Read Me Please", font=("Courier", 20), fg = "white", state = DISABLED)
	button4.grid(row = 3, column = 0, pady = 2)
	button6 = Button(frame, bg ="grey", width = "20", height = "2", text = "Exit", font=("Courier", 20), fg = "white", command = lambda: exitG(menu))
	button6.grid(row = 5, column = 0, pady = 2)
	menu.mainloop()















	




def register():
	global register
	register = Tk()
	ws = register.winfo_screenwidth()
	hs = register.winfo_screenheight()
	register.geometry(("%dx%d" % (ws,hs)))
	register.attributes('-fullscreen', True)
	register.state('zoomed')
	label = Label(register, bg ="#012", width = "200", height = "200")
	label.pack(side = "top", fill = "x")
	welcome = Label(register, bg ="#012", text = "Welcome to Space Defender", font=("Courier", 44), fg = "white")
	welcome.place(x = ws/4, y = "130")
	frame = Frame(register, bg = "#012")
	frame.place(x = ws/2 - 200, y ="360")
	button1 = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign Up", font=("Courier", 20), fg = "white", command  = sign_up)
	button1.grid(row = 0, column = 0, pady = 2)
	button2 = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign In", font=("Courier", 20), fg = "white", command = sign_in)
	button2.grid(row = 1, column = 0, pady = 2)
	button3 = Button(frame, bg ="grey", width = "20", height = "2", text = "Exit", font=("Courier", 20), fg = "white", command = lambda: exitG(register))
	button3.grid(row = 5, column = 0, pady = 2)
	register.mainloop()
# command  = sign_up, command = sign_in




	











	


	





def start():
	menu.destroy()
	start_game()












def shop():
	pass


def start_game():

	#defining vars from the file 
	global shoot_speed, buttonpause, nick, health, new_score, money, bul_speed, enemy_speed, labhealth, repause, sec_enemy, boss_keyf, score, ability_work, first_abil, second_abil, time_slow, new_speed_of_game, money, new_money, stop_creating
	repause = False
	ability_work = False
	time_slow = False
	number_shoots = int(ammount_bull)
	health = int(fhealth)
	new_money = int(money)
	new_score = int(score)
	shoot_speed = int(bul_speed)
	new_speed_of_game = int(speed_of_game)
	# enemy_speed = 2
	#all list which will be used 
	shoot_id = []
	enemy_list = []
	score = 21
	stop_creating = False
	boss_keyf = 0



	def speed_of_the_game():
		global new_speed_of_game
		if not repause:
			if new_speed_of_game > 2000: 
				new_speed_of_game -= 120
			canvas.after(2000, speed_of_the_game)



	def bos_key(event):
		global boss_keyf, boss
		print(boss_keyf)
		if boss_keyf == 0:
			set_pause()
			boss = Toplevel()
			ws = boss.winfo_screenwidth()
			hs = boss.winfo_screenheight()
			boss.geometry(("%dx%d" % (ws,hs)))
			boss.attributes('-fullscreen', True)
			boss.attributes('-topmost', 'true')
			smart_diagram = PhotoImage(file = "images/bos_key.png")
			label = Label(boss, image = smart_diagram)
			label.pack()
			boss_keyf = 1
			boss.mainloop()
		if boss_keyf == 1:
			boss.destroy()
			boss_keyf = 0
			unpause()

	def not_lose_pause():
		canvas.after(5000, speed_of_the_game)
		canvas.after(20000, set_abil_true)

	def cheet(event):

		def get_cheet():
			global cheet, health, new_money
			cheet = cheet_entr.get()
			cheet_win.destroy()
			if cheet == "increase health":
				health += 10000
			if cheet == "increase health":
				new_money += 1000000


		global cheet, cheet_entr, cheet_win
		# cheet = False
		set_pause()
		cheet_win = Toplevel()
		cheet_win.geometry("+600+400")
		cheet_win.attributes('-topmost', 'true')
		cheet_win.title("CHEEEET")

		cheet_lab1 = Label(cheet_win, font=("Courier", 14), text = "Please remember that using of ")
		cheet_lab1.pack()

		cheet_lab2 = Label(cheet_win, font=("Courier", 14), text = "Cheat Codes make gameplay worse.")
		cheet_lab2.pack()

		cheet_lab3 = Label(cheet_win, font=("Courier", 20), text = "Enter the secret code")
		cheet_lab3.pack()

		cheet_entr = Entry(cheet_win, font=("Courier", 20),  width = 15, borderwidth = 8)
		cheet_entr.pack(side = "left")

		cheet_but = Button(cheet_win, font=("Courier", 20), width = 6, bg = "grey", text = "go", command = get_cheet)
		cheet_but.pack(side = "left")
		cheet_win.mainloop()

	def abil__ac():
		if ability_work:
			first_abil.config(state = NORMAL)
			second_abil.config(state = NORMAL)
		if not ability_work:
			first_abil.config(state = DISABLED)
			second_abil.config(state = DISABLED)
			abil_delay()


	def abil_heal():
		global health, ability_work
		health += 30
		ability_work = False
		abil__ac()

	def abil_time_diz():
		global time_slow 
		time_slow = False



	def abil_time():
		global time_slow, ability_work
		time_slow = True
		ability_work = False
		abil__ac() 
		canvas.after(8000, abil_time_diz)

	def set_abil_true():
		if not repause:
			global ability_work
			ability_work = True
			abil__ac()

	def abil_delay():
		canvas.after(20000, set_abil_true)


	def lose():
		def exit_game():
			leaderb.destroy()
			gamewindow.destroy( )

		def final_restart():
			global shoot_speed, buttonpause, nick, health, new_score, money, bul_speed, enemy_speed, labhealth, repause, sec_enemy, boss_keyf, score, ability_work, first_abil, second_abil, time_slow, new_speed_of_game, money, new_money, stop_creating
			repause = False
			ability_work = False
			time_slow = False
			number_shoots = 3
			health = 100
			new_money = 0
			new_score = 0
			shoot_speed = 4
			new_speed_of_game = 4000
			boss_keyf = 0			
			global stop_creating
			stop_creating = False
			create_enemy()

		def restart():
			global shoot_speed, buttonpause, nick, health, new_score, money, bul_speed, enemy_speed, labhealth, repause, sec_enemy, boss_keyf, score, ability_work, first_abil, second_abil, time_slow, new_speed_of_game, money, new_money, stop_creating
			stop_creating = True
			leaderb.destroy()
			canvas.after(10000, final_restart)









		global new_score, nick
		leaderb = Toplevel()
		ws = leaderb.winfo_screenwidth()
		hs = leaderb.winfo_screenheight()
		leaderb.geometry(("%dx%d" % (ws,hs)))
		leaderb.attributes('-fullscreen', True)
		leaderb.attributes('-topmost', 'true')
		leadcan = Canvas(leaderb, width = ws, height = hs - 200, bg = "black")
		file_1 = open("leaderboard/name.txt", "a")
		text = str(nick) + "\n" 
		file_1.write(text)
		file_1.close()


		file_2 = open("leaderboard/score.txt", "a")
		text2 = str(new_score) + "\n"
		file_2.write(text2)
		file_2.close()

		file_1 = open("leaderboard/name.txt", "r")
		names = file_1.read().split()
		file_1.close()

		file_2 = open("leaderboard/score.txt", "r")
		score = file_2.read().split()
		file_2.close()

		record = {}
		for i in range(len(names)):
			record[names[i]] =  int(score[i])
		list_record = list(record.items())
		list_record.sort(key=lambda i: i[1])
		textv2 = leadcan.create_text(ws/2, 30 ,fill="#f4eb13" ,font="Times 30 italic bold", text= "Game Over")

		# print(list_record[0])

		for i in range(len(list_record) - 1, -1, -1):
			place = str(list_record[i])
			place = place.replace(")", '')
			place = place.replace("(", '')
			place = place.replace("'", '')
			text = str(len(list_record) - i) + ") " + place
			textv2 = leadcan.create_text(500, 40 + 80 * (len(list_record) - i) ,fill="#f4eb13" ,font="Times 30 italic bold", text= text)
		leadcan.pack()
		buttonrestart = Button(leaderb,height= 5, text = "Restart" , font=("Courier", 20) ,bg = "grey", command = restart)
		buttonrestart.pack(side = "left")
		buttonex = Button(leaderb,height= 5, text = "Exit" , font=("Courier", 20) ,bg = "grey", command = exit_game)
		buttonex.pack(side = "right")
		leaderb.mainloop()








	def main_game_loop():
		global repause
		if health <= 0:
			# set_pause()
			lose()




		if not repause:
			canvas.after(50, main_game_loop)

	def unpause():
		global repause
		buttonpause.config(state = DISABLED) # in order to not broke the game, by fast cliking you can call some function twice
		text_3 = canvas.create_text(ws/2,hs/2 - 80 ,fill="#f4eb13" ,font="Times 60 italic bold",text="3")
		canvas.update()
		time.sleep(2)
		canvas.delete(text_3)

		text_2 = canvas.create_text(ws/2,hs/2 - 80 ,fill="#f4eb13" ,font="Times 60 italic bold",text="2")
		canvas.update()
		time.sleep(2)
		canvas.delete(text_2)


		text_1 = canvas.create_text(ws/2,hs/2 - 80 ,fill="#f4eb13" ,font="Times 60 italic bold",text="1")
		canvas.update()
		time.sleep(2)
		canvas.delete(text_1)

		text_go = canvas.create_text(ws/2,hs/2 - 80 ,fill="#f4eb13" ,font="Times 60 italic bold",text="GO!")
		canvas.update()
		time.sleep(2.3)
		canvas.delete(text_go)


		buttonpause.config(text = "Pause")
		buttonpause.config(command = set_pause)
		repause = False
		move_shoot()
		create_enemy()
		move_enemy()
		del_shoot()
		del_enemy()
		interaction()

		not_lose_pause()
		main_game_loop()
		buttonpause.config(state = NORMAL)
	def set_pause():
		global repause
		repause = True

		buttonpause.config(text = "Unpause")
		buttonpause.config(command = unpause)

			

	def exit():

		name = "users/" + nick + ".txt"
		file = open(name, "w")
		# 0) nick, 1) pass, 2) healt,  3) score, 4) money, 5) speed of bullet, 6) ammount of bullet, 7) speed of game
		text = nick + "\n" + str(password2) + "\n" + str(health) + "\n" + str(new_score) + "\n" + str(new_money) + "\n" + "1" + "\n" + "3" + "\n" + "4000"
		file.write(text)
		file.close()






		gamewindow.destroy()







	def leftKey(event):
		if not repause:
			canvas.move(hero, -20, 0)
	def rightKey(event):
		if not repause:
			canvas.move(hero, 20, 0)

#control block for shooting
#///////////////////////////////////////////////////

	def coords_shoot(id_num):
		pos = canvas.coords(id_num)
		x = (pos[0] + pos[2]) / 2
		y = (pos[1] + pos[3]) / 2
		return x, y

	def del_shootv2(j):
		canvas.delete(shoot_id[j])
		del shoot_id[j]

	def del_shoot():
		if not repause:
			for i in range (len(shoot_id) - 1, -1, -1):
				x,y = coords_shoot(shoot_id[i])
				if y < 0:
					del_shootv2(i)
			canvas.after(30, del_shoot)

#control block for the enemy ships 
#////////////////////////////////////////////////////

	def score_displ():
		global score_can
		score_text = "Score: " + str(new_score)
		score_can =canvas.create_text(140, 40, fill="#f4eb13" ,font="Times 30 italic bold",text=score_text)
		 
	def del_enemy():
		global health, enemy_dmg
		if not repause:
			if len(enemy_list) != 0:
				for i in range (len(enemy_list) - 1, -1, -1):
					x,y = coords_enemy(enemy_list[i])
					if y > 1000:
						del_enemyv2(i)
						health -= enemy_dmg 
			canvas.after(30, del_enemy)

	def coords_enemy(id_num):
		pos = canvas.bbox(id_num)
		x = (pos[0] + pos[2]) / 2
		y = (pos[1] + pos[3]) / 2
		return x, y

	def del_enemyv2(j):
		canvas.delete(enemy_list[j])
		del enemy_list[j]

#//////////////////////////////////////////////////////


	def get_distance(enemy, shoot):
		x1,y1 = coords_enemy(enemy)
		x2,y2 = coords_shoot(shoot)
		return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

	def interaction():
		global new_score, enemy_cost, score_can, new_money
		if not repause:
			a = 0
			for i in range(len(enemy_list) -1, -1, -1):
				a = 0
				for n in range(len(shoot_id) -1,-1, -1):
					if a == 0:
						if get_distance(enemy_list[i], shoot_id[n]) < 32:
							del_enemyv2(i)
							del_shootv2(n)
							new_score += int(enemy_cost)
							new_money += int(money_for_enemy)
							canvas.delete(score_can)
							score_displ()
							a = 1
			canvas.after(30, interaction)









	def move_shoot():
		if not repause:
			for i in range(len(shoot_id)):
				canvas.move(shoot_id[i], 0, -shoot_speed)
			am_text = "Ammo: " + str(number_shoots - len(shoot_id)) + "/" + str(number_shoots)
			ammo.config(text = am_text)
			he_text = "HP: " + str(health) 
			labhealth.config(text = he_text)
			money_text = "Money:  " + str(new_money)
			money.config(text = money_text)
			canvas.after(10, move_shoot)

	def move_enemy():
		global time_slow
		if not repause:
			for i in range(len(enemy_list)):
				if not time_slow:
					canvas.move(enemy_list[i], 0, enemy_speed)
				elif time_slow:
					canvas.move(enemy_list[i], 0, enemy_speed / 3)

			
			canvas.after(30, move_enemy)


	def create_enemy():
		global repause, new_score, enemy_cost, enemy_speed, enemy_dmg, money_for_enemy, new_speed_of_game, stop_creating
		if not repause and not stop_creating:
			if new_score < 20:
				randX = randint(400, ws - 400)	
				consY = -70
				enemy = canvas.create_oval(25, 25, 100, 100, fill = "#631c1c")
				enemy_list.append(enemy)
				canvas.move(enemy, randX, consY)
				enemy_cost = 10
				enemy_speed = 2
				enemy_dmg = 15
				money_for_enemy = 10

			if new_score >= 20 and new_score < 100:
				randX = randint(400, ws - 400)	
				consY = -70
				second_enemy = canvas.create_image(0,0, image = sec_enemy)
				enemy_list.append(second_enemy)
				canvas.move(second_enemy, randX, consY)
				enemy_cost = 100
				enemy_speed = 4
				enemy_dmg = 25
				money_for_enemy = 30

			if new_score >= 100 and new_score < 1000:
				randX = randint(400, ws - 400)	
				consY = -70
				third_enemy = canvas.create_image(0,0, image = thi_enemy)
				enemy_list.append(third_enemy)
				canvas.move(third_enemy, randX, consY)
				enemy_cost = 100
				enemy_speed = 5
				enemy_dmg = 30
				money_for_enemy = 50

			if new_score >= 1000:
				randX = randint(400, ws - 400)	
				consY = -70
				enemy_r4 = canvas.create_image(0,0, image = enemy_n4)
				enemy_list.append(enemy_r4)
				canvas.move(enemy_r4, randX, consY)
				enemy_cost = 100
				enemy_speed = 8
				enemy_dmg = 50
				money_for_enemy = 100

			canvas.after(new_speed_of_game, create_enemy)



	def shoot(event):
		if not repause:
			if len(shoot_id) < number_shoots:
				pos = canvas.coords(hero)
				x = pos[0]
				y = pos[1] - 20
				bullet = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill = "yellow")
				shoot_id.append(bullet)
		
			



	gamewindow = Tk()
	gamewindow.focus_force()
	mainhero = PhotoImage(file = "images/mainhero.png")
	sec_enemy = PhotoImage(file = "images/enemy.png")
	thi_enemy = PhotoImage(file = "images/second_enemy.png")
	enemy_n4  = PhotoImage(file = "images/enemy_4.png")
	ws = gamewindow.winfo_screenwidth()
	hs = gamewindow.winfo_screenheight()
	gamewindow.geometry(("%dx%d" % (ws+10 ,hs + 10)))
	gamewindow.attributes('-fullscreen', True)
	gamewindow.attributes("-topmost", True)
	nhs = hs - 100
	canvas = Canvas(gamewindow, height = nhs, width = ws, bg = "#af854c")
	canvas.bind("p", bos_key)
	canvas.bind("f", cheet)
	canvas.bind("<space>", shoot)
	canvas.bind("<Left>", leftKey)
	canvas.bind("<Right>", rightKey)
	# canvas.bind("<Up>", upKey)
	# canvas.bind("<Down>", downKey)
	canvas.focus_set()
	mainscene = PhotoImage(file = "images/main.jpg")
	canvas.create_image(0,0, anchor = NW, image = mainscene)
	canvas.pack()
	buttonex = Button(gamewindow,height= 5, text = "Save and Exit" , font=("Courier", 20) ,bg = "grey", command = exit)
	buttonex.pack(side = "right")
	buttonpause = Button(gamewindow,height= 5, width = 11,text = "Pause" , font=("Courier", 20) ,bg = "grey", command = set_pause)
	buttonpause.pack(side = "right")
	shop = Button(gamewindow,height= 5, width = 10, text = "Shop" , font=("Courier", 20) ,bg = "grey", state = DISABLED)
	shop.pack(side = "right")

	health_text = "HP: " + str(health) 
	money_text = "Money: " + str(money) 




	money = Label(gamewindow, height = 5, width = 28, text = money_text, font=("Courier", 20) ,bg = "grey")
	money.pack(side = "right", padx = 1)
	labhealth = Label(gamewindow, height = 5, width = 14, text = health_text, font=("Courier", 20) ,bg = "grey")
	labhealth.pack(side = "right")
	ammo_text = "Ammo: " + str(number_shoots - len(shoot_id)) + "/" + str(number_shoots)
	ammo = Label(gamewindow, height = 5, width = 14, text = ammo_text, font=("Courier", 20) ,bg = "grey")
	ammo.pack(side = "right", padx = 1)
	hero = canvas.create_image(0,0, image = mainhero)
	canvas.move(hero, ws/2, hs - 180)

	first_abil = Button(gamewindow,height= 5,width =10, text = "Heal" , font=("Courier", 20) ,bg = "grey", command = abil_heal, state = DISABLED)
	first_abil.pack(side = "left")
	second_abil = Button(gamewindow,height= 5, text = "Jumping bullet" , font=("Courier", 20) ,bg = "grey", command = abil_time, state = DISABLED)
	second_abil.pack(side = "left")

	move_shoot()
	create_enemy()
	move_enemy()
	del_shoot()
	del_enemy()
	interaction()
	score_displ()
	abil__ac()
	speed_of_the_game()
	main_game_loop()
	gamewindow.after(1, lambda: gamewindow.focus_force()) #In order to set focus on the main window
	gamewindow.mainloop()























































register()