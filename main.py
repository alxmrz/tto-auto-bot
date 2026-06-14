import time

import mss
from pynput import keyboard

from src.bot import Bot
from src.brain import EasyBrain
from src.config import Config
from src.eyes import Eyes
from src.hands import Hands
from src.image import Image
from src.logger import Logger


logger = Logger(enable=True)
config = Config()
running = True


def on_press(key):
    global running
    if key == keyboard.Key.esc:
        logger.info("EXIT")
        running = False


sct = mss.MSS()

try:
    image = Image(sct, config.threshold)
    bot = Bot(EasyBrain(logger), Eyes(config, image, logger), Hands(logger), logger)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while running:
        bot.run()
        time.sleep(1)
finally:
    sct.close()
