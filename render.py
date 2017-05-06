import markdown
import html2text
import json

with open('jobs.json', 'r') as jobsfile:
    jobs = json.load(jobsfile)
    for each in jobs:
        #contains 'by', 'id', 'kids', 'parent', 'text', 'time', 'comment' 
        if not 'deleted' in each:
            print('<br>')
            print('By: ', each['by'])
            print('<br>')
            print('HN-id: ' + 'https://news.ycombinator.com/item?id=' + str(each['id']))

            if 'kids' in each:
                print('<br>')
                print('Comments: ', len(each['kids']))
                print('<br>')

            #print()

            #For terminal formatted markdown
            #print(html2text.html2text(each['text']))

            #For HTML formatted markdown:
            print('<small><b>')
            print(markdown.markdown(html2text.html2text(each['text'])))
            print('</b></small>')
            #print()
            print('<b>----------------------------------------------------------------</b>')
            #print()


            #exit()

    #print(json.dumps(json.load(jobsfile), indent=4, sort_keys=True))
