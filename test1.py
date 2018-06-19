import urllib.request
import threading

'''with urllib.request.urlopen('http://soc.southalabama.edu') as response:
    html = response.read()

    print(html)'''

def code(string):
    print(string)

thread = threading.Thread(target=code,args=("Hello",))

thread.start()
