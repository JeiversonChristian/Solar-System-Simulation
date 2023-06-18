# -------------------------------------------------------------------------------------------------------
# Bibliotecas

# Pygame - principal biblioteca, a que vai gerir tudo. Gera interfaces 2D.
# Precisa ser instalada para funcionar. Comando no Windows: pip install pygame
import pygame 

# Math - biblioteca para as matemágicas.
# Não precisa ser instalada
import math
# -------------------------------------------------------------------------------------------------------

pygame.init()

LARGURA_TELA = 1400
ALTURA_TELA = 800
JANELA = pygame.display.set_mode( (LARGURA_TELA, ALTURA_TELA) )
pygame.display.set_caption("Solar System Simulation")

PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (100, 149, 237)
LARANJA = (255, 165, 0)

# UA -> Unidades Astronômicas
# 1,496 x 10^11 metros
UA = 1.496e11

# Cosntante Gravitacional
G = 6.67428e-11

# Quanto tempo passa a cada atualização
# 3600 segundos = 1 hora    
PASSAGEM_TEMPO = 3600 * 24

class Orbe:

    def __init__(self, x, y, raio, cor, massa):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.massa = massa
        self.x_vel = 0
        self.y_vel = 0
        self.eh_sol = False
        self.dist_sol = 0
        self.orbita = []

    def desenhar(self, janela, escala):
        x = self.x * escala + LARGURA_TELA / 2
        y = self.y * escala + ALTURA_TELA / 2
        pygame.draw.circle(janela, self.cor, (x,y), self.raio)

def main():
    fator_escala = 250
    # 1UA = 100 pixels
    escala = fator_escala / UA

    relogio = pygame.time.Clock()

    raio_terra = (6.371 * 10**3) * escala * (10**6)
    raio_sol = raio_terra * (110**(1/2))
    raio_marte = raio_terra / 2**(1/2)

    sol = Orbe(0, 0, raio_sol, AMARELO, 1.98892 * 10**30 )
    sol.eh_sol = True

    terra = Orbe(-1*UA, 0, raio_terra, AZUL, 5.9722 * 10**24)
    marte = Orbe(-1.524*UA, 0, raio_marte, LARANJA, 6.39 * 10**23)

    orbes = [sol, terra, marte]

    rodando = True
    while rodando == True:
        # 60 FPS no máximo
        relogio.tick(60)

        raio_terra = (6.371 * 10**3) * escala * (10**6)
        terra.raio = raio_terra
        raio_sol = raio_terra * (110**(1/2))
        sol.raio = raio_sol
        raio_marte = raio_terra / 2**(1/2)
        marte.raio = raio_marte

        JANELA.fill(PRETO)

        for orbe in orbes:
            orbe.desenhar(JANELA, escala)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 4:  # Rolagem para cima
                print("Rolagem para cima")
            elif evento.button == 5:  # Rolagem para baixo
                print("Rolagem para baixo")

        if evento.type == pygame.MOUSEWHEEL:
            if evento.y > 0:  # Rolagem para cima
                fator_escala += 3
                evento.y = 0
                escala = fator_escala / UA
            elif evento.y < 0:  # Rolagem para baixo
                fator_escala -= 3
                evento.y = 0
                escala = fator_escala / UA
            JANELA.fill(PRETO)

    pygame.quit()

main()
