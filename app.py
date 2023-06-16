from flask import Flask, render_template, request, redirect, url_for

# Function definition should be placed before using it
def format_number(value):
    try:
        # Convert to float
        number = float(value.replace(',', '.'))
        
        # Format with comma as decimal separator and period as thousand separator
        formatted = '{:,.2f}'.format(number).replace(',',' ').replace('.',',').replace(' ','.')
        
    except ValueError:
        formatted = value
        
    return formatted

app = Flask(__name__)
# Now that the function is defined, you can assign it as a custom filter
app.jinja_env.filters['format_number'] = format_number

# Define the fases and effects lists
fasen = ['Alle fases', 'A1 - Productie: Winning grondstoffen', 'A2 - Productie: Transport', 'A3 - Productie: Productie', 'A4 - Bouw: Transport', 'A5 - Bouw: Bouw en installatie', 'B1 - Gebruik: Gebruik', 'B2 - Gebruik: Onderhoud', 'B3 - Gebruik: Reparaties', 'B4 - Gebruik: Vervangingen', 'B5 - Gebruik: Hernieuwing', 'B6 - Gebruik: Energie', 'B7 - Gebruik: Water', 'C1 - Sloop en verwerking: Sloop', 'C2 - Sloop en verwerking: Transport', 'C3 - Sloop en verwerking: Afvalbewerking', 'C4 - Sloop en verwerking: Finale afvalbewerking', 'D - Hergebruik en externe milieubaten -en lasten']
effecten = ['Alle effecten', 'NOx - Stikstof', 'CO2 - Klimaatverandering', 'SO2 - Verzuring', 'PO4 - Vermesting', 'CFK-11 - Ozonlaagaantasting', 'C2H4 - Ethyleen smog', 'Uitputting brandstoffen', 'Uitputting natuurlijke hulpbronnen', 'Giftige stoffen zoetwater', 'Giftige stoffen zoutwater', 'Giftige stoffen vaste land', 'Giftige stoffen mensen']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_fases = request.form.getlist('fasen')
        selected_effects = request.form.getlist('effecten')
        return render_template('form.html', selected_fases=selected_fases, selected_effects=selected_effects)
    return render_template('index.html', fases=fasen, effects=effecten)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    results = {}
    selected_effects = set()
    for key, value in data.items():
        fase, effect = key.split('|')
        fase = fase.strip()
        effect = effect.strip()
        selected_effects.add(effect)
        if fase not in results:
            results[fase] = {}
        results[fase][effect] = value
    return render_template('results.html', results=results, selected_effects=selected_effects)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
