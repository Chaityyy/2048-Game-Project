#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import Frame, Label, CENTER
import LogicFinal as Lf
import Constants as c


# In[3]:


class Game2048(Frame):
    def __init__(self):
        
        Frame.__init__(self)
        
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)
        
        self.commands = {c.KeyUp: Lf.move_up, c.KeyDown: Lf.move_down, c.KeyLeft: Lf.move_left, c.KeyRight: Lf.move_right}
        
        self.gridCells = []
        self.initGrid()
        self.initMatrix()
        self.upgradeGridCells()
        
        self.mainloop()
        
    def initGrid(self):
        background = Frame(self, bg = c.Bkgd_Color_Game, width=c.size, height=c.size)
        background.grid()
        
        for i in range(c.Grid_Len):
            gridRow = []
            for j in range(c.Grid_Len):
                cell = Frame(background, bg = c.Bkgd_Color_EmptyCell, width=c.size/c.Grid_Len, height=c.size/c.Grid_Len)
                cell.grid(row=i, column=j, padx=c.Grid_Padding, pady=c.Grid_Padding)
                
                t = Label(master=cell, text="", bg = c.Bkgd_Color_EmptyCell, justify=CENTER, font=c.Font, width=5, height=2)
                t.grid()
                
                gridRow.append(t)
            self.gridCells.append(gridRow)
    
    def initMatrix(self):
        self.matrix = Lf.start_game()
        Lf.add_new_2(self.matrix)
        Lf.add_new_2(self.matrix)
        
    def upgradeGridCells(self):
        for i in range(c.Grid_Len):
            for j in range(c.Grid_Len):
                newNum = self.matrix[i][j]
                if newNum == 0:
                    self.gridCells[i][j].configure(text="", bg = c.Bkgd_Color_EmptyCell)
                else:
                    self.gridCells[i][j].configure(text=str(newNum), bg = c.Bkgd_Color_Dict[newNum], 
                                                   fg = c.Cell_Color_Dict[newNum])
        
        self.update_idletasks()
    
    def key_down(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[key](self.matrix)
            if changed:
                Lf.add_new_2(self.matrix)
                self.upgradeGridCells()
                changed = False
                
                if Lf.get_curr_state(self.matrix) == 'WON':
                    self.gridCells[1][1].configure(text="You", bg = c.Bkgd_Color_EmptyCell)
                    self.gridCells[1][2].configure(text="WON!", bg = c.Bkgd_Color_EmptyCell)
                    
                if Lf.get_curr_state(self.matrix) == 'LOST':
                    self.gridCells[1][1].configure(text="You", bg = c.Bkgd_Color_EmptyCell)
                    self.gridCells[1][2].configure(text="LOST!", bg = c.Bkgd_Color_EmptyCell)


# In[4]:


gamegrid = Game2048()


# In[ ]:




