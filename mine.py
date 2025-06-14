import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as m
from cryptography.fernet import Fernet


window=tk.Tk()
selected_file = False

window.title("ENCY&DECY Tool")

window_icon = tk.PhotoImage(file='img\\icons8-secured-file-24.png')
window.iconphoto(False, window_icon)

#FUNCTIONS
#file opening
def filename(): 
    global selected_file
    selected_file = fd.askopenfilename()

    if selected_file:  
        file_search_Button.config(image=tickMark_image, text="Selected", compound=tk.RIGHT)
        m.showinfo(
            title="selected file",
            message=selected_file
        )
    else: 
        file_search_Button.config(image=WrongMark_image, text="No file selected", compound=tk.RIGHT)
    
    

#encryption
def file_encryption_function():
    if selected_file: 
        with open(selected_file,'rb') as SF:
            file_data=SF.read()
            SF.close()
        key=Fernet.generate_key()
        fer=Fernet(key)
        encrypted_data = fer.encrypt(file_data)

        index_of_extension_ency = selected_file.rfind(".")
        extension_selected_file = selected_file[index_of_extension_ency:]

        m.showinfo(
            message="save encrypted file"
        )

        save_encrypted_file = fd.asksaveasfilename(defaultextension=f'{extension_selected_file}.enc',filetypes=[("Encrypted Files",f"*{extension_selected_file}.enc")],title="save encrypted file")
        
        with open(save_encrypted_file,'wb') as SEF:
            SEF.write(encrypted_data)
            SEF.close()
        create_key_file = save_encrypted_file[:-4] + ".key"
       
        with open(create_key_file,'wb') as CKF:
            CKF.write(key)
            CKF.close()
        m.showinfo(
            title="files saved as",
            message="encrypted file : " + save_encrypted_file +"\n" + "key file : " + create_key_file 
        )
        
    else:
        filename()
        

#decrypt
def file_decryption_function():
    if selected_file:

        if selected_file[-4:]==".enc":
            with open(selected_file,'rb') as SDF:
                encrypted_data=SDF.read()
                SDF.close()

            m.showinfo(
                title="select a key file",
                message="select sutiable key file for\n" + selected_file 
            )

            select_key_file=fd.askopenfilename(title="select a key file")

            with open(select_key_file,'rb')as SKF:
                key=SKF.read()
                SKF.close()

            fer=Fernet(key)
            decrypted_data=fer.decrypt(encrypted_data)

            decrypted_file_extension = selected_file[:-4]

            index_of_extension_decy = decrypted_file_extension.rfind(".")

            decrypted_file_extension = decrypted_file_extension[index_of_extension_decy:]

            m.showinfo(
                message="save decrypted file "
            ) 
            save_decrypted_file = fd.asksaveasfilename(defaultextension=decrypted_file_extension,title="save decrypted file")        
            
            with open(save_decrypted_file,"wb") as SDF:
                SDF.write(decrypted_data)
                SDF.close()

        else:
            m.showerror(
                title="select encrypted file",
                message=selected_file[-4:]+ " not supported\n"+"select '.enc' file"
            )
            filename()
    else:
        filename()
        


#window sizing
window.geometry('700x400')


#specifying rows in grid
window.grid_rowconfigure(0,weight=1)
window.grid_rowconfigure(1,weight=1)
window.grid_rowconfigure(2,weight=2)
window.grid_rowconfigure(3,weight=1)

#specifying columns in grid
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=4)
window.grid_columnconfigure(2,weight=1)
window.grid_columnconfigure(3,weight=4)
window.grid_columnconfigure(4,weight=1)

window.resizable(False,False)

window_title= tk.Label(window,text="File Encryption & Decryption Tool",font=('Arial',20),background='pink')
window_title.grid(row=0,column=1,columnspan=3,padx=10,pady=10)

file_search_Button= tk.Button(window,text="select file ",command=filename,bg='lightgray',font=('Arial',10))
file_search_Button.grid(row=1,column=1,columnspan=4,ipadx=10,ipady=5)

tickMark_image = tk.PhotoImage(file='img\\icons8-correct-20.png')

WrongMark_image = tk.PhotoImage(file='img\\icons8-wrong-20.png')

Encryption_Button= tk.Button(window,text="Encrypt",command=file_encryption_function,bg='lightblue',font=('Arial',10))
Encryption_Button.grid(row=2,column=1,ipadx=20,ipady=15)

Decryption_Button= tk.Button(window,text="Decrypt",command=file_decryption_function,bg='lightblue',font=('Arial',10))
Decryption_Button.grid(row=2,column=3,ipadx=20,ipady=15)


window.mainloop()
