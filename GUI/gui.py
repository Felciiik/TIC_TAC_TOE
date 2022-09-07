import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TIC TAC TOE")

root.columnconfigure([0, 1, 2, 3, 4], minsize=150, weight=1)
root.rowconfigure([0, 1, 2, 3, 4], minsize=150, weight=1)


frame_for_board = tk.Frame(
                        master=root,
                        relief=tk.GROOVE,
                        borderwidth=2,
                        width=500,
                        height=500
                        )

# frame_for_board_cells = tk.Frame(
#                         master=frame_for_board,
#                         relief=tk.RAISED,
#                         borderwidth=1
#                         )
# frame_for_board_cells.grid()
# cell_on_board = tk.Button(
#                         master=frame_for_board_cells,
#                         text="I am first button on grid",
#                         )
# cell_on_board.grid()

frame_for_buttons = tk.Frame(
                        master=root,
                        relief=tk.GROOVE,
                        borderwidth=1,
                        width=350,
                        height=350
                        )

label_row = tk.Label(master=frame_for_buttons, text="Choose row number:", relief=tk.GROOVE, borderwidth=2)
entry_row = tk.Entry(master=frame_for_buttons, width=5, relief=tk.GROOVE, borderwidth=2)
label_col = tk.Label(master=frame_for_buttons, text="Choose column number:", relief=tk.GROOVE, borderwidth=2)
entry_col = tk.Entry(master=frame_for_buttons, width=5, relief=tk.GROOVE, borderwidth=2)

ok_button = tk.Button(master=frame_for_buttons , text="OK")

frame_for_board.grid(column=0, row=0, columnspan=3, rowspan=5, padx=5, pady=5)
frame_for_buttons.grid(column=3, row=0, columnspan=2, rowspan=5, padx=5, pady=5)
label_row.grid(column=3, row=0, columnspan=1, rowspan=1, sticky="w")
entry_row.grid(column=4, row=0, columnspan=1, rowspan=1)
label_col.grid(column=3, row=1, columnspan=1, rowspan=1, sticky="w")
entry_col.grid(column=4, row=1, columnspan=1, rowspan=1)
ok_button.grid(column=3, row=3, columnspan=2, rowspan=1)

if __name__ == '__main__':
    root.mainloop()