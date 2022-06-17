#Comp75 -Lab 3 script

def list_movies():
    pass

def list_genre():
    pass

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
    stud_name_id(hackers_dream['full_name'],hackers_dream["student_id"])
    

main()

