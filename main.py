from scrappers.indeed import Indeed
import logging
# from multiprocessing import Process



# p = Process(target=run)
# p.start()
# p.join()
logging.basicConfig()
log = logging.getLogger("Pyjobs")
log.setLevel(logging.DEBUG)

log.info("Starting "+ __name__)

s1 = Indeed(log)
s1.run()
    