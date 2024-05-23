# Autofill Google Form
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')

# URL to the form you want to fill. formResponse should be used instead of viewform
url = os.getenv('url')


def get_values(course,promo,cursus,project):
    """It returns a dict of different form data to be submitted by send_form method."""

    values = {
        "entry.23904865" : os.getenv('name'),
        "entry.1480848492" : project,
        "entry.1770104696" : str(os.getenv('mail')) + "(Jusqu'à 10h disponibles par semaine, 10 groupes / mois)",
        "entry.1277129807" : promo,
        "entry.1677673843" : course,
        "entry.615985793" : "Non - No",
        "entry.1027757300" : cursus,
        "entry.555479852" : "FR uniquement",
        "entry.78623536" : "Non - No",
    }

    return values



def send_forms(url, values):
    """It takes google form url and the data which is a dict of key/value."""
    try:
        r = requests.post(url, data=values)
        print("\t\t",r,"\n")
        time.sleep(30)
    except:
        print("Error Occured!")
    return r



for course in ['DE']:
    for promo in ['JUN24','JUL24','AUG24','SEP24']: # ['DEC23','JAN24','FEB24','MAR24','APR24','MAY24','JUN24','JUL24','AUG24']:
        for cursus in ['Continu - Part-time','Bootcamp - Full-time']: #'Bootcamp - Full-time'
            for project in ['NY News', 'Satisfaction client', 'OPA', 'Job market', 'DST Airlines']:
            #for project in ['Recommendation de films', 'Prévision météo Australie', 'Classification de produits e-commerce Rakuten',
            # 'Accidents routiers en France', 'Recommendation de musiques', 'Paris sportifs']:

                final_data = get_values(course,promo,cursus,project)
                
                print(course,promo,cursus,"---",project)
                r = send_forms(url, final_data)




