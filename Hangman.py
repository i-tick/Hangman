
import random
movies = ['lagaan','highway','thor','dangal','newton']
pp1 = 10

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn="".join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    global pp1
    ref=list(movie)
    qn_list=list(qn)
    n=len(movie)
    temp=[];
    for i in range(n):
        if ref[i]==letter:
            temp.append(letter)
        else:
            temp.append(qn_list[i])
    qn_new="".join(str(x) for x in temp)   
    return qn_new

def play():
    print("LET'S PLAY")
    p1name="GROUP 1"
    p2name="GROUP 2"
    turn=0
    #willing=True
    #player 1
    print(p1name, "its your turn")
    picked_movie=random.choice(movies)
    qn=create_question(picked_movie)
    modified_qn=qn
    print(qn)
    global pp1
    temp_movie = picked_movie
    not_said=True
    while(not_said):
        letter=input("Your letter: ")
        if(is_present(letter,temp_movie)):
            temp_movie = picked_movie.replace(letter,"")
            pp1+=3
            print(pp1)
            modified_qn=unlock(modified_qn,picked_movie,letter)
            print(modified_qn)
            if(modified_qn == picked_movie):
                print("you won")
                print("score",pp1)
                break
        else:
            print(letter, "not found")
            pp1=pp1-2
            print("score",pp1)
            if(pp1<=0):
                print("you lose")
                break

    print()
play()
