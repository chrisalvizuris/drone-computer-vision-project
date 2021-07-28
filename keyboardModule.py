import pygame


# pygame is a library used to create python games
# in order for pygame to detect keys being pressed, we must create a game window


def init():
    pygame.init()
    window = pygame.display.set_mode((350, 350))


def get_key(key_value):
    answer = False
    for event in pygame.event.get(): pass
    key_input = pygame.key.get_pressed()
    my_key = getattr(pygame, 'K_{}'.format(key_value))
    if key_input[my_key]:
        answer = True
    pygame.display.update()
    return answer


def main():
    if get_key('LEFT'):
        print('Left key pressed')
    if get_key('RIGHT'):
        print('Right key pressed')


if __name__ == '__main__':
    init()
    while True:
        main()
