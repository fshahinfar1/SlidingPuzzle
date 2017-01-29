import pygame
import card
from random import randrange
tmp = [0, 1, 2, 3, 4, 5, 6, 7, 8]
white = (255, 255, 255)


class Board(object):
    def __init__(self):
        self.grid = []
        self.z_pos = [2, 2]
        lst_tmp = []
        count = 1
        self.cols , self.rows = 3, 3
        for i in range(self.cols):
            for j in range(self.rows):
                #index = randrange(len(tmp))
                #num = tmp[index]
                #new_card = card.Card(num)
                new_card = card.Card(count)
                lst_tmp.append(new_card)
                count += 1
                if count == 9:
                    count = 0
                #del tmp[index]
            self.grid.append(lst_tmp)
            lst_tmp = []
        self.pos = (50, 50)
        self.size = self.width, self.height = 200, 200
        self.shuffle()
    
    def shuffle(self):
        key_map = {0: self.k_up, 1: self.k_down, 2: self.k_left, 3: self.k_right}
        for t in range(100):
            x = randrange(4)
            key_map[x]()

    def change_cards(self, pos0, pos1):
        x0, y0 = pos0
        x1, y1 = pos1
        if x1 < 0 or y1 < 0 or x1 > 2 or y1 > 2:
            return
        self.grid[x0][y0], self.grid[x1][y1] = self.grid[x1][y1], self.grid[x0][y0]
        self.z_pos = pos1

    def get_zero(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j].num == 0:
                    return i, j
        return -1, -1

    def draw(self, screen):
        rect = [self.pos[0],self.pos[1],self.width,self.height]
        pygame.draw.rect(screen,white,rect)
        for i in range(3):
            for j in range(3):
                new_pos = [0,0]
                new_pos[0] = 3 + self.pos[0] + (j * 65)
                new_pos[1] = 3 + self.pos[1] + (i * 65)
                self.grid[i][j].draw(screen, new_pos)
    
    def k_up(self):
        new_pos = [0, 0]
        new_pos[0] = self.z_pos[0] + 1
        new_pos[1] = self.z_pos[1]
        self.change_cards(self.z_pos, new_pos)
    
    def k_down(self):
        new_pos = [0, 0]
        new_pos[0] = self.z_pos[0] -1
        new_pos[1] = self.z_pos[1]
        self.change_cards(self.z_pos, new_pos)
    
    def k_right(self):
        new_pos = [0, 0]
        new_pos[0] = self.z_pos[0]
        new_pos[1] = self.z_pos[1] - 1
        self.change_cards(self.z_pos, new_pos)
    
    def k_left(self):
        new_pos = [0, 0]
        new_pos[0] = self.z_pos[0]
        new_pos[1] = self.z_pos[1] + 1
        self.change_cards(self.z_pos, new_pos)
    
    def check_board_state(self):
        correct_rows = 0
        for i in range(self.rows):
            row = self.grid[i][:]
            if row[0].num != i + 1 + i * (self.cols - 1):
                continue  # check the next row this one is not correct
            flag = True
            for j in range(self.cols - 1):
                if row[j].num +1 != row[j+1].num:
                    if not ((i == self.rows - 1) and (j == self.cols -2) and (row[j+1].num == 0)):
                       flag = False 
                       break  # this row is not correct
            if flag:
                correct_rows += 1
        if correct_rows == self.rows:
            return True
        return False
