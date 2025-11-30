import random

QUESTIONS = {
    "technical": [
        "Explain the difference between a stack and a queue.",
        "How would you optimize a slow SQL query?",
        "Describe a project where you used APIs."
    ],
    "behavioral": [
        "Tell me about yourself.",
        "Describe a challenge you faced.",
        "Tell me about a time you worked under pressure."
    ],
    "hr": [
        "Why do you want this job?",
        "What are your strengths and weaknesses?",
        "Where do you see yourself in 5 years?"
    ]
}

def generate_question(topic="behavioral", level="medium", resume_summary=None):
    # pick a category that exists
    if topic not in QUESTIONS:
        topic = "behavioral"

    # choose a random question
    question = random.choice(QUESTIONS[topic])

    return {
        "text": question,
        "topic": topic,
        "difficulty": level
    }
