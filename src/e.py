from download import download
import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import csv
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib import animation
from IPython.display import HTML

url = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_GeolocCompteurs.csv"
path_target = "resources\MMM_MMM_GeolocCompteurs.csv"
download(url, path_target, replace=True)

coordinates_list= []

with open(path_target, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    check=True
    for row in spamreader:
        if check:
            check=False
            continue 
        coordinates_list.append((row[3],row[4]))
        


ox.utils.config(use_cache=True) # caching large download
G = ox.graph_from_place("Montpellier, France", network_type="bike")
fig, ax = ox.plot_graph(G,show=False, close=False)
scatter_list=[]
#for item in coordinates_list:
#   scatter_list.append(ax.scatter(float(item[1]),float(item[0]),c='yellow'))
    



def animate(i):
    
    try:
            
        ax.scatter(float(coordinates_list[i][1]),float(coordinates_list[i][0]),c='red')
    except:
            
        print('error')

# Make the animation
animation = FuncAnimation(fig, animate, frames=10,interval=200)


writergif = PillowWriter(fps=10)
animation.save('animation.gif',writer=writergif)

