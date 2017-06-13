#importing function file that
#contains all methods of edit, create, delete, etc
from funct_methoz import*

initiate t
start_root = Tk()
start_root.title("TODOList APPLICATION")#title
width_screen = start_root.winfo_screenwidth()
height_screen = start_root.winfo_screenheight()

# windows size:
width = 600
height = 200

#
x = (width_screen/2) - (width/2)
y = (height_screen/2) - (height/2)
start_root.geometry('%dx%d+%d+%d' % (width, height, x, y))
start_root.resizable(0, 0)

#===main function to start the application
if __name__ == '__main__':
    start_root.mainloop()
