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
    identifier = models.CharField(max_length = 255, null = True, unique = True, verbose_name='ID')
    prenom = models.CharField(max_length = 255, verbose_name='Prénom')
    nom = models.CharField(max_length = 255, verbose_name='Nom')
    email = models.EmailField(max_length = 255, unique = True, verbose_name='Email')
    telephone = models.CharField(max_length = 255, unique = True, verbose_name='Téléphone')
    pays = models.CharField(max_length = 255, verbose_name='Pays')
    ville = models.CharField(max_length = 255, verbose_name='Ville')
    addresse_physique = models.CharField(max_length = 255, verbose_name='Addresse Physique')
    Type_pe = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT, verbose_name='Type PE')
    raison_social = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT, verbose_name='Raison Social')
    addresse_commande = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT, verbose_name='Addresse Comande')
    addresse_facture = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT, verbose_name='Addresse Facture')
    statut_juridique = models.CharField(max_length = 10, choices = STATUT_JURIDIQUE, verbose_name='Statut Juridique')
    annee_creation = models.IntegerField(null = True, blank = True, verbose_name='Année de création')
    registre_commerce = models.CharField(max_length = 255, null = True, blank = True, default=DEFAULT, verbose_name='Registre de commerce')
    capital_social = models.IntegerField(null = True, blank = True, verbose_name='Capital social')
    chiffre_affaire = models.IntegerField(null = True, blank = True, verbose_name="Chiffre d'affaire")
    note_fournisseur = models.IntegerField(null = True, blank = True, verbose_name='Note du fournisseur')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
