from numpy import histogram, inf
from pandas import *
from matplotlib import pyplot

infected = read_csv('nb_infected.csv')

initial = infected['Rang initial d’infectés']
duree = infected['durée épidémie']
proportion = infected['proportion maximale infectés']
distribution = infected['distribution des multi-infections']

#Evaluer les nombres initiaux infectés

#histogramme
pyplot.figure(1)
pyplot.bar(initial,distribution)
pyplot.xlabel('Rang initial d’infectés')
pyplot.ylabel('distribution des multi-infections')
pyplot.title('Evaluation impact initial infecté')
pyplot.savefig("infecté_distribution.pdf")

#graphe
pyplot.figure(2)
pyplot.plot(initial,duree)
pyplot.plot(initial,proportion)
pyplot.xlabel('Rang initial d’infectés')
pyplot.title('durée épidémie /proportion maximale infectés ')
pyplot.legend()
pyplot.savefig("infecté_épidémie_proportion.pdf")

#########################################################################################

infected = read_csv('travel_distance.csv')

ray_mob = infected['Rang rayon mob']
duree = infected['durée épidémie']
proportion = infected['proportion maximale infectés']
distribution = infected['distribution des multi-infections']

#Evaluer les nombres initiaux infectés

#histogramme
pyplot.figure(3)
pyplot.bar(ray_mob,distribution)
pyplot.xlabel('Rang rayon mobilité')
pyplot.ylabel('distribution des multi-infections')
pyplot.title('Evaluation impact rayon mobilité sur distribution des multi-infections')
pyplot.savefig("rayon_mobilité_distribution.pdf")

#graphe
pyplot.figure(4)
pyplot.plot(ray_mob,duree)
pyplot.plot(ray_mob,proportion)
pyplot.xlabel('Rang rayon mobilité')
pyplot.title('Impact rayon mobilité sur durée épidémie /proportion maximale infectés ')
pyplot.legend()
pyplot.savefig("rayon_mobilité_épidémie_proportion.pdf")

#######################################################################################

infected = read_csv('nb_vaccinated.csv')

vaccin = infected['Rang vacciné']
duree = infected['durée épidémie']
proportion = infected['proportion maximale infectés']
distribution = infected['distribution des multi-infections']

#Evaluer les nombres initiaux infectés

#histogramme
pyplot.figure(5)
pyplot.bar(vaccin,distribution)
pyplot.xlabel('Rang des vaccinés')
pyplot.ylabel('distribution des multi-infections')
pyplot.title('Evaluation impact nombre vacciné sur distribution des multi-infections')
pyplot.savefig("vacciné_distribution.pdf")

#graphe
pyplot.figure(6)
pyplot.plot(vaccin,duree,label='durée épidémie')
pyplot.plot(vaccin,proportion,label='proportion maximale infectés')
pyplot.xlabel('Rang des vaccinés')
pyplot.title('Impact nombre vacciné sur durée épidémie /proportion maximale infectés ')
pyplot.legend()
pyplot.savefig("vacciné_épidémie_proportion.pdf")

#######################################################################################

infected = read_csv('vaccine_efficiency.csv')

vaccin = infected['Rang vaccin efficacité']
duree = infected['durée épidémie']
proportion = infected['proportion maximale infectés']
distribution = infected['distribution des multi-infections']

#Evaluer les nombres initiaux infectés

#histogramme
pyplot.figure(7)
pyplot.bar(vaccin,distribution)
pyplot.xlabel('Rang vaccin efficacité')
pyplot.ylabel('distribution des multi-infections')
pyplot.title('Evaluation impact efficacité vaccianle sur distribution des multi-infections')
pyplot.savefig("efficacité_vaccianle_distribution.pdf")

#graphe
pyplot.figure(8)
pyplot.plot(vaccin,duree,label='durée épidémie')
pyplot.plot(vaccin,proportion,label='proportion maximale infectés')
pyplot.xlabel('Rang vaccin efficacité')
pyplot.title('Impact efficacité vaccianle sur durée épidémie /proportion maximale infectés ')
pyplot.legend()
pyplot.savefig("efficacité_vaccianle_épidémie_proportion.pdf")

