from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

class calc_screen(Screen):
	def clear(self):
		'''clearing the inputs'''
		self.ids.text_input.text="0"
	
	def back(self):
		'''removing last digit of input'''
		if self.ids.text_input.text!="0" and len(self.ids.text_input.text)>1 and self.ids.text_input.text!="Error":
			self.ids.text_input.text=self.ids.text_input.text[:-1]
		else:
			self.ids.text_input.text="0"
	
	def update(self,n):
		'''updating the value of input'''
		if self.ids.text_input.text=="0":
			self.ids.text_input.text=n
		else:
			self.ids.text_input.text=self.ids.text_input.text+n
			
	def add(self):
			self.ids.text_input.text=self.ids.text_input.text+"+"
	
	def subtract(self):
			self.ids.text_input.text=self.ids.text_input.text+"-"
	
	def multipy(self):
			self.ids.text_input.text=self.ids.text_input.text+"*"
	
	def divide(self):
		self.ids.text_input.text=self.ids.text_input.text+"/"
	
	def equal(self):
		try:
			self.ids.text_input.text=str(eval(self.ids.text_input.text))
		except:
			self.ids.text_input.text="Error"
	
	def change_sign(self):
		self.equal()
		try:
			self.ids.text_input.text=str(-float(self.ids.text_input.text))
		except:
			self.ids.text_input.text="Error"
			
			
class calc(App):
	def build(self):
		#Window.clearcolor=(1,1,1,1)
		return calc_screen()
		
if __name__=="__main__":
	calc().run()
	