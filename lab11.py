class Projector_screen:

    quality=100

    def __init__(self, height = 1 , width = 2, manufacturer = "Google", connectionType = "wall"):
        self.height = height
        self.width = width
        self.manufacturer = manufacturer
        self.connectionType = connectionType

    @staticmethod
    def return_static_quality(self):
        return self.quality

    def __del__(self):
        print("destructor")

    def __str__(self):
        return '{self.manufacturer} projector connected to the {self.connectionType} with parameters of height: {self.height} and width:{self.width} '.format(self=self)  
           
def main():
    Projector1 = Projector_screen()
    print(Projector1)
    Projector2 = Projector_screen(5,6,"Samsung","ceil")
    print(Projector2)
    Projector3 = Projector_screen(height=5,manufacturer="Apple",connectionType="floor")
    print(Projector3)
    Projector1.quality=50
    print (Projector1.quality)
    print(Projector_screen.return_static_quality(Projector1))

if __name__ == "__main__":
    main()