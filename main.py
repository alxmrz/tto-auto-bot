import time
from pynput import keyboard

from src.bot import Bot
from src.brain import EasyBrain
from src.config import Config
from src.eyes import Eyes
from src.hands import Hands
from src.logger import Logger


def on_press(key):
    global running
    if key == keyboard.Key.esc:
        logger.info("EXIT")
        running = False


logger = Logger(enable=True)
bot = Bot(EasyBrain(logger), Eyes(Config(), logger), Hands(), logger)

listener = keyboard.Listener(on_press=on_press)
listener.start()

running = True

while running:
    bot.run()
    time.sleep(1)
