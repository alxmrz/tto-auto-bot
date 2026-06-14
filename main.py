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


def on_press(key):
    global running
    if key == keyboard.Key.esc:
        logger.info("EXIT")
        running = False


logger = Logger(enable=True)
config = Config()
sct = mss.MSS()

try:
    image = Image(sct)
    bot = Bot(EasyBrain(logger), Eyes(config, image, logger), Hands(), logger)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    running = True

    while running:
        bot.run()
        time.sleep(1)
finally:
    sct.close()
