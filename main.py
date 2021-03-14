import gi
import subprocess 

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Custom Commands")
        
        # load CSS
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path("/usr/share/PinephoneHacks/PinephoneHacks.css")
        Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)


        self.button = Gtk.Button(label="Enable Data")
        self.button.connect("clicked", self.on_button_clicked)
        vbox.add(self.button)
        
        #exit button
        self.button2 = Gtk.Button(label="Exit")
        self.button2.connect("clicked", self.AppClose)
        vbox.add(self.button2)
        
        self.add(vbox)
        
        

    def on_button_clicked(self, widget):
        print("Connecting WAN")
        output = subprocess.Popen(['/usr/bin/ofonoctl', 'wan', '--connect','--ap'], text=True,
        stdout=subprocess.PIPE)

        stdout, _ = output.communicate()
        print("output>>"+stdout)
        
    def AppClose(self, widget):
        exit()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
