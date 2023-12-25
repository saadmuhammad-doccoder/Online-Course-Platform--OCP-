from tkinter import ttk
import tkinter as tk
import json

class LoginForm(ttk.Frame):
    def __init__(self,parent):
        super().__init__(master = parent)
        
        #initial variable which will manage the state of user if the user wants to log in or not.
        self.want_to_log_in = True
        
        #Custom styling
        button_style = ttk.Style()
        button_style.configure("Custom.TButton",
                foreground="#071013",
                background="#23B5D3",
                font=("Helvetica", 12))
        
        # Radiobtn  styling
        radio_button_style = ttk.Style()
        radio_button_style.configure("Custom.TRadiobutton",
                background="black",
                foreground="white",
                padding=10)
        
        
        ######################################################################
        #                          LOGIN FORM WIDGETS                        # ######################################################################
        
        
        # MAIN HEADER LABEL WIDGET
        self.__header_SignIn = ttk.Label(master = parent,
                                text = "SignIn",
                                foreground = "#23B5D3",
                                background = "#071013",
                                font = "Helvetica 32")
        
        # NAME LABEL WIDGET
        self.__username = ttk.Label(master = parent,
                                  background = '#071013',
                                  text = "Name: ",
                                  font = "Helvetica",
                                  foreground = "#23B5D3")
        
        # NAME ENTRY WIDGET
        self.__username_entry = ttk.Entry(master = parent,
                                        background = '#071013',
                                        font = "Helvetica")
        
        #PASSWORD LABEL WIDGET
        self.__password = ttk.Label(master = parent,
                                  background = '#071013',
                                  text = "Password: ",
                                  font = "Helvetica",
                                  foreground = "#23B5D3")
        
        # PASSWORD ENTRY WIDGET
        self.__password_entry = ttk.Entry(master = parent,
                                        background = '#071013',
                                        font = "Helvetica",
                                        show = "*")
        
        # LOGIN BTN WIDGET
        self.__login_button = ttk.Button(master = parent,
                                       text = "Sign In",
                                       style = "Custom.TButton",
                                       command = self.check_user_presence)

      
        
        
        self.initial_frame = tk.StringVar(value = False)
        # STATE TOGGLING RADIO BTN WIDGET ( IF USER WANTS TO REGISTER )
        self.__register = ttk.Radiobutton(master = parent,
                                          text = "Want to register?",
                                          variable = self.initial_frame,
                                          style="Custom.TRadiobutton",
                                          command = self.toggle_registration_form,
                                          value = True)
        
        # STATE TOGGLING RADIO BTN WIDGET ( IF USER WANTS TO LOGIN )
        self.__login = ttk.Radiobutton(master = parent,
                                          text = "Want to Login?",
                                          variable = self.initial_frame,
                                          style="Custom.TRadiobutton",
                                          command = self.toggle_login_form,
                                          value = False)
              
        
        #########################################################################                 PLACING STATE MANAGING BUTTONS                       #
        ########################################################################
        
        # PLACING STATE TOGGLING RADIO BTN FOR REGISTERING
        self.__register.place(relx = 0.3,
                                  rely = 0.2,
                                  height = 50,
                                  width = 130)
            
        # PLACING STATE TOGGLING RADIO BTN FOR LOGIN
        self.__login.place(rely = 0.2,
                               relx = 0.5,
                               height = 50,
                               width = 130)
        
        
        
        ######################################################################
        #                   REGISTRATION FORM WIDGETS                        # ######################################################################
        
        # HEADER LABEL ( REGISTER HERE! )
        self.__header_SignUp = ttk.Label(master = parent,
                                text = "SignUp",
                                foreground = "#23B5D3",
                                background = "#071013",
                                font = "Helvetica 32")
        
        self.__email_label = ttk.Label(master = parent,
                                text = "Enter email: ",
                                foreground = "#23B5D3",
                                background = "#071013",
                                font = "Helvetica")
        
        
        self.__email_entry = ttk.Entry(master = parent,
                                        background = '#071013',
                                        font = "Helvetica")
        
        # CONFIRM PASSWORD LABEL     
        self.__confirm_password = ttk.Label(master = parent,
                                  background = '#071013',
                                  text = " Confirm Password: ",
                                  font = "Helvetica",
                                  foreground = "#23B5D3")
        
        # CONFIRM PASSWORD ENTRY
        self.__confirm_password_entry = ttk.Entry(master = parent,
                                        background = '#071013',
                                        font = "Helvetica",
                                        show = "*")
        
          # REGISTER BTN WIDGET
        self.__register_button = ttk.Button(master = parent,
                                          text = "Register",
                                          style = "Custom.TButton",
                                          command = self.signup_user)
        
        self.__user_role = tk.StringVar(value = "Student")
        # RADIOBTN FOR CHOOSING ROLE ( AS AN INSTRUCTOR )
        self.__user_role_as_instructor = ttk.Radiobutton(master = parent,
                                           text = "Instructor",
                                           style = "Custom.TRadiobutton",
                                           value = "Instructor",
                                           variable = self.__user_role)
        
        # RADIOBTN FOR CHOOSING ROLE ( AS A STUDENT )
        self.__user_role_as_student = ttk.Radiobutton(master = parent,
                                           text = "Student",
                                           style = "Custom.TRadiobutton",
                                           value = "Student",
                                           variable = self.__user_role)
        
        
        # FRAME PLACING METHOD LOGINFORM
        self.place(relx = 0.5,
                   rely = 0.5,
                   anchor = "center")
            
    # METHOD USED FOR BTN TO CHECK IF THE USER EXISTS IN THE DATA STRUCTURE
    def check_user_presence(self):
        self.__username_of_user = self.__username_entry.get()
        self.__password_of_user = self.__password_entry.get()
        
        with open("reg_userdata.json","w") as f:
            data = json.load(f)
            for user_index in data:
                for user in user_index:
                    if user_index["username"] == self.__username_of_user and user_index["userpassword"] == self.__password_of_user:
                        print("Signed In")
                        return True
                    else:
                        print("Error occured")
                        return False
    
    # METHOD USED TO TOGGLE REGISTRATION FORM
    def toggle_login_form(self):
        
            # REMOVING UNNECESSARY WIDGETS
            self.__header_SignUp.place_forget()
            self.__register_button.place_forget()
            self.__confirm_password.place_forget()
            self.__confirm_password_entry.place_forget()
            self.__email_label.place_forget()
            self.__email_entry.place_forget()
            
            # PLACING HEADER
            self.__header_SignIn.place(relx = 0.4,
                            rely = 0.1,
                            height = 70,
                            width = 250)
            
            # PLACING USERNAME LABEL
            self.__username.place(relx = 0.15,
                                rely = 0.3)        
            
            # PLACING USERNAME ENTRY
            self.__username_entry.place(relx = 0.4,
                                    rely = 0.3)
            
            # PLACING PASSWORD LABEL
            self.__password.place(relx = 0.15,
                                rely = 0.4)
            
            # PLACING PASSWORD ENTRY 
            self.__password_entry.place(relx = 0.4,
                                    rely = 0.4)
            
            # PLACING LOGIN BUTTON
            self.__login_button.place(relx = 0.527,
                                    rely = 0.7,
                                    height = 30,
                                    width = 110)

    # METHOD USED TO TOGGLE LOGIN FORM          
    def toggle_registration_form(self):
            
            # REMOVING UNNECESSARY ITEMS FOR REGISTRATION
            self.__header_SignIn.place_forget()
            self.__login_button.place_forget()
            
            
            # ADDING WIDGETS FOR REGISTRATION
            self.__header_SignUp.place(relx = 0.4,
                            rely = 0.1,
                            height = 70,
                            width = 270)
            
             # PLACING USERNAME LABEL
            self.__username.place(relx = 0.15,
                                rely = 0.3)        
            
            # PLACING USERNAME ENTRY
            self.__username_entry.place(relx = 0.4,
                                    rely = 0.3)
            
            # PLACING PASSWORD LABEL
            self.__password.place(relx = 0.15,
                                rely = 0.4)
            
            # PLACING PASSWORD ENTRY 
            self.__password_entry.place(relx = 0.4,
                                    rely = 0.4)
            
            # PLACING CONFIRM PASSWORD LABEL
            self.__confirm_password.place(relx = 0.15,
                                          rely = 0.5)
            
            # PLACING CONFIRM PASSWORD ENTRY
            self.__confirm_password_entry.place(relx = 0.4,
                                                rely = 0.5)
            
            # PLACING EMAIL ADDRESS LABEL
            self.__email_label.place(relx = 0.15,
                                     rely = 0.6)
            
            # PLACING EMAIL ADDRESS ENTRY
            self.__email_entry.place(relx = 0.4,
                                     rely = 0.6)
            
            # PLACING USER ROLE BTN ( INSTRUCTOR )
            self.__user_role_as_instructor.place(relx = 0.3,
                                  rely = 0.7,
                                  height = 50,
                                  width = 130)
            
            # PLACING USER ROLE BTN ( STUDENT )
            self.__user_role_as_student.place(rely = 0.8,
                               relx = 0.5,
                               height = 50,
                               width = 130)
            
            # PLACING SIGNUP BTN
            self.__register_button.place(relx = 0.527,
                                    rely = 0.7,
                                    height = 30,
                                    width = 110)
            
    def signup_user(self):
        name = self.__username_entry.get()
        password = self.__confirm_password_entry.get()
        email = self.__email_entry.get()
        role = self.__user_role.get()
        check_presence = self.check_user_presence()
        if not check_presence:
            with open("reg_userdata.json","w") as f:
                data = json.load(f)
                for role in data:
                    if data[role] == self.__user_role:
                        user_data = {
                            "id" : role,
                            "username" : name,
                            "password" : password,
                            "email"  : email
                        }
                        data[role].dump(user_data)
                        print("Data saved")
                    else:
                        print("Error occured")
                    
