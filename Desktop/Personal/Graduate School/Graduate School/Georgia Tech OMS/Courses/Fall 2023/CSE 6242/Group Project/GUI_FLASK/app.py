from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_address = request.form.get('user_address')
    user_max_radius = request.form.get('user_max_radius')
    user_gas_needed = request.form.get('user_gas_needed')
    user_fuel_economy = request.form.get('user_fuel_economy')
    user_gas_type = request.form.get('user_gas_type')

    return f"Submitted! User Address: {user_address}, User Max Distance: {user_max_radius}, User Gas Needed: {user_gas_needed}, User Fuel Economy: {user_fuel_economy}, User Gas Type: {user_gas_type}"

if __name__ == '__main__':
    app.run(debug=True)