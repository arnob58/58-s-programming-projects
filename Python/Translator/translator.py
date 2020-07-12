from tqdm import tqdm
print("Importing modules...." )
from textblob import TextBlob as blob
from textblob import Word
import pyperclip, sys, time
print("Import Done!")


def saveFile(item, file):
    """
    input: item with needs to be saved
    saves item in file
    """
    with open(file, "w") as file:
        file.write(item)
    
def translate(sentence, to_sen = 'bn', to_file = False, file_name = None):
    """
    input: sentence to convert, and language to convert
    returns translated sentence
    """
    err_sentence = "Sir, I can't translate this. Make sure you have said translate when you start detecting."
    
    def detect(sentence):
        """
        input: sentence or string
        returns detected language
        """
        try: return blob.detect_language(blob(sentence))
        except Exception as e:
            print(e)
            return None
    try:
        answer = blob.detect_language(blob(sentence))
        if answer != None:
           translated =  str(blob.translate(blob(sentence),from_lang=answer, to = to_sen))
        else:
            return err_sentence

        if to_file:
            saveFile(translated, file_name)
            print("File written on {file}".format(file=file_name))

        return translated
    
    except Exception as e:
        print(e)
        return err_sentence
    

def file_translate(file, to_sen = 'bn', sfile = "tranlated.txt"):
    """
    input: file to translate, language to translate and a file name to save file
    translated and save whole file
    """
    
    paragraph = ''
    print("File translating Start....")
    print("File Reading begin...")
    
    try:
        with open(file, 'r') as file:
            sentences = blob(file.read()).sentences
            #print(sentences)
        
        print("Translating: ",end='')
        progress = tqdm(total = len(sentences), desc = "Translating:", unit = "sentence/s")
        for item in sentences:
            progress.update(1)
            paragraph += translate(str(item)) + '\n'
            time.sleep(0.2)

        progress.close()
        print("\nTranslating Done! Saving your file")
        saveFile(paragraph, sfile)

        

    except Exception as e: print(e)
            
def man_input():
    """
    input data manually
    """
    print("Programmed has executed without terminal or console. Please manually input data. To skip one item just press enter:")
    sentence = input('sentence: ')
    file = input('file: ')
    language = input('language: ')
    save_file = input('save: ')

    return sentence, file, language, save_file


if __name__ == "__main__":
    import argparse
    
    desc = """
    This Small Translator Program takes a file or sentence, and translate it back
    Note:
    * If a file and a sentence is given, the file will be translated as it has top priority\n
    * If you pass a file but no save file then, a default "translated.txt" will be created to store the result. BE CAREFUL ABOUT THAT\n
    * You need to pass two letter language code as the language. For Example if you want to translate in Bangla pass "bn" instead of "bangla"\n
      google to find your two letter language code\n\n
    """
    
    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument("-s", "--sentence", required=False,
                        help = "Sentence you want to tranlate")
    parser.add_argument("-f", "--file", required=False,
                        help = "file which you want to translate")
    parser.add_argument("-l", "--language", required=False,
                        help = "Language you want to tranlate")
    parser.add_argument("-sf", "--save", required=False,
                        help = "File where you want to save the result")

    try:
        args = vars(parser.parse_args())
        error = False
    except Exception as E:
        print(E)
        error = True
        

    if len(sys.argv) > 1:
        sentence = args['sentence']
        file = args['file']
        language = args['language']
        save_file = args['save']
    elif len(sys.argv) == 1 or error == True:
        sentence, file, language, save_file = man_input()
    

    try:
        if file != '':
            if save_file == '' : save_file = 'translated.txt'
            if language == '' : language = 'bn'
            file_translate(file, language, save_file)

        elif sentence != '':
            to_file = False
            if save_file != '' : to_file = True
            if language == '' : language = 'bn'
            ret = translate(sentence, language, to_file, save_file)
            if ret != None: print("Translation:",ret)

        else:
            print("Nothing to translated found, program will exit")

    except Exception as e: print(e)

    print("Done! Program will exit now")

    
