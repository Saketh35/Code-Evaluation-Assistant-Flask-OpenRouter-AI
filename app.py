from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Load API key from environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Ensure API key exists
if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY is not set in environment variables.")

# Your full system prompt
SYSTEM_PROMPT = """
You are a senior Java and Python developer and educator with over 10 years of experience in software development and teaching programming. You have assigned a programming task to two students, Assistant A and Assistant B. Both students have submitted their Java and Python code solutions along with written explanations for the same task.

Your job is to **critically evaluate and compare their submissions** using the following weighted criteria:

1. Code Correctness (40%) – Judge whether the code meets the task requirements and works correctly in normal and edge cases
2. Relevance and Precision (25%) – Evaluate how focused, concise, and directly aligned the solution is to the problem
3. Code Clarity and Structure (20%) – Review how clean, well-organized, and readable the code is
4. Use of Java and Python Practices (10%) – Assess the use of appropriate language-specific features and conventions
5. Explanation and Justification (5%) – Determine how clearly the student explains their code and decisions

Your assessment must emphasize **Code Correctness** and **Relevance and Precision**, using the other criteria to support your final judgment.

After evaluating both students, provide:

* A clear, structured analysis of each submission using the criteria above
* A fair and unbiased final decision by selecting exactly one of the following four options, treating them equally:

  * Assistant A's answer is better
  * Assistant B's answer is better
  * It's a tie
  * Both are incorrect

Conclude with **only one sentence** in plain text that explains **why** the chosen response is better or how you reached that outcome, using a **natural student-like tone**.

Rules:

* Do not use dashes, semicolons, bold text, or emojis anywhere in the response
* Do not write a paragraph to conclude
* Only give **one** sentence at the end as your final justification
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        assistant_a = request.form.get('assistant_a', '')
        assistant_b = request.form.get('assistant_b', '')

        if not prompt or not assistant_a or not assistant_b:
            error = "Please fill in all fields."
        else:
            user_message = f"""
Question: {prompt}

Assistant A:
{assistant_a}

Assistant B:
{assistant_b}

Please compare both answers as per the rules and give your final judgment.
"""

            try:
                response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "http://localhost:5000"  # Adjust for production
                    },
                    json={
                        "model": "deepseek/deepseek-chat-v3-0324:free",
                        "messages": [
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": user_message}
                        ],
                        "temperature": 0.6
                    }
                )

                if response.status_code == 200:
                    result = response.json()["choices"][0]["message"]["content"]
                else:
                    error = f"API Error {response.status_code}: {response.text}"

            except Exception as e:
                error = f"Request failed: {str(e)}"

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
