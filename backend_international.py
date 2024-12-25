from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/costs/<program>', methods=['GET'])
def get_costs(program):
    data = {
        "medical": {
            "tuition_fee": "AUD 70,000 per year",
            "duration": "6 years",
            "living_cost": "AUD 20,000 per year"
        },
        "engineering": {
            "tuition_fee": "AUD 50,000 per year",
            "duration": "4 years",
            "living_cost": "AUD 20,000 per year"
        },
        "architecture": {
            "tuition_fee": "AUD 55,000 per year",
            "duration": "5 years",
            "living_cost": "AUD 20,000 per year"
        }
    }
    
    if program in data:
        return jsonify(data[program])
    else:
        return jsonify({"error": "Program not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
