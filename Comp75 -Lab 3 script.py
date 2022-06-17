#Comp75 -Lab 3 script



def list_genre(movies):
    list=[]
    for genre in movies['movies']:
        list.append(genre['genre'])
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
    for i in range(len(list)):
        if(i==0):
            print("Some of my Fav movies are:",end=" ")
        
        if(i<len(list)-1):
            
            print(list[i]+',',end=" ")
        else:
            print("and",list[i]+".")

def list_toppings(toppings,case_cos):
    print("My fav Pizza Toppings are:")
    for top in toppings['pizza_toppings']:
        if(case_cos==False):
            print("-",top)
        elif(case_cos==True):
            print("-",top.lower())

def stud_name_id(full_name,stud_id):
    first_name=full_name.split( )
    print("My name is",first_name[0],",But you can call me Lord",full_name,"\n")
    print("My Student ID is",stud_id,"\n")
    pass

def add_piz_top(pizza, top_tup):
    pizza['pizza_toppings']+=top_tup
    pizza['pizza_toppings'].sort()
    case_cos=True
    return pizza,case_cos
    pass

#create empty main function w/ pass call
def main():

    #create dictonary w/ information
    hackers_dream={
        "full_name": "Evan Robertson",

        "student_id": 69420,

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
    pizza_top_tuple=("Raw Chicken","The biG toe fRom the right foot of your firstborn","Olives")
    case_constant=False
    #function Calls
    stud_name_id(hackers_dream['full_name'],hackers_dream["student_id"])
    list_genre(hackers_dream)
    list_title(hackers_dream)
    list_toppings(hackers_dream,case_constant)
    hackers_dream,case_constant=add_piz_top(hackers_dream,pizza_top_tuple)
    list_toppings(hackers_dream,case_constant)

main()

