from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the fases and effects lists
fasen = ['Alle fases', 'A1 - Productie: Winning grondstoffen', 'A2 - Productie: Transport', 'A3 - Productie: Productie', 'A4 - Bouw: Transport', 'A5 - Bouw: Bouw en installatie', 'B1 - Gebruik: Gebruik', 'B2 - Gebruik: Onderhoud', 'B3 - Gebruik: Reparaties', 'B4 - Gebruik: Vervangingen', 'B5 - Gebruik: Hernieuwing', 'B6 - Gebruik: Energie', 'B7 - Gebruik: Water', 'C1 - Sloop en verwerking: Sloop', 'C2 - Sloop en verwerking: Transport', 'C3 - Sloop en verwerking: Afvalbewerking', 'C4 - Sloop en verwerking: Finale afvalbewerking', 'D - Hergebruik en externe milieubaten -en lasten']
effecten = ['Alle effecten', 'CO2 - Klimaatverandering', 'SO2 - Verzuring', 'PO4 - Vermesting', 'CFK-11 - Ozonlaagaantasting', 'C2H4 - Ethyleen smog', 'Uitputting brandstoffen', 'Uitputting natuurlijke hulpbronnen', 'Giftige stoffen zoetwater', 'Giftige stoffen zoutwater', 'Giftige stoffen vaste land', 'Giftige stoffen mensen']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_fases = request.form.getlist('fasen')
        selected_effects = request.form.getlist('effecten')
        return render_template('form.html', selected_fases=selected_fases, selected_effects=selected_effects)
    return render_template('index.html', fases=fasen, effects=effecten)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
