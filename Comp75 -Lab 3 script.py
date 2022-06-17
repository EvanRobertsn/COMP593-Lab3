#Comp75 -Lab 3 script


def list_genre(movies):
    list=[]
    for genre in movies['movies']:
        list.append(genre['genre'])
    print(len(list))
    for i in range(len(list)):
        if(i==0):
            print("Some of my Fav movies Genres are:",end=" ")
        
        if(i<len(list)-1):
            
            print(list[i]+',',end=" ")
        else:
            print("and",list[i]+".")

def list_title(titles):
    list=[]
    for title in titles['movies']:
        list.append(title['title'])
    print(list)

def list_toppings():
    pass

def stud_name_id(full_name,stud_id):
    first_name=full_name.split( )
    print("My name is",first_name[0],"But you can call me Lord",full_name)
    print("My Student ID is",stud_id)
    pass

def add_piz_top():
    pass

#create empty main function w/ pass call
def main():

    #create dictonary w/ information
    hackers_dream={
        "full_name": "Evan Robertson",

        "student_id": 45,

        "pizza_toppings": ["Mushrooms","Pepperoni","Bacon"],

        "movies":[
            #create Nested Dictonaries
            {
                "title": "The ShawShank Redemption",

                "genre": "Drama"
            },
            {
                "title": "The Usual Suspects",
                "genre": "Action Drama"
            }
        ]
    }
    

    #add new movie to movie dictonary
    new_movie={
    "title": "Megamind",

    'genre': "Animated Comedy"
    }
    hackers_dream['movies'].append(new_movie)
    
    #function Calls


    stud_name_id(hackers_dream['full_name'],hackers_dream["student_id"])
    list_genre(hackers_dream)
    list_title(hackers_dream)

main()

