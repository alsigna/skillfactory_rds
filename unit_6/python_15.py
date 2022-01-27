from collections import Counter  
import pandas as pd
import pdb  


# imdb_data = pd.read_csv("./imdb.csv")
  
# Считаем, сколько фильмов в каждом жанре  
def count_genres(column):  
    genres = []  
    pdb.set_trace()  
    for movie_genres in column:  
        splitted = movie_genres.split(",")  
        genres.extend(splitted)  
    counter = Counter(genres)  
      
    return counter   
   
# print(count_genres(imdb_data["Genre"]))  

user_db = [
    {"name": "Elena", "age": 19, "salary": 80000},
    {"name": "Sergey", "age": 31, "salary": 160000},
    {"name": "Olga", "age": 33, "salary": 170000},
    {"name": "Vadim", "age": 17, "salary": 45000}
]

from collections import defaultdict

def group_values(db, value_key, group_key, step):
    grouped = defaultdict(list) 
    for item in db:
        grouped[item[group_key] // step * step].append(item[value_key])
    return grouped

print(group_values(user_db, "salary", "age", 10))
