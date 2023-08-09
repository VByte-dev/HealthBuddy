from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#-----------------------------------------------------------------------------------------#

def get_nutrition_info(query):
    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
    api_key = 'si/4UTmmXL6LxBwrV9EHSg==sZHC1HDXmNSGC1sP'

    headers = {'X-Api-Key': api_key}

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()[0]
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the API request:", e)
        return None

def main(query):
    print("Welcome to the Nutrition API!")
    
    q = query
    result = get_nutrition_info(q)
    if result:
        print("Nutrition Information:")
        print(result)
    else:
        print("No nutrition information available.")

    return result
#-----------------------------------------------------------------------------------------#

@app.route('/', methods = ['GET'])
def homePage():
    try:

        query = request.args.get('query')
        if query == '':
            r = {'name': 'Search for Something!', 'calories': '', 'serving_size_g' : '', 'fat_total_g':'', 'fat_saturated_g': '', 'protein_g':'', 'sodium_mg':'', 'potassium_mg':'', 'cholesterol_mg':'', 'carbohydrates_total_g':'', 'fiber_g':'', 'sugar_g':''}
        
        else:
            r = main(query)
        
    except Exception as E:
        r = {'name': 'No Results', 'calories': '', 'serving_size_g' : '', 'fat_total_g':'', 'fat_saturated_g': '', 'protein_g':'', 'sodium_mg':'', 'potassium_mg':'', 'cholesterol_mg':'', 'carbohydrates_total_g':'', 'fiber_g':'', 'sugar_g':''}
        print(f'{E}!')
    return render_template('mainPage.html',name = r['name'].capitalize(), calories = r['calories'], sz = r['serving_size_g'], ft = r['fat_total_g'], fs = r['fat_saturated_g'], protein = r['protein_g'], sm = r['sodium_mg'], pm=r['potassium_mg'], c = r['cholesterol_mg'], ch=r['carbohydrates_total_g'], fiber=r['fiber_g'], sugar=r['sugar_g'] )
    

#-----------------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')