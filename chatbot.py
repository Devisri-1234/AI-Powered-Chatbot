from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "hello",
    "hi",
    "hey",
    "how are you",
    "what is your name",
    "who are you",
    "what can you do",
    "python",
    "i have doubt in python",
    "machine learning",
    "artificial intelligence",
    "contact support",
    "how can i contact support",
    "thank you",
    "thanks",
    "bye"
    "hello",
    "hi",
    "what is your name",
    "who are you",
    "what courses do you offer",
    "how can i contact support",
    "bye",
    "string is mutable or immutable",
]

answers = [
    "Hello! How can I help you?",
    "Hi there!",
    "Hey! Nice to meet you.",
    "I am doing great. How can I help you today?",
    "My name is AI Chatbot.",
    "I am an AI-powered virtual assistant.",
    "I can answer questions related to Python, AI, ML and programming.",
    "Python is a popular programming language used in web development, AI and data science.",
    "Sure! Tell me your Python doubt and I will try to help.",
    "Machine Learning is a branch of AI that enables systems to learn from data.",
    "Artificial Intelligence is the simulation of human intelligence in machines.",
    "You can contact support at support@example.com.",
    "You can contact our support team at support@example.com.",
    "You're welcome!",
    "Glad to help!",
    "Goodbye! Have a great day."
    "Hello! How can I help you?",
    "Hi there!",
    "I am an AI Chatbot.",
    "I am a virtual assistant.",
    "We offer Python, AI, ML and Data Science courses.",
    "Contact us at support@example.com",
    "Goodbye!",
    "immutable",

]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(user_input):

    user_input = user_input.lower()

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, X)

    index = similarity.argmax()

    score = similarity[0][index]

    if score < 0.4:
        return "Sorry, I don't understand. Please ask about Python, AI, ML or programming."

    return answers[index]