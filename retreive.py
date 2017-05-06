import json
import requests

jobs = []
a  = requests.get('https://hacker-news.firebaseio.com/v0/item/14238005.json?print=pretty')

jobsjson = a.json()['kids']

print(len(jobsjson),'len')

for i in range(len(jobsjson)): #range(5): #len(jobsjson)):
    print(jobsjson[i])
    b = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(jobsjson[i]) + '.json?print=pretty')
    print(b.json())
    jobs.append(b.json())

with open('jobs.json', 'w') as jobsfile:
    json.dump(jobs, jobsfile)
    exit()
