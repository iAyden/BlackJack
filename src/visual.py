import pygame
from player import Player

from game import *
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
def draw_cards(cards, x, y, hide_first):
    if isinstance(cards, tuple):  # Si se pasa una sola carta en forma de tupla
        cards = [cards]  # Convertir a lista para reutilizar el código

    for i, card in enumerate(cards):
        if i == 0 and hide_first:  # Ocultar la primera carta
            screen.blit(card_back, (x + i * (CARD_WIDTH + 10), y))
        else:
            pygame.draw.rect(screen, WHITE, (x + i * (CARD_WIDTH + 10), y, CARD_WIDTH, CARD_HEIGHT))
            if isinstance(card, tuple):  
                value, color, suit = card
                draw_text(str(value), x + i * (CARD_WIDTH + 15) + 25, y + 30, 
                          RED if color == "red" else BLACK)
                draw_text(suits_symbols[suit], x + i * (CARD_WIDTH + 20) + 10, y + 90,
                          RED if color == "red" else BLACK)
            else:
                draw_text(str(card), x + i * (CARD_WIDTH + 10) + 30, y + 30, BLACK)

# Función para dibujar botones
def draw_button(text, x, y, width, height, color, text_color=WHITE):
    pygame.draw.rect(screen, color, (x, y, width, height))
    draw_text(text, x + 10, y + 10, text_color)
    return pygame.Rect(x, y, width, height)

#def new_game():
    
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
    bust = False
    draw = False
    playerwinner = False
    dealerwinner = False
    #click = pygame.mouse.get_pressed()
    while running:
        screen.fill(GREEN)
        
        mouse = pygame.mouse.get_pos()
        if check_if_bust_twentyone(sum_player) == False:
            bust = True
        if bust == True or playerwinner == True or dealerwinner == True or draw == True:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:    
                    if event.button == 1:
                            draw_button("New Game", 650, 310, 285, 65, BLUE)
                            if 650 <= mouse[0] <= 650 + 285 and 310 <= mouse[1] <= 310 + 65:
                                    button_hit = None
                                    button_stand = None
                                    show_dealer_cards = False
                                    bust = False
                                    draw = False
                                    playerwinner = False
                                    dealerwinner = False       
                                    reset_deck()
                                    player_hand = give_cards_to_player()
                                    player_cards = [(c.value, c.color, c.suits) for c in player_hand]
                                    dealer_hand = give_cards_to_dealer()
                                    dealer_cards = [(d.value, d.color, d.suits) for d in dealer_hand]

                                    sum_player = sum([c[0] for c in player_cards])
                                    sum_dealer = sum([c[0] for c in dealer_cards])
                                    check_if_bust_twentyone(sum_player)

        else:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 800 <= mouse[0] <= 800 + 187 and 310 <= mouse[1] <= 310 + 65:
                            hit_card_player()
                            player_cards = [(c.value, c.color, c.suits) for c in player_hand]
                            sum_player = sum([c[0] for c in player_cards])
                        #card_tuple = [{card.value, card.color, card.suits}]
                            draw_cards(player_cards, 50, 375, False)
                        elif 800 <= mouse[0] <= 800 + 187 and 380 <= mouse[1] <= 380 + 65:
                            if sum_dealer == sum_player:

                                    draw = True
                            else:
                                while 18>sum_dealer: 
                                        
                                        
                                        hit_card_dealer()
                                        dealer_cards = [(c.value, c.color, c.suits) for c in dealer_hand]
                                            
                                            
                                        sum_dealer = sum([c[0] for c in dealer_cards])
                                            
                                winner = check_winner(sum_dealer,sum_player)
                                print(f"Winner boolean {winner}")
                                if sum_dealer == sum_player:

                                    draw = True
                                else:
                                    if winner == True:
                                        playerwinner = True
                                    else:
                                        dealerwinner = True
                                    
         #   if event.type == pygame.MOUSEBUTTONDOWN:
                #if button_hit.is_clicked(event.pos):
        #        print("hola")

        # Dibujar cartas del jugador
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        draw_text(f"Your game: {sum_player}", 50, 315)
        draw_cards(player_cards, 50, 375, False)

        # Dibujar cartas del dealer
        draw_text(f"Dealer: ", 50, 20)

        draw_cards(dealer_cards, 50, 75, True)
        if draw == False:
            if sum_player == 21:
                playerwinner = True
            if sum_dealer == 21:
                dealerwinner = True
        if bust == True:
            draw_button("New Game", 650, 310, 285, 65, BLUE)
            draw_text(f"BUST", 500, 250)
            draw_cards(dealer_cards, 50, 75, False)
            draw_text(f"Dealer: {sum_dealer}", 50, 20)
        if draw == True:
            draw_button("New Game", 650, 310, 285, 65, BLUE)
            draw_cards(dealer_cards, 50, 75, False)
            draw_text(f"Dealer: {sum_dealer}", 50, 20)
            draw_text("Draw", 500, 250)
        if playerwinner == True:
            draw_button("New Game", 650, 310, 285, 65, BLUE)
            draw_text(f"Player Wins", 500, 250)
            draw_cards(dealer_cards, 50, 75, False)
            draw_text(f"Dealer: {sum_dealer}", 50, 20)
        if dealerwinner == True:
            draw_button("New Game", 650, 310, 285, 65, BLUE)
            draw_text(f"Dealer Wins", 500, 250)
            draw_cards(dealer_cards, 50, 75, False)
            draw_text(f"Dealer: {sum_dealer}", 50, 20)
        
        if playerwinner == False and dealerwinner == False and draw == False and bust == False:
            draw_button("Hit", 800, 310, 187, 65, BLUE)
            draw_button("Stand", 800, 380, 187, 65, BLUE) 
        #button_double = draw_button("Double", 800, 450, 187, 65, BLUE)
        #button_split = draw_button("Split", 800, 520, 187, 65, BLUE)

        pygame.display.flip()
        clock.tick(30) #Telling pygame the loop is not going to be more faster than 30 (with this is where we limitate the frame rate)
    pygame.quit()

main()
 