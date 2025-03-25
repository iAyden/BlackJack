import pygame

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fuentes
font = pygame.font.Font(None, 36)

# Dimensiones de las cartas
CARD_WIDTH, CARD_HEIGHT = 80, 120
card_back = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
card_back.fill(RED)

# Función para mostrar texto en pantalla
def draw_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Función para dibujar cartas
def draw_cards(cards, x, y, hide_first=False):
    for i, card in enumerate(cards):
        if i == 0 and hide_first:  # Ocultar la primera carta
            screen.blit(card_back, (x + i * (CARD_WIDTH + 10), y))
        else:
            pygame.draw.rect(screen, WHITE, (x + i * (CARD_WIDTH + 10), y, CARD_WIDTH, CARD_HEIGHT))
            draw_text(str(card), x + i * (CARD_WIDTH + 10) + 30, y + 30, BLACK)

# Función para dibujar botones
def draw_button(text, x, y, width, height, color, text_color=WHITE):
    pygame.draw.rect(screen, color, (x, y, width, height))
    draw_text(text, x + 10, y + 10, text_color)
    return pygame.Rect(x, y, width, height)

# Juego principal (solo visual)
def main():
    running = True
    clock = pygame.time.Clock()

    # Ejemplo de cartas
    player_cards = [5, 10]
    dealer_cards = [5, 8]

    sum_player = sum(player_cards)
    sum_dealer = sum(dealer_cards)

    # Botones
    button_hit = None
    button_stand = None
    show_dealer_cards = False

    while running:
        screen.fill(GREEN)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibujar cartas del jugador
        draw_text((f"Your game: {sum_player} "), 50, 400)
        draw_cards(player_cards, 50, 450)

        # Dibujar cartas del dealer
        draw_text((f"Dealer: {sum_dealer} "), 50, 50)
        draw_cards(dealer_cards, 50, 100, hide_first=not show_dealer_cards)


     
        # Dibujar botones
        button_hit = draw_button("Hit", 600, 290, 150, 50, BLUE)
        button_stand = draw_button("Stay", 600, 370, 150, 50, BLUE)
        button_double = draw_button("Double", 600, 450, 150, 50, BLUE)
        button_split = draw_button("Split", 600, 520, 150, 50, BLUE)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

main()
