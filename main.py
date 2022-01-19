# New Sample Editor by Python
# you can Make this, see build Folder
# hope enjoy

from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter import messagebox as msg
from functools import partial
import threading
import subprocess
import py_compile

class notepad() :
    def __init__(self) :
        global path2
        
        self.root = Tk()
        self.root.geometry("700x500")
        self.password_lock = StringVar()
        self.scrol = ""
        self.text_z = ""
        self.editor = Text(self.root, width="300", height="90",bg = "black",fg = "green",selectbackground = "blue",tabs = 33,insertbackground = "green")
        self.scrol = Scrollbar(self.root)
        self.scrol.pack(side = "right" , fill = "y")
        self.scrol.config(command = self.editor.yview )
        self.editor.config(yscrollcommand = self.scrol.set)
        self.editor.pack(side = "top")
        
        self.font = ""
        self.mn = Menu(self.root)
        self.path = ""
        path2 = self.path
        self.imports = ['random','HHH','requests','tkinter']
               
    def class_code(self) :
        code_edit2 = self.editor.get('1.0' , '1.6')
        if code_edit2 != "" :
            pass
        else :
            for i in self.imports :
                i_koli2 = f"import {i}\n"
                self.editor.insert('0.1', i_koli2)
            self.editor.insert(END,'class main() :\n\tdef __init__(self) : \n\t\tpass\n\tdef run(self) : \n\t\tpass\n\nroot = main()\nroot.run()')
        
    def new_blank_file(self) :
        text_lengh = self.editor.get("0.1" , END)
        if len(text_lengh) > 1 :
            msg.showinfo("Save File" , "Are You Save the File ?")
        else :
            self.path = ""
            self.editor.delete('1.0',END)
            self.root.title("New File Black - Dark-Notepad - Not Save")

    def center_text(self) :
        self.editor.tag_configure("center",justify = "center")
        self.editor.tag_add("center","0.1","end")
        self.editor.pack()
        
    def right_text(self) :
        self.editor.tag_configure("right",justify = "right")
        self.editor.tag_add("right","0.1","end")
        self.editor.pack()        
    
    def left_text(self) :
        self.editor.tag_configure("left",justify = "left")
        self.editor.tag_add("left","0.1","end")
        self.editor.pack() 
        
    def open_file_notepad(self) :
        try :
            if self.path == "" :
                self.path = askopenfilename(title = "Open File")
                with open(self.path , "r") as open_read :
                    read_open_read = open_read.read()
                    self.editor.delete('1.0' , END)
                    self.editor.insert('1.0' , read_open_read)
                    open_read.close()
                self.root.title(self.path + " - Dark-Notepad - Not Save")
            elif self.path != "" :
                res_choose = msg.askquestion("Open File" , "Your Want Save This File ?")
                if res_choose == "yes" :
                    notepad.save_file_notepad(self)
                else :
                    self.path = askopenfilename(title = "Open File")
                    with open(self.path , "r") as open_read :
                        read_open_read = open_read.read()
                        self.editor.delete('1.0' , END)
                        self.editor.insert('1.0' , read_open_read)
                        open_read.close()
                    self.root.title(self.path + " - Dark-Notepad - Not Save")                    
        except :
            pass
    def inset_imports(self) :
        code_edit = self.editor.get('1.0', '1.6')
        if code_edit == "import" :
            pass
        else :
            for i in self.imports :
                i_koli = f"import {i}\n"
                self.editor.insert('1.0',i_koli)
    def save_file_notepad(self) :
        try :
            text_lengh_save = self.editor.get("0.1" , END)
            if len(text_lengh_save) < 2 :
                pass
            elif self.path != "" :
                with open(self.path,'w') as save_file :
                    code = self.editor.get('1.0' , END)
                    save_file.write(code)
                    save_file.close()
                self.root.title(self.path + " - Dark-Notepad - Save File")
                self.text_z = self.editor.get("0.1" , END)
            else :
                self.path = asksaveasfilename(filetypes = [('Python Files','*.py')])
                with open(self.path,'w') as save_file :
                    code = self.editor.get('1.0' , END)
                    save_file.write(code)
                    save_file.close()
                self.root.title(self.path + " - Dark-Notepad - Save File")
                self.text_z = self.editor.get("0.1" , END)
        except :
            pass                 
        
            
    def rev_text(self) :
        if self.text_z == "" :
            pass
        else :
            self.editor.delete("0.1" , END)
            self.editor.insert("0.1" , self.text_z)
            
    def c_sharp_style(self) :
        self.editor.insert('0.1' , "using System;\nusing System.Collections.Generic;\nusing System.Linq;\nusing System.Threading.Tasks;\n\nnamespace main\n{\n\tclass main\n\t{\n\t\tstatic void Main(String[] args)\n\t\t{\n\t\t\tConsole.WriteLine('hello world');\n\t\t}")
            
    def c_style(self) :
        self.editor.insert('0.1', "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nint main()\n{\n\t return 0;\n}")
    def cpp_style(self) :
        self.editor.insert('0.1', "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main(int argc, char *argv[])\n{\n\treturn 0;\n}")
    def c_plus_plus_style(self) :
        self.editor.insert('0.1', '#include <iostream>\n#include <string>\n#include <array>\n\nusing namespace std;\n\nint main()\n{\n\treturn 0;\n}')

    def php_style(self) :
        code_edit3 = self.editor.get('1.0', '1.5')
        if code_edit3 == "<?php" :
            pass
        else :
            self.editor.insert('0.1' , "<?php\n\n?>")
    
    def menu_bg_color_text(self) :
        color = askcolor(title = "Choose the Background Color Notepad")
        self.editor.config(bg = color[1])
        
    def menu_font_color(self) :
        color = askcolor(title = "Choose the colot text")
        self.editor.config(fg = color[1])
        
    def select_background(self) :
        color = askcolor(title = "Choose The Background Selection Text")
        self.editor.config(selectbackground = color[1])
        
    def info_des(self) :
        info_page = Toplevel(self.root)
        info_page.geometry("400x400")
        info_page.config(bg = "black")
        info_page.title("Dark Notepad Info")
        label_info = Label(info_page, text = "-- Welcome to the Dark Notepad --", bg = "black" , fg = "white").pack()
        label_info2 = Label(info_page , text = "The programm is a notepad with programming and best text", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "In Menu . you are select style language programming !", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "You Can Change the color text and background Programm", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "--------------------------------------------------------------------------", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "0o. Keyboard Help .o0", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Save File : [ Control + s ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Open File : [ Control + o ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "New File : [ Control + n ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Info Notepad : [ f5 ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Rev Text : [ Control + z ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Chnage Color Text : [ Control + e + t ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Chnage Background Notepad : [ Control + e + g ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Chnage Background Selection : [ Control + e + l ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Write Import Python : [ Control + l ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Write Style php : [ Control + c + p ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Write Style Class Python : [ Control + c + l ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Write Style C# : [ Control + c + s ]", bg = "black",fg = "white").pack()
        label_info2 = Label(info_page , text = "Good Luck !", bg = "black",fg = "white").pack()
        
    
    def lock_action(self) :
        if (self.password_lock.get() == "123") :
            self.lock_notepad.destroy()
        else :
            error_password_page = Toplevel(self.root)
            Label(error_password_page, text = 'Your password is not found !', bg = "black" , fg = "white").pack()
            
    def lock_notepad(self) :
        self.lock_notepad = Toplevel(self.root)
        self.lock_notepad.geometry("300x200")
        self.lock_notepad.config(bg = "black")
        Label(self.lock_notepad, text = "--- Lock Screen Dark Notepad ---", bg = "black", fg = "white").pack()
        Label(self.lock_notepad, text = "", bg = "black").pack()
        Label(self.lock_notepad, text = "password : ", bg = "black", fg = "white").pack()
        password = Entry(self.lock_notepad, textvariable = self.password_lock).pack()
        Label(self.lock_notepad, text = "", bg = "black").pack()
        btn = Button(self.lock_notepad, text = "Unlock" , command = partial(notepad.lock_action, self)).pack()
        
        
            
    def menu_code(self) :
        self.menu_code = Menu(self.mn , tearoff = 0, bg = "black", fg = "green" , activeborderwidth = "2", activebackground = 'blue', activeforeground = "white")
        self.mn.add_cascade(label = "Code" , menu = self.menu_code)
        self.menu_code.add_command(label = "Imports library", command = partial(notepad.inset_imports,self))
        self.menu_code.add_command(label = "Class Style", command = partial(notepad.class_code,self))
        self.menu_code.add_command(label = "php Style", command = partial(notepad.php_style,self))    
        self.menu_code.add_command(label = "C# Style", command = partial(notepad.c_sharp_style,self))    
        self.menu_code.add_command(label = "c++ Style", command = partial(notepad.c_plus_plus_style, self))
        self.menu_code.add_command(label = "c Style", command = partial(notepad.c_style, self))
        self.menu_code.add_command(label = "C++ style", command = partial(notepad.cpp_style, self))
    def menu_edit(self) :
        self.menu_edit = Menu(self.mn , tearoff = 0, bg = "black", fg = "green" , activeborderwidth = "2", activebackground = 'blue', activeforeground = "white")
        self.menu_edit.add_command(label = "Color Text", command = partial(notepad.menu_font_color,self))
        self.menu_edit.add_command(label = "Background Color Text", command = partial(notepad.menu_bg_color_text,self))
        self.menu_edit.add_command(label = "Background Select Text", command = partial(notepad.select_background,self))
        self.menu_edit.add_command(label = "Text Center", command = partial(notepad.center_text,self))
        self.menu_edit.add_command(label = "Text Right", command = partial(notepad.right_text,self))
        self.menu_edit.add_command(label = "Text left", command = partial(notepad.left_text,self))
        self.mn.add_cascade(label = "Edit" , menu = self.menu_edit)
    def menu_New(self) :
        self.menu_one = Menu(self.mn , tearoff = 0, bg = "black" , fg = "green",activeborderwidth = "2",activebackground='blue', activeforeground='white')
        self.menu_one.add_command(label = "New File" , command = partial(notepad.new_blank_file,self))
        self.menu_one.add_command(label = "Save File" , command = partial(notepad.save_file_notepad,self))
        self.menu_one.add_command(label = "Open File" , command = partial(notepad.open_file_notepad,self))
        self.menu_one.add_command(label = "Rev Text", command = partial(notepad.rev_text, self))
        self.menu_one.add_command(label = "Lock" , command = partial(notepad.lock_notepad,self))
        self.menu_one.add_command(label = "Info" , command = partial(notepad.info_des,self))
        self.mn.add_cascade(label = "New" , menu = self.menu_one)
        self.root.config(menu = self.mn)
    
    def keyboard_run(self) :
        self.root.bind("<Control-s>", lambda x: notepad.save_file_notepad(self))
        self.root.bind("<Control-o>", lambda x: notepad.open_file_notepad(self))
        self.root.bind("<Control-n>", lambda x: notepad.new_blank_file(self))
        self.root.bind("<F5>", lambda x: notepad.info_des(self))
        self.root.bind("<Control-z>" , lambda x: notepad.rev_text(self))
        self.root.bind("<Control-l>", lambda x: notepad.inset_imports(self))
        self.root.bind("<Control-c><p>", lambda x: notepad.php_style(self))
        self.root.bind("<Control-c><s>", lambda x: notepad.c_sharp_style(self))
        self.root.bind("<Control-p>", lambda x: notepad.c_plus_plus_style(self))
        self.root.bind("<Control-c>", lambda x: notepad.c_style(self))
        self.root.bind("<Control-c><l>", lambda x: notepad.class_code(self))
        self.root.bind("<Control-e><t>", lambda x: notepad.menu_font_color(self))
        self.root.bind("<Control-e><g>", lambda x: notepad.menu_bg_color_text(self))
        self.root.bind("<Control-e><l>", lambda x: notepad.select_background(self))     
        self.root.bind("<Control-Shift-Z>", lambda x: notepad.lock_notepad(self))     
        self.root.bind("<Control-Shift-z>", lambda x: notepad.lock_notepad(self))     
        
    def run(self) :
        self.root.title("Dark-Notepad")
        notepad.keyboard_run(self)
        notepad.menu_New(self)
        notepad.menu_edit(self)
        notepad.menu_code(self)
        # notepad.edit_text(self)
        # t1 = threading.Thread(target = notepad.edit_text, args = (self,))
        # t1.start()
        self.root.mainloop()    
        
notepad_start = notepad()
notepad_start.run()
