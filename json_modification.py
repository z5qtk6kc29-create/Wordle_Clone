from datetime import datetime, timedelta
import json
import os

def cleanup_data():
    global most_recent_words

    three_months_ago = datetime.now() - timedelta(days=90)

    if os.path.exists('recent_words.json'):
            with open('recent_words.json', 'r') as file:
                data = json.load(file)
            
            filtered_data = {
                word: date_str for word, date_str in data.items()
                if datetime.strptime(date_str, '%Y-%m-%d') > three_months_ago
            }

            with open('recent_words.json', 'w') as file:
                json.dump(filtered_data, file, indent=4)
                
            return filtered_data
    return {}

def track_word(computer_choice):
    most_recent_words["".join(computer_choice)] = datetime.now().strftime("%Y-%m-%d")
    with open('recent_words.json', 'w') as file:
        json.dump(most_recent_words, file, indent=4)
    return most_recent_words

#Here is where it will load existing data to file, or start with empty d
if os.path.exists('recent_words.json'):
    with open('recent_words.json', 'r') as file:
        most_recent_words = json.load(file)
else:
    most_recent_words = {}