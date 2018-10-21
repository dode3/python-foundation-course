import urllib
def read_text():
    quotes = open("C:\Python27\profanity\movie_quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(check_prof):
    connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q="+check_prof)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("profinity alert")
    elif "false" in output:
        print("it's clean")
    else :
        print("can't scan it")


read_text()
