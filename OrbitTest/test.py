#https://www.sharebrained.com/2011/10/18/track-the-iss-pyephem/
from datetime import datetime
import ephem
line1 = "ISS"
line2 = "1 25544U 98067A   18068.53357280  .00016717  00000-0  10270-3 0  9003"
line3 = "2 25544  51.6397 155.5133 0002684 172.9694 187.1496 15.54190241 23018"
iss =  ephem.readtle(line1, line2, line3)




home = ephem.Observer()
home.lat = 0
home.lon = 0
home.elevation = 0
home.date = datetime.utcnow()

s = datetime.utcnow()
print(datetime.utcnow())

#print(iss.compute(home))
print(iss.compute(s))



print(iss.ra)
print(iss.dec)