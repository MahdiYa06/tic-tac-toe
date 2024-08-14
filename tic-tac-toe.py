import tkinter as tk



window = tk.Tk()
window.title('tic-tac-toe')

def points():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    label_player_1 = tk.Label(board_frame, text='Player 1', font=('Aviny', 16), padx=10)
    label_player_2 = tk.Label(board_frame, text='Player 2', font=('Aviny', 16), padx=10)
    label_player_1.grid(row=0, column=0)
    label_player_2.grid(row=0, column=2)
    
    
    
    point_frame = tk.Frame(window)
    point_frame.grid(row=1) 
    p1_point = tk.Label(point_frame, padx=20, text='0')
    p2_point = tk.Label(point_frame, padx=20, text='0')    
    p1_point.grid(row=0, column=0)
    p2_point.grid(row=0, column=1)
    
    
    
def board():
    buttons = []
    counter = 0
    board_frame = tk.Frame(window)
    board_frame.grid(row=2)
    
    for row in range(1, 4):
        for column in range(1, 4):
            index = counter
            buttons.append(index)
            buttons[index] = tk.Button(board_frame, text=f'btn {index}')
            buttons[index].config(width = 10, height = 4, font = ('None', 18, 'bold'))
            buttons[index].grid(row = row, column = column)
            
            counter += 1
    
points()
board()

window.mainloop()