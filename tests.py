#file = open("openfoodfacts_search.csv", "r")
#data = file.read()

#occurrences = data.casefold().count("lecithin")
#print('Number of occurrences of "lecithin total":', occurrences)

#occurrences = data.count(", lecithin")
#print('Number of occurrences of "lecithin":', occurrences)

#occurrences = data.count("lecithin")
#print('Number of occurrences of "lecithin itself":', occurrences)
#occurrences = data.count("LECITHIN")
#print('Number of occurrences of "LECITHIN itself":', occurrences)
#occurrences = data.count("Lecithin")
#print('Number of occurrences of "Lecithin itself":', occurrences)

#occurrences = data.count(",lecithin")
#print('Example to account for comma":', occurrences)

#occurrences = data.count("(lecithin)")
#print('Number of occurrences of "(lecithin)":', occurrences)
#occurrences = data.count(", soy lecithin,")
#print('Number of occurrences of "soy lecithin":', occurrences)
#occurrences = data.count(", sunflower lecithin,")
#print('Number of occurrences of "sunflower lecithin":', occurrences)

#occurrences = data.count(", phosphatidyl choline")
#print('Number of occurrences of "phosphatidyl choline":', occurrences)

# with open('openfoodfacts_search.csv') as f:
  #  for line in f:
    #    count += line.count("lecithin")

#import re

#mystr = "lecithin "
#mystr = mystr + "another Lecithin"
#mystr = mystr + ", LECITHIN"

#print (mystr)

#searchObj = re.findall (r"\W*Lecithin", mystr, re.IGNORECASE)
#print (searchObj)