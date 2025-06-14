
# Code Evaluation Assistant (Flask + OpenRouter AI)

This is a simple Flask web app I built that uses OpenRouter's free LLMs to evaluate and compare two student code submissions (in Java or Python) based on detailed criteria.

The app is meant to simulate what a senior developer or educator would do when grading or giving feedback. You enter the original programming question, both students' code (plus their written explanations), and the app uses an AI model to judge their work and pick the better response.

## 🧠 How It Works

- I use `deepseek-chat-v3-0324:free` from OpenRouter, which is one of the best free models for code reasoning.
- The system prompt defines a strict evaluation process based on 5 weighted criteria:
  1. Code Correctness (40%)
  2. Relevance and Precision (25%)
  3. Code Clarity and Structure (20%)
  4. Use of Java and Python Practices (10%)
  5. Explanation and Justification (5%)

It then gives a final decision like:  
*Assistant A is better*, *Assistant B is better*, *It's a tie*, or *Both are incorrect*.  
And it ends with just one sentence explaining the outcome in a casual, student-like tone.

## 🔧 Tech Stack

- Python 3
- Flask
- OpenRouter API
- HTML + basic form templates
- `.env` file for secure API key handling

## 🚀 How to Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
````

2. **Set up a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install flask python-dotenv requests
   ```

4. **Create a `.env` file** in the root folder and add your OpenRouter API key:

   ```
   OPENROUTER_API_KEY=your_key_here
   ```

5. **Run the app**

   ```bash
   python app.py
   ```

6. **Open your browser and go to**

   ```
   http://localhost:5000
   ```

## 📝 Example Use

Just type in your prompt (the assignment question), paste both students' answers (code + explanation), and hit submit. The AI will evaluate both and give you a structured comparison + final judgment.

## 🌐 Notes

* This project is mostly for learning and experimenting with LLMs in real-world grading scenarios.
* Be sure to respect OpenRouter's free usage limits.
* You can change the model or temperature settings in `app.py` if you want different results.

## 📚 Future Ideas

* Add a login system and history of evaluations
* Support more languages or rubric customization
* Let users upload files instead of pasting code

---

### Feedback Welcome

If you're into AI + education or just love tinkering with LLMs and Flask, feel free to fork this or open an issue. Always down to improve or learn from others.

```