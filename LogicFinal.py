#!/usr/bin/env python
# coding: utf-8

# In[23]:


import random
def start_game():
    
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_new_2(mat):
    
    r = random.randint(0,3)
    c = random.randint(0,3)
    while( mat[r][c] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2
    
def get_curr_state(mat):
    
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
            
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'NOT OVER'
            
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i+1][j]:
                return 'NOT OVER'
            
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'NOT OVER'
        
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'NOT OVER'
        
    return 'LOST'


# In[24]:


def compress(mat):
    changed = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                mat[i][pos] = mat[i][j]
                if pos != j:
                    changed = True
                    mat[i][j] = 0
                pos += 1
    
    return mat, changed

def merge(mat):
    changed = True
    for i in range(4):
        for j in range(3):
            if mat[i][j] != 0 and mat[i][j] == mat[i][j+1]:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                changed = True
    
    return mat, changed

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


# In[35]:


def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    
    changed = changed1 or changed2
    
    new_grid, temp = compress(new_grid)
    return new_grid, changed

def move_right(grid):
    rev_grid = reverse(grid)
    new_grid, changed = move_left(rev_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed

def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

