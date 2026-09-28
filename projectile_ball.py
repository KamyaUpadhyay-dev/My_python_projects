import pygame

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
    
# Colors
RED = pygame.Color("red")
BLACK = pygame.Color("black")
GROUND = pygame.Color("darkgreen")
WHITE = pygame.Color("white")

# Physics Variables
gravity = 0.5  
launch_pos = (200, 450)
b_pos = list(launch_pos)
b_vel = [0, 0]
is_flying = False
is_dragging = False

running = True
while running:
    screen.fill(WHITE)
    pygame.draw.rect(screen, GROUND, (0, 550, WIDTH, 50)) # Ground
    
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not is_flying:
                is_dragging = True
                
        if event.type == pygame.MOUSEBUTTONUP:
            if is_dragging:
                is_dragging = False
                is_flying = True
                # Physics: Velocity is proportional to the drag distance
                b_vel[0] = (launch_pos[0] - mouse_pos[0]) * 0.15
                b_vel[1] = (launch_pos[1] - mouse_pos[1]) * 0.15

    # --- Physics Update ---
    if is_flying:
        b_vel[1] += gravity  # Applying gravity to vertical velocity
        b_pos[0] += b_vel[0]
        b_pos[1] += b_vel[1]
        
        # Reset if it hits ground or goes off screen
        if b_pos[1] >= 540 or b_pos[0] > WIDTH:
            is_flying = False
            b_pos = list(launch_pos)
            b_vel = [0, 0]

    # --- Drawing ---
    # Draw slingshot line when dragging
    if is_dragging:
        pygame.draw.line(screen, BLACK, launch_pos, mouse_pos, 2)
        pygame.draw.circle(screen, RED, mouse_pos, 15)
    else:
        pygame.draw.circle(screen, RED, (int(b_pos[0]), int(b_pos[1])), 15)

    # Draw launch point (slingshot base)
    pygame.draw.circle(screen, BLACK, launch_pos, 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()