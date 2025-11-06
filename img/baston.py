import random
from abc import ABC, abstractmethod


class Personnage(ABC):
    def __init__(self, nom, hp, attaque, mana):
        self.nom = nom
        self._hp = hp
        self._attaque_de_base = attaque 
        self._mana = mana 

    def get_attaque_de_base(self):
        return self._attaque_de_base

    def get_mana(self):
        return self._mana
    
    def consommer_mana(self, cout):
        if self._mana >= cout:
            self._mana -= cout
            return True
        return False
    
    @abstractmethod 
    def attaquer(self, cible):
        pass
    
    @abstractmethod
    def attaque_speciale(self, cible):
        pass

    def verif_mana(self, cout=10):
        return self._mana >= cout

    def est_vivant(self):
        return self._hp > 0


class Heros(Personnage):
    """Classe de base pour tous les héros, ajoutant un bonus d'attaque."""
    def __init__(self, nom, hp, attaque, mana, bonus_attaque):
        super().__init__(nom, hp, attaque, mana)
        self.bonus_attaque = bonus_attaque
    
    def attaquer(self, cible):
        degats = self.get_attaque_de_base() + self.bonus_attaque
        cible._hp -= degats
        print(f" {self.nom} attaque {cible.nom} et inflige {degats} dégâts.")

    def attaque_speciale(self, cible):
        cout_mana = 10
        if self.consommer_mana(cout_mana):
            degat_speciaux = self.get_attaque_de_base() * 3 + self.bonus_attaque
            cible._hp -= degat_speciaux
            print(f" {self.nom} utilise **'Frappe Héroïque'** sur {cible.nom} et inflige {degat_speciaux} dégâts.")
        else:
            print(f" {self.nom} n'a pas assez de mana pour la Frappe Héroïque.")


class Guerrier(Heros):
    """Classe pour Aragorn, spécialisé dans la force brute."""
    def attaque_speciale(self, cible):
        cout_mana = 8
        if self.consommer_mana(cout_mana):
            degat_speciaux = (self.get_attaque_de_base() + self.bonus_attaque) * 2.2
            cible._hp -= degat_speciaux
            print(f" {self.nom} utilise **'Coup Puissant'** sur {cible.nom} et inflige {degat_speciaux:.0f} dégâts!")
        else:
            print(f" {self.nom} n'a pas assez de mana ({self.get_mana()} restants) pour le Coup Puissant.")


class Legolas(Heros):
    """Héros archer spécialisé dans les dégâts de précision."""
    def attaque_speciale(self, cible):
        cout_mana = 15
        if self.consommer_mana(cout_mana):
            degat_speciaux = (self.get_attaque_de_base() + self.bonus_attaque) * 3
            cible._hp -= degat_speciaux
            print(f" {self.nom} décoche un **'Tir Vif'** sur {cible.nom} et inflige un coup critique de {degat_speciaux:.0f} dégâts!")
        else:
            print(f" {self.nom} n'a pas assez de mana ({self.get_mana()} restants) pour le Tir Vif.")


class Monstre(Personnage):
    """Classe de base pour les monstres, implémentant les attaques par défaut."""
    
    def attaquer(self, cible):
        degats = self.get_attaque_de_base() 
        if random.random() < 0.2:
            degats *= 2
            print(f"💥 {self.nom} inflige un coup critique de {degats} dégâts")
        else:
            print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        cible._hp -= degats

    def attaque_speciale(self, cible):
        cout_mana = 10
        if self.consommer_mana(cout_mana):
            degat_poison = self.get_attaque_de_base() * 1.5
            cible._hp -= degat_poison
            print(f" {self.nom} crache du **'Poison Mortel'** sur {cible.nom} et inflige {degat_poison:.0f} dégâts.")
        else:
            print(f" {self.nom} n'a pas assez de mana pour l'attaque spéciale.")
            self.attaquer(cible) 

class Gobelin(Monstre):
    """Monstre simple, utilise les attaques de la classe Monstre."""

