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

COR_FUNDO_UNIVERSO = (0, 0, 0)
COR_SOL = (255, 255, 0)
COR_TERRA = (100, 149, 237)
COR_MARTE = (255, 165, 0)
COR_MERCURIO = (139, 126, 102)
COR_VENUS = (255, 87, 34)

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
        if x >= 0 and y >=0:
            pygame.draw.circle(janela, self.cor, (x,y), self.raio)

    def calc_atracao(self, outro_orbe):
        outro_x = outro_orbe.x
        outro_y = outro_orbe.y
        dist_x = outro_x - self.x
        dist_y = outro_y - self.y
        # Distância entre dois pontos no Plano Cartesiano
        dist = (dist_x**2 + dist_y**2)**(1/2)
        if outro_orbe.eh_sol == True:
            self.dist_sol = dist
        # Força de atração: F = GMm/d²
        F = G * self.massa * outro_orbe.massa / dist**2
        # Ângulo entre a distância dos orbes e o eixo X
        # ArcoTangente de (y/x)
        ang_theta = math.atan2(dist_y, dist_x)
        # Componentes X e Y da Força
        Fx = math.cos(ang_theta) * F
        Fy = math.sin(ang_theta) * F
        return Fx, Fy
    
    def atualizar_posicao(self, orbes):
        total_Fx = 0
        total_Fy = 0
        for orbe in orbes:
            # Não queremso calcular a força de atração consigo mesmo, pois dá uma divisão por zero
            if self == orbe:
                continue
            Fx, Fy = self.calc_atracao(orbe)
            total_Fx += Fx
            total_Fy += Fy
        # F = ma
        # -> a = F/m
        # v = at
        # -> v = (F/m)t 
        self.x_vel += (total_Fx / self.massa) * PASSAGEM_TEMPO
        self.y_vel += (total_Fy / self.massa) * PASSAGEM_TEMPO
        # x = vt
        self.x += self.x_vel * PASSAGEM_TEMPO
        self.y += self.y_vel * PASSAGEM_TEMPO
        self.orbita.append((self.x, self.y))

def main():
    fator_escala = 250
    # 1UA = 100 pixels
    escala = fator_escala / UA

    relogio = pygame.time.Clock()

    raio_terra = (6.371 * 10**3) * escala * (7*10**5)
    raio_sol = raio_terra * (110**(1/2))
    raio_mercurio = raio_terra / 1.7**(1/2)
    raio_venus = raio_terra / 0.95**(1/2)
    raio_marte = raio_terra / 2**(1/2)

    sol = Orbe(0, 0, raio_sol, COR_SOL, 1.98892 * 10**30 )
    sol.eh_sol = True

    mercurio = Orbe(0.387*UA, 0, raio_mercurio, COR_MERCURIO, 3.30 * 10**23)
    mercurio.y_vel = -47.4 * 10**3

    venus = Orbe(0.723*UA, 0, raio_venus, COR_VENUS, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 10**3

    terra = Orbe(-1*UA, 0, raio_terra, COR_TERRA, 5.9722 * 10**24)
    terra.y_vel = 29.783 * 10**3

    marte = Orbe(-1.524*UA, 0, raio_marte, COR_MARTE, 6.39 * 10**23)
    marte.y_vel = 24.077 * 10**3

    orbes = [sol, mercurio, venus, terra, marte]

    rodando = True
    while rodando == True:
        # 60 FPS no máximo
        relogio.tick(60)

        raio_terra = (6.371 * 10**3) * escala * (7*10**5)
        terra.raio = raio_terra

        raio_sol = raio_terra * (110**(1/2))
        sol.raio = raio_sol

        raio_mercurio = raio_mercurio = raio_terra / 1.7**(1/2)
        mercurio.raio = raio_mercurio

        raio_venus = raio_terra / 0.95**(1/2)
        venus.raio = raio_venus

        raio_marte = raio_terra / 2**(1/2)
        marte.raio = raio_marte

        JANELA.fill(COR_FUNDO_UNIVERSO)

        for orbe in orbes:
            orbe.atualizar_posicao(orbes)
            orbe.desenhar(JANELA, escala)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.MOUSEWHEEL:
                if evento.y > 0:  # Rolagem para cima
                    fator_escala += 3
                    evento.y = 0

                elif evento.y < 0:  # Rolagem para baixo
                    fator_escala -= 3
                    evento.y = 0

            escala = fator_escala / UA
            JANELA.fill(COR_FUNDO_UNIVERSO)

            if evento.type == pygame.QUIT:
                rodando = False

    pygame.quit()

main()
