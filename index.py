import pygame
import sys
import random

sprites =[pygame.image.load("./assets/car/reto.png"),pygame.image.load("./assets/car/wheals.png")] 

pygame.init()
pygame.mixer.init()
gameProps={"width":700,"height":700}
cores = [
        '#f2f0e5', 
        '#b8b5b9', 
        '#868188', 
        '#646365', 
        '#45444f', 
        '#3a3858',
        '#212123', 
        '#352b42', 
        '#43436a', 
        '#4b80ca', 
        '#68c2d3', 
        '#a2dcc7',
        '#ede19e', 
        '#d3a068', 
        '#b45252', 
        '#6a536e', 
        '#4b4158', 
        '#80493a',
        '#a77b5b', 
        '#e5ceb4', 
        '#c2d368', 
        '#8ab060', 
        '#567b79', 
        '#4e584a',
        '#7b7243', 
        '#b2b47e', 
        '#edc8c4', 
        '#cf8acb', 
        '#5f556a'
         ]
screen = pygame.display.set_mode((gameProps['width'], gameProps['height']))
pygame.display.set_caption("GSEVEN SNAKE")
#pista 
wayWIDTH = 400
wayHEIGHT = 700
wayCOLOR = cores[4]
wayX = (gameProps["width"]/2) - wayWIDTH/2
wayY = 0
carDX = 0
faixaWIDTH = wayWIDTH/2
velocity = .5
wayVelocity = .5
player_width = 70
player_height = 120
player_x =wayX+5
player_y = wayHEIGHT/1.3
carPositions = [wayX+10,wayX+10+100,wayX+10+200,wayX+10+300]
clock = pygame.time.Clock()



class Car:
  def __init__(self, type , x):
                 #min,max,wid,height
    self.types = [[80,220,cores[5]],[80,120,cores[9]],[80,160,cores[14]],[80,210,cores[12]]] 
    self.type = self.types[type]
    self.width = self.type[0]
    self.height = self.type[1]
    self.color = self.type[2]
    self.x = x
    self.y = -self.height
  def _move(self):
    self.y += wayVelocity
  def _draw(self):
    pygame.draw.rect(screen,  self.color, (self.x, self.y, self.width, self.height))





way = []


print (way)
def draw():
  pygame.draw.rect(screen, wayCOLOR, (wayX, wayY, wayWIDTH, wayHEIGHT))
  # Área da imagem que você deseja desenhar no jogador
  car_position = player_x - wayX
  # Mapeament do intervalo de 1 a 200 para o intervalo de 0 a 60
  mapped_position = 60 - (((car_position - 1) * (60 - 0) / (200 - 1)) + 0)-10
  # Arredondando para o número mais próximo
  if(car_position>100):
    mapped_position = ((((car_position/2) - 1) * (60 - 0) / (200 - 1)) + 0)-10
  closest_mapped_position = round(mapped_position)
  source_rect = pygame.Rect(closest_mapped_position*315, 0, 315, 599)

  wh_source_rect = pygame.Rect(0, 0, 315, 599)
  # Superfície temporária para a área da imagem que será desenhada no jogador

  if(carDX!=0):
    wh_cropped_surface = sprites[1].subsurface(wh_source_rect)
    wh_cropped_surface = pygame.transform.scale(wh_cropped_surface, (player_width, player_height))
    if carDX >0:
      fliped  = pygame.transform.flip(wh_cropped_surface, True, False)
      screen.blit(fliped, (player_x, player_y, player_width, player_height))
    else:
      screen.blit(wh_cropped_surface, (player_x, player_y, player_width, player_height))
    
  cropped_surface = sprites[0].subsurface(source_rect)
  if (car_position>100):
    #flipando caso nescessario
    cropped_surface = pygame.transform.scale(cropped_surface, (player_width, player_height))
    cropped_surface = pygame.transform.flip(cropped_surface, True, False)
    
  else:
    cropped_surface = pygame.transform.scale(cropped_surface, (player_width, player_height))
  print(car_position)
  screen.blit(cropped_surface, (player_x, player_y, player_width, player_height))


  # pygame.draw.rect(screen, cores[2], (player_x, player_y, player_width, player_height))


  for car in way:
    car._draw()
    car._move()

def move():
  global player_x

  if(carDX<0 and player_x<wayX):
    return
  if(carDX>0 and player_x > (wayWIDTH+wayX)-player_width-1):
    return
  player_x+=carDX

ultimo_tempo = pygame.time.get_ticks()
tempo_atual = ultimo_tempo
interval = random.randint(10, 15)*wayVelocity*200
def initGame():  # Intervalo aleatório entre 0.5 e 2.0 segundos
    global ultimo_tempo
    global tempo_atual
    global interval
    mytype = random.randint(0, 3)
    position = random.randint(0, 3)
    interval = random.randint(10, 15)*wayVelocity*200
    way.append(Car(mytype, carPositions[position]))

          

  # Intervalo aleatório entre 2 e 6 segundos




# Chamar a função para executar 5 vezes, por exemplo 
while True:
  tempo_atual = pygame.time.get_ticks()
  
  if tempo_atual - ultimo_tempo >= interval:
    initGame()
    ultimo_tempo = tempo_atual 

  for event in pygame.event.get():
      #fechando aplicação
    if event.type == pygame.KEYDOWN:
      if(event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
        carDX = -velocity
      elif(event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
        carDX = velocity
    if event.type == pygame.KEYUP:
      if((event.key == pygame.K_a) or (event.key == pygame.K_LEFT)) and carDX<0 :
        carDX = 0
      if ((event.key == pygame.K_d) or (event.key == pygame.K_RIGHT)) and carDX>0:
        carDX = 0


    #Quit game   
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  # Atualização da tela
  screen.fill(cores[8])
  move()
  draw()
  pygame.display.flip()

  