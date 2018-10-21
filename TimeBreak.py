import time
import webbrowser

repeat=0
print("this program started on "+time.ctime())
while (repeat<3):
 time.sleep(10)
 webbrowser.open("https://www.youtube.com/watch?v=GiBDvn6-fXU")
 repeat = repeat + 1

 
