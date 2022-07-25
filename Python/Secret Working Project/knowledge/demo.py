from knowledge_view import GoogleKnowledgeViewConsole as View
from knowledge_model import GoogleKnowledgeBrowserModel as Model
from knowledge_browser import GoogleKnowledgeConsoleController as Controller
import logging, json

logging.basicConfig(filename="main.log", level=logging.DEBUG)

def main(n = 10):
    try:
        view = View()
        logging.debug('hello')
        logging.debug('view created')
        cred = get_cred("cred.json")
        cx = cred['cx']
        api_key = cred['api_key']
        logging.debug('credentials loaded')
        model = Model(cx,api_key)
        logging.debug('model created')
        controller = Controller(model, view)
        logging.debug('controller created')
        controller.start_loop(n)
    
    except Exception:
        raise RuntimeError

def get_cred(json_file):
    try:
        with open(json_file) as f:
            return json.loads(f.read())
    except Exception as e:
        logging.error("Error: {}".format(e))
        raise RuntimeError

if __name__ == '__main__':
    try:
        n = int(input("Enter the number of times you want to get knowledge: "))
        if n == "":
            n = None
        main(n)
    except Exception as e:
        logging.error(e)
        print("Critical Error Found when initialization...program will close now!")
    
    input("Press Enter to Exit")

