from scrappers.indeed import Indeed
from scrappers.tiobe import Tiobe
from ctwitter.consumer import Consumer
import logging
from dotenv import load_dotenv

def run():
    # query indeed
    s1 = Indeed(log)
    s1.run()

    # tiobe top langs query
    tiobe = Tiobe(log)
    tiobe.run()

    # twitter consumer
    p = Consumer(log, "golang job")
    p.run()


if __name__ == '__main__':

    # start logging
    logging.basicConfig()
    log = logging.getLogger("Pyjobs")
    log.setLevel(logging.DEBUG)

    log.info("Program started")

    # load env
    load_dotenv()

    run()
    



    