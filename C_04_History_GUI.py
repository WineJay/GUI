from idlelib.history import History
from tkinter import *
from functools import partial # To prevent unwanted windows

class Converter():
    """
    Temperature conversion tool (°C to °F  or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame, text="History / Export",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", 14, "bold"),
                                     width=12, command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Opens history dialogue box and disables history button
        (so that user's can't create multiple history boxes).
        """
        HistoryExport(self)

class HistoryExport:

    """
    Displays history dialogue box
    """
    def __init__(self, partner):

        # setup dialogue box and background color
        green_back = "#D5E8D4"
        peach_back = "#ffe6cc"
        background = "#ffff00"

        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and releases history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # strings for 'long' labels....

        recent_intro_txt = ("Below are your recent calculations - showing "
                            "3 / 3 calculations. All Calculations are "
                            "shown to the nearest degree")

        export_instructions_txt = ("Please push <Export> to save your calculations in files. "
                                   "If the filename already exists, it will be")

        calculations = ""

        # label list ( label text | format | bg)
        history_labels_lists = [
            ["History / Export", ("Arial", 16, "bold"), None],
            [recent_intro_txt, ("Arial", 11) , None],
            ["calculation list", ("Arial", 14) , green_back],
            [export_instructions_txt, ("Arial", 11), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_lists):
            make_label = Label(self.history_box, text=item[0], font=item[1], bg=item[2],
                                wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

        # Retrieve export instruction label so that we can configure it to show the filenameif the user exports

        self

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", 12, "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)
        # List and loop to set background colour on
        # everything except for the buttons.
        recolour_list = [self.help_frame, self.help_heading_label, self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_history(self, partner):
        """
        Closes History box (and enables History / Export button)
        """
        # put help button back to normal...
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()