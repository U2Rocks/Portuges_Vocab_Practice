import tkinter as tk
import random
import time
from Language_Lists import verb_list

# text for buttons will be chosen from a list of words that is coded into the app

question_dict = {
    'adeus': 'goodbye',
    'hoje': 'today',
    'hora': 'hour',
    'longe': 'far',
    'mau': 'bad',
    'perto': 'near',
    'segundo': 'second',
    'talvez': 'maybe',
    'ontem': 'yesterday',
    'bom': 'good',
    'gato': 'cat',
    'semana': 'week',
    'amanhã': 'tomorrow',
    'fazer': 'make',
    'loga': 'shop',
    'sorrir': 'smile',
    'poder': 'can',
    'usar': 'use',
    'ir': 'go',
    'vir': 'come',
    'rir': 'laugh',
    'ver': 'see',
    'café': 'coffee',
    'cerveja': 'beer',
    'chá': 'tea',
    'vinho': 'wine',
    'não': 'no',
    'delicioso': 'delicious',
    'segunda-feira': 'monday',
    'terça-feira': 'tuesday',
    'quarta-feira': 'wednesday',
    'quinta-feira': 'thursday',
    'sexta-feira': 'friday',
    'sábado': 'saturday',
    'domingo': 'sunday',
    'maio': 'may',
    'janeiro': 'january',
    'fevereiro': 'feburary',
    'março': 'march',
    'abril': 'april',
    'junho': 'june',
    'julho': 'july',
    'agosto': 'august',
    'setembro': 'september',
    'outubro': 'october',
    'novembro': 'november',
    'dezembro': 'december',
    'água': 'water',
    'frango': 'chicken',
    'carneiro': 'lamb',
    'peixe': 'fish',
    'pé': 'foot',
    'perna': 'leg',
    'cabeça': 'head',
    'braço': 'arm',
    'mão': 'hand',
    'dedo': 'finger',
    'corpo': 'body',
    'estômago': 'stomach',
    'costas': 'back',
    'peito': 'chest',
    'enfermeira': 'nurse',
    'funcionário': 'employee',
    'policial': 'police officer',
    'cozinheiro': 'cook',
    'engenheiro': 'engineer',
    'médico': 'doctor',
    'gerente': 'manager',
    'professora': 'teacher',
    'programador': 'programmer',
    'vendedor': 'salesman',
    'ano': 'year',
    'bonito': 'beautiful',
    'feio': 'ugly',
    'difícil': 'dificult',
    'minuto': 'minute',
    'calendário': 'calendar',
    'sim': 'yes',
    'zunido': 'buzz',
    'felicidade': 'happiness',
    'paixão': 'passion',
    'mãe': 'mother',
    'alguém': 'someone',
    'verdade': 'truth',
    'ninguém': 'no one',
    'dinheiro': 'money',
    'outro': 'other',
    'apenas': 'only',
    'antes': 'before',
    'sempre': 'always',
    'também': 'also/too',
}

# this function runs when you press the start game button and initiates all other functions


