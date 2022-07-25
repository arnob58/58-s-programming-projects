import logging
import requests as req
from abc import ABC, abstractmethod

logging.basicConfig(filename="model.log", level=logging.DEBUG)
class KnowledgeBrowserModel(ABC):

    @abstractmethod
    def get_knowledge(self, item):
        pass

class GoogleKnowledgeBrowserModel(KnowledgeBrowserModel):
    def __init__(self, cx, api_key, url = None, api_version = 'v1'):
        """
        input: cx, api_key, googleurl and the api_version
        """
        self._url = None
        self.cx = cx
        self.api_key = api_key
        if self.url == None:
            url = "https://www.googleapis.com/customsearch/{ver}?key={API_KEY}&cx={CX}"
        self.api_version = api_version
        self.url = url

    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url):
        self._url = url.format(ver = self.api_version, API_KEY = self.api_key, CX = self.cx)

    def get_knowledge(self, item):
        """
        input: item as an search item 
        return the search item as json
        """
        search_item = self.url + '&q={item}'.format(item = item)
        logging.debug(search_item)
        item = req.get(search_item)
        logging.debug(item.status_code)
        if item.status_code == 404:
            logging.error("404 error")
            return None
        elif item.status_code == 400:
            logging.error("400 error")
            return None
        logging.debug(item)
        return req.get(search_item).json()


if __name__ == '__main__':
    model =  GoogleKnowledgeBrowserModel("010134349476185983731:uaf42xhrqhk","AIzaSyDf9lFFwv-GzW6c95CPcJEv5MLNssnLfaE", api_version=1)
    print(model.url)
    print(model.get_knowledge("python"))