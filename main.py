import random
import time

# Valence Aware Dictionary and sEntiment Reasoner (VADER)
from nltk.sentiment import SentimentIntensityAnalyzer


RESPONSES_TO_A_GOOD_DAY = [
    "That's wonderful to hear! I'm glad you had a good day.",
    "I'm so happy to hear that your day went well!",
    "Sounds like you had an amazing day! Keep up the positive vibes!",
    "I'm thrilled for you! May your good days continue.",
    "Your positive energy is contagious! Keep enjoying those good days.",
    "It's great to see you having a good day. Wishing you many more!",
    "Awesome! Keep cherishing those moments of joy and positivity.",
    "I hope your good days keep on coming! You deserve all the happiness.",
    "That's fantastic news! Sending you more good vibes for the days ahead.",
    "Keep embracing the positivity! Here's to more good days in the future!"
]

RESPONSES_TO_A_BAD_DAY = [
    "I'm sorry you're feeling this way. Remember, challenges make us stronger.",
    "I can imagine how tough that must be. Hang in there, better days are coming.",
    "It's okay to have bad days. Just remember, you're not alone in this journey.",
    "I'm here for you. Don't hesitate to reach out if you need to talk.",
    "Sending you strength and positive vibes to help you through this rough patch.",
    "Tough times don't last, but tough people do. You've got this!",
    "I believe in your ability to overcome this. Take it one step at a time.",
    "Tomorrow is a new day with new opportunities. Keep your head up!",
    "Bad days are just a part of life's journey. Don't lose hope; things will get better.",
    "You're stronger than you think. Remember to take care of yourself and reach out for support."
]


RESPONSES_TO_A_NEUTRAL_DAY = [
    "I appreciate you letting me know. Neutral days can be a chance to relax and recharge.",
    "Thanks for sharing. Every day, regardless of how it feels, is a step forward.",
    "It's okay to have neutral days. They provide a break from the highs and lows.",
    "I hear you. Neutral days can be a good opportunity to reflect and find balance.",
    "I understand. Neutral days can offer a sense of calm and stability.",
    "Thanks for opening up. Neutral days are a natural part of life's rhythm.",
    "I'm here for you no matter what kind of day you're having. Your feelings are valid.",
    "Neutral days are a chance to practice self-care and focus on your well-being.",
    "I'm glad you shared that with me. Remember, every day is a new chance for something positive.",
    "Thanks for being honest. Neutral days can be the foundation for better days ahead."
]



def get_user_input():
    day_sentiment = input("Please, tell me how your day went: ")
    return day_sentiment



def categorize_sentiment(user_input):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(user_input)


    if scores["compound"] > 0.3:
        return "positive"
    
    elif (scores["compound"] <= 0.3 and
          scores["compound"] >= -0.40):
        return "neutral"
    
    else:
        return "negative"


def respond_based_on_sentiment(sentiment_category):
    if sentiment_category == "positive":
        return random.choice(RESPONSES_TO_A_GOOD_DAY)

    if sentiment_category == "neutral":
        return random.choice(RESPONSES_TO_A_NEUTRAL_DAY)
    
    if sentiment_category == "negative":
        return random.choice(RESPONSES_TO_A_BAD_DAY)
    

def main():
    user_input = get_user_input()
    sentiment_category = categorize_sentiment(user_input)
    response = respond_based_on_sentiment(sentiment_category)
    time.sleep(2)
    print("Analysing sentiment, wait for response.")
    time.sleep(4)
    print(response)


if __name__ == "__main__":
    main()