import json

with open('jobs.json', 'r') as jobsfile:
    print(json.dumps(json.load(jobsfile), indent=4, sort_keys=True))
