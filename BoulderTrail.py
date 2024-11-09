from flask import Flask, jsonify, request, render_template
import pandas as pd

app = Flask(__name__)

# Read data from CSV file
data = pd.read_csv('BoulderTrailHeads.csv')

# Render the results through htmk
@app.route('/')
def index():
    return render_template('index.html')

# Return returns based on filter selection (BikeTrail or Fishing)
@app.route('/filter', methods=['GET'])
def filter_data():
    bike_trail = request.args.get('BikeTrail')
    fishing = request.args.get('FISHING')
    
    if bike_trail not in ['Yes', 'No'] and fishing not in ['Yes', 'No']:
        return jsonify({"error": "Invalid filter value. Use 'Yes' or 'No' for both BikeTrail and FISHING"}), 400
    
    filtered_data = data[(data['BikeTrail'] == bike_trail) & (data['FISHING'] == fishing)]
    
    return jsonify(filtered_data.to_dict(orient='records'))

# run app on local machine
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
	