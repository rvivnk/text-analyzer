import nltk
from collections import Counter
import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords
from wordcloud import WordCloud

nltk.download('stopwords')

def analyze(text):
    letters_count = sum(c.isalpha() for c in text)
    sentences = [s.strip() for s in text.replace('!', '.').replace('?', '.').split('.') if s.strip()]
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    words = [word for word in words if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    num_words = len(words)
    num_sentences = len(sentences)
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(10)
    return letters_count, num_words, num_sentences, most_common_words, words

def plot_word_frequency(most_common_words):
    if not most_common_words:
        print("Немає слів для побудови графіка.")
        return
    words_plot, counts_plot = zip(*most_common_words)
    plt.figure(figsize=(10, 5))
    plt.bar(words_plot, counts_plot, color='skyblue')
    plt.title('Найчастіше вживані слова')
    plt.xlabel('Слова')
    plt.ylabel('Частота')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

def plot_word_cloud(words):
    if not words:
        print("Немає слів для побудови хмари слів.")
        return
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Хмара слів')
    plt.show()
