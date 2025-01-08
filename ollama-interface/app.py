from flask import Flask, request, jsonify, render_template, Response
import requests
import json
import markdown
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr),
        logging.FileHandler('app.log')
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def stream_response(prompt):
    try:
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "model": "qwen2.5-coder",
            "prompt": prompt,
            "stream": True
        }
        
        response = requests.post(OLLAMA_API_URL, json=data, headers=headers, stream=True)
        
        if response.status_code != 200:
            logger.error(f"Ollama API error: {response.status_code} - {response.text}")
            yield f"Error: Failed to get response from Ollama API (Status code: {response.status_code})"
            return
        
        for line in response.iter_lines():
            if line:
                try:
                    json_response = json.loads(line)
                    if 'response' in json_response:
                        yield json_response['response']
                except json.JSONDecodeError as e:
                    logger.error(f"JSON decode error: {e}")
                    yield "Error: Failed to parse response from Ollama"
                    
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error: {e}")
        yield f"Error: Failed to connect to Ollama API: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        yield f"Error: An unexpected error occurred: {str(e)}"

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering template: {e}")
        return "Error: Failed to load the page", 500

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        if not data:
            logger.error("No JSON data received")
            return "Error: No input data provided", 400
            
        prompt = data.get('prompt', '')
        if not prompt:
            logger.error("No prompt provided")
            return "Error: No prompt provided", 400
        
        return Response(stream_response(prompt), mimetype='text/event-stream')
    except Exception as e:
        logger.error(f"Error in generate endpoint: {e}")
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
