import logging
from abc import ABC, abstractmethod

logging.basicConfig(filename="controller.log", level=logging.DEBUG)

class KnowledgeController(ABC):

    def __init__(self, model, view):
        """
        input: knowledge Model and View
        """
        self.model = model
        self.view = view

class GoogleKnowledgeConsoleController(KnowledgeController):

    def main(self):
        """
        get query from the user
        get knowledge from the model
        show the knowledge to the view
        """
        try:
            query = self.view.get_query()
            logging.debug("query: {}".format(query))
            logging.debug('view worked and got user input')
            knowledge = self.model.get_knowledge(query)
            logging.debug('model worked and got knowledge')
            self.view.show_result(knowledge)
            print('view worked and showed result to the user')
            return 0
        except Exception as e:
            return e


    def start_loop(self, n = None):
        """
        starts a loop to get knowledge from the model
        if n is none, loop will go forever, warning, it might exceed quota
        or else n runs the loop n times
        """
        if n == None:
            while True:
                ret = self.main()
                if ret != 0:
                    logging.error("Error: {}".format(ret))
        else:
            for i in range(n):
                ret = self.main()
                if ret != 0:
                    logging.error("Error: {}".format(ret))




    