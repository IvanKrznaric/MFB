from manim import *
import numpy as np

class mnozenje(Scene):
	def construct(self):
		self.camera.background_color = WHITE
		zadatak = Tex("Problem", color = BLACK)
		okvir = SurroundingRectangle(zadatak, color = PINK, fill_opacity = 0.4)
		opis = Tex("Find the product of the following matrices:", color = BLACK, font_size = 40)
		opis.next_to(okvir)
		#tekst = VGroup(zadatak, okvir, opis)
		tekst = MarkupText("Matrix multiplication:", font_size= 40, font = "Arial", color = DARK_BLUE)
		tekst.move_to(3.5*UP + 4*LEFT)
		copyright_text = MarkupText("Ivan Krznarić, Faculty of Economics and Business, University of Zagreb \n© Copyright 2025 ", font_size=12, font = "Arial", color = BLACK).to_edge(UR).shift(LEFT * (-0.3) + UP * 0.3)
		self.add(tekst, copyright_text)
		self.wait(1.5)
		
		a = np.array([[0,1],[1,0],[2,2]])
		b = np.array([[4,0,1], [3,2, 8]])
		c = np.dot(a,b)

		A = Matrix(a)
		A.set_color(BLACK)
		A.move_to(UP+LEFT*4)
		B = Matrix(b)
		B.set_color(BLACK)
		C = Matrix(c)
		C.set_color(BLACK)
		self.play(Write(A))
		#self.play(A.animate.move_to(UP+LEFT*4))
		Dot = Tex(".", color = BLACK, font_size = 100)
		Dot.next_to(A)
		self.play(Write(Dot), run_time = 0.5)
		B.next_to(Dot)
		self.play(Write(B))
		
		self.wait(1)

		jednako = Tex("=", color = BLACK, font_size = 75)
		jednako.next_to(B)
		self.play(Write(jednako), run_time = 0.5)
		
		C.next_to(jednako)
		elementi_C =VGroup(*C) #ovom naredbom rasčlanim matricu C na tri dijela - elementi matrice (to je nulti dio), lijeva zagrada i desna zagrada
		for i in elementi_C[1:]: #u ovoj for petlji ispišem lijevu i desnu zagradu matrice C
			self.play(Write(i))
		elementi_C = VGroup(*elementi_C[0]) #ovime sad varijablu elementi_C pretvaram u četiri broja koja predstavljaju elemente matrice C
		elementi_C_kopija = elementi_C.copy()
		
		retci_A = A.get_rows()
		A = VGroup(retci_A[0], retci_A[0], retci_A[1], retci_A[1], retci_A[2], retci_A[2])
		stupci_B = B.get_columns()
		B = VGroup(stupci_B[0], stupci_B[1], stupci_B[2], stupci_B[0], stupci_B[1], stupci_B[2], stupci_B[0], stupci_B[1], stupci_B[2] )
		
		i = 0
		j = 0
		for r in A.copy():
			for c in B.copy():
				prvi_faktor = VGroup(SurroundingRectangle(r, color = BLUE, fill_opacity = 0.5), r)
				drugi_faktor = VGroup(SurroundingRectangle(c, color = RED, fill_opacity = 0.5), c)
				self.play(Create(prvi_faktor))
				self.play(Create(drugi_faktor))
				prvi_faktor_kopija = prvi_faktor.copy()
				prvi_faktor_kopija.next_to(A, DOWN*6)
				drugi_faktor_kopija = drugi_faktor.copy()
				drugi_faktor_kopija.next_to(prvi_faktor_kopija)
				self.play(Create(prvi_faktor_kopija), run_time = 0.75)
				self.wait(0.5)
				self.play(Create(drugi_faktor_kopija), run_time = 0.75)
				self.wait(0.5)
				
				#sada zapravo kodiram množenje
				prvi_A = prvi_faktor_kopija[1][0]
				drugi_A = prvi_faktor_kopija[1][1]
				#treci_A = prvi_faktor_kopija[1][2]
				prvi_B = drugi_faktor_kopija[1][0]
				drugi_B = drugi_faktor_kopija[1][1]
				#treci_B = drugi_faktor_kopija[1][2]
				arc1 = ArcBetweenPoints(prvi_A.get_top(), prvi_B.get_top(), angle= -1*np.pi/2)
				arc2 = ArcBetweenPoints(drugi_A.get_bottom(), drugi_B.get_bottom(), angle = np.pi/2)
				arc1.set_color(BLACK)
				arc2.set_color(BLACK)
				self.play(Create(arc1), run_time = 0.5)
				self.play(Create(arc2), run_time = 0.5)
				self.wait(0.5)
				

				#sada množim svaki sa svakim
				prvi_A_kopija = prvi_A.copy()
				prvi_A_kopija.next_to(drugi_faktor_kopija, RIGHT*5)
				self.play(Write(prvi_A_kopija), run_time = 0.5)
				Dot1 = Tex(".", color = BLACK, font_size = 50)
				Dot1.next_to(prvi_A_kopija)
				self.play(Write(Dot1), run_time = 0.1)
				prvi_B_kopija = prvi_B.copy()
				prvi_B_kopija.next_to(Dot1)
				self.play(Write(prvi_B_kopija), run_time = 0.5)
				plus = Tex("+", color = BLACK, font_size = 50)
				plus.next_to(prvi_B_kopija)
				self.play(Write(plus), run_time = 0.5)
				drugi_A_kopija = drugi_A.copy()
				drugi_A_kopija.next_to(plus)
				self.play(Write(drugi_A_kopija), run_time = 0.5)
				Dot2 = Tex(".", color = BLACK, font_size = 50)
				Dot2.next_to(drugi_A_kopija)
				self.play(Write(Dot2), run_time = 0.5)
				drugi_B_kopija = drugi_B.copy()
				drugi_B_kopija.next_to(Dot2)
				self.play(Write(drugi_B_kopija), run_time = 0.5)
				#treci_A_kopija = treci_A.copy()
				#self.play(Write(treci_A_kopija), run_time = 0.5)
				#Dot3 = Tex(".", color = BLACK, font_size = 50)
				#Dot3.next_to(treci_A_kopija)
				#self.play(Write(Dot3), run_time = 0.5)
				#treci_B_kopija = treci_B.copy()
				#treci_B_kopija.next_to(Dot3)
				#self.play(Write(treci_B_kopija), run_time = 0.5)
				jednako = Tex("=", color = BLACK, font_size = 50)
				jednako.next_to(drugi_B_kopija)
				self.play(Write(jednako), run_time = 0.5)
				rez = elementi_C_kopija[i]
				rez.next_to(jednako)
				self.play(Write(rez), run_time = 0.5)
				self.wait(0.75)
				self.play(ReplacementTransform(rez, elementi_C[i]))
				i = i+1
				
				
				
                #sada čistim
				self.remove(arc1, arc2)
				self.remove(prvi_A_kopija, Dot1, prvi_B_kopija, plus, drugi_A_kopija, Dot2, drugi_B_kopija, jednako, rez) 
				self.remove(prvi_faktor_kopija)
				self.remove(drugi_faktor_kopija)
				self.remove(prvi_faktor)
				self.remove(drugi_faktor)
		self.wait(2)
		
