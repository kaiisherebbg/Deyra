# 📓 mood_journal.py — Mood Tracker Terminal App 💻🧠
import json
from datetime import datetime
import os
import time
import matplotlib.pyplot as plt

# 📁 Data and Suggestions
DATA_FILE = "mood_data.json"
SUGGESTED_TAGS = ["school", "friends", "family", "health", "work", "coding", "tired", "excited", "happy", "sad"]
MOOD_ICONS = {1: "😞", 2: "😕", 3: "😐", 4: "🙂", 5: "😄"}

# 🔄 Load existing mood data or start fresh
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# 💾 Save mood data
def save_data(data):
    print("💾 Saving", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print(" ✅ Done!")

# 📝 Log a new mood
def log_mood():
    print("\n📝 --- Log Your Mood ---")
    mood = int(input("😌 Mood rating (1-5): "))

    print("🏷️ Suggested tags:", ", ".join(SUGGESTED_TAGS))
    tags = input("🔖 Tags (comma-separated): ")
    note = input("🗒️ Note: ")

    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "mood": mood,
        "tags": [tag.strip() for tag in tags.split(",")],
        "note": note
    }
    data = load_data()
    data.append(entry)
    save_data(data)
    print("✅ Mood logged successfully!")

# 📚 View all mood logs
def view_logs():
    print("\n📖 --- Mood Logs ---")
    data = load_data()
    for entry in data:
        icon = MOOD_ICONS.get(entry['mood'], "❓")
        print(f"🕒 [{entry['timestamp']}] {icon} Mood: {entry['mood']} 🏷️ Tags: {', '.join(entry['tags'])}")
        print(f"🗒️ Note: {entry['note']}\n")

# 📈 Plot mood over time
def plot_mood_graph():
    data = load_data()
    if not data:
        print("❌ No data to plot.")
        return

    dates = [datetime.strptime(entry['timestamp'], "%Y-%m-%d %H:%M") for entry in data]
    moods = [entry['mood'] for entry in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, moods, marker='o', linestyle='-', color='blue')
    plt.title("📊 Mood Over Time")
    plt.xlabel("📅 Date")
    plt.ylabel("💬 Mood (1 = 😞 ... 5 = 😄)")
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

# 🚪 Main menu loop
def main():
    while True:
        print("\n📓 Mood Journal — Track your feelings 💖")
        print("1️⃣ Log Mood")
        print("2️⃣ View Logs")
        print("3️⃣ View Mood Graph")
        print("4️⃣ Exit")
        choice = input("👉 Choose an option: ")

        if choice == '1':
            log_mood()
        elif choice == '2':
            view_logs()
        elif choice == '3':
            plot_mood_graph()
        elif choice == '4':
            print("👋 Goodbye! Take care 💫")
            break
        else:
            print("❌ Invalid choice. Try again!")

# ▶️ Run the app
if __name__ == "__main__":
    main()
