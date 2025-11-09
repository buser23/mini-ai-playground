#!/usr/bin/env python3
import datetime

def ai_playground():
    print("🧠 Mini AI Prompt Playground")
    print("-----------------------------")
    print("Type a prompt or question (type 'exit' to quit).")
    print()
    
    history = []

    while True:
        user_input = input(">>> ")
        if user_input.lower().strip() == "exit":
            break

        # Guarda o prompt e a hora
        history.append((datetime.datetime.now().strftime("%H:%M:%S"), user_input))
        print(f"🤔 Prompt saved at {history[-1][0]}: '{user_input}'")
        print("✨ (Imagine the AI replying with something brilliant...)\n")

    print("\n🧾 Session Summary:")
    for time, prompt in history:
        print(f"[{time}] {prompt}")
    print("\nGoodbye! 👋")

if __name__ == "__main__":
    ai_playground()
