import pygame
import csv
import random
import math

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


# pygame setup
pygame.init()

# Cargar el ícono
icon = pygame.image.load('img/ug.png')
pygame.display.set_icon(icon)

# Establecer el nombre de la ventana
pygame.display.set_caption("SIM UG HAULAGE")

screen = pygame.display.set_mode((1540, 790))
clock = pygame.time.Clock()
running = True

# Load the images
terrain_image = pygame.image.load('ug_layout_n.png')
rocas_image = pygame.image.load("img/rocas.png")

#jumbo
jumbo_image = pygame.image.load("img/jumbov2_i.png")
jumbo_rect = jumbo_image.get_rect()

#simba
simba_image = pygame.image.load("img/simba_i.png")
simba_rect = simba_image.get_rect()

#scoop
scoop_image = pygame.image.load("img/scoop_i.png")
scoop1_rect = scoop_image.get_rect()
scoop2_rect = scoop_image.get_rect()
scoop3_rect = scoop_image.get_rect()

#volquete
volquete_image = pygame.image.load("img/camion_r.png")
volquete1_rect = volquete_image.get_rect()
volquete2_rect = volquete_image.get_rect()
volquete3_rect = volquete_image.get_rect()

#camioneta
camioneta_image = pygame.image.load("img/camioneta.png")
camioneta_rect = camioneta_image.get_rect()

#bobcat1
bobcat_image = pygame.image.load("img/bobcat.png")
bobcat1_rect = bobcat_image.get_rect()

def load_and_process_points(file_name):
    points = []
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) == 2:
                x, y = map(float, row)
                points.append((x, y))
    points = [(x, screen.get_height() - y) for x, y in points]
    return points

speed = 1

def move_vehicle(vehicle_rect, points, current_index, direction=1):
    if current_index < 0:
        current_index = 0
        direction = 1
    elif current_index >= len(points) - 1:
        current_index = len(points) - 1
        direction = -1

    next_point = points[current_index + direction]
    if vehicle_rect.center != next_point:
        x, y = vehicle_rect.center
        dx = next_point[0] - x
        dy = next_point[1] - y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > speed:
            angle = math.atan2(dy, dx)
            x += speed * math.cos(angle)
            y += speed * math.sin(angle)
            vehicle_rect.center = (x, y)
        else:
            current_index += direction
            vehicle_rect.center = next_point

    return current_index, direction


direction_camioneta = 1
direction_scoop1 = 1
direction_scoop2 = 1
direction_scoop3 = 1
direction_bobcat1 = 1
direction_volquete1 = 1
direction_volquete2 = 1
direction_volquete3 = 1


#Leer puntos
p_camioneta = load_and_process_points('ruta_camioneta.csv')
p_scoop1 = load_and_process_points('ruta_scoop_1.csv')
p_scoop2 = load_and_process_points('ruta_scoop_2.csv')
p_scoop3 = load_and_process_points('ruta_scoop_3.csv')
p_bobcat = load_and_process_points('ruta_bobcat_1.csv')
p_volquete1 = load_and_process_points('ruta_volquete_1.csv')
p_volquete2 = load_and_process_points('ruta_volquete_2.csv')
p_volquete3 = load_and_process_points('ruta_volquete_3.csv')
p_bobcat1 = load_and_process_points('ruta_bobcat_1.csv')


# Posición inicial de la camioneta
current_point_index = 0
camioneta_rect.center = p_camioneta[current_point_index]

# Posición inicial del scoop1
current_scoop1_index = 0
scoop1_rect.center = p_scoop1[current_scoop1_index]

# Posición inicial del scoop2
current_scoop2_index = 0
scoop2_rect.center = p_scoop2[current_scoop2_index]

# Posición inicial del scoop3
current_scoop3_index = 0
scoop3_rect.center = p_scoop3[current_scoop3_index]

# Posición inicial del bobcat1
current_bobcat1_index = 0
bobcat1_rect.center = p_bobcat1[current_bobcat1_index]

# Posición inicial del volquete1
current_volquete1_index = 0
volquete1_rect.center = p_volquete1[current_volquete1_index]

# Posición inicial del volquete2
current_volquete2_index = 0
volquete2_rect.center = p_volquete2[current_volquete2_index]

# Posición inicial del volquete3
current_volquete3_index = 0
volquete3_rect.center = p_volquete3[current_volquete3_index]



