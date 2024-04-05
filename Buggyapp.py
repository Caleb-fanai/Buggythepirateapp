from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.utils import platform
from kivy.clock import Clock
import subprocess

class BuggyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        
        # Create an image
        img = Image(source='/sdcard/Download/Buggy.png', size_hint=(1, 0.7))  # Larger image
        
        # Create a label
        label = Label(text='Press the Button to Play', size_hint=(1, 0.1))
        
        # Create a button with smaller size
        btn = Button(text='Play Now', size_hint=(1, 0.1))  # Smaller button
        btn.bind(on_press=self.show_popup)
        
        # Add the image, label, and button to the layout
        layout.add_widget(img)
        layout.add_widget(label)
        layout.add_widget(btn)
        
        return layout
    
    def show_popup(self, instance):
        # Create and show a popup message
        popup = Popup(title='Hello I am Caleb the creator',
                      content=Label(text='Playing wait for a few seconds...'),
                      size_hint=(None, None), size=(400, 200))
        popup.open()
        
        # Execute the Python script using subprocess
        self.run_script()
        
        # Schedule the dismissal of the popup after 8 seconds
        Clock.schedule_once(lambda dt: popup.dismiss(), 8)
    
    def run_script(self):
        # Check the platform to determine the correct Python interpreter
        python_executable = 'python' if platform == 'win' else 'python3'
        
        # Path to your Python script
        script_path = '/sdcard/Buggythepirate/retry.py'
        
        # Execute the Python script using subprocess
        subprocess.Popen([python_executable, script_path])

if __name__ == '__main__':
    BuggyApp().run()