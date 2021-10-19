import tkinter as tk
import math
import random
import time


answer = ""   
points = 0
#number of incorrect attempts allowed. If you reach 0 incorrect attempts, the game ends.
attempts = 3
#45 second timer for added difficulty.
seconds = 45.0

global time_attack_seconds
time_attack_seconds = 35.0





"""
Mathematical functions, instructions, and normal mode developed by me.
"""







#Hints:
current_hint = ""
sphere_volume_hint = "The formula is: 4/3πr^3 where r is the radius"
rectangular_prism_volume_hint = "The formula is: whl where w is the width, h is the height, and l is the length"
triangular_prism_volume_hint = "The formula is: 1/2bhl where b is the base, h is the height, and l is the length"
cone_volume_hint = "The formula is: 1/3πhr^2 where h is the height and r is the radius."
square_pyramid_volume_hint = "The formula is: 1/3hb^2 where h is the height and b is the base"
cylinder_volume_hint = "The formula is: πhr^2 where h is the height and r is the radius"
rectangle_area_hint = "The formula is: wl where w is the width and l is the length"
circle_area_hint = "The formula is: πr^2 where r is the radius"

def hint_activation(hint_label):
    global points
    points = points - 1
    hint_label["text"] = current_hint


#Math Problem Templates:
def sphere_volume():
    global current_hint
    current_hint=sphere_volume_hint
    radius=random.randint(0,10)
    question="Find the volume of a sphere with the radius of " + str(radius) + " units. Pi= 3.14. Round to the nearest 2 decimal places."
    global answer
    answer=round((4/3) * (3.14 * radius ** 3),2)
    return question

def rectangular_prism_volume():
    global current_hint
    current_hint=rectangular_prism_volume_hint
    width=random.randint(0,10)
    length=random.randint(0,10)
    height=random.randint(0,10)
    question="Find the volume of a rectangular prism with the length of " + str(length) + " units, width of " + str(width) + " units, and height of " + str(height) + " units. Use pi= 3.14. Round to the nearest 2 decimal places."
    global answer
    answer=round((length*width*height),2)
    return question

def triangular_prism_volume():
    global current_hint
    current_hint = triangular_prism_volume_hint
    length = random.randint(0, 10)
    base = random.randint(0, 10)
    height = random.randint(0, 10)
    question="Find the volume of a right triangular prism with the length of " + str(length) + " units, base of " + str(base) + " units, and height of " + str(height) + " units. Round to the nearest 2 decimal places."
    global answer
    answer = round(((length * base * height ) / 2 ), 2)
    return question

def cone_volume():
    global current_hint
    current_hint = cone_volume_hint
    radius = random.randint(0, 10)
    height = random.randint(0, 10)
    question="Find the volume of a cone with a radius of " + str(radius) + " units and the height of " + str(height) + " units. Use pi= 3.14. Round to the nearest 2 decimal places."
    global answer
    answer = round(((1.0/3) * 3.14 * radius * radius * height), 2)
    return question

def square_pyramid_volume():
    global current_hint
    current_hint = square_pyramid_volume_hint
    base = random.randint(0, 10)
    height = random.randint(0, 10)
    question = "Find the volume of a right square pyramid with the base of " + str(base) + " units and the height of " + str(height) + " units. Round to the nearest 2 decimal places."
    global answer
    answer = round(((1.0/3) * (base^2) * height), 2)
    return question

def cylinder_volume():
    global current_hint
    current_hint = cylinder_volume_hint
    radius = random.randint(0, 10)
    height = random.randint(0, 10)
    question = "Find the volume of a cylinder with a radius of " + str(radius) + " units and the height of " + str(height) + " units. Use pi= 3.14. Round to the nearest 2 decimal places."
    global answer
    answer = round((3.14 * radius * radius * height), 2)
    return question

def rectangle_area():
    global current_hint
    current_hint = rectangle_area_hint
    length = random.randint(0, 10)
    width = random.randint(0, 10)
    question = "Find the area of a rectangle with the length of " + str(length) + " units and the width of " + str(width) + " units. Round to the nearest 2 decimal places."
    global answer
    answer = round((length * width), 2)
    return question

def circle_area():
    global current_hint
    current_hint = circle_area_hint
    radius = random.randint(0, 10)
    question="Find the area of a circle with the radius of " + str(radius) + " units. Pi= 3.14. Round to the nearest 2 decimal places."
    global answer
    answer = round((3.14 * radius * radius), 2)
    return question

