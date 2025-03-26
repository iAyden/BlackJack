import pygame
from player import Player

from game import create_cards_for_deck, give_cards_to_player, give_cards_to_dealer

# Inicializar pygame
pygame.init()

create_cards_for_deck()

# Configuración de pantalla
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Diccionario para mapear palos a símbolos
suits_symbols = {
    "heart": "♥",
    "diamond": "♦",
    "spade": "♠",
    "club": "♣"
}

# Fuentes
font = pygame.font.SysFont("segoeuiemoji", 54)  # O prueba con Arial si no funciona

# Dimensiones de las cartas
CARD_WIDTH, CARD_HEIGHT = 120, 180
card_back = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
card_back.fill(RED)

# Función para mostrar texto en pantalla
def draw_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Función para dibujar cartas
def draw_cards(cards, x, y, hide_first=False):
    for i, card in enumerate(cards):
        if i == 0 and hide_first:  # Hide first card
            screen.blit(card_back, (x + i * (CARD_WIDTH + 10), y))
        else:
            pygame.draw.rect(screen, WHITE, (x + i * (CARD_WIDTH + 10), y, CARD_WIDTH, CARD_HEIGHT))
            if isinstance(card, tuple):  # Check if it's a tuple (value, color, suit)
                value, color, suit = card
                # Display value and suit
                draw_text(str(value), x + i * (CARD_WIDTH + 15) + 25, y + 30, 
                         RED if color == "red" else BLACK)
                # Display suit symbol
                draw_text(suits_symbols[suit], x + i * (CARD_WIDTH + 20) + 10, y + 90,
                         RED if color == "red" else BLACK)
            else:  # Fallback for non-tuple cards
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

    player_hand = give_cards_to_player()
    player_cards = [(c.value, c.color, c.suits) for c in player_hand]
    dealer_hand = give_cards_to_dealer()
    dealer_cards = [(d.value, d.color, d.suits) for d in dealer_hand]

    sum_player = sum([c[0] for c in player_cards])
    sum_dealer = sum([c[0] for c in dealer_cards])
    
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
         #   if event.type == pygame.MOUSEBUTTONDOWN:
                #if button_hit.is_clicked(event.pos):
        #        print("hola")

        # Dibujar cartas del jugador

        draw_text(f"Your game: {sum_player}", 50, 315)
        draw_cards(player_cards, 50, 375)

        # Dibujar cartas del dealer
        draw_text(f"Dealer: ", 50, 20)

        draw_cards(dealer_cards, 50, 75, hide_first=not show_dealer_cards)


     
        # Dibujar botones
        button_hit = draw_button("Hit", 800, 310, 187, 65, BLUE)
        button_stand = draw_button("Stay", 800, 380, 187, 65, BLUE)
        button_double = draw_button("Double", 800, 450, 187, 65, BLUE)
        button_split = draw_button("Split", 800, 520, 187, 65, BLUE)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

main()
