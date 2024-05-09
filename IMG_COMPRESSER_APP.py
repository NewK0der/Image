import tkinter as tk
import tkinter.ttk as ttk
import PIL
from PIL import Image
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import Tk, BOTH, Menu
from pdf2image import convert_from_path
import PyPDF4



class ImgCompressorApp:
    #pdf to Text convert
    def pdftotxt_convert(self):
        try:
            loc=self.file_loc.get()
            file=self.file_nam.get()
            txt_file=self.des_name.get()
            pdf = open(loc+"/"+file+".pdf","rb")
            text_file=open(txt_file+".txt","w")
            pdfreader=PyPDF4.PdfFileReader(pdf)
            x=pdfreader.numPages

            for page_num in range(x):
                page = pdfreader.getPage(page_num)
                text = page.extractText()
                print(text)
                text_file.writelines(text)
            text_file.close()
            messagebox.showinfo("Info","File Saved Successfully..")
        except:
            messagebox.showerror("Error","Invalid File or File location")
    
    #pdf to image convert
    def pdfconvert(self):
        try:
            loc = self.file_location.get()
            file = self.file_name.get()
            pdf_file = loc+'/'+file+'.pdf'
            pages = convert_from_path(pdf_file,500,poppler_path=r'C:\Program Files\poppler-23.07.0\Library\bin')
            img_file = pdf_file.replace(".pdf","")
            c = 0
            for page in pages:
                c+=1
                jpeg_file = img_file + "-" + str(c) + ".jpeg"
                page.save(jpeg_file,'JPEG')
            messagebox.showinfo("Info","File Saved Successfully..")
        except:
             messagebox.showerror("Error","Invalid File or File location")
    #Select File Function
    def select_file(self):
        try:
            self.file_path=askopenfilename()
            self.img=PIL.Image.open(self.file_path)
            self.myHeight,self.myWidth=self.img.size
            self.file_type=self.img.format
            self.file_name=self.img.filename
            self.select_con_file.configure(text=self.file_name.split("/")[-1])
            self.img=self.img.resize((self.myHeight,self.myWidth),PIL.Image.ANTIALIAS)
        except:
            #self.convert()
            messagebox.showerror("Error","Invalid File or File not selected")
            
    #File Resize
    def file_resize(self):
        i=self.img.resize((int(self.width.get()),int(self.height.get())))
        save_path=asksaveasfilename()
        extension=self.file_name.split(".")[-1]
        i.save(save_path+"_resized."+extension)
        messagebox.showinfo("Info","File Saved Successfully..")
        
    #File Convert
    def file_convert(self):
        file_type=self.type.get()
        save_path=asksaveasfilename()
        self.img=self.img.convert('RGB')
        if file_type=='PNG':
            self.img.save(save_path+"_converted.png")
            messagebox.showinfo("Info","File Saved Successfully..")
        elif file_type=='PDF':
            self.img.save(save_path+"_converted.pdf")
            messagebox.showinfo("Info","File Saved Successfully..")
        elif file_type=='JPEG':        
            self.img.save(save_path+"_converted.jpeg")
            messagebox.showinfo("Info","File Saved Successfully..")
        elif file_type=='GIF':        
            self.img.save(save_path+"_converted.gif")
            messagebox.showinfo("Info","File Saved Successfully..")
        else:
            messagebox.showerror("Error","Invalid File or File Not Selected")
        

    #File Compress
    def file_compress(self):
        
        save_path=asksaveasfilename()
        qlty=self.quality.get()
        
        if self.file_type=='PNG':        
            self.img.save(save_path+"_compressed.png",optimize= True,quality=qlty)
            messagebox.showinfo("Info","File Saved Successfully..")
        elif self.file_type=='JPEG':        
            self.img.save(save_path+"_compressed.jpeg",optimize= True,quality=qlty)
            messagebox.showinfo("Info","File Saved Successfully..")
        else:
            messagebox.showerror("Error","Invalid File or File Not Selected")


    #pdfcompress design
    def pdfcompress(self):
        self.pdfcompress_frame = tk.Frame(self.main)
        self.pdfcompress_frame.configure(
            background="#ffffff", height=200, width=200)
        self.select_com_icon = tk.Label(self.pdfcompress_frame)
        self.img_fileicon1 = tk.PhotoImage(file="file icon1.png")
        self.select_com_icon.configure(
            cursor="hand2",
            image=self.img_fileicon1,
            text='label1')
        self.select_com_icon.place(
            anchor="nw", height=120, width=120, x=190, y=10)
        self.quality = tk.Scale(self.pdfcompress_frame)
        self.quality.configure(
            background="#0080ff",
            cursor="hand2",
            digits=2,
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            from_=1,
            length=5,
            orient="horizontal",
            to=99)
        self.quality.place(anchor="nw", height=50, width=300, x=130, y=190)
        self.label7 = tk.Label(self.pdfcompress_frame)
        self.label7.configure(
            background="#0080ff",
            cursor="hand2",
            font="{Cambria} 14 {bold}",
            foreground="#ffffff",
            justify="center",
            text='QUALITY :')
        self.label7.place(anchor="nw", height=30, width=90, x=10, y=200)
        self.com_save = tk.Button(self.pdfcompress_frame)
        self.com_save.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SAVE'
            )
        self.com_save.place(anchor="nw", height=30, width=90, x=190, y=250)
        self.select_con_file = tk.Button(self.pdfcompress_frame)
        self.select_con_file.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SELECT FILE'
            )
        self.select_con_file.place(
            anchor="nw", height=30, width=120, x=190, y=140)
        self.pdfcompress_frame.place(anchor="nw", height=290, width=500, y=110)

        # Main widget
        self.mainwindow = self.main


    

    #pdf to text frame
    def pdftotxt(self):
        self.pfd_text_frame = tk.Frame(self.main)
        self.pfd_text_frame.configure(
            background="#ffffff", height=200, width=200)
        self.label11 = tk.Label(self.pfd_text_frame)
        self.label11.configure(
            background="#ffffff",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#000000",
            justify="left",
            text='File Location :')
        self.label11.place(anchor="nw", height=25, width=120, x=10, y=20)
        self.p_t_save = tk.Button(self.pfd_text_frame)
        self.p_t_save.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SAVE',
            command=self.pdftotxt_convert)
        self.p_t_save.place(anchor="nw", height=30, width=90, x=190, y=250)
        self.label12 = tk.Label(self.pfd_text_frame)
        self.label12.configure(
            background="#ffffff",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#000000",
            justify="left",
            text='File Name :')
        self.label12.place(anchor="nw", height=25, width=100, x=10, y=85)
        self.file_loc = tk.Entry(self.pfd_text_frame)
        self.file_loc.configure(
            background="#c0c0c0",
            font="{Arial} 12 {}",
            foreground="#000000")
        self.file_loc.place(anchor="nw", height=25, width=450, x=20, y=55)
        self.file_nam = tk.Entry(self.pfd_text_frame)
        self.file_nam.configure(
            background="#c0c0c0",
            font="{Arial} 12 {bold}",
            foreground="#000000")
        self.file_nam.place(anchor="nw", height=25, width=450, x=20, y=120)
        self.label13 = tk.Label(self.pfd_text_frame)
        self.label13.configure(
            background="#ffffff",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#000000",
            justify="left",
            text='Text file name :')
        self.label13.place(anchor="nw", height=25, width=120, x=20, y=150)
        self.des_name = tk.Entry(self.pfd_text_frame)
        self.des_name.configure(
            background="#c0c0c0",
            font="{Arial} 12 {bold}",
            foreground="#000000")
        self.des_name.place(anchor="nw", height=25, width=450, x=20, y=180)
        self.pfd_text_frame.place(anchor="nw", height=290, width=500, y=110)

    #Pdf to Image Frame
    def pdftoimg(self):
        self.pdf_to_image_frame = tk.Frame(self.main)
        self.pdf_to_image_frame.configure(
            background="#ffffff", height=200, width=200)
        self.label8 = tk.Label(self.pdf_to_image_frame)
        self.label8.configure(
            background="#ffffff",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#000000",
            justify="left",
            text='File Location :')
        self.label8.place(anchor="nw", height=25, width=130, x=10, y=20)
        self.p_i_save = tk.Button(self.pdf_to_image_frame)
        self.p_i_save.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SAVE',
            command=self.pdfconvert)
        self.p_i_save.place(anchor="nw", height=30, width=90, x=190, y=200)
        self.label9 = tk.Label(self.pdf_to_image_frame)
        self.label9.configure(
            background="#ffffff",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#000000",
            justify="left",
            text='File Name (without extention) :')
        self.label9.place(anchor="nw", height=25, width=230, x=20, y=100)
        self.file_location = tk.Entry(self.pdf_to_image_frame)
        self.file_location.configure(
            background="#c0c0c0",
            font="{Arial} 12 {}",
            foreground="#000000")
        self.file_location.place(anchor="nw", height=30, width=450, x=20, y=55)
        self.file_name = tk.Entry(self.pdf_to_image_frame)
        self.file_name.configure(
            background="#c0c0c0",
            font="{Arial} 12 {}",
            foreground="#000000")
        self.file_name.place(anchor="nw", height=30, width=450, x=20, y=135)
        self.pdf_to_image_frame.place(
            anchor="nw", height=290, width=500, y=110)

    
    #Resize Frame
    def resize(self):
        self.resize_frame = tk.Frame(self.main)
        self.resize_frame.configure(
            background="#ffffff", height=200, width=200)
        self.select_res_icon = tk.Label(self.resize_frame)
        self.img_fileicon1 = tk.PhotoImage(file="file icon1.png")
        self.select_res_icon.configure(
            cursor="hand2",
            image=self.img_fileicon1)
        self.select_res_icon.place(
            anchor="nw", height=120, width=120, x=190, y=10)
        self.label2 = tk.Label(self.resize_frame)
        self.label2.configure(
            background="#ffffff",
            cursor="hand2",
            font="{Cambria} 14 {bold}",
            foreground="#000000",
            justify="center",
            text='Width :')
        self.label2.place(anchor="nw", height=30, width=90, x=10, y=200)
        self.res_save = tk.Button(self.resize_frame)
        self.res_save.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SAVE',
            command=self.file_resize)
        self.res_save.place(anchor="nw", height=30, width=90, x=190, y=250)
        self.select_con_file = tk.Button(self.resize_frame)
        self.select_con_file.configure(
            background="#0000ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SELECT FILE',
            command=self.select_file)
        self.select_con_file.place(
            anchor="nw", height=30, width=120, x=190, y=140)
        self.label5 = tk.Label(self.resize_frame)
        self.label5.configure(
            background="#ffffff",
            cursor="hand2",
            font="{Cambria} 14 {bold}",
            foreground="#000000",
            justify="center",
            text='Hight :')
        self.label5.place(anchor="nw", height=30, width=90, x=280, y=200)
        self.width = tk.Spinbox(self.resize_frame)
        self.width.configure(
            background="#c0c0c0",
            font="{Cambria} 14 {}",
            foreground="#000000")
        self.width.place(
            anchor="nw",
            bordermode="outside",
            height=30,
            width=80,
            x=100,
            y=200)
        self.height = tk.Spinbox(self.resize_frame)
        self.height.configure(
            background="#c0c0c0",
            font="{Cambria} 14 {bold}",
            foreground="#000000")
        self.height.place(anchor="nw", height=30, width=80, x=370, y=200)
        self.resize_frame.place(anchor="nw", height=290, width=500, y=110)
        

    #compress design
    def compress(self):
        self.compress_frame = tk.Frame(self.main)
        self.compress_frame.configure(
            background="#ffffff", height=200, width=200)
        self.select_com_icon = tk.Label(self.compress_frame)
        self.img_fileicon1 = tk.PhotoImage(file="file icon1.png")
        self.select_com_icon.configure(
            cursor="hand2",
            image=self.img_fileicon1,
            text='label1')
        self.select_com_icon.place(
            anchor="nw", height=120, width=120, x=190, y=10)
        self.quality = tk.Scale(self.compress_frame)
        self.quality.configure(
            background="#0080ff",
            cursor="hand2",
            digits=2,
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            from_=1,
            length=5,
            orient="horizontal",
            to=99)
        self.quality.place(anchor="nw", height=50, width=300, x=130, y=190)
        self.label7 = tk.Label(self.compress_frame)
        self.label7.configure(
            background="#0080ff",
            cursor="hand2",
            font="{Cambria} 14 {bold}",
            foreground="#ffffff",
            justify="center",
            text='QUALITY :')
        self.label7.place(anchor="nw", height=30, width=90, x=10, y=200)
        self.com_save = tk.Button(self.compress_frame)
        self.com_save.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SAVE',
            command=self.file_compress)
        self.com_save.place(anchor="nw", height=30, width=90, x=190, y=250)
        self.select_con_file = tk.Button(self.compress_frame)
        self.select_con_file.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SELECT FILE',
            command=self.select_file)
        self.select_con_file.place(
            anchor="nw", height=30, width=120, x=190, y=140)
        self.compress_frame.place(anchor="nw", height=290, width=500, y=110)

        # Main widget
        self.mainwindow = self.main


    #Convert Design
    def convert(self):
        self.convert_frame = tk.Frame(self.main)
        self.convert_frame.configure(
            background="#ffffff", height=200, width=200)
        self.select_icon = tk.Label(self.convert_frame)
        self.img_fileicon1 = tk.PhotoImage(file="file icon1.png")
        self.select_icon.configure(
            cursor="hand2",
            image=self.img_fileicon1)
        self.select_icon.place(anchor="nw", height=120, width=120, x=190, y=10)
        self.label10 = tk.Label(self.convert_frame)
        self.label10.configure(
            background="#0080ff",
            cursor="hand2",
            font="{Cambria} 14 {bold}",
            foreground="#ffffff",
            justify="center",
            text='TYPE :')
        self.label10.place(anchor="nw", height=30, width=90, x=10, y=200)
        self.type = ttk.Combobox(self.convert_frame)
        self.type.configure(values='Select PNG JPEG PDF GIF',
                            background="#0080ff",
                            cursor="hand2",
                            font="{Cambria} 14 {bold}",
                            foreground="#ffffff",
                            justify="center",
                            state="readonly")
        self.type.insert(0,"Select")
        self.type.place(anchor="nw", height=30, x=120, y=200)
        self.con_save = tk.Button(self.convert_frame)
        self.con_save.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SAVE',
            command=self.file_convert)
        self.con_save.place(anchor="nw", height=30, width=90, x=190, y=250)
        self.select_con_file = tk.Button(self.convert_frame)
        self.select_con_file.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='SELECT FILE',
            command=self.select_file)
        self.select_con_file.place(
            anchor="nw", height=30, width=120, x=190, y=140)
        self.convert_frame.place(anchor="nw", height=290, width=500, y=110)

        # Main widget
        self.mainwindow = self.main


        
    


    
        
    def __init__(self, master=None):
        # build ui
        self.main = tk.Tk() if master is None else tk.Toplevel(master)
        self.main.configure(background="#ffffff", height=400, width=500)
        self.main.title("Document Operation")
        self.main.resizable(0,0)
        label3 = ttk.Label(self.main)
        self.img_logo = tk.PhotoImage(file="logo.png")
        label3.configure(image=self.img_logo, justify="center")
        label3.place(anchor="nw", height=50, width=50, x=0, y=0)
        label4 = ttk.Label(self.main)
        label4.configure(
            background="#0000ff",
            font="{Sylfaen} 16 {bold}",
            foreground="#ffffff",
            text='DOCUMENT OPERATION')
        label4.place(anchor="nw", height=50, width=450, x=51, y=0)
        '''self.res = tk.Button(self.main)
        self.res.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='RESIZE',
            command= self.resize)
        self.res.place(anchor="nw", height=30, width=80, x=180, y=60)'''
        self.pdf_bt = tk.Menubutton(self.main)
        self.pdf_bt.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='PDF')
        self.pdf_bt.place(anchor="nw", height=30, width=60, x=100, y=60)
        
        self.pdf_bt.menu=Menu(self.pdf_bt,tearoff=0)
        self.pdf_bt["menu"]=self.pdf_bt.menu
        self.pdf_bt.menu.add_command(label='Pdf to Image',
                                     background="#c0c0c0",
                                     font="{Cambria} 12 {bold}",
                                     foreground="#000000",
                                     command=self.pdftoimg)
        self.pdf_bt.menu.add_command(label='Pdf to Text',
                                     background="#c0c0c0",
                                     font="{Cambria} 12 {bold}",
                                     foreground="#000000",
                                     command=self.pdftotxt)
        self.pdf_bt.menu.add_command(label='Compress',
                                     background="#c0c0c0",
                                     font="{Cambria} 12 {bold}",
                                     foreground="#000000",
                                     command=self.pdfcompress)

        self.image_bt = tk.Menubutton(self.main)
        self.image_bt.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='Image')
        self.image_bt.place(anchor="nw", height=30, width=60, x=10, y=60)
        self.image_bt.menu=Menu(self.image_bt,tearoff=0)
        self.image_bt["menu"]=self.image_bt.menu
        self.image_bt.menu.add_command(label='CONVERT',
                                     background="#c0c0c0",
                                     font="{Cambria} 12 {bold}",
                                     foreground="#000000",
                                     command=self.convert)
        self.image_bt.menu.add_command(label='COMPRESS',
                                     background="#c0c0c0",
                                     font="{Cambria} 12 {bold}",
                                     foreground="#000000",
                                     command=self.compress)
        self.image_bt.menu.add_command(label='RESIZE',
                                     background="#c0c0c0",
                                     font="{Cambria} 12 {bold}",
                                     foreground="#000000",
                                     command=self.resize)
        
        '''self.com = tk.Button(self.main)
        self.com.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='COMPRESS',
            command=self.compress)
        self.com.place(anchor="nw", height=30, width=90, x=290, y=60)
        self.con = tk.Button(self.main)
        self.con.configure(
            background="#0080ff",
            compound="center",
            cursor="hand2",
            font="{Cambria} 12 {bold}",
            foreground="#ffffff",
            justify="center",
            text='CONVERT',
            command=self.convert)
        self.con.place(anchor="nw", height=30, width=90, x=400, y=60)'''
        
        

        # Main widget
        self.mainwindow = self.main

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = ImgCompressorApp()
    app.run()

