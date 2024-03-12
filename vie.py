import argparse
import os
import pandas as pd
import requests
import subprocess
from datetime import datetime

def get_offers(limit, skip):
    url = "https://civiweb-api-prd.azurewebsites.net/api/Offers/search"
    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "limit": limit,
        "skip": skip,
        "query": "",
        "activitySectorId": [],
        "missionsTypesIds": [],
        "missionsDurations": [],
        "gerographicZones": [],
        "countriesIds": [],
        "studiesLevelId": [],
        "companiesSizes": [],
        "specializationsIds": [],
        "entreprisesIds": [0],
        "missionStartDate": None
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP error codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")
        return {"error": "The request failed."}

def fetch_all_offers(total_offers):
    all_offers = []

    print(f"Retrieving {total_offers} offers...")

    total_offers_retrieved = 0
    offers_per_request = 90

    while total_offers_retrieved < total_offers:
        remaining_offers = total_offers - total_offers_retrieved
        current_limit = min(offers_per_request, remaining_offers)

        result = get_offers(current_limit, total_offers_retrieved)

        if 'result' in result and result['result']:
            all_offers.extend(result['result'])
            total_offers_retrieved += len(result['result'])
            print(f"Offers retrieved: {total_offers_retrieved} / {total_offers}")
        else:
            print("No offers retrieved. Stopping retrieval.")
            break

    return all_offers

def save_to_csv(offers_data, filename):
    df = pd.DataFrame(offers_data)
    df.to_csv(filename, index=False)
    print(f"CSV file '{filename}' created successfully.")

def save_to_html(offers_data, filename):
    df = pd.DataFrame(offers_data)
    df = df[['Lien'] + [col for col in df.columns if col != 'Lien']]
    with open(filename, 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n')
        f.write('<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">\n')
        f.write('<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n')
        f.write('<script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>\n')
        f.write('<script>\n')
        f.write('$(document).ready(function() {\n')
        f.write('    $("#offres").DataTable();\n')
        f.write('});\n')
        f.write('</script>\n')
        f.write('</head>\n<body>\n')
        f.write(df.to_html(index=False, render_links=True, classes='sortable" id="offres'))
        f.write('</body>\n</html>')
    print(f"HTML file '{filename}' created successfully.")

def main():
    parser = argparse.ArgumentParser(description="Script to retrieve offers from an API and save them to a CSV or HTML file.")
    parser.add_argument("total_offers", type=int, help="Total number of offers to retrieve")
    parser.add_argument("output_file", type=str, help="Output file name (with extension)")
    args = parser.parse_args()

    total_offers = args.total_offers
    output_file = args.output_file

    _, file_extension = os.path.splitext(output_file)
    output_format = file_extension[1:].lower()

    offers = fetch_all_offers(total_offers)

    if not offers:
        print("No offers retrieved.")
        return

    offers_data = []

    for offer in offers:
        specializations = offer.get('specializations', [])
        date_string = offer['missionStartDate']
        date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
        formatted_date = date_object.strftime("%d/%m/%Y")
        offer_data = {
            'Lien': f'https://mon-vie-via.businessfrance.fr/offres/{offer["id"]}',
            'Nom de l\'organisation': offer['organizationName'],
            'Titre de la mission': offer['missionTitle'],
            'Type de mission': offer['missionType'],
            'Pays de l\'offre': offer['countryName'],
            'Secteur d\'activité': offer['activitySectorN1'],
            'Spécialisations': ', '.join([spec['specializationLabel'] for spec in specializations if spec and spec['specializationLabel']]) if specializations else '',
            'Date de début de la mission': formatted_date,
            'Durée de la mission': offer['missionDuration'],
            'Nombre de vues': offer['viewCounter'],
            'Nombre de candidats': offer['candidateCounter'],
        }
        offers_data.append(offer_data)

    if output_format == "csv":
        save_to_csv(offers_data, output_file)
    elif output_format == "html":
        save_to_html(offers_data, output_file)
    else:
        print("Invalid file format. Please provide a CSV or HTML file.")

    try:
        if output_format == "html":
            os.startfile(output_file)
        elif output_format == "csv":
            subprocess.Popen(['start', output_file], shell=True)
    except AttributeError:
        print(f"Unable to open the file {output_file}. Please open it manually.")


if __name__ == "__main__":
    main()
