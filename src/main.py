from scrappers.indeed import Indeed
from scrappers.tiobe import Tiobe
from ctwitter.consumer import Consumer
import logging
from dotenv import load_dotenv

def run(keyword, location):
    # query indeed
    # s1 = Indeed(log)
    # s1.run(keyword, location)

    # tiobe top langs query
    # tiobe = Tiobe(log)
    # tiobe.run()

    # twitter consumer
    p = Consumer(log, keyword + " AND job OR position OR hiring ")
    p.run()


if __name__ == '__main__':

    # start logging
    logging.basicConfig()
    log = logging.getLogger("Pyjobs")
    log.setLevel(logging.DEBUG)

    log.info("Program started")

    # load env
    load_dotenv()

    positions = ["golang", "java", "javascript", "ruby", "rails", "ror", 
                "dotnet", "node", "angular", "python", "data", "machine learning", 
                "JSP", "AJAX", "jQuery", "JSON","HTML", "CSS", "php", "mysql", "graph", 
                "mongo", "databases", "elasticsearch", "linear regression", "nlp", "3d",
                "mock", "tdd", "SOLID principles", "bdd", "ios", "android", "macos", "linux",
                "git", "subversion", "as400", "laravel", "symfony", "oauth", "codeigniter", 
                "yii", "ruby on rails", "AI", "Data Science", "Deep Learning", "Big Data", 
                "BigData"]
    

    for position in positions:
        log.info("querying for " + position)
        run(position, "london")
    



    