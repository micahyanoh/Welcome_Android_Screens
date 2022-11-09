from kivy.core.window import Window
from kivy.utils import rgba
from kivy.lang import Builder
from kivymd.app import MDApp

Window.size = (350,600)


class YourApp(MDApp):
    def build(self):
        return Builder.load_file('Your.kv')
    
    def current_slide(self,index):
        for i in range(4):
            if index==i:
                self.root.ids[f'slide{index}'].color= rgba(50, 44, 106, 255)
            else:
                self.root.ids[f'slide{i}'].color= rgba(233,237,240,255)
    
    def next(self):
        self.root.ids.carousel.load_next(mode='next')    

if __name__ == '__main__':
    YourApp().run()
        