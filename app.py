# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

# Copyright 2025 emanoyhl and emanoyhl.net find me at github.com/emanoyhl 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Sample questions
questions = [
    {
        "question": "What is the best way to create a strong password?",
        "options": [
            "Use a combination of letters, numbers, and symbols",
            "Use your name and birthdate",
            "Use the same password for all accounts"
        ],
        "answer": 0
    },
    {
        "question": "What should you do if you receive an email from an unknown sender?",
        "options": [
            "Delete the email without opening it",
            "Open the email and click on all links",
            "Reply to the email to ask for more information"
        ],
        "answer": 0
    },
    {
        "question": "Why is it important to update your software regularly?",
        "options": [
            "To fix security vulnerabilities and bugs",
            "To make your device look new",
            "It is not important"
        ],
        "answer": 0
    },
    {
        "question": "What is phishing?",
        "options": [
            "A method to catch fish",
            "A fraudulent attempt to obtain sensitive information",
            "A type of computer virus"
        ],
        "answer": 1
    },
    {
        "question": "What should you do if you suspect your account has been compromised?",
        "options": [
            "Change your password immediately",
            "Ignore it",
            "Assume it's not a big deal"
        ],
        "answer": 0
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

@app.route('/api/submit', methods=['POST'])
def submit_answers():
    data = request.json
    score = sum(1 for i, answer in enumerate(data['answers']) if answer == questions[i]['answer'])
    return jsonify({"score": score})

if __name__ == '__main__':
    app.run(debug=True)