import tkinter as tk
from tkinter import filedialog
import text_analyzer

root = tk.Tk()
root.title("Аналіз Тексту")

text_entry = tk.Text(root, height=15, width=80)
text_entry.pack(padx=10, pady=10)


def analyze_text():
    text = text_entry.get("1.0", tk.END)
    letters_count, num_words, num_sentences, most_common_words, words = text_analyzer.analyze(text)
    result_label.config(
        text=f"Кількість літер: {letters_count}\nКількість слів: {num_words}\nКількість речень: {num_sentences}")

    print(f"Кількість літер: {letters_count}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість речень: {num_sentences}")
    print("\nНайчастіше вживані слова:")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")

    if most_common_words:
        text_analyzer.plot_word_frequency(most_common_words)
    else:
        print("Немає слів для побудови графіка.")

    if words:
        text_analyzer.plot_word_cloud(words)
    else:
        print("Немає слів для побудови хмари слів.")


analyze_button = tk.Button(root, text="Аналізувати текст", command=analyze_text)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="Кількість літер: 0\nКількість слів: 0\nКількість речень: 0", justify="left")
result_label.pack(pady=10)


def load_file():
    file_path = filedialog.askopenfilename(title="Виберіть файл",
                                           filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_entry.delete("1.0", tk.END)
            text_entry.insert(tk.END, text)


load_button = tk.Button(root, text="Завантажити файл", command=load_file)
load_button.pack(pady=10)

root.mainloop()
