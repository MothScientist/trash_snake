import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from time import time
import logging
import disk_space
import input_validation
import file_conversion

# pip freeze > requirements.txt

logging.basicConfig(level=logging.DEBUG,
                    filename=f"{__name__}.log",
                    filemode='a',
                    format="%(filename)s - %(asctime)s - %(funcName)s - %(levelname)s: %(message)s"
                    )

logging.getLogger("matplotlib.font_manager").disabled = True  # To suppress log-trash from matplotlib
logging.getLogger('matplotlib.pyplot').disabled = True


def search_directory_window():
    window_main.withdraw()  # Closes parent window when opened

    window_search = tk.Toplevel(window_main)
    window_search["bg"] = "#075154"
    window_search.title("Search settings input window")
    window_search.geometry("400x230")
    window_search.resizable(width=False, height=False)

    font_1 = font.Font(family="Arial", size=11, weight="normal", slant="roman", underline=False, overstrike=False)

    # Labels
    list_directory_label = tk.Label(window_search, text="Select drive:",
                                    font=font_1, fg="white", bg="#075154")

    filename_label = tk.Label(window_search, text="Write filenames:",
                              font=font_1, fg="white", bg="#075154")

    keywords_label = tk.Label(window_search, text="Specify keywords*:",
                              font=font_1, fg="white", bg="#075154")

    list_directory_label.place(x=0, y=0)
    filename_label.place(x=0, y=30)
    keywords_label.place(x=0, y=60)

    # Buttons
    txt_checkbutton = ttk.Checkbutton(window_search, text=".txt")
    log_checkbutton = ttk.Checkbutton(window_search, text=".log")
    docx_checkbutton = ttk.Checkbutton(window_search, text=".docx")
    xlsx_checkbutton = ttk.Checkbutton(window_search, text=".xlsx")
    jpeg_checkbutton = ttk.Checkbutton(window_search, text=".jpeg")
    png_checkbutton = ttk.Checkbutton(window_search, text=".png")
    ico_checkbutton = ttk.Checkbutton(window_search, text=".ico")
    pdf_checkbutton = ttk.Checkbutton(window_search, text=".pdf")
    djvu_checkbutton = ttk.Checkbutton(window_search, text=".djvu")
    odt_checkbutton = ttk.Checkbutton(window_search, text=".odt")

    start_button = tk.Button(window_search, text="START SEARCH",
                             font=font.Font(family="Arial", size=15, weight="normal", slant="roman",
                                            underline=False, overstrike=False), fg="white", bg="#075154")

    txt_checkbutton.place(x=20, y=100)
    log_checkbutton.place(x=100, y=100)
    docx_checkbutton.place(x=180, y=100)
    xlsx_checkbutton.place(x=260, y=100)
    pdf_checkbutton.place(x=340, y=100)
    jpeg_checkbutton.place(x=20, y=130)
    png_checkbutton.place(x=100, y=130)
    ico_checkbutton.place(x=180, y=130)
    djvu_checkbutton.place(x=260, y=130)
    odt_checkbutton.place(x=340, y=130)

    start_button.place(x=120, y=180)

    # Input Fields
    # <name>.get() - to get the selected value
    list_directory_combobox = ttk.Combobox(window_search, width=10, values=disk_space.scan_disks(), state="readonly")

    check_filename_entry = (window_search.register(input_validation.check_filename), "%P")
    filename_entry = ttk.Entry(window_search, width=38, validate="key", validatecommand=check_filename_entry)

    check_keywords_entry = (window_search.register(input_validation.check_keywords), "%P")
    keywords_entry = ttk.Entry(window_search, width=35, validate="key", validatecommand=check_keywords_entry)

    list_directory_combobox.place(x=100, y=6)
    filename_entry.place(x=122, y=35)
    keywords_entry.place(x=140, y=65)

    window_search.protocol("WM_DELETE_WINDOW", lambda: [window_main.deiconify(),
                                                        window_search.destroy()])
    # When the window is closed, it goes completely out of memory and the parent window returns.


