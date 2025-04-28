from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    expression = ''
    result = ''
    if request.method == 'POST':
        expression = request.form.get("expression", "")
        try:
            result = eval(expression)  # Obliczanie wyniku
        except Exception:
            result = 'Błąd'  # Obsługa błędów
    return render_template('index.html', expression=expression, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)