import unicodecsv
from datetime import datetime

year_start = 1917 # Starting year of frequency use.
year_finish = 1994

csv_file = open('crest_topic_by_year.csv', 'w')
csv_writer = unicodecsv.writer(csv_file)

row = ["Word"]
for i in range(year_start, year_finish+1):
    row.append(i)
csv_writer.writerow(row)

keywords = ["Islam","Christian", "Muslim", "Buddhi", "Athies", "Hindu", "Sikh", "Jew", "Judaism"]

for word in keywords:
    print "starting on next keyword, " + word
    csvNumber = 1
    data = [word]
    for i in range(year_start, year_finish+1):
        data.append(0)
    print "Set a blank slate of years"

    while csvNumber <= 4:
        with open('crest_lite_' + str(csvNumber) + '.csv') as crest_csv:
            reader = unicodecsv.DictReader(crest_csv)
            for row in reader:
                if word in row['title']:
                    try:
                        print "Publication date is " + str(row['publication_date'])
                        datetime_object = datetime.strptime(row['publication_date'], '%B %d, %Y')
                        print datetime_object.strftime('%Y')
                        data[int(datetime_object.strftime('%Y'))- year_start + 1] += 1
                        print "Increment the occurrences for " + word + " to a total of " +  str(data[int(datetime_object.strftime('%Y'))- year_start] + 1)
                    except:
                        print "Some error, probably due to lack of date."
            csvNumber += 1
    csv_writer.writerow(data)

print "All done"