def storage_info_window():
    window_main.withdraw()  # Closes parent window when opened

    window_storage_info = tk.Toplevel(window_main)
    window_storage_info["bg"] = "#F0AD87"
    window_storage_info.title("Disk space information")
    window_storage_info.geometry("550x400")
    window_storage_info.resizable(width=False, height=False)

    # Create list wint string with info about storage
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

    # Input Field
    check_keywords_entry = (window_storage_info.register(input_validation.check_filename), "%P")

    filename_entry = ttk.Entry(window_storage_info, width=41, validate="key", validatecommand=check_keywords_entry)

    filename_entry.place(x=88, y=359)

    def data_processing_png():
        try:
            save_directories = filedialog.askdirectory(parent=window_storage_info, title='Select directories')
            filename = filename_entry.get()
            if len(filename) == 0:
                filename = "MemoryInfo"
            disk_space.space_on_disks_graph(save_directories, filename)
            logging.debug(f"Device memory data saved successfully: {save_directories}/{filename}")
        except Exception as e:
            logging.error(f"Image save error: {e}")

    def data_processing_txt():
        try:
            save_directories = filedialog.askdirectory(parent=window_storage_info, title='Select directories')
            filename = filename_entry.get()
            if len(filename) == 0:
                filename = "MemoryInfo"
            with open(f"{save_directories}/{filename}.txt", "w") as file:
                file.write(f"""+-----------------+\n{datetime.fromtimestamp(time())}\n+-----------------+\n""")
                file.write(info_disk_list)
                logging.debug(f"Device memory data saved successfully: {save_directories}/{filename}")
        except Exception as e:
            logging.error(f"Error writing to file: {e}")

    # Buttons
    save_png_button = tk.Button(window_storage_info, text=".png", width=14,
                                font=font.Font(family="Arial", size=10, weight="bold", slant="italic",
                                               underline=False, overstrike=False), fg="#783B36", bg="#FD766A",
                                command=data_processing_png)

    save_txt_button = tk.Button(window_storage_info, text=".txt", width=14,
                                font=font.Font(family="Arial", size=10, weight="bold", slant="italic",
                                               underline=False, overstrike=False), fg="#783B36", bg="#FD766A",
                                command=data_processing_txt)

    save_png_button.place(x=425, y=340)
    save_txt_button.place(x=425, y=370)

    # Labels
    main_info_label = tk.Label(window_storage_info, text=info_disk_list,
                               font=font.Font(family="Arial", size=14, weight="normal", slant="roman",
                                              underline=False, overstrike=False), fg="#783B36", bg="#F0AD87")

    input_label = tk.Label(window_storage_info, text="You can save this data by entering a name for the file below:",
                           font=font.Font(family="Arial", size=12, weight="normal", slant="roman",
                                          underline=True, overstrike=False), fg="#783B36", bg="#F0AD87")

    filename_label = tk.Label(window_storage_info, text="Filename:",
                              font=font.Font(family="Arial", size=12, weight="normal", slant="italic",
                                             underline=False, overstrike=False), fg="#783B36", bg="#F0AD87")

    save_label = tk.Label(window_storage_info, text="save as...",
                          font=font.Font(family="Arial", size=12, weight="normal", slant="italic",
                                         underline=False, overstrike=False), fg="#783B36", bg="#F0AD87")

    main_info_label.place(x=0, y=0)
    input_label.place(x=0, y=325)
    filename_label.place(x=10, y=356)
    save_label.place(x=340, y=355)

    window_storage_info.protocol("WM_DELETE_WINDOW", lambda: [window_main.deiconify(),
                                                              window_storage_info.destroy()])
    # When the window is closed, it goes completely out of memory and the parent window returns.


def file_conversion_window():
    window_main.withdraw()  # Closes parent window when opened

    window_file_conversion = tk.Toplevel(window_main)
    window_file_conversion["bg"] = "#20232A"
    window_file_conversion.title("File conversion")
    window_file_conversion.geometry("200x100")
    window_file_conversion.resizable(width=False, height=False)

    def types_conversion():
        try:
            match var.get():
                case ".docx to .txt":
                    file_conversion.docx_to_txt(filedialog.askopenfilename(filetypes=[("Word documents", "*.docx")]))
                case ".pdf to .txt":
                    file_conversion.pdf_to_txt(filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))
                # case ".pdf to .mp3":
                #     file_conversion.pdf_to_mp3(filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))
                # case ".txt to .mp3":
                #     file_conversion.txt_to_mp3(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]))
                case ".png to .ico":
                    file_conversion.png_to_ico(filedialog.askopenfilename(filetypes=[("PNG files", "*.png")]))
        except FileNotFoundError:
            messagebox.showerror("Error!", "File not found")
        else:
            messagebox.showinfo("Result", "Successfully!")

    option_list = [
        ".docx to .txt",
        ".pdf to .txt",
        # ".pdf to .mp3",
        # ".txt to .mp3",
        ".png to .ico"
    ]

    # Labels
    select_label = tk.Label(window_file_conversion, text="Select conversion type:",
                            font=font.Font(family="Arial", size=12, weight="normal", slant="roman",
                                           underline=False, overstrike=False), fg="#59F5EA", bg="#20232A")

    select_label.place(x=17, y=0)

    # Buttons
    start_button = tk.Button(window_file_conversion, text="Convert File",
                             font=font.Font(family="Arial", size=12, weight="normal", slant="roman",
                                            underline=False, overstrike=False), fg="white", bg="#20232A",
                             command=types_conversion)

    start_button.place(x=50, y=55)

    # Input Fields
    var = tk.StringVar()
    # var.trace("w", types_conversion)
    combo_box = ttk.Combobox(window_file_conversion, textvariable=var)
    combo_box['values'] = option_list
    combo_box.current(0)
    combo_box.place(x=32, y=27)

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
