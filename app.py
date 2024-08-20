from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from sudoku_solver import solve_sudoku, is_valid  # Ensure these functions are correctly implemented

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    grid = request.json['grid']
    if solve_sudoku(grid):
        return jsonify(grid)
    else:
        return jsonify({'error': 'No solution exists'})

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    sudoku_grid = extract_sudoku_from_image(image)
    return jsonify(sudoku_grid)

def extract_sudoku_from_image(image):
    # This function needs to be implemented to use OpenCV and pytesseract
    # For simplicity, we return a dummy grid here
    return [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]

if __name__ == '__main__':
    app.run(debug=True)