#Pages
def attempt(attempt_value, title_label_subtitle, x): ####################################################### ATTEMPT FUNCTION CHECKS FOR NON NUMBER INPUTS
    global points
    global attempts
    try:
        if float(attempt_value) == float(answer):
            print("Correct")
            points = points + 2
            if x == "r":
                transition(3)
                changepage()
            if x == "t":
                transition(8)
                changepage()
        if float(attempt_value) != float(answer):
            print("Incorrect")
            attempts= attempts - 1
            points=points-1
            if x == "r":
                transition(4)
                changepage()
    except ValueError:
        title_label_subtitle["text"] = "Please enter a numeric value!"
        
def transition(number):
    global pagenum
    pagenum = number

def home_page(root):
    global points
    global attempts
    points = 0
    attempts = 3
    page = tk.Frame(root, width = 500, height = 500)
    home_background_image=tk.PhotoImage(file = "home_page_background.png")
    home_background_label = tk.Label(page, borderwidth=15, relief="ridge", image=home_background_image)
    home_background_label.place(x=0, y=0, relwidth=1.009, relheight=1)
    home_background_label.image = home_background_image

    play_button = tk.Button(page, text = 'Play Game', command = lambda:[transition(2), changepage()], height = 3, width = 17,borderwidth=3, relief="solid")
    play_button.place(x = 190, y = 120)

    instructions_button = tk.Button(page, text = 'Instructions', command = lambda:[transition(1), changepage()], height = 3, width = 17,borderwidth=3, relief="solid")
    instructions_button.place(x = 190, y = 280)
    
    page.pack()

    time_attack = tk.Button(page, text = 'Time Attack', command = lambda:[transition(6), changepage()], height = 3, width = 17, borderwidth=3, relief="solid")
    time_attack.place(x = 190, y = 200)

    applications_home_button = tk.Button(page, text = "Applications in Real Life", command = lambda:[transition(10), changepage()], height = 3, width = 17, borderwidth=3, relief="solid")
    applications_home_button.place(x = 190, y = 360)

def game(root):
    global attempts
    print ("You have " + str(attempts) + " attempts")
    page = tk.Frame(root, width = 500, height = 500)

    page.config(bg = "salmon")
    
    game_background_image = tk.PhotoImage(file = "game_background.png")
    game_background_label = tk.Label(page, borderwidth = 15, relief = "ridge", image = game_background_image)
    game_background_label.place(x = 0, y = 0, relwidth = 1.009, relheight = 1)
    game_background_label.image = game_background_image

    entry_box = tk.Entry(page, font = ("comic sans", 14))
    entry_box.place(x = 55, y = 210, height = 27, width = 330)
    #"""

    title_label_subtitle = tk.Label(page, 
        text = "Solve:",
        font = ("MS Sans Serif", 15),
        bg = "silver",
        wraplength = 400,
        justify = "left")
    title_label_subtitle.place(x = 55, y = 115)

    entry_button = tk.Button(page,
        text = 'Enter', 
        font = ("MS Sans Serif", 10),
        command = lambda: attempt(entry_box.get(), title_label_subtitle, "r"), 
        height = 1, 
        width = 5)
    entry_button.place(x = 390, y = 210)
    #"""
    button = tk.Button(page, 
        text = 'Back', 
        font = ("MS Sans Serif", 10),
        command = lambda:[transition("Home"), changepage()], 
        height = 2, 
        width = 5)
    button.place(x = 5, y = 5)
    
    #input types of questions elements in the list
    types_of_questions_list = [sphere_volume, rectangular_prism_volume, triangular_prism_volume,cone_volume, square_pyramid_volume, cylinder_volume, rectangle_area, circle_area]
    type_of_question= random.choice(types_of_questions_list)()

    question_label= tk.Label(page, 
        text = type_of_question,
        font = ("MS Sans Serif", 10),
        wraplength = 400,
        justify = "left")
    question_label.place(x = 55, y = 150)

    hint_label= tk.Label(page, 
        text = "Hints appear here.",
        font = ("MS Sans Serif", 10),
        wraplength = 400,
        justify="left")
    hint_label.place(x = 55, y = 295)

    hint_button= tk.Button(page, 
        text = 'Press here for a hint (-1 points)', 
        font = ("MS Sans Serif", 10),
        command = lambda: hint_activation(hint_label),
        height = 2, 
        width = 49)
    hint_button.place(x = 55, y = 250)

    #timer
    countdown_label = tk.Label(page)
    countdown_label.place(x = 230, y = 70)
    countdown_label.config(height = 1, font = ('times', 20, 'bold'))
    page.pack()
    global seconds
    for k in numpy.arange(seconds, 0, -0.1):
        countdown_label["text"] = round(k,2)
        page.update()
        time.sleep(0.1)

    attempts = attempts - 1

    transition(4)
    changepage()

