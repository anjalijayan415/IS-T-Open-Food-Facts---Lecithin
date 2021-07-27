,
import re
import csv
import matplotlib.pyplot as plt

class LecithinType:
    def __init__(self, fullname):
        self.fullname = fullname
        self.occurrences = 0
        self.brand_names = []
        self.product_names = []


def store_unique_values_with_dictionary(dict, value):

    if value in dict.keys():
      print ("found value ")
      dict[value] += 1
    else:
      print ("not found value ")
      dict[value] = 1
    return dict


lecithin_types = []

from csv import DictReader

lecithin_dict = {}
large_lecithin_dict = {}
with open('columns.csv', 'r') as read_obj:
  csv_dict_reader = DictReader(read_obj)
  for row in csv_dict_reader:
        
        if row['ingredients_text'].find('lecithin') != -1:
          
          print(row['product_name'], "#", row['brands'])

          searchObj = re.findall (r",([^,]*Lecithin[^\]\[,\)]*),", row['ingredients_text'], re.IGNORECASE)

          for match in searchObj:
            print ("the small match")
            print (match)
            store_unique_values_with_dictionary(large_lecithin_dict, match)
          
          searchObj = re.findall (r",([^,]*\({1}[^\(]*Lecithin.*\]{1}),", row['ingredients_text'], re.IGNORECASE)

          for match in searchObj:
            print ("the match")
            print (match)
            store_unique_values_with_dictionary(large_lecithin_dict, match)
            
          searchObj = re.findall (r",([^,]*Lecithin)", row['ingredients_text'], re.IGNORECASE)

          for match in searchObj:
            print ("the other match")
            print (match)
            print ("the row")
            store_unique_values_with_dictionary(lecithin_dict, match)
            
          print (row['ingredients_text'])
         # input("Press Enter to continue...")  

input("Done - Press Enter to continue...")         
for k, v in lecithin_dict.items():
    print(k, v)
input("Done again - Press Enter to continue...") 

input("About to print large match - Press Enter to continue...")         
for k, v in large_lecithin_dict.items():
    print(k, v)
    input ("stop")
input("Done again - Press Enter to continue...") 

csv_file = "lecithin_count.csv"
with open('lecithin_dict.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in lecithin_dict.items():
       writer.writerow([key, value])



counts = [80,1,4,1,1,2,1,1]
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
labels = ['soy lecithin', 'cocoa butter soy lecithin', 'lecithin', 'emulsifier (soya lecithin)', 'sunflower lecithin', 'soya lecithin', 'oil soy lecithin', 'organic sunflower lecithin']

figure = plt.figure()
plt.xlabel("Formatting Differences")
plt.ylabel("Count")
plt.xticks(rotation=90)
#plt.size(figsize = (10,10))

plt.bar(labels,counts)

plt.savefig("barplot.png")
plt.show()