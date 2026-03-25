import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from text_analyzer import TextAnalyzer
from visualizer import Visualizer

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define commands

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Use /analyze, /frequency, /wordcloud, or /stats to analyze your text.')

def analyze(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    analyzer = TextAnalyzer(text)
    result = analyzer.analyze()
    update.message.reply_text(result)


def frequency(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    analyzer = TextAnalyzer(text)
    result = analyzer.get_frequency()  # assuming this returns a string
    update.message.reply_text(result)


def wordcloud(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    visualizer = Visualizer(text)
    image_url = visualizer.create_wordcloud()  # assuming this returns the URL of the image
    update.message.reply_text(f'Wordcloud generated: {image_url}')


def stats(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)
    analyzer = TextAnalyzer(text)
    stats = analyzer.get_stats()  # assuming this returns a string
    update.message.reply_text(stats)


def main() -> None:
    updater = Updater("YOUR_TOKEN")  # Replace 'YOUR_TOKEN' with the actual token
    dp = updater.dispatcher
    
    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("analyze", analyze))
    dp.add_handler(CommandHandler("frequency", frequency))
    dp.add_handler(CommandHandler("wordcloud", wordcloud))
    dp.add_handler(CommandHandler("stats", stats))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()