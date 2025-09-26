import random

class Personnage:
    def __init__(self, nom, hp, attaque, mana):
        self.nom = nom
        self._hp = hp
        self.__attaque_de_base = attaque
        self.__mana = mana

    def get_attaque_de_base(self):
        return self.__attaque_de_base

    def attaquer(self, cible):
        degats = self.__attaque_de_base
        cible._hp -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégats.")
    
    def attaque_speciale(self, cible):
        if self.__mana >= 10:
            self.__mana -= 10
            degat_speciaux = self.__attaque_de_base * 2
            cible._hp -= degat_speciaux
            print(f"{self.nom} lance une attaque speciale sur {cible.nom} et inflige {degat_speciaux} dégats.")
        else:
            print(f"{self.nom} n'a pas assez de mana pour l'attaque spéciale.")

    def verif_mana(self):
        if self.__mana >= 10:
            return True
        else:
            return False

    def est_vivant(self):
        return self._hp > 0

class Heros(Personnage):
    def __init__(self, nom, hp, attaque, mana, bonus_attaque):
        super().__init__(nom, hp, attaque, mana)
        self.bonus_attaque = bonus_attaque

    def attaquer(self, cible):
        degats = self.get_attaque_de_base() + self.bonus_attaque
        cible._hp -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégats.")

class Monstre(Personnage):
    def attaquer(self, cible):
        if random.random() < 0.2:
            degats = self.get_attaque_de_base() * 2
            cible._hp -= degats
            print(f"{self.nom} inflige un coup critique de {degats} dégats")
        else:
            super().attaquer(cible)


heros = Heros("Aragorn", 100, 15, 30, 5)
monstre = Monstre("Gobelin", 50, 10, 0)
print("---- Début du combat amélioré! ----")
while heros.est_vivant() and monstre.est_vivant():
    if heros.verif_mana():
        heros.attaque_speciale(monstre)
    else:
        heros.attaquer(monstre)
    print(f" {monstre.nom} a {monstre._hp} Hp restants.")

    if monstre.est_vivant():
        if monstre.verif_mana():
            monstre.attaque_speciale(heros)
        else:
            monstre.attaquer(heros)
        print(f" {heros.nom} a {heros._hp} Hp restants.")

print("--- fin de combat ---")
if heros.est_vivant():
    print(f"Victoire! {heros.nom} a terrassé son adversaire.")
else: 
    print(f"Défaite... {monstre.nom} a eu raison de {heros.nom}.")
