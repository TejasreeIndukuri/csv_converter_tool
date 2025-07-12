from flask import Flask, request, jsonify, send_file
import os
from converters import csv_to_tsv, csv_to_excel, csv_to_json, json_to_csv

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    operation = request.form['operation']
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    output_file = os.path.join(UPLOAD_FOLDER, f"converted_{file.filename}")

    try:
        if operation == 'csv_to_tsv':
            csv_to_tsv.convert(filename, output_file)
        elif operation == 'csv_to_excel':
            csv_to_excel.convert(filename, output_file)
        elif operation == 'csv_to_json':
            csv_to_json.convert(filename, output_file)
        elif operation == 'json_to_csv':
            json_to_csv.convert(filename, output_file)
        else:
            return jsonify({'error': 'Unsupported operation'}), 400
        return send_file(output_file, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