#Función de lectura de etiquetas
def draw_text(screen, text, rect, text_x=-18, text_y=-30):
    text_x += rect.centerx
    text_y += rect.centery
    screen.blit(text, (text_x, text_y))

def r_text(text, font, color=(255, 255, 255)):
    return font.render(text, True, color)

# Mostrar código de equipos
f1 = pygame.font.SysFont('arial', 12, bold=True)
scoop1_text = r_text("Scoop 1", f1)
scoop2_text = r_text("Scoop 2", f1)
scoop3_text = r_text("Scoop 3", f1)
truck1_text = r_text("Truck 1", f1)
truck2_text = r_text("Truck 2", f1)
truck3_text = r_text("Truck 3", f1)
bobcat1_text = r_text("Bobcat 1", f1)
camioneta1_text = r_text("Supv Mina", f1)
simba_text = r_text("Simba 1", f1)
jumbo1_text = r_text("Jumbo 1", f1)
jumbo2_text = r_text("Jumbo 2", f1)

f2 = pygame.font.SysFont('arial', 9, bold=True)
ton_text = r_text("Ton:", f2, (10, 239, 255))
acum_text = r_text("Ac Ton:", f2, (10, 239, 255))
cycle_text = r_text("Avg Cycle:", f2, (10, 239, 255))
mp_text = r_text("Mt perf:", f2, (10, 239, 255))

elapsed_time_seconds = 0

# Posición Y_inicial del Simba
simba_y = 340
simba_vibration_amplitude = 1

# Posición X_inicial de los Jumbos
jumbo1_x = 348
jumbo2_x = 360
jumbo_vibration_amplitude = 1

vibr_spd = 0.1







def generar_grafico():
    fig, ax = plt.subplots()
    # Agrega tus datos y configuración de gráfico aquí
    # Por ejemplo:
    data = [10, 20, 30, 40, 50]
    labels = ['A', 'B', 'C', 'D', 'E']
    ax.bar(labels, data)
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Valores')
    ax.set_title('Gráfico de Barras')
    return fig

def generar_tabla():
    # Crea un DataFrame de ejemplo
    data = {'Nombre': ['A', 'B', 'C', 'D', 'E'],
            'Edad': [25, 30, 35, 40, 45]}
    df = pd.DataFrame(data)
    # Convierte el DataFrame a una tabla HTML
    tabla_html = df.to_html(index=False)
    return tabla_html


##Ciclos

# Define las variables de seguimiento de posición anterior para cada scoop
prev_scoop1_index = current_scoop1_index
prev_scoop2_index = current_scoop2_index
prev_scoop3_index = current_scoop3_index

ciclos_scoop1 = 0
ciclos_scoop2 = 0
ciclos_scoop3 = 0

