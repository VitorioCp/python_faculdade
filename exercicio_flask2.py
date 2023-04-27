from flask import Flask
app = Flask (__name__)

@app.route('/')
def cumprimento():
    boas_vindas = '<h1>Ola, programadores!</h1>'
    instr = '<p>Entre dois numero</p>'
    return boas_vindas + instr

@app.route('/somar/')
@app.route('/somar/<num01>/<num02>')
def soma(num01 = 0, num02 = 0):
    resultado = float(num01)+float(num02)
    return str*(resultado)

if __name__ == '__main__':
    app.run(debug=True)