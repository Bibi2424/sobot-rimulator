import pygtk
pygtk.require("2.0")
import gtk

class Simu:
	def __init__(self):
		interface = gtk.Builder()
		interface.add_from_file('glade_window.glade')
		
		# self.myLabel = interface.get_object("myLabel")
		self.button3 = interface.get_object("button3")
		interface.connect_signals(self)

	def on_main_window_destroy(self, widget):
		print 'Quiting...'
		gtk.main_quit()

	def on_button1_clicked(self, widget):
		print ' Clicked button1'
		if self.button3.is_sensitive():
			self.button3.set_sensitive( False )
		else:
			self.button3.set_sensitive( True )

	def on_button2_clicked(self, widget):
		print ' Clicked button2'

if __name__ == "__main__":
	Simu()
	gtk.main()