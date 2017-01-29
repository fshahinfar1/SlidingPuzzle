import pygame, sys
import board
pygame.init()

size = width, height = 300, 300
white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
done = False
flag_win = False
#board
game_board = board.Board()

while not done:
    if not flag_win:
        flag_win = game_board.check_board_state()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
            break
        elif i.type == pygame.KEYDOWN:
            if not flag_win:
                if i.key == pygame.K_UP:
                    game_board.k_up()
                elif i.key == pygame.K_DOWN:
                    game_board.k_down()
                elif i.key == pygame.K_RIGHT:
                    game_board.k_right()
                elif i.key == pygame.K_LEFT:
                    game_board.k_left()
                elif i.key == pygame.K_ESCAPE:
                    done = True
                    break
            else:
                if i.key == pygame.K_ESCAPE:
                    done = True
                    break
                else:
                    game_board.shuffle()
                    flag_win = False
            
    # Draw
    screen.fill(black)
    game_board.draw(screen)
    if flag_win:
        font = pygame.font.SysFont("comic", 50, True, False)
        win_text = font.render("You Win", True, (250,100,25))
        w, h = win_text.get_rect().size
        w = w/2
        h = h/2
        text_pos = (150-w, 150-h)
        screen.blit(win_text, text_pos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()



