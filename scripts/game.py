import pygame
import time

pygame.init()

# scale to window size
window_width = 720
window_height = 720

window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption('Coffee Game')
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 30, True)

start_time = time.time()
time_elapsed = 0.00
weight = 0.00
clicks = []

running = True
while running:
    pygame.time.delay(100)
    window_width = window.get_width()
    window_height = window.get_height()
    if time_elapsed > 60:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'escape':
                running = False
            if pygame.key.name(event.key) == 'space':
                weight += 1
                clicks.append((time.time() - start_time, weight))

    window.fill((255, 255, 255))

    # draw x and y axis
    pygame.draw.line(window, (0, 0, 0), (50, window_height // 2), (window_width - 50, window_height // 2), 2)
    pygame.draw.line(window, (0, 0, 0), (50, 50), (50, window_height - 50), 2)

    # draw x and y axis labels
    time_elapsed = time.time() - start_time
    text = font.render(str(time_elapsed), 1, (0, 0, 0))
    window.blit(text, (100, 100))

    # plot clicks
    for i in range(len(clicks)):
        x = 50 + int(clicks[i][0] * 100)  # scale time to pixels
        y = window_height // 2 - int(clicks[i][1] * 10)  # scale clicks to pixels
        pygame.draw.circle(window, (255, 0, 0), (x, y), 5)

        # interpolate line between clicks
        if i < len(clicks) - 1:
            next_x = 50 + int(clicks[i + 1][0] * 100)
            next_y = window_height // 2
            pygame.draw.line(window, (0, 255, 0), (x, y), (next_x, next_y), 2)

            # calculate interpolated y values
            num_intermediate_points = next_x - x
            for j in range(num_intermediate_points):
                intermediate_x = x + j
                intermediate_y = y + (next_y - y) * j // num_intermediate_points
                pygame.draw.circle(window, (0, 0, 255), (intermediate_x, intermediate_y), 3)

    text = font.render(str(weight), 1, (0, 0, 0))
    window.blit(text, (100, 200))

    pygame.display.flip()  # update the display
    clock.tick(60)  # limit the fps to 60

pygame.quit()
