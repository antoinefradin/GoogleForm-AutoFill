# Autofill Google Form
import requests
import time
import os
from dotenv import load_dotenv
from random import randint


load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')

# URL to the form you want to fill. formResponse should be used instead of viewform
url = os.getenv('url')


def get_values(course,promo,cursus,project):
    """It returns a dict of different form data to be submitted by send_form method."""

    values = {
        "entry.23904865" : os.getenv('name'),
        "entry.1480848492" : project,
        "entry.1770104696" : str(os.getenv('mail')) + "(Beaucoup de disponibilités à partir du 1er Septembre 2024)",
        "entry.1277129807" : promo,
        "entry.1677673843" : course,
        "entry.615985793" : "Oui - Yes",
        "entry.1027757300" : cursus,
        "entry.555479852" : "FR or EN", #"FR uniquement",
        #"entry.78623536" : "Non - No",
    }

    return values



def send_forms(url, values):
    """It takes google form url and the data which is a dict of key/value."""
    try:
        r = requests.post(url, data=values)
        print("\t\t",r,"\n")
        time.sleep(randint(25,35))
    except:
        print("Error Occured!")
    return r


send_de = True
send_mlops = True
send_ds = False
send_da = False


if send_de:
    for course in ['DE']:
        for promo in ["OCT24","NOV24","DEC24"]: # ['DEC23','JAN24','FEB24','MAR24','APR24','MAY24','JUN24','JUL24','AUG24']:
            for cursus in ['Continu - Part-time','Bootcamp - Full-time']: #'Bootcamp - Full-time'
                for project in ['NY News', 'Satisfaction client', 'OPA', 'Job market', 'DST Airlines',"Itinéraire de vacances"]:

                    final_data = get_values(course,promo,cursus,project)
                    
                    print(course,promo,cursus,"---",project)
                    r = send_forms(url, final_data)


if send_ds:
    for course in ['DS']:
        for promo in ["SEP24","OCT24","NOV24","DEC24"]: 
            for cursus in ['Continu - Part-time','Bootcamp - Full-time']:
                for project in ["Système de recommendation de films", "Prévision météo Australie", 'Classification de produits e-commerce Rakuten',
                 'Emission de CO2 par les véhicules', 'Recommendation de plantes', 'Analyse des tirs de joueurs NBA']:

                    final_data = get_values(course,promo,cursus,project)
                    
                    print(course,promo,cursus,"---",project)
                    r = send_forms(url, final_data)

if send_mlops:
    for course in ['MLOps']:
        for promo in ["SEP24","OCT24","NOV24","DEC24"]: 
            for cursus in ['Continu - Part-time','Bootcamp - Full-time']:
                for project in ["Recommendation de films", "Prévision météo Australie", 'Classification de produits e-commerce Rakuten',
                   'Recommendation de musiques', 'Paris sportif']:

                    final_data = get_values(course,promo,cursus,project)
                    
                    print(course,promo,cursus,"---",project)
                    r = send_forms(url, final_data)


if send_da:
    for course in ['DA']:
        for promo in ["SEP24","OCT24","NOV24","DEC24"]: 
            for cursus in ['Continu - Part-time','Bootcamp - Full-time']: 
                for project in ["Data job, Energie, Recommendation de films", "Prédire le succès d\'une campagne de financement participatif", "Mon Petit Gazon"]:

                    final_data = get_values(course,promo,cursus,project)
                    
                    print(course,promo,cursus,"---",project)
                    r = send_forms(url, final_data)