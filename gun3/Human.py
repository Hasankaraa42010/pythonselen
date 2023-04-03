class Human:
    name="Halit"
    def __init__(self):
        print("Sınıf newlendi")
    def __init__(self,name):
        self.name=name 
    def __str__(self) -> str:
        return f"Sınıfı direl printte çağırınca gelen yazı:{self.name}"  
    def talk(self,sentence):
        print(f"{self.name}:{sentence}")
    def talk2(self,sentence):
        print(f"Human talk:{sentence}")   