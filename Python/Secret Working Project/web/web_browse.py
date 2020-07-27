"""
browser class
take a string
browse the web
"""
 
import webbrowser as wb
import threading
import re, time

class WebBrowse(object):

    key_members = ['http:', 'https:', 'www.']


    def __init__(self, is_url = False, pref_browser = None, key_members = None):
        if key_members != None: self.key_members = key_members
        self.base_url = "https://www.google.com/search?q="
        self.is_url = is_url
        if pref_browser != None:
            try:
                wb.get(pref_browser)
            except:
                pass


    def search_by_file(self, file_name, async_search = True):
        """
        take a file_name, check if it valid, loops to get urls
        optional: async_search if true then search in aysnc or search one by one one at the time
        open url
        NOTE: if url line contains other words, if might fail to fetch url
        """
        job = self.search_many_async
        statement = "searching in threads"
        if async_search == False:
            job = self.search_many
            statement = "searching one by one"
        resp = self.open_file(file_name)
        
        if resp != True: print("No file found. Check your directory")
        else:
            with open(file_name, 'r') as file:
                for _ in file:
                    string = file.readline().strip()
                    urls_container = []
                    for member in self.key_members:
                        urls_container.append(self.get_match(string, member))
                        #print(urls_container)
                    for urls in urls_container:
                        for url in urls:
                            print(statement)
                            job(url)
    
    @staticmethod
    def show_msg(url, typ):
        """
        input: url and type to validate
        returns msg
        """
        if isinstance(url, typ) and len(url) > 0:
            return 0, "Searching: {url}".format(url = url)      
        return [1, "No valid url find to search"]

    def search_many(self, urls, sleep_time = 1):
        """
        Take a list of urls
        search by one by one, rejects invalid urls
        invaild urls = anything which is not a string or have 0 length
        """
        for url in urls:
            resp = self.show_msg(url, str)
            if resp[0] == 0:
                print(resp[-1])
                self.search(url)
            else: print(resp[-1])
            time.sleep(sleep_time)


    def search_many_async(self, urls, sleep_time = 1):
        """
        Take a list of urls
        search by one by one, rejects invalid urls
        invaild urls = anything which is not a string or have 0 length
        """
        ths = []
        for url in urls:
            resp = self.show_msg(url, str)
            if resp[0] == 0:
                print(resp[-1])
                t = threading.Thread(target= self.search, args =(url,))
                ths.append(t)
                t.start()
                
            else: print(resp[-1])
            time.sleep(sleep_time)

        for t in ths: t.join()
                

    def search(self, string = None):
        """
        search the webpage
        """
        if string == None or len(string) == 0: string = 'google'
        for member in self.key_members:
            if self.validate_query_from_start(string, member) == True: 
                self.is_url = True
                break
        if self.is_url == False: string = self.base_url + string
        return wb.open_new_tab(string)
        
    
    @staticmethod
    def get_match(string, validator):
        """
        Take a string and a validator, and validate if only the first sentence is validator
        returns url or empty list
        """
        return [re.findall("(^{val}\S*)".format(val=validator), string)]

    @staticmethod
    def open_file(file):
        """
        check if file exists, if yes, return True
        else return False
        """
        try:
            f = open(file, 'r')
            f.close()
            return True
        except FileNotFoundError:
            return False
    
    @staticmethod 
    def validate_query_from_start(string, validator):
        """
        Take a string and a validator, and validate if only the first sentence is validator
        returns True and False if validator exists
        """
        return bool(re.search("^{val}".format(val=validator), string))
    
