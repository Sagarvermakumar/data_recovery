import customtkinter
from PIL import Image, ImageTk
import os



# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{1100}x{580}")
        self.title("Recover your data")
        
      # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        def findDrive():
            pass

   # create sidebar frame 
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)


        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Componey Name....",font=customtkinter.CTkFont(size=20,bg="red" weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Dashboard", font=customtkinter.CTkFont(size=18))
        self.logo_label.grid(row=1, column=0, padx=25, pady=(20, 10))

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Scan result", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=2, column=0, padx=20, pady=(20, 10))
        
       
########################################### sidebar work start ###################################################
        
        # scan result : row and column configurations 
        self.scan_result_frame = customtkinter.CTkFrame(self.sidebar_frame, width=100, corner_radius=2,border_color="red")
        self.scan_result_frame.grid(row=3, column=0,   sticky="nsew")
        self.scan_result_frame.grid_rowconfigure(3, weight=1)

    
# disk drive name

        self.disk_name =customtkinter.CTkLabel(master=self.scan_result_frame, text="User drive name")
        self.disk_name.grid(row=0, column=0, padx=20, pady=(20, 10))

# scan result : photo
        self.icon1_photo =customtkinter.CTkLabel(master=self.scan_result_frame, text="Ic")
        self.icon1_photo.grid(row=1, column=0, padx=2, pady=(20, 10))
       
        self.text_photo = customtkinter.CTkLabel(master=self.scan_result_frame, text="Photos")
        self.text_photo.grid(row=1, column=1,padx=2, pady=(20, 10))

        self.total_result_photo = customtkinter.CTkLabel(master=self.scan_result_frame, text="NOR")
        self.total_result_photo.grid(row=1, column=2, padx=20, pady=(20, 10))

# scan result : Videos
        self.icon_video =customtkinter.CTkLabel(master=self.scan_result_frame, text="Ic")
        self.icon_video.grid(row=2, column=0, padx=2, pady=(20, 10))
       
        self.video_text = customtkinter.CTkLabel(master=self.scan_result_frame, text="Videos")
        self.video_text.grid(row=2, column=1,padx=2, pady=(20, 10))

        self.total_result_video = customtkinter.CTkLabel(master=self.scan_result_frame, text="NOR")
        self.total_result_video.grid(row=2, column=2, padx=20, pady=(20, 10))

     

# scan result : Audios
        self.icon_audio =customtkinter.CTkLabel(master=self.scan_result_frame, text="Ic")
        self.icon_audio.grid(row=3, column=0, padx=2, pady=(20, 10))
       
        self.audio_text = customtkinter.CTkLabel(master=self.scan_result_frame, text="Audios")
        self.audio_text.grid(row=3, column=1,padx=2, pady=(20, 10))

        self.total_result_audio = customtkinter.CTkLabel(master=self.scan_result_frame, text="NOR")
        self.total_result_audio.grid(row=3, column=2, padx=20, pady=(20, 10))

     
# scan result : Documents
        self.icon_document =customtkinter.CTkLabel(master=self.scan_result_frame, text="Ic")
        self.icon_document.grid(row=4, column=0, padx=2, pady=(20, 10))
       
        self.document_text = customtkinter.CTkLabel(master=self.scan_result_frame, text="Documents")
        self.document_text.grid(row=4, column=1,padx=2, pady=(20, 10))

        self.total_result_document = customtkinter.CTkLabel(master=self.scan_result_frame, text="NOR")
        self.total_result_document.grid(row=4, column=2, padx=20, pady=(20, 10))

     
        
# scan result : Archives
        self.icon_document =customtkinter.CTkLabel(master=self.scan_result_frame, text="Ic")
        self.icon_document.grid(row=5, column=0, padx=2, pady=(20, 10))
       
        self.document_text = customtkinter.CTkLabel(master=self.scan_result_frame, text="Documents")
        self.document_text.grid(row=5, column=1,padx=2, pady=(20, 10))

        self.total_result_document = customtkinter.CTkLabel(master=self.scan_result_frame, text="NOR")
        self.total_result_document.grid(row=5, column=2, padx=20, pady=(20, 10))

     
# scan result : Others
        self.icon_others =customtkinter.CTkLabel(master=self.scan_result_frame, text="Ic")
        self.icon_others.grid(row=6, column=0, padx=2, pady=(20, 10))
       
        self.others_text = customtkinter.CTkLabel(master=self.scan_result_frame, text="Others")
        self.others_text.grid(row=6, column=1,padx=2, pady=(20, 10))

        self.total_result_others = customtkinter.CTkLabel(master=self.scan_result_frame, text="NOR")
        self.total_result_others.grid(row=6, column=2, padx=20, pady=(20, 10))

     
 ########################################### sidebar work end ###################################################       
        
    #  row and column configurations : top pannel
        

window = App()
window.mainloop()
