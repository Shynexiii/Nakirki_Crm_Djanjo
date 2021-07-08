from django.forms import ModelForm, TextInput, Select, NumberInput

from .models import Provider


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = [
            'identifier', 'prenom', 'nom',
            'email', 'telephone', 'pays', 'ville', 'addresse_physique', 'Type_pe', 'raison_social', 'addresse_commande',
            'addresse_facture', 'statut_juridique', 'annee_creation', 'registre_commerce', 'capital_social',
            'chiffre_affaire', 'note_fournisseur'
        ]

        widgets = {
            'identifier': TextInput(attrs={'class': 'form-control'}),
            'prenom': TextInput(attrs={'class': 'form-control'}),
            'nom': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'telephone': TextInput(attrs={'class': 'form-control'}),
            'pays': TextInput(attrs={'class': 'form-control'}),
            'ville': TextInput(attrs={'class': 'form-control'}),
            'addresse_physique': TextInput(attrs={'class': 'form-control'}),
            'Type_pe': TextInput(attrs={'class': 'form-control'}),
            'raison_social': TextInput(attrs={'class': 'form-control'}),
            'addresse_commande': TextInput(attrs={'class': 'form-control'}),
            'addresse_facture': TextInput(attrs={'class': 'form-control'}),
            'statut_juridique': Select(attrs={'class': 'form-control'}),
            'annee_creation': TextInput(attrs={'class': 'form-control'}),
            'registre_commerce': TextInput(attrs={'class': 'form-control'}),
            'capital_social': NumberInput(attrs={'class': 'form-control'}),
            'chiffre_affaire': NumberInput(attrs={'class': 'form-control'}),
            'note_fournisseur': NumberInput(attrs={'class': 'form-control'}),
        }
