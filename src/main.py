from scrappers.indeed import Indeed
from ctwitter.consumer import Consumer
import logging
from dotenv import load_dotenv


if __name__ == '__main__':

    # start logging
    logging.basicConfig()
    log = logging.getLogger("Pyjobs")
    log.setLevel(logging.DEBUG)

    log.info("Program started")

    # load env
    load_dotenv()

    # s1 = Indeed(log)
    # s1.run()

    # p = Consumer(log)
    # p.run()



    