from django.shortcuts import render
from .models import Annonce
from .forms import Form_Annonce, Form_Add
from django.db.models import Avg
import requests
import json

# Create your views here.

def accueil(request):
    ann_form = Form_Annonce()
    add_form = Form_Add()

    result_moy, quartile10, quartile90, err = None, None, None, None
    message = None

    if request.method == "POST":
        form_a = Form_Annonce(request.POST)
        form_l = Form_Add(request.POST)
        if form_a.is_valid():
            data = form_a.cleaned_data
            if data['code_ville']:
                result_moy = Annonce.objects.filter(code_ville = data['code_ville']).aggregate(moyenne = Avg('prix'))['moyenne']
                liste_prix = Annonce.objects.filter(code_ville = data['code_ville']).order_by('prix').values_list('prix', flat=True)
                if len(liste_prix) != 0:
                    quartile10 = liste_prix[len(liste_prix) // 10]
                    quartile90 = liste_prix[len(liste_prix) * 9 // 10]
                else: err = True
            elif data['ville']:
                data['ville'] = data['ville'].lower()
                result_moy = Annonce.objects.filter(ville = data['ville']).aggregate(moyenne = Avg('prix'))['moyenne']
                liste_prix = Annonce.objects.filter(ville = data['ville']).order_by('prix').values_list('prix', flat=True)
                if len(liste_prix) != 0:
                    quartile10 = liste_prix[len(liste_prix) // 10]
                    quartile90 = liste_prix[len(liste_prix) * 9 // 10]
                else: err = True
            elif data['departement']:
                result_moy = Annonce.objects.filter(departement = data['departement']).aggregate(moyenne = Avg('prix'))['moyenne']
                liste_prix = Annonce.objects.filter(departement = data['departement']).order_by('prix').values_list('prix', flat=True)
                if len(liste_prix) != 0:
                    quartile10 = liste_prix[len(liste_prix) // 10]
                    quartile90 = liste_prix[len(liste_prix) * 9 // 10]
                else: err = True
            if result_moy: result_moy = int(result_moy)
        if form_l.is_valid():
            # Find the id, ask API and return useful data
            lien = str(form_l.cleaned_data['lien'])
            
            id_bien = lien[lien.find("/ag") + 3: lien.find("?q")]

            url = "https://www.bienici.com/realEstateAd.json?id=ag" + str(id_bien)
            response = requests.get(url)
            if response.ok:
                json_data = json.loads(response.content)
                code_postal, ville, prix = json_data['postalCode'], json_data['city'], json_data['priceWithoutFees']
                try:
                    annonce = Annonce(prix = prix, departement = code_postal[:-3], ville = ville, code_ville = code_postal)
                    annonce.save()
                    message = "L'annonce " + id_bien + " a bien été enregistrée dans la base de données"
                except:
                    message = "Erreur lors de l'ajout de l'annonce"
                    pass

    return render(request, "app_data/home.html", context={"ann_form": ann_form, "add_form": add_form, "result_moy": result_moy, "quartile10": quartile10, "quartile90": quartile90, "err": err, "message": message})
    
