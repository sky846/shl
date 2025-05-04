# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    role = data['role']
    skills = data['skills'].split(',')

    # Dummy logic – you can replace with real recommendation rules
    recommendations = []
    if role.lower() == "software developer":
        if "Python" in skills:
            recommendations.append("Take SHL Python Developer Assessment")
        if "C++" in skills:
            recommendations.append("Take SHL C++ Developer Assessment")
        if not recommendations:
            recommendations.append("Try SHL Cognitive Ability Test")

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=False)
