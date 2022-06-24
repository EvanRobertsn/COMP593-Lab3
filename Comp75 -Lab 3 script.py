#Comp75 -Lab 3 script By EVAN ROBERTSON for Professor Jeremy Dalby
#lists movie genres in data structure
def list_genre(movies):
    list=[]
    #creates list of movie genres
    for genre in movies['movies']:
        list.append(genre['genre'])
    #list all movie genres from list
    for i in range(len(list)):
        if(i==0):
            print("Some of my Fav movies Genres are:",end=" ")
        #check if the genre is not the last entry
        if(i<len(list)-1):
            
            print(list[i]+',',end=" ")
        else:
            print("and",list[i]+".")
#same as list_genre but for movie titles
def list_title(titles):
    list=[]
    for title in titles:
        list.append(title['title'])
    for i in range(len(list)):
        if(i==0):
            print("Some of my Fav movies are:",end=" ")
        
        if(i<len(list)-1):
            
            print(list[i].title()+',',end=" ")
        else:
            print("and",list[i].title()+".")
#lists the toppings on my pizza
def list_toppings(toppings):
    print("My favourite Pizza Toppings are:")
    for top in toppings['pizza_toppings']:
         print("-",top)
#lists my name and student ID
def stud_name_id(db):
    first_name=db['full_name'].split( )
    print("My name is",first_name[0],",But you can call me Lord",db['full_name'],"\n")
    print("My Student ID is",db['student_id'],"\n")
#adds topping to my pizza topping list from a tuple
def add_piz_top(pizza, top_tup):
    pizza['pizza_toppings']+=top_tup
    pizza['pizza_toppings'].sort()
    for i in range(len(pizza['pizza_toppings'])):
        pizza['pizza_toppings'][i]=pizza['pizza_toppings'][i].lower()
    return pizza


def main():

    #create dictonary w/ information
    hackers_dream={
        "full_name": "CLARENCE BEEFTANK",

        "student_id": 69420,

        "pizza_toppings": ["Mushrooms","Pepperoni","Bacon"],

        "movies":[
            #create Nested Dictonaries
            {
                "title": "the shawshank redemption",

                "genre": "Drama"
            },
            {
                "title": "the usual suspects",
                "genre": "Action Drama"
            }
        ]
    }
    

    #add new movie to movie dictonary
    new_movie={
    "title": "megamind",

    'genre': "Animated Comedy"
    }
    #add new movie to the dictonary
    hackers_dream['movies'].append(new_movie)
    
    pizza_top_tuple=("Raw Chicken","The biG toe fRom the right foot of your firstborn","Olives")
    
    #function Calls within main
    stud_name_id(hackers_dream)
    
    

    list_toppings(hackers_dream)
    #add pizza toppings to data structure
    hackers_dream=add_piz_top(hackers_dream,pizza_top_tuple)

    list_toppings(hackers_dream)
    list_genre(hackers_dream)

    list_title(hackers_dream['movies'])

main()

