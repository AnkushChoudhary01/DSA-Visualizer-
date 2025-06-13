import pygame
import random
from config import WIDTH, HEIGHT, BACKGROUND_COLOR, BAR_COLOR
from sorting import bubble_sort, insertion_sort ,selection_sort, merge_sort, quick_sort

# Initiallize pygame
pygame.init()

# Create the Pygame window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Bar Visualizer")

# Clock to control frame rate
clock = pygame.time.Clock()

# Generate a list of random number representing bars height 
def generate_array(n):
    return [random.randint(50, HEIGHT - 50) for _ in range(n)]

# Draw bars according to current state of the array
def draw_bars(arr):
    win.fill(BACKGROUND_COLOR)  #clear screen with background color
    bar_width = WIDTH // len(arr) #Calculated width for each bar

    for i, val in enumerate(arr):
        # Draw each bars as a vertical rectangle
        pygame.draw.rect(win, BAR_COLOR, (i * bar_width, HEIGHT - val, bar_width - 2, val)) # Position and Size

    pygame.display.update() # refresh screen

def main():
    print("Visualizer started...")
    array = generate_array(50) # Initiate random Bars
    sorting = True # whether sorting is currently active 
    running = True # Main Loop control
    algorithm = "bubble" # Default algo

    while running:
        clock.tick(60) # Run Loop at 60 FPS
        draw_bars(array) # it draws current state of bars

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    algorithm = "bubble"
                    print("Algorithm set to Bubble Sort")

                elif event.key == pygame.K_i:
                    algorithm = "insertion"
                    print("Algorithm set to Insertion Sort")

                elif event.key == pygame.K_s:
                    algorithm = "selection"
                    print("Algorithm set to Selection Sort")

                elif event.key == pygame.K_m:
                    algorithm = "merge"
                    print("Algorithm set to Merge Sort")

                elif event.key == pygame.K_q:
                    algorithm = "quick"
                    print("Algorithm set to Quick Sort")

                if event.key == pygame.K_SPACE and not sorting:
                    # start visualizer when space is pressed
                    sorting = True
                    if algorithm == "bubble":
                        bubble_sort(array, draw_bars, 10)

                    elif algorithm == "insertion":
                        insertion_sort(array, draw_bars, 10)

                    elif algorithm == "selection":
                        insertion_sort(array, draw_bars, 10)

                    elif algorithm == "merge":
                        merge_sort(array, draw_bars, 10)

                    elif algorithm == "quick":
                        quick_sort(array, draw_bars, 10)

                elif event.key == pygame.K_r:
                    # reset the bars when space is pressed
                    array = generate_array(500)
                    sorting = False
    
    # Quit the screen when looop ends
    pygame.quit()

# run main function if script is executed directly
if __name__ == "__main__":
    main()
