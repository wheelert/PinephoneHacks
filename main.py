import gi
import subprocess
import dbus

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
        
        bus = dbus.SystemBus()
        proxy = bus.get_object('org.freedesktop.PolicyKit1', '/org/freedesktop/PolicyKit1/Authority')
        authority = dbus.Interface(proxy, dbus_interface='org.freedesktop.PolicyKit1.Authority')

        system_bus_name = bus.get_unique_name()

        subject = ('system-bus-name', {'name' : system_bus_name})
        action_id = 'org.freedesktop.policykit.exec'
        details = {}
        flags = 1            # AllowUserInteraction flag
        cancellation_id = '' # No cancellation id

        result = authority.CheckAuthorization(subject, action_id, details, flags, cancellation_id)
        if(result[0] == 1):
            output = subprocess.Popen(['/usr/bin/pkexec','/usr/bin/ofonoctl', 'wan', '--connect','--ap'], text=True,
            stdout=subprocess.PIPE)

            stdout, _ = output.communicate()
            print("output>>"+stdout)
        
    def AppClose(self, widget):
        exit()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
