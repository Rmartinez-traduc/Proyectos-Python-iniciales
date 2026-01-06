import pygame

pygame.init() # Inicializa todos los módulos de Pygame


# Dimensiones de la ventana
ancho = 800
alto = 600

# Crear ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Pong clásico con Pygame")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Dimensiones de las palas
ancho_pala = 10
alto_pala = 100

# Posiciones iniciales
pala_izquierda = pygame.Rect(10, alto//2 - alto_pala//2, ancho_pala, alto_pala)
pala_derecha = pygame.Rect(ancho - 10 - ancho_pala, alto//2 - alto_pala//2, ancho_pala, alto_pala)

# Bola
tamaño_bola = 15
bola = pygame.Rect(ancho//2 - tamaño_bola//2, alto//2 - tamaño_bola//2, tamaño_bola, tamaño_bola)
velocidad_bola_x = 5
velocidad_bola_y = 5

# Variables de puntuación
puntaje_izquierda = 0
puntaje_derecha = 0

font = pygame.font.SysFont("arial", 40)

reloj = pygame.time.Clock() # Reloj para controlar FPS

ejecutando = True
while ejecutando:
    reloj.tick(60) # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        pala_izquierda.y -= 5  # Mover hacia arriba
    if teclas[pygame.K_s]:
        pala_izquierda.y += 5  # Mover hacia abajo
    
    if teclas[pygame.K_UP]:
        pala_derecha.y -= 5
    if teclas[pygame.K_DOWN]:
        pala_derecha.y += 5
    
    if pala_izquierda.top < 0:
        pala_izquierda.top = 0
    if pala_izquierda.bottom > alto:
        pala_izquierda.bottom = alto
    
    if pala_derecha.top < 0:
        pala_derecha.top = 0
    if pala_derecha.bottom > alto:
        pala_derecha.bottom = alto
    
    # Dentro del ciclo principal:
    bola.x += velocidad_bola_x
    bola.y += velocidad_bola_y

    # Rebote en bordes
    if bola.top <= 0 or bola.bottom >= alto:
        velocidad_bola_y *= -1 # Cambiar dirección vertical
    
    # Reobte en palas
    if bola.colliderect(pala_izquierda) or bola.colliderect(pala_derecha):
        velocidad_bola_x *= -1 # Cambiar dirección horizontal


    # Punto y reinicio
    if bola.left <= 0:
        puntaje_izquierda += 1
        bola.center = (ancho//2, alto//2)
        velocidad_bola_x *= -1

    if bola.right >= ancho:
        puntaje_derecha += 1
        bola.center = (ancho//2, alto//2)
        velocidad_bola_x *= -1

    # Dibujar todo 
    ventana.fill(negro)
    pygame.draw.rect(ventana, blanco, pala_izquierda)
    pygame.draw.rect(ventana, blanco, pala_derecha)
    pygame.draw.ellipse(ventana, blanco, bola)
    
    texto_izquierdo = font.render(f"{puntaje_izquierda}", True, blanco)
    texto_derecho = font.render(f"{puntaje_derecha}", True, blanco)
    ventana.blit(texto_izquierdo, (ancho//4, 20))
    ventana.blit(texto_derecho, (ancho * 3//4, 20))

    pygame.display.update()

pygame.quit()  # Cerrar Pygame