# Define las posiciones iniciales de los scoops
scoop1_initial_position = p_scoop1[0]
scoop2_initial_position = p_scoop2[0]
scoop3_initial_position = p_scoop3[0]



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # En el bucle principal, actualiza el movimiento de los vehículos
    current_point_index, direction_camioneta = move_vehicle(camioneta_rect, p_camioneta, current_point_index, direction_camioneta)
    current_scoop1_index, direction_scoop1 = move_vehicle(scoop1_rect, p_scoop1, current_scoop1_index, direction_scoop1)
    current_scoop2_index, direction_scoop2 = move_vehicle(scoop2_rect, p_scoop2, current_scoop2_index, direction_scoop2)
    current_scoop3_index, direction_scoop3 = move_vehicle(scoop3_rect, p_scoop3, current_scoop3_index, direction_scoop3)
    
    current_volquete1_index, direction_volquete1 = move_vehicle(volquete1_rect, p_volquete1, current_volquete1_index, direction_volquete1)
    current_volquete2_index, direction_volquete2 = move_vehicle(volquete2_rect, p_volquete2, current_volquete2_index, direction_volquete2)
    current_volquete3_index, direction_volquete3 = move_vehicle(volquete3_rect, p_volquete3, current_volquete3_index, direction_volquete3)
    current_bobcat1_index, direction_bobcat1 = move_vehicle(bobcat1_rect, p_bobcat1, current_bobcat1_index, direction_bobcat1)

    # current_point_index = move_vehicle(camioneta_rect, p_camioneta, current_point_index)
    # current_scoop1_index = move_vehicle(scoop1_rect, p_scoop1, current_scoop1_index)
    # current_scoop2_index = move_vehicle(scoop2_rect, p_scoop2, current_scoop2_index)
    # current_scoop3_index = move_vehicle(scoop3_rect, p_scoop3, current_scoop3_index)
    # #current_scoop2_index = move_vehicle(scoop2_rect, p_scoop2, current_scoop2_index)
    # current_volquete1_index = move_vehicle(volquete1_rect, p_volquete1, current_volquete1_index)
    # current_volquete2_index = move_vehicle(volquete2_rect, p_volquete2, current_volquete2_index)
    # current_volquete3_index = move_vehicle(volquete3_rect, p_volquete3, current_volquete3_index)
    # current_bobcat1_index = move_vehicle(bobcat1_rect, p_bobcat1, current_bobcat1_index)
    

    color = (202, 240, 248)
    screen.fill(color)
    screen.blit(terrain_image, (0,0))

    
    #ciclos scoop
    # Verificar si Scoop 1 ha completado un ciclo
    if current_scoop1_index == prev_scoop1_index and direction_scoop1 == -1:
        ciclos_scoop1 += 1

    # Verificar si Scoop 2 ha completado un ciclo
    if current_scoop2_index == prev_scoop2_index and direction_scoop2 == -1:
        ciclos_scoop2 += 1

    # Verificar si Scoop 3 ha completado un ciclo
    if current_scoop3_index == prev_scoop3_index and direction_scoop3 == -1:
        ciclos_scoop3 += 1

    # Actualiza las variables previas de posición
    prev_scoop1_index = current_scoop1_index
    prev_scoop2_index = current_scoop2_index
    prev_scoop3_index = current_scoop3_index




    # Simba: Aplica la vibración vertical
    simba_y += simba_vibration_amplitude * math.sin(pygame.time.get_ticks() * vibr_spd)
    simba_y = max(338, simba_y) 
    simba_y = min(342, simba_y) 
    # Dibuja Simba Y
    screen.blit(simba_image, (155, simba_y))
    
    # Jumbo: Aplica la vibración Horizontal
    jumbo1_x += jumbo_vibration_amplitude * math.sin(pygame.time.get_ticks() * vibr_spd)
    jumbo1_x = max(jumbo1_x, 346)
    jumbo1_x = min(jumbo1_x, 350)

    jumbo2_x += jumbo_vibration_amplitude * math.sin(pygame.time.get_ticks() * vibr_spd)
    jumbo2_x = max(jumbo2_x, 358)
    jumbo2_x = min(jumbo2_x, 360)

    screen.blit(jumbo_image, (jumbo1_x, 470))
    screen.blit(jumbo_image, (jumbo2_x, 612))


    ###Scoop1
    screen.blit(rocas_image, (130,110))
    screen.blit(rocas_image, (155,110))
    screen.blit(rocas_image, (180,110))
    
    ###Scoop2
    screen.blit(rocas_image, (30,260))
    screen.blit(rocas_image, (55,260))  
    screen.blit(rocas_image, (80,260))

    ###Scoop3
    screen.blit(rocas_image, (295,550))
    screen.blit(rocas_image, (320,545))  
    screen.blit(rocas_image, (345,540))
     
    #volquetes
    #screen.blit(volquete_image, (1070,100))
    #screen.blit(volquete_image, (1030,260))

    #Equipos en movimiento
    screen.blit(camioneta_image, camioneta_rect)
    screen.blit(scoop_image, scoop1_rect)
    screen.blit(scoop_image, scoop2_rect)
    screen.blit(scoop_image, scoop3_rect)
    screen.blit(volquete_image, volquete1_rect)
    screen.blit(volquete_image, volquete2_rect)
    screen.blit(volquete_image, volquete3_rect)
    screen.blit(bobcat_image, bobcat1_rect)

   
    #Etiquetas###################################
    #scoops
    draw_text(screen, scoop1_text, scoop1_rect)
    draw_text(screen, scoop2_text, scoop2_rect)
    draw_text(screen, scoop3_text, scoop3_rect)


    # En la parte de las etiquetas

    # Tonelaje movido por Scoop 1
    #draw_text(screen, ton_text, scoop1_rect, text_x=-15, text_y=12)
    #draw_text(screen, r_text(str(tonelaje_scoop1), f2,(10, 239, 255)), scoop1_rect, text_x=15, text_y=12)

    #tn
    draw_text(screen, ton_text, scoop1_rect,text_x=-15, text_y=12)
    draw_text(screen, ton_text, scoop2_rect,text_x=-15, text_y=12) 
    draw_text(screen, ton_text, scoop3_rect,text_x=-15, text_y=12)
    #ac tn
    draw_text(screen, acum_text, scoop1_rect,text_x=-15, text_y=20)
    draw_text(screen, acum_text, scoop2_rect,text_x=-15, text_y=20)
    draw_text(screen, acum_text, scoop3_rect,text_x=-15, text_y=20)
    #avg cycle
    draw_text(screen, cycle_text, scoop1_rect,text_x=-15, text_y=28)
    draw_text(screen, cycle_text, scoop2_rect,text_x=-15, text_y=28)
    draw_text(screen, cycle_text, scoop3_rect,text_x=-15, text_y=28)


    # Número de ciclos de Scoop 1
    draw_text(screen, r_text(f"Ciclos Scoop 1: {ciclos_scoop1}", f2), scoop1_rect, text_x=15, text_y=12)

    # Número de ciclos de Scoop 2
    draw_text(screen, r_text(f"Ciclos Scoop 2: {ciclos_scoop2}", f2), scoop2_rect, text_x=15, text_y=12)

    # Número de ciclos de Scoop 3
    draw_text(screen, r_text(f"Ciclos Scoop 3: {ciclos_scoop3}", f2), scoop3_rect, text_x=15, text_y=12)

    #volquetes
    draw_text(screen, truck1_text, volquete1_rect)
    draw_text(screen, truck2_text, volquete2_rect)
    draw_text(screen, truck3_text, volquete3_rect)
    #tn
    draw_text(screen, ton_text, volquete1_rect,text_x=-15, text_y=12)
    draw_text(screen, ton_text, volquete2_rect,text_x=-15, text_y=12)
    draw_text(screen, ton_text, volquete3_rect,text_x=-15, text_y=12)
    #ac tn
    draw_text(screen, acum_text, volquete1_rect,text_x=-15, text_y=20)
    draw_text(screen, acum_text, volquete2_rect,text_x=-15, text_y=20)
    draw_text(screen, acum_text, volquete3_rect,text_x=-15, text_y=20)
    #avg cycle
    draw_text(screen, cycle_text, volquete1_rect,text_x=-15, text_y=28)
    draw_text(screen, cycle_text, volquete2_rect,text_x=-15, text_y=28)
    draw_text(screen, cycle_text, volquete3_rect,text_x=-15, text_y=28)

    #bobcat   
    draw_text(screen, bobcat1_text, bobcat1_rect)
   
    #camioneta
    draw_text(screen, camioneta1_text, camioneta_rect)

    #simba
    screen.blit(simba_text, (170, 330))
    screen.blit(mp_text, (170, 370))
   
    #Jumbos
    screen.blit(jumbo1_text, (375, 457))
    screen.blit(mp_text, (375, 497))
    screen.blit(jumbo2_text, (395, 600))
    screen.blit(mp_text, (395, 640))

    #############################################
    #Lineas y puntos de referencia
    def draw_circles(screen, point_list):
        for point in point_list:
            pygame.draw.circle(screen, (255, 0, 0), point, 5)

    #print("Current Scoop Index:", current_scoop1_index)
    #print("Current Scoop Point:", p_scoop1[current_scoop1_index])
    #pygame.draw.lines(screen, (137, 252, 0), False, p_scoop1, 2)
    #pygame.draw.lines(screen, (137, 252, 0), False, p_volquete1, 2)

    print(f"Current Scoop Index: {ciclos_scoop1}")

    # Calculate elapsed time in minutes (considering acceleration)
    elapsed_time_seconds += 1

    elapsed_hours = elapsed_time_seconds // (3600*3)  # 3600 segundos en una hora
    elapsed_minutes = (elapsed_time_seconds % 3600) // (60*3)
    elapsed_seconds = elapsed_time_seconds % (60*3)

    font = pygame.font.Font(None, 28)
    elapsed_time_text = font.render(f"Tiempo Sim: {elapsed_hours:02d}:{elapsed_minutes:02d}:{elapsed_seconds:02d}", True, (255, 255, 255))
    screen.blit(elapsed_time_text, (1300, 630))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

#img = generar_grafico() 
#tabla_html = generar_tabla()
