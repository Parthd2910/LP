# Simple Customer Support Chatbot

def chatbot():
    print("Welcome to ShopSmart Assistant! How can I help you today?")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I assist you today?")
        elif "product" in user_input or "available" in user_input:
            print("Bot: You can check product availability on our website's product page.")
        elif "return" in user_input:
            print("Bot: Our return policy allows returns within 30 days of delivery. Please keep the receipt.")
        elif "delivery" in user_input:
            print("Bot: Delivery usually takes 3-5 business days. You can track your order online.")
        elif "contact" in user_input or "support" in user_input:
            print("Bot: You can contact our support at support@shopsmart.com or call 1800-123-456.")
        elif "exit" in user_input or "bye" in user_input:
            print("Bot: Thank you for visiting ShopSmart. Have a great day!")
            break
        else:
            print("Bot: I'm sorry, I didn't understand that. Please ask another question.")

chatbot()
