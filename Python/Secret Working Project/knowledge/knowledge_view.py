from abc import ABC, abstractmethod


class KnowledgeView(ABC):
    @abstractmethod
    def show_knowledge(self, knowledge):
        pass

class GoogleKnowledgeView(KnowledgeView):
    def show_knowledge(self, knowledge):
        """
        input: Enter a already gotten knowledge from google API as json
        returns info as processed json
        """
        info = '\n'.join([i['snippet'] for i in knowledge['items']])
        info = info.replace("...", "\n")
        return info

class GoogleKnowledgeViewConsole(GoogleKnowledgeView):

    def show_result(self, knowledge):
        """
        input: knowledge as json
        process it to get purified knowledges
        print the knowledge
        """
        info = self.show_knowledge(knowledge)
        print(info)
    
    def get_query(self):
        """
        returns query gotten from user from the console
        """
        return input("Enter your query: ")
        