def start_game():
    # get length of game for user or use default game length
    g_length = game_length.get()
    if g_length == 'Enter a Number between 1-20':
        g_length = 3
    else:
        g_length == int(g_length)
    print(g_length)
    # remove start button and game length entry box from window
    start_button.forget()
    game_length.forget()
    # this function will check our grabbed item list for any duplicates and continue the while loop if necessary

    def checkforduplicates(inputList):
        if len(inputList) == len(set(inputList)):
            return False
        else:
            return True
    # this function gets the text to be used for future functions

    def grab_items():
        global question_text_1
        global question_text_2
        global question_text_3
        global question_text_4
        global display_text
        # grab the four items to be used for the question
        # this while statement is designed to prevent duplicates
        Notchecked = True
        while Notchecked:
            answer_list = []
            for i in range(4):
                i = random.choice(list(question_dict.keys()))
                answer_list.append(i)
            # print(answer_list)
            Notchecked = checkforduplicates(answer_list)
            # print(Notchecked)
        random.shuffle(answer_list)
        # print(answer_list)
        display_text = question_dict[answer_list[0]]
        print("diplay text for comparison: " + display_text)
        random.shuffle(answer_list)
        question_text_1 = answer_list[0]
        question_text_2 = answer_list[1]
        question_text_3 = answer_list[2]
        question_text_4 = answer_list[3]
    # load text into buttons and create key interface items

    def load_items():
        reset_canvas_color()
        global ans_button_1
        global ans_button_2
        global ans_button_3
        global ans_button_4
        global question_display_text
        # load buttons for the four possible anwsers
        if canvas.find_all() == ():
            question_display_text = canvas.create_text(
                200, 100, fill="black", font="Helvetica 20 bold", text=display_text)
        else:
            canvas.itemconfigure(1, text=display_text)
        ans_button_1 = tk.Button(root, text=question_text_1, padx=100, pady=20, command=lambda: check_anwser(
            str(question_text_1)), font='Helvetica 12 bold')
        ans_button_2 = tk.Button(root, text=question_text_2, padx=100, pady=20, command=lambda: check_anwser(
            str(question_text_2)), font='Helvetica 12 bold')
        ans_button_3 = tk.Button(root, text=question_text_3, padx=100, pady=20, command=lambda: check_anwser(
            str(question_text_3)), font='Helvetica 12 bold')
        ans_button_4 = tk.Button(root, text=question_text_4, padx=100, pady=20, command=lambda: check_anwser(
            str(question_text_4)), font='Helvetica 12 bold')
        # pack buttons for answer
        ans_button_1.pack()
        ans_button_2.pack()
        ans_button_3.pack()
        ans_button_4.pack()
        # selecting our random anwsers
    # remove buttons and clear display text for next question

    def clear_board():
        ans_button_1.destroy()
        ans_button_2.destroy()
        ans_button_3.destroy()
        ans_button_4.destroy()
    # check if anwser is correct and initiate the clearing of the board

    def check_anwser(text_input):
        canvas_text = canvas.itemcget(1, 'text')
        print("Canvas Text: " + canvas_text)
        ans_check = str(question_dict[text_input])
        print("input anwser raw: " + text_input)
        print("input anwser value: " + ans_check)
        if ans_check == canvas_text:
            add_score(True)
            print("You get a Point!")
            time.sleep(.5)
        else:
            add_score(False)
            print("No Point Gained!")
            time.sleep(.5)
        print("-------------------------------------")
        clear_board()
        load_board()
        # this line of code determines the length of the game
        if turn == int(g_length):
            load_score_screen()
            iterate_score(0)
            iterate_turn(0)

    # iterate score for record keeping or reset score with 0
    def iterate_score(code):
        global score
        if code == 0:
            score = 0
        if code == 1:
            score = score + 1
    # iterate turn for record keeping or reset turn with 0

    def iterate_turn(code):
        global turn
        if code == 0:
            turn = 0
        if code == 1:
            turn = turn + 1
    # notifies user if person is wrong

    def wrong():
        canvas.configure(bg='red')
        canvas.update_idletasks()
    # notifies user if person is right

    def right():
        canvas.configure(bg='green')
        canvas.update_idletasks()

    def reset_canvas_color():
        canvas.configure(bg='#adc4c9')
    # add to score based on whether anwser is true or false

    def add_score(bool):
        global turn
        first_turn = "score" in globals()
        if first_turn == False:
            iterate_turn(0)
            iterate_score(0)
            print("score count started")
        if bool == True:
            right()
            # canvas.configure(bg='#adc4c9')
            iterate_score(1)
            iterate_turn(1)
            print("turn number: " + str(turn) + " and score is: " + str(score))
        if bool == False:
            wrong()
            # canvas.configure(bg='#adc4c9')
            iterate_turn(1)
            print("turn number: " + str(turn) + " and score is: " + str(score))
    # loads score screen and prompts user to exit or try again

    def load_score_screen():
        global play_again_button
        # max_score variable is used for score screen purposes only
        max_score = g_length
        final_message = "you scored " + \
            str(score) + " points out of " + str(max_score) + "!"
        canvas.itemconfigure(1, text=final_message)
        play_again_button = tk.Button(root, text="Click Here to Play Another Round!",
                                      padx=10, pady=10, command=reset_board, font='Helvetica 15 bold')
        play_again_button.pack()
        print("----------------------")
        print("End of Game Board Clear!")
        print("----------------------")
        clear_board()

    # clears score screen and restarts game
    def reset_board():
        play_again_button.forget()
        load_board()
        pass
    # get items and load the board

    def load_board():
        grab_items()
        load_items()

    # call functions for initial load
    load_board()
    # functions should be loaded 20 times in a row and then score is displayed
    # after score is displayed provide an option to go another round


# config root
root = tk.Tk()
root.title('Common Portuges Words Practice')
root.geometry('500x500')
root.minsize(400, 500)
root.maxsize(400, 500)
root.config(bg="blue")

# display start button and get game legnth
canvas = tk.Canvas(root, height=200, width=400, bg="#adc4c9")
start_button = tk.Button(root, text='Click here to start game',
                         command=start_game, font='Helvetica 12 bold')
game_length = tk.Entry(root, font='Helvetica 15 bold', justify='center')
game_length.insert(0, 'Enter a Number between 1-20')
# pack items onto starting screen
canvas.pack(side='top')
start_button.pack(side='top', pady=5)
game_length.pack(ipady=20, ipadx=60)

# call root loop to start application
root.mainloop()
