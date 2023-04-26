import tkinter as tk
from tkinter import ttk
import logging
import disk_space

# pip freeze > requirements.txt

logging.basicConfig(level=logging.DEBUG,
                    filename=f"{__name__}.log",
                    filemode='a',
                    format="%(filename)s - %(asctime)s - %(funcName)s - %(levelname)s: %(message)s"
                    )
logging.getLogger("matplotlib.font_manager").disabled = True  # To suppress log-trash from matplotlib
logging.getLogger('matplotlib.pyplot').disabled = True


def search_directory_window():
    def check_filename(name):
        pass  # validation of input in windows

    def check_keywords(name):
        pass

    window_main.withdraw()  # Closes parent window when opened

    window_search = tk.Toplevel(window_main)
    window_search["bg"] = "#075154"
    window_search.title("Search settings input window")
    window_search.geometry("400x300")
    window_search.resizable(width=False, height=False)

    # Labels
    list_directory_label = tk.Label(window_search, text="Select drive:",
                                    font=9, fg="white", bg="#075154")

    filename_label = tk.Label(window_search, text="Write filenames:",
                              font=9, fg="white", bg="#075154")

    keywords_label = tk.Label(window_search, text="Specify keywords*:",
                              font=9, fg="white", bg="#075154")

    list_directory_label.place(x=10, y=10)
    filename_label.place(x=10, y=50)
    keywords_label.place(x=10, y=90)

    # Buttons

    # Input Fields
    # <name>.get() - to get the selected value
    list_directory_combobox = ttk.Combobox(window_search, values=disk_space.scan_disks(), state="readonly")

    check_filename_entry = (window_search.register(check_filename), "%P")
    filename_entry = ttk.Entry(window_search, width=32, validate="key", validatecommand=check_filename_entry)

    check_keywords_entry = (window_search.register(check_keywords), "%P")
    keywords_entry = ttk.Entry(window_search, width=30, validate="key", validatecommand=check_keywords_entry)

    list_directory_combobox.place(x=110, y=10)
    filename_entry.place(x=145, y=50)
    keywords_entry.place(x=157, y=90)

    window_search.protocol("WM_DELETE_WINDOW", lambda: [window_main.deiconify(),
                                                        window_search.destroy()])
    # When the window is closed, it goes completely out of memory and the parent window returns.


def storage_info_window():
    window_main.withdraw()  # Closes parent window when opened

    window_storage_info = tk.Toplevel(window_main)
    window_storage_info["bg"] = "#8B470B"
    window_storage_info.title("Disk space information")
    window_storage_info.geometry("550x400")
    window_storage_info.resizable(width=False, height=False)

    #
    # disks = disk_space.scan_disks()
    storages = list(str(i[:2]) for i in disk_space.scan_disks())
    storage_area = []
    for storage in storages[:8]:
        temp_area = disk_space.storage_info(storage)
        storage_area.append(f" {temp_area[0]:.{2}f} Gb"
                            f" | Used: {temp_area[1]:.{2}f} Gb"
                            f" | Free: {temp_area[2]:.{2}f} Gb")
    info_disk_list = ""
    for i in range(len(storages)):
        info_disk_list += storages[i] + storage_area[i] + "\t\n\n"
    #

    # Labels
    main_info_label = tk.Label(window_storage_info, text=info_disk_list,
                               font=8, fg="white", bg="#8B470B")

    main_info_label.place(x=0, y=0)

    window_storage_info.protocol("WM_DELETE_WINDOW", lambda: [window_main.deiconify(),
                                                              window_storage_info.destroy()])
    # When the window is closed, it goes completely out of memory and the parent window returns.


def file_conversion_window():
    window_main.withdraw()  # Closes parent window when opened
    window_file_conversion = tk.Toplevel(window_main)
    window_file_conversion["bg"] = "#898B0B"
    window_file_conversion.title("File conversion")
    window_file_conversion.geometry("400x300")
    window_file_conversion.resizable(width=False, height=False)
    window_file_conversion.protocol("WM_DELETE_WINDOW", lambda: [window_main.deiconify(),
                                                                 window_file_conversion.destroy()])
    # When the window is closed, it goes completely out of memory and the parent window returns.


logging.info("\n-----   Program launched   -----")

window_main = tk.Tk()
window_main["bg"] = "#420C5D"
window_main.title("Trash snake")
# window_main.iconbitmap('.ico')
window_main.geometry("400x300")
window_main.resizable(width=False, height=False)

mainmenu = tk.Menu(window_main)
window_main.config(menu=mainmenu)

settingsmenu = tk.Menu(mainmenu, tearoff=0)
settingsmenu.add_command(label="Change language")

helpmenu = tk.Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Documentation")
helpmenu.add_command(label="User guide")

othermenu = tk.Menu(mainmenu, tearoff=0)
othermenu.add_command(label="About")
othermenu.add_command(label="Feedback")
othermenu.add_command(label="Open logs")
othermenu.add_command(label="Clear logs")

mainmenu.add_cascade(label="Settings", menu=settingsmenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)
mainmenu.add_cascade(label="Other", menu=othermenu)


# Buttons
search_main_button = tk.Button(window_main, text="Search directory/file", fg="black", bg="white",
                               font=("Century Gothic", 12), command=search_directory_window)
storage_info_button = tk.Button(window_main, text="Info about my storage", fg="black", bg="white",
                                font=("Century Gothic", 12), command=storage_info_window)

file_conversion_button = tk.Button(window_main, text="File conversion", fg="black", bg="white",
                                   font=("Century Gothic", 12), command=file_conversion_window)

search_main_button.place(x=125, y=50)
storage_info_button.place(x=117, y=100)
file_conversion_button.place(x=147, y=150)


# Labels
main_window_label = tk.Label(window_main, text="Made by https://github.com/MothScientist",
                             font=("Century Gothic", 10), fg="white", bg="#420C5D")
main_window_label.place(x=62, y=280)


window_main.mainloop()


# disks = info_about_system.scan_disks()
# patterns = [r"build"]  # document keywords
# extensions = [r"txt"]  # document extension
# path_to_file = file_search.search_files(info_about_system.scan_disks(), patterns, extensions)
# txt_path, doc_path, pdf_path = file_search.sort_files_extensions(path_to_file)
# search = file_search.DocSearching(patterns)
# search.search_in_txt(txt_path)
# info_about_system.space_on_disks_graph("W:/trash_snake_project/updates", "MyMemory")
