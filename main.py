from scrappers.indeed import Indeed
from ctwitter.puller import Puller
import logging
from dotenv import load_dotenv


# start logging
logging.basicConfig()
log = logging.getLogger("Pyjobs")
log.setLevel(logging.DEBUG)

# load env
load_dotenv()

log.info("Starting "+ __name__)
s1 = Indeed(log)
s1.run()

p = Puller(log)
p.run()



    