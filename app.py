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
fasen = ['Alle fases', 'A1-A3: Productie', 'A1 - Productie: Winning grondstoffen', 'A2 - Productie: Transport', 'A3 - Productie: Productie', 'A4 - Bouw: Transport', 'A5 - Bouw: Bouw en installatie', 'B1 - Gebruik: Gebruik', 'B2 - Gebruik: Onderhoud', 'B3 - Gebruik: Reparaties', 'B4 - Gebruik: Vervangingen', 'B5 - Gebruik: Hernieuwing', 'B6 - Gebruik: Energie', 'B7 - Gebruik: Water', 'C1 - Sloop en verwerking: Sloop', 'C2 - Sloop en verwerking: Transport', 'C3 - Sloop en verwerking: Afvalbewerking', 'C4 - Sloop en verwerking: Finale afvalbewerking', 'D - Hergebruik en externe milieubaten -en lasten']
effecten = ['MKI volledig', 'MKI: CO2 - Klimaatverandering', 'MKI: SO2 - Verzuring', 'MKI: PO4 - Vermesting', 'MKI: CFK-11 - Ozonlaagaantasting', 'MKI: C2H4 - Ethyleen smog', 'MKI: Uitputting brandstoffen', 'MKI: Uitputting natuurlijke hulpbronnen', 'MKI: Giftige stoffen zoetwater', 'MKI: Giftige stoffen zoutwater', 'MKI: Giftige stoffen vaste land', 'MKI: Giftige stoffen mensen', 'NOx - Stikstof']

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
    selected_effects = []
    for key, value in data.items():
        fase, effect = key.split('|')
        fase = fase.strip()
        effect = effect.strip()
        if effect not in selected_effects:
            selected_effects.append(effect)
        if fase not in results:
            results[fase] = {}
        results[fase][effect] = value
    return render_template('results.html', results=results, selected_effects=selected_effects)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
