import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pandas as pd

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_frequency_distribution(self, column):
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.data, x=column)
        plt.title(f'Frequency Distribution of {column}')
        plt.xticks(rotation=45)
        plt.show()

    def plot_word_cloud(self, column):
        text = ' '.join(self.data[column].dropna().astype(str).tolist())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud')
        plt.show()

    def text_statistics(self, column):
        text = ' '.join(self.data[column].dropna().astype(str).tolist())
        num_words = len(text.split())
        num_unique_words = len(set(text.split()))
        print(f'Total Words: {num_words}')
        print(f'Unique Words: {num_unique_words}')
        return {'Total Words': num_words, 'Unique Words': num_unique_words}

# Example usage:
# df = pd.DataFrame({'text_column': ['text 1', 'text 2', 'text 3']})
# visualizer = DataVisualizer(df)
# visualizer.plot_frequency_distribution('text_column')
# visualizer.plot_word_cloud('text_column')
# visualizer.text_statistics('text_column')
