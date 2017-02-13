import alist

content2 = alist.liste('http://127.0.0.1:5000/api/connection','054E508852624649B8B250B341CFF639')
#print content2
print content2['options']['ports'][0]
