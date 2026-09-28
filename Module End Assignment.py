feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        '  Very GOOD Sevice!!!',
        'poor support,   not happy',
        'GREAT experience! will come again.',
        'okay   okay...',
        'not   BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

n = int(input("How many more feedbacks do you want to add?"))
for i in range(n):
    name = input("Enter name:")
    feedback = input("Enter feedback:")
    rating = int(input("Enter rating(1-5):"))
    feedback_data['S_No'].append(len(feedback_data['S_No'])+ 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

for i in range(len(feedback_data['Feedback'])):
    text = feedback_data['Feedback'][i]
    text = text.replace('.','')
    text = text.replace(',','')
    text = text.replace('!','')
    text = text.replace('?','')
    text = ' '.join(text.split())
    text = text.lower()
    feedback_data['Feedback'][i]=text
    
def count_word_in_feedbacks(word):
    count = 0
    for feedback in feedback_data['Feedback']:
        if word.lower() in feedback.split():
            count = count + 1
        return count
    print("\nWord Count")
    print("Number of feedbacks containing 'good':", count_word_in_feedbacks('good'))
    print("Number of feedbacks containing 'poor':", count_word_in_feedbacks('poor'))
    print("Number of feedbacks containing 'excellent':", count_word_in_feedbacks('excellent'))

    print("\nFinal Cleaned Feedback Data:")
    print(feedback_data)

    total_rating = 0
    for rating in feedback_data['Rating']:
        total_rating = total_rating + rating
        average_rating = total_rating / len(feedback_data['Rating'])
        print("\nAverage Rating:",round(average_rating,2))
        
longest_feedback = ""
longest_word_count = 0
for feedback in feedback_data['Feedback']:
    word_count = len(feedback.split())
    if word_count > longest_word_count:
        longest_word_count = word_count
        longest_feedback = feedback
print("\nLongest Feedback")
print(longest_feedback)
print("Number of words:",longest_word_count)

unique_words = set()
for feedback in feedback_data['Feedback']:
    words = feedback.split()
    for word in words:
        unique_words.add(word)
print("\nUnique Words:")
print(unique_words)