#######################################################################################

infected = read_csv('infection_period.csv')

vaccin = infected['Rang duree infection']
duree = infected['durée épidémie']
proportion = infected['proportion maximale infectés']
distribution = infected['distribution des multi-infections']

#Evaluer les nombres initiaux infectés

#histogramme
pyplot.figure(9)
pyplot.bar(vaccin,distribution)
pyplot.xlabel('Rang duree infection')
pyplot.ylabel('distribution des multi-infections')
pyplot.title('Evaluation impact durée d infection sur distribution des multi-infections')
pyplot.savefig("infection_distribution.pdf")

#graphe
pyplot.figure(10)
pyplot.plot(vaccin,duree,label='durée épidémie')
pyplot.plot(vaccin,proportion,label='proportion maximale infectés')
pyplot.xlabel('Rang duree infection')
pyplot.title('Impact durée d infection sur durée épidémie /proportion maximale infectés ')
pyplot.legend()
pyplot.savefig("infection_épidémie_proportion.pdf")

#######################################################################################

infected = read_csv('contagion_period.csv')

vaccin = infected['Rang duree de contamination']
duree = infected['durée épidémie']
proportion = infected['proportion maximale infectés']
distribution = infected['distribution des multi-infections']

#Evaluer les nombres initiaux infectés

#histogramme
pyplot.figure(11)
pyplot.bar(vaccin,distribution)
pyplot.xlabel('Rang duree de contamination')
pyplot.ylabel('distribution des multi-infections')
pyplot.title('Evaluation impact durée de contamination sur distribution des multi-infections')
pyplot.savefig("contamination_distribution.pdf")

#graphe
pyplot.figure(12)
pyplot.plot(vaccin,duree,label='durée épidémie')
pyplot.plot(vaccin,proportion,label='proportion maximale infectés')
pyplot.xlabel('Rang duree de contamination')
pyplot.title('Impact durée de contamination sur durée épidémie /proportion maximale infectés ')
pyplot.legend()
pyplot.savefig("contamination_épidémie_proportion.pdf")

#######################################################################################

infected = read_csv('immune_period.csv')

vaccin = infected['Rang duree immunité']
duree = infected['durée épidémie']
proportion = infected['proportion maximale infectés']
distribution = infected['distribution des multi-infections']

#Evaluer les nombres initiaux infectés

#histogramme
pyplot.figure(13)
pyplot.bar(vaccin,distribution)
pyplot.xlabel('Rang duree immunité')
pyplot.ylabel('distribution des multi-infections')
pyplot.title('Evaluation impact durée d immunité sur distribution des multi-infections')
pyplot.savefig("immunité_distribution.pdf")

#graphe
pyplot.figure(14)
pyplot.plot(vaccin,duree,label='durée épidémie')
pyplot.plot(vaccin,proportion,label='proportion maximale infectés')
pyplot.xlabel('Rang duree immunité')
pyplot.title('Impact durée d immunité sur durée épidémie /proportion maximale infectés ')
pyplot.legend()
pyplot.savefig("immunité_épidémie_proportion.pdf")

#######################################################################################

infected = read_csv('nb_nodes.csv')

vaccin = infected['Rang densité']
duree = infected['durée épidémie']
proportion = infected['proportion maximale infectés']
distribution = infected['distribution des multi-infections']

#Evaluer les nombres initiaux infectés

#histogramme
pyplot.figure(15)
pyplot.bar(vaccin,distribution)
pyplot.xlabel('Rang densité')
pyplot.ylabel('distribution des multi-infections')
pyplot.title('Evaluation impact densité sur distribution des multi-infections')
pyplot.savefig("densité_distribution.pdf")

#graphe
pyplot.figure(16)
pyplot.plot(vaccin,duree,label='durée épidémie')
pyplot.plot(vaccin,proportion,label='proportion maximale infectés')
pyplot.xlabel('Rang densité')
pyplot.title('Impact densité sur durée épidémie /proportion maximale infectés ')
pyplot.legend()
pyplot.savefig("densité_épidémie_proportion.pdf")
#######################################################################################

pyplot.show()