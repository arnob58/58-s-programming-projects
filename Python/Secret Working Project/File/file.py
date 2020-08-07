"""
take a file name EX: chrome
Open if found return 0
    search file
        search in current dir
        search in os.environ
            try finding name
                if found, try fetch path name
                    goto 2
                if found multiple name, prompt user 
                    get input: Names or cancel
                    goto 2
    if found continue, else go to last line
    open file
else return 1
"""
import os, re


class fileHandler(object):

    ignore = ['C:\\Windows\\system32' , 'C:\\Windows']
    info = []
    def __init__(self, current_dir = None, in_env = False, path_key = None, file_info_name = None):

        if current_dir == None: self.current_dir = os.getcwd()
        else: self.current_dir = current_dir
        
        if path_key == None: self.key = 'PATH'
        else: self.key = path_key

        if file_info_name == None: self.file_info_name = "info.txt"
        
        self.in_env = in_env
        self.exhausted = False

        self.get_values()

    def get_values(self):
        try:
            with open(self.file_info_name, 'r') as f:
                info.append(f.read().splitlines())
        except FileNotFoundError: self.save_new()

    def save_new(self):
        with open(self.file_info_name, 'w') as f:
            for item in self.info:
                f.write("%s\n" % item)
                
    def save(self, item):
        with open(self.file_info_name, 'a') as f:
            for item in self.info:
                f.write("%s\n" % item)
        
    def search_in_dir(self, filename, current_dir = None):
        """
        input: filename
        checks filename exist, execute open_file
        """
        resp = 1
        if current_dir == None: current_dir = self.current_dir
        for root, dir, files in os.walk(current_dir):
            #print(files)
            search_item = self.search(filename.lower(), files)
            #print(search_item)
            if search_item != None:
                resp = self.open_file(search_item[0], current_dir)
                break
        return resp

    def open(self, filename):
        """
        input: filename
        checks filename exist, execute open_file
        checks if file is referenced in env_variables, execute file
        or else say file cannot be found
        """
        error_msg = "No file to Open"
        if self.in_env == False:
            resp = self.search_in_dir(filename, self.current_dir)
            if resp == 1 and self.exhausted == False:
                resp = self.search_in_env(filename)
            else: print(error_msg)
        else:
            resp = self.search_in_env(filename)
        if resp == 1:
            print(error_msg)
            

    @staticmethod
    def search(name, names):
        """
        input: name and list of names
        uses regrex to find names
        """
        resp = []
        for n in names:
            if bool(re.match(name, n.lower())) == True: resp.append(n)
            if len(resp) > 0: return resp
        return None

    def search_in_env(self, filename, path_key = None, delimiter = ";"):
        """
        input: filename to open, optional: delimiter which basically split environment values
        searches file in the directories under env key, default is "PATH"(windows)
        """
        if path_key == None: path_key = self.key
        paths = os.getenv(path_key).split(delimiter)
        resp = 1
        for path in paths:
            if path not in self.ignore:
                print(path)
                resp = self.search_in_dir(filename, path)
            if resp == 0: return resp
        self.exhausted = True
        return resp 
        
    
    def open_file(self, filename = None, current_dir = None):
        """
        input: filename
        opens a file and returns 0 if file exist
        else return 1
        """
        if current_dir == None: current_dir = self.current_dir
        if filename != None:
            file_name = current_dir+ "\\" + filename
            print(file_name)
            try: os.startfile(file_name)
            except Exception as e:
                print(e)
                return 1
            return 0
        return 1



sample = fileHandler()
b = sample.open('pyt3251hon')
