from groq import generate_response

def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")

    vague = input("Enter the Vague Prompt:")
    print("\nAI's response to Vague Prompt:")
    print(generate_response(vague))

    specific = input("\nNow make it more Specific:")
    print("\nAI's response for Specific Prompt:")
    print(generate_response(specific))

    context = input("\nNow add Context to your Specific Prompt:")
    print("\nAI's response for Contextual Prompt:")
    print(generate_response(context))

    print("\n--- Reflection ---")
    print("1.How did the AI's response change when the prompt was made more specific?")
    print("2.How did the AI's response improve with the added context?")
    print("3.Which prompt produced the most relevant and tailored response? Why?")

if __name__ == "__main__":
    prompt_engineering_activity()