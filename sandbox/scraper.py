
import pynput.keyboard
import time # pause in between website opens
import webbrowser # open website

# this function inputs the key combination to open "page source"
def pageSource():
    keyboard = pynput.keyboard.Controller()
    keyCtrl = pynput.keyboard.Key.ctrl
    keyU = "u"
    
    keyboard.press(keyCtrl)
    keyboard.press(keyU)
    keyboard.release(keyCtrl)
    keyboard.release(keyU)
    


def main():
    # Test url's
    URLS = ("https://wiki.wizard101central.com/wiki/Quest:Local_Expertise"
          , "https://wiki.wizard101central.com/wiki/Quest:Hypothetically_Speaking"
          , "https://wiki.wizard101central.com/wiki/Quest:All_You_Need_To_Do")
    
    # open website
    webbrowser.open(URLS[0])
    time.sleep(2)
    
    pageSource()


if __name__ == "__main__":
    main()