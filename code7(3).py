import json
import csv

with open('movies.json', 'r') as f:
    data = json.load(f)

with open('movie.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'rating', 'votes'])
    
    for item in data:
        title = item.get('title', '')
        try:
            rating = float(item.get('rating', 0))
        except (ValueError, TypeError):
            rating = 0.0
        try:
            votes = int(item.get('votes', 0))
        except (ValueError, TypeError):
            votes = 0
        
        writer.writerow([title, rating, votes])