def correct_page(root):
    global points
    global attempts
    page = tk.Frame(root, width = 500, height = 500)
    page.config(bg = "pale green")
    title_label = tk.Label(page, 
        text="Correct!",
        bg = "pale green",
        font = ("MS Sans Serif", 35))
    title_label.place(x = 175, y = 0)

    point_value_label= tk.Label(page, 
        text = "The correct answer is: " + str(answer) + ". You have: " + str(points) + " points. " + "You have: " + str(attempts) + " attempts left.",
        font = ("MS Sans Serif", 20),
        wraplength=400,
        bg = "pale green",
        justify = "left")
    point_value_label.place(x = 75, y = 70)
    page.pack()
    
    for q in numpy.arange(3, 0, -1):
        page.update()
        time.sleep(1)

    transition(2)
    changepage()

def incorrect_page(root):
    global points
    global attempts
    page = tk.Frame(root, width = 500, height = 500)
    page.config(bg = "brown")
    title_label = tk.Label(page, 
        text = "Incorrect",
        bg = "brown",
        font = ("MS Sans Serif", 35))
    title_label.place(x = 145, y = 0)

    point_value_label = tk.Label(page, 
        text = "The correct answer is: " + str(answer) + ". You have: " + str(points) + " points." + "You have: " + str(attempts) + " attempts left.",
        font = ("MS Sans Serif", 20),
        wraplength = 400,
        bg = "brown",
        justify = "left")
    point_value_label.place(x = 75, y = 70)
    page.pack()
    
    if attempts == 0:
        for q in numpy.arange(3, 0, -1):
            page.update()
            time.sleep(1)

        transition(5)
        changepage()

    else:
        for q in numpy.arange(3, 0, -1):
            page.update()
            time.sleep(1)

        transition(2)
        changepage()

def gameover_page(root):
    page = tk.Frame(root, width = 500, height = 500)
    page.config(bg = "antique white")
    title_label= tk.Label(page, 
        text = "Game Over!",
        font = ("MS Sans Serif", 35),
        bg = "antique white")
    title_label.place(x = 115, y = 0)

    title_label_subtitle= tk.Label(page, 
        text = "You scored: " + str(points) + " points",
        font = ("MS Sans Serif", 20),
        bg = "antique white")
    title_label_subtitle.place(x = 125, y = 70)

    button= tk.Button(page, 
        text = 'Back', 
        font = ("MS Sans Serif", 10),
        command = lambda:[transition("Home"), changepage()], 
        height = 2, 
        width = 5)
    button.place(x = 5, y = 5)
    page.pack()

def instructions(root):
    page = tk.Frame(root, width = 500, height = 500)

    instructions_background_image = tk.PhotoImage(file = "instructions_page_background.png")
    instructions_background_label = tk.Label(page, borderwidth = 15, relief = "ridge", image = instructions_background_image)
    instructions_background_label.place(x = 0, y = 0, relwidth = 1.009, relheight = 1)
    instructions_background_label.image = instructions_background_image

    button = tk.Button(page, 
        text = 'Back', 
        font = ("MS Sans Serif", 10),
        command = changepage, 
        height = 2, 
        width = 5)
    button.place(x = 5, y = 5)
    page.pack()







"""
Time attack and real world application functions developed by my partner.
"""






def time_attack_page(root):
    page = tk.Frame(root, width = 500, height = 500)

    time_attack_background_image = tk.PhotoImage(file = "time_attack_page_background.png")
    time_attack_background_label = tk.Label(page, borderwidth = 15, relief="ridge", image = time_attack_background_image)
    time_attack_background_label.place(x = 0, y = 0, relwidth = 1.009, relheight = 1)
    time_attack_background_label.image = time_attack_background_image

    button = tk.Button(page, 
        text = "Back", 
        font = ("MS Sans Serif", 10),
        command = lambda:[transition("Home"), changepage()], 
        height = 2, 
        width = 5)
    button.place(x = 5, y = 5)

    go_to_t_game = tk.Button(page,
        text = "Play Time Attack",
        font = ("MS Sans Serif", 10),
        command = lambda:[transition(7), changepage()],
        height = 2,
        width = 20)
    go_to_t_game.place(x = 165, y = 400)

    page.pack()

def t_game(root):
    global time_attack_seconds #Allows t_game to access time_attack_seconds
    if time_attack_seconds < 35:
        time_attack_seconds = 35
    page = tk.Frame(root, width = 500, height = 500)

    tgame_background_image = tk.PhotoImage(file = "tgame_background.png")
    tgame_background_label = tk.Label(page, borderwidth = 15, relief="ridge", image = tgame_background_image)
    tgame_background_label.place(x = 0, y = 0, relwidth = 1.009, relheight = 1)
    tgame_background_label.image = tgame_background_image
    
    title_label_subtitle = tk.Label(page, 
        text = "Solve:",
        font = ("MS Sans Serif", 15),
        wraplength = 400,
        justify = "left")
    title_label_subtitle.place(x = 52, y = 115)

    t_entry_box = tk.Entry(page, font=("comic sans", 14))
    t_entry_box.place(x = 55, y = 210, height = 27, width = 330)
    
    t_entry_button= tk.Button(page,
        text = 'Enter', 
        font = ("MS Sans Serif", 10),
        command = lambda: attempt(t_entry_box.get(), t_title_label_subtitle, "t"),  ###########################################
        height = 1, 
        width = 5)
    t_entry_button.place(x = 382, y = 210)

    t_button= tk.Button(page, 
        text = 'Back', 
        font = ("MS Sans Serif", 10),
        command = lambda:[transition("Home"), changepage()], 
        height = 2, 
        width = 5)
    t_button.place(x = 5, y = 5)
    page.pack()
    
    #input types of questions elements in the list
    types_of_questions_list = [sphere_volume, rectangular_prism_volume, triangular_prism_volume,cone_volume, square_pyramid_volume, cylinder_volume, rectangle_area, circle_area]
    type_of_question= random.choice(types_of_questions_list)()

    t_question_label= tk.Label(page, 
        text = type_of_question,
        font = ("MS Sans Serif", 10),
        wraplength = 400,
        width = 49,
        justify = "left")
    t_question_label.place(x = 52, y = 150)

    t_hint_label= tk.Label(page, 
        text = "Hints appear here.",
        font = ("MS Sans Serif", 10),
        wraplength = 400,
        justify = "left")
    t_hint_label.place(x = 52, y = 295)

    t_hint_button= tk.Button(page, 
        text = 'Press here for a hint (-1 points)', 
        font = ("MS Sans Serif", 10),
        command = lambda: hint_activation(t_hint_label),
        height = 2, 
        width = 49)
    t_hint_button.place(x = 52, y = 250)

    points_label = tk.Label(page,
    text = "Score: " + str(points),
    font = ("MS Sans Serif", 10),
    wraplength = 400)
    points_label.place(x = 52, y = 355)
    
    t_countdown_label = tk.Label(page)
    t_countdown_label.place(x = 230, y = 70)
    t_countdown_label.config(height = 1, font = ('times', 20, 'bold'))
    page.pack()
    for k in numpy.arange(time_attack_seconds, 0, -0.1):
        t_countdown_label["text"] = round(k,2)
        time_attack_seconds -= 0.1
        page.update()
        time.sleep(0.1)
    
    transition(5)
    changepage()

def t_correct(root):
    global points
    global attempts
    page = tk.Frame(root, width = 500, height = 500)
    page.config(bg = "pale green")
    title_label= tk.Label(page, 
        text="Correct!",
        bg = "pale green",
        font=("MS Sans Serif", 35))
    title_label.place(x = 175, y = 0)

    point_value_label= tk.Label(page, 
        text = "The correct answer is: " + str(answer) + ". You have: " + str(points) + " points.",
        font = ("MS Sans Serif", 20),
        wraplength = 400,
        bg = "pale green",
        justify="left")
    point_value_label.place(x = 75, y = 70)
    page.pack()
    
    for q in numpy.arange(1, 0, -1):
        page.update()
        time.sleep(1)

    transition(7)
    changepage()

def t_incorrect(root):
    global points
    global attempts
    page = tk.Frame(root, width = 500, height = 500)
    page.config(bg = "pale green")
    title_label= tk.Label(page, 
        text="Correct!",
        bg = "pale green",
        font=("MS Sans Serif", 35))
    title_label.place(x = 175, y = 0)

    point_value_label= tk.Label(page, 
        text="The correct answer is: " + str(answer) + ". You have: " + str(points) + " points.",
        font=("MS Sans Serif", 20),
        wraplength = 400,
        bg = "pale green",
        justify="left")
    point_value_label.place(x = 75, y = 70)
    page.pack()
    
    for q in numpy.arange(1, 0, -1):
        page.update()
        time.sleep(1)

    transition(7)
    changepage()

def applications_home(root):
    page = tk.Frame(root, width = 500, height = 500)
    apps_background_image = tk.PhotoImage(file = "applications_background.png")
    apps_background_label = tk.Label(page, borderwidth = 15, relief = "ridge", image = apps_background_image)
    apps_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    apps_background_label.image = apps_background_image

    circle_app = tk.Button(page,
        text = "Circles",
        font = ("MS Sans Serif", 20),
        command = lambda:[transition(11), changepage()],
        height = 1,
        width = 5,
        borderwidth = 3, 
        relief = "solid")
    
    cones_app = tk.Button(page,
    text = "Cones",
    font = ("MS Sans Serif", 20),
    command = lambda:[transition(12), changepage()],
    width = 5,
    borderwidth=3, 
    relief="solid")

    cylinder_app = tk.Button(page,
    text = "Cylinders",
    font = ("MS Sans Serif", 13),
    height = 2,
    command = lambda:[transition(13), changepage()],
    width = 9,
    borderwidth=3, 
    relief="solid")

    circle_app.place(x = 200,y = 210)
    cones_app.place(x = 200, y = 280)
    cylinder_app.place(x = 200, y = 350)

    button= tk.Button(page, 
        text = 'Back', 
        font = ("MS Sans Serif", 10),
        command = lambda:[transition("Home"), changepage()], 
        height = 2, 
        width = 5)
    button.place(x = 5, y = 5)
    page.pack()

    page.pack()

def circle_apps(root):
    page = tk.Frame(root, width = 500, height = 500)

    circle_background_image = tk.PhotoImage(file = "circle_background.png")
    circle_background_label = tk.Label(page, borderwidth = 15, relief = "ridge", image = circle_background_image)
    circle_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    circle_background_label.image = circle_background_image

    button= tk.Button(page, 
        text = 'Back', 
        font=("MS Sans Serif", 10),
        command = lambda:[transition(10), changepage()], 
        height = 2, 
        width = 5)
    button.place(x = 5, y = 5)
    page.pack()

    page.pack()

def cone_apps(root):
    page = tk.Frame(root, width = 500, height = 500)
    cone_label = tk.PhotoImage(file = "cone_background.png")
    cone_image_label = tk.Label(page, borderwidth = 15, relief = "ridge", image = cone_label)
    cone_image_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    cone_image_label.image = cone_label

    button= tk.Button(page, 
        text = 'Back', 
        font = ("MS Sans Serif", 10),
        command = lambda:[transition(10), changepage()], 
        height = 2, 
        width = 5)
    button.place(x = 5, y = 5)
    page.pack()

def cylinder_apps(root):
    page = tk.Frame(root, width = 500, height = 500)

    cylinder_label = tk.PhotoImage(file = "cylinder_background.png")
    cylinder_image_label = tk.Label(page, borderwidth = 15, relief = "ridge", image = cylinder_label)
    cylinder_image_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    cylinder_image_label.image = cylinder_label

    button = tk.Button(page, 
        text = 'Back', 
        font = ("MS Sans Serif", 10),
        command = lambda:[transition(10), changepage()],  
        width = 5)
    button.place(x = 5, y = 5)

    page.pack()

def changepage():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        instructions(root)
    elif pagenum == 2:
        game(root)
    elif pagenum == 3:
        correct_page(root)
    elif pagenum == 4:
        incorrect_page(root)
    elif pagenum == 5:
        gameover_page(root)
    elif pagenum == 6:
        time_attack_page(root)
    elif pagenum == 7:
        t_game(root)
    elif pagenum == 8:
        t_correct(root)
    elif pagenum == 9:
        t_incorrect(root)
    elif pagenum == 10:
        applications_home(root)
    elif pagenum == 11:
        circle_apps(root)
    elif pagenum == 12:
        cone_apps(root)
    elif pagenum == 13:
        cylinder_apps(root)
    else:
        home_page(root)
        pagenum = 1
    pagenum = ""


pagenum = 1
root = tk.Tk()
root.geometry("500x500")
home_page(root)
root.mainloop()