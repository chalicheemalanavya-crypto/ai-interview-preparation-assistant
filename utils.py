import random
from questions import questions

def get_questions(topic):
    topic = topic.lower()
    if topic in questions:
        return random.sample(questions[topic], len(questions[topic]))
    else:
        return ["No questions found for this topic"]

def evaluate_answer(answer):
    if len(answer.split()) < 5:
        return "❌ Weak Answer"
    elif len(answer.split()) < 15:
        return "⚠️ Medium Answer"
    else:
        return "✅ Strong Answer"