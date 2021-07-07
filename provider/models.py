from django.db import models

class Provider(models.Model):
    STATUT_JURIDIQUE = (
        ("GIE", "GIE"),
        ("SURL", "SURL"),
        ("SAU", "SAU"),
        ("SARL", "SARL"),
        ("SARLU", "SARLU"),
        ("SAS", "SAS"),
        ("SCP", "SCP"),
        ("SA", "SA"),
        ("SNC", "SNC"),
        ("SUCCURSALE", "SUCCURSALE"),
    )
    DEFAULT = "Non Définit"
    identifier = models.CharField(max_length = 255, null = True, unique = True)
    prenom = models.CharField(max_length = 255)
    nom = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique = True)
    telephone = models.CharField(max_length = 255, unique = True)
    pays = models.CharField(max_length = 255)
    ville = models.CharField(max_length = 255)
    addresse_physique = models.CharField(max_length = 255)
    Type_pe = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT)
    raison_social = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT)
    addresse_commande = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT)
    addresse_facture = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT)
    statut_juridique = models.CharField(max_length = 10, choices = STATUT_JURIDIQUE)
    annee_creation = models.IntegerField(null = True, blank = True)
    registre_commerce = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT)
    capital_social = models.IntegerField(null = True, blank = True)
    chiffre_affaire = models.IntegerField(null = True, blank = True)
    note_fournisseur = models.IntegerField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
