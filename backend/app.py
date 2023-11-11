from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/mbti-result', methods=['POST'])
def mbti_result():
    data = request.json
    mbti_type, index, color = calculate_mbti_type(data)
    return jsonify({'type': mbti_type, 'index': index, 'color': color})

def calculate_mbti_type(scores):
    a, b, c, d = scores['a'], scores['b'], scores['c'], scores['d']

    if a > 0 and b > 0 and c > 0 and d > 0:
        return "ENFP", "6", "#1ABC9C"
    elif a > 0 and b > 0 and c > 0 and d < 0:
        return "ENFJ", "4", "#F1C40F"
    elif a > 0 and b > 0 and c < 0 and d > 0:
        return "ENTP", "1", "#FF6F00"
    elif a > 0 and b > 0 and c < 0 and d < 0:
        return "ENTJ", "3", "#C0392B"
    elif a > 0 and b < 0 and c > 0 and d > 0:
        return "ESFP", "12", "#FFC0CB"
    elif a > 0 and b < 0 and c > 0 and d < 0:
        return "ESFJ", "14", "#F39C12"
    elif a > 0 and b < 0 and c < 0 and d > 0:
        return "ESTP", "8", "#8E44AD"
    elif a > 0 and b < 0 and c < 0 and d < 0:
        return "ESTJ", "10", "#2C3E50"
    elif a < 0 and b > 0 and c > 0 and d > 0:
        return "INFP", "5", "#9B59B6"
    elif a < 0 and b > 0 and c > 0 and d < 0:
        return "INFJ", "0", "#0B3D91"
    elif a < 0 and b > 0 and c < 0 and d > 0:
        return "INTP", "7", "#7FBC8D"
    elif a < 0 and b > 0 and c < 0 and d < 0:
        return "INTJ", "2", "#333333"
    elif a < 0 and b < 0 and c > 0 and d > 0:
        return "ISFP", "9", "#8E44AD"
    elif a < 0 and b < 0 and c > 0 and d < 0:
        return "ISFJ", "13", "#16A085"
    elif a < 0 and b < 0 and c < 0 and d > 0:
        return "ISTP", "15", "#2980B9"
    elif a < 0 and b < 0 and c < 0 and d < 0:
        return "ISTJ", "11", "#34495E"
    else:
        return "Unknown", "N/A", "#000000"


if __name__ == '__main__':
    app.run(debug=True)