class Urukai(Monstre):
    """Un monstre spécialisé avec des attaques modifiées (Rage Sanguinaire)."""

    def attaquer(self, cible):
        degats = self.get_attaque_de_base() 
        if random.random() < 0.3:
            degats *= 2.5
            cible._hp -= degats
            print(f" {self.nom} inflige un coup critique brutal de {degats:.0f} dégâts.")
        else:
            cible._hp -= degats
            print(f" {self.nom} attaque {cible.nom} et inflige {degats:.0f} dégâts.")
        

    def attaque_speciale(self, cible):
        cout_mana = 15
        if self.consommer_mana(cout_mana):
            degat_speciaux = self.get_attaque_de_base() * 3
            cible._hp -= degat_speciaux
            soin = degat_speciaux * 0.5
            self._hp += soin
            print(f" {self.nom} utilise **'Rage Sanguinaire'** sur {cible.nom} ({degat_speciaux:.0f} dégâts) et se soigne de {soin:.0f} PV!")
        else:
            print(f" {self.nom} n'a pas assez de mana ({self.get_mana()} restants). Attaque normale à la place.")
            self.attaquer(cible) 


options_heros = {
    "A": Guerrier("Aragorn", 120, 15, 30, 10),
    "L": Legolas("Legolas", 90, 18, 50, 7)
}


classes_monstres = [Gobelin, Urukai]


print("------------------------------------------------")
print("BIENVENUE DANS LA BASTON !")
print("Choisissez votre Héros:")
print("  [A] Aragorn (Guerrier - PV élevés, Attaque Puissante, Coût Mana : 8)")
print("  [L] Legolas (Archer - Dégâts très élevés, Coût Mana : 15)")
print("------------------------------------------------")

choix_heros = input("Entrez A ou L pour sélectionner votre héros : ").strip()

while choix_heros not in options_heros:
    print("Choix invalide. Veuillez entrer A ou L.")
    choix_heros = input("Entrez A ou L pour sélectionner votre héros : ").strip()


heros = options_heros[choix_heros]



ClasseMonstreAleatoire = random.choice(classes_monstres)


if ClasseMonstreAleatoire == Urukai:
    monstre = Urukai("Urukai-Lurtz", 100, 15, 30) 
elif ClasseMonstreAleatoire == Gobelin:
    monstre = Gobelin("Petit Gobelin", 60, 10, 10) 
else:

    monstre = Monstre("Monstre Inconnu", 70, 12, 5)


print(f"\nVous avez choisi : **{heros.nom}** !")
print(f"Votre adversaire sera : **{monstre.nom}** ({ClasseMonstreAleatoire.__name__}) !")
print("---- Que le duel commence ! ----")
print(f"{heros.nom} ({heros._hp} Hp, {heros.get_mana()} Mana) VS {monstre.nom} ({monstre._hp} Hp, {monstre.get_mana()} Mana)")
print("---")


while heros.est_vivant() and monstre.est_vivant():
    cout_heros = 15 if isinstance(heros, Legolas) else 8 if isinstance(heros, Guerrier) else 10
    

    if heros.verif_mana(cout_heros):
        heros.attaque_speciale(monstre)
    else:
        heros.attaquer(monstre)
    print(f" {monstre.nom} a {monstre._hp:.0f} Hp restants.")
    
    if not monstre.est_vivant():
        break

    cout_monstre = 15 if isinstance(monstre, Urukai) else 10
    
    if monstre.verif_mana(cout_monstre):
        monstre.attaque_speciale(heros)
    else:
        monstre.attaquer(heros)
    print(f" {heros.nom} a {heros._hp:.0f} Hp restants.")
    print("---")

print("--- FIN DU COMBAT ---")
if heros.est_vivant():
    print(f" Victoire! {heros.nom} a terrassé son adversaire.")
else: 
    print(f" Défaite... {monstre.nom} a eu raison de {heros.nom}.")