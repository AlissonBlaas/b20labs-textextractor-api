from flask import Flask, request, jsonify
from flask_cors import CORS
from text_extractor import PyMuPDFTextExtractor
from text_generator import OpenAITextGenerator
from text_processing import TextProcessingService
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/extract-text', methods=['POST'])
def extract_and_generate_text():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    file_data = file.read()


    text_extractor = PyMuPDFTextExtractor()
    text_generator = OpenAITextGenerator(api_key=os.environ['OPENAI_API_KEY'])

    text_processor = TextProcessingService(text_extractor, text_generator)
    result = text_processor.process_text(file_data)

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=443, debug=True)