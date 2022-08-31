class MaPhrase:
    def __init__(self,maphrase):
        self.mots = maphrase.split()

    def titre(self):
        self.Mots = [mot.title() for mot in self.mots]

    def __len__(self):
        return len(" ".join(self.mots))
    
