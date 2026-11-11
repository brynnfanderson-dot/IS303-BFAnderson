import pandas as pd
#pandas are spreadsheets for python 
#student_info = {
   # "name": "Zendaya",
    #"year": "Freshman",
    #"age": 30,
    #"graduated": False,
    #"Fav_class": "IS 303"
#}

#df = pd.DataFrame([student_info])
#print(df)

#student_info = {
 #   "name": ["Tom", "Lebron", "George", "Lafawnda"],
  #  "gpa": [2.7, 4.0, 1.1, 3.6]
#}

#result = pd.DataFrame(student_info)
#print(result)

restaurant_info = pd.read_csv("restruantinto.csv")
#print(restaurant_info.loc[restaurant_info['FoodType'] == 'TexMex'])
#print(restaurant_info.at[1, "Rating"])
#restaurant_info.at[1, "Rating"] = 12
#print(restaurant_info)

print(restaurant_info.query("Rating >= 10"))