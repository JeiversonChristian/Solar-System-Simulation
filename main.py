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

LARGURA_TELA = 800
ALTURA_TELA = 800
JANELA = pygame.display.set_mode( (LARGURA_TELA, ALTURA_TELA) )
pygame.display.set_caption("Solar System Simulation")

BRANCO = (255,255,255)
AMARELO = (255,255,0)

class Orbe:
    # UA -> Unidades Astronômicas
    # 1,496 x 10^11 metros
    UA = 1.496e11

    # Cosntante Gravitacional
    G = 6.67428e-11

    # 1UA = 100 pixels
    ESCALA = 250 / UA

    # Quanto tempo passa a cada atualização
    # 3600 segundos = 1 hora    
    PASSAGEM_TEMPO = 3600 * 24

    def __init__(self, x, y, raio, cor, massa):
        self.x = x
        self.y = y
        self.raio = raio * self.ESCALA * 10
        self.cor = cor
        self.massa = massa
        self.x_vel = 0
        self.y_vel = 0
        self.eh_sol = False
        self.dist_sol = 0
        self.orbita = []

    def desenhar(self, janela):
        x = self.x * self.ESCALA + LARGURA_TELA / 2
        y = self.y * self.ESCALA + ALTURA_TELA / 2
        pygame.draw.circle(janela, self.cor, (x,y), self.raio)

def main():
    relogio = pygame.time.Clock()

    sol = Orbe(0,0, 696340000, AMARELO, 1.98892 * 10**30 )
    sol.eh_sol = True

    orbes = [sol]

    rodando = True
    while rodando == True:
        # 60 FPS no máximo
        relogio.tick(60)

        #JANELA.fill(BRANCO)

        for orbe in orbes:
            orbe.desenhar(JANELA)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

    pygame.quit()

main()
