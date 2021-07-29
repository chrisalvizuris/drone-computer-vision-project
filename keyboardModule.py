import pygame


def init():
    """
    Initializes the pygame window. Needed in order for pygame to detect keys being pressed.

    :return: N/A
    """
    pygame.init()
    window = pygame.display.set_mode((350, 350))


def get_key(key_value):
    """
    Detects when a key is being pressed and formats as string.

    :param key_value: The keyboard key being pressed. Entered as a string in keyboardController.
    :return: Key pressed response
    """
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
