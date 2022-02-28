import numpy 
from pandas import *
import re


statList=[]
stat2List=[]
saneList=[]
infectedList =[]
immuneList =[]
epidemieDuration=[]
infectList=[]
multi_infections=[]
howmanynumber = []
listofavg = []

with open('1_nb_infected.txt','r') as file:
    for child in file:
        # we could retrieve values only with show_parameters = 0 but that's help us to cut
        # each part
        if re.match('\d{1,3} \d{1,3} \d{1,3}', child):
            statList.append(child)

#Retrieve the statistics generated in the nb_infected file 

for line in statList:
    # first value represent sane people
    sane = line.split(' ')[0]
    saneList.append(int(sane))
    # second value represent infected people
    infected = line.split(' ')[1]
    infectedList.append(int(infected))
    # third value represent immune people
    immune = line.split(' ')[2]
    immuneList.append(immune)

#generate file for question (iii)

with open('2_nb_infected.txt', 'r') as file:
    for child in file:
        if(re.match('[0-9]+', child)):
            values = child.split(' ')
            for i in range (100):
                stat2List.append(values[i])


# convert the list to numpy array for treatement
#  and reshape it to 1000 lines of 100 columns    
tab = numpy.reshape(numpy.array(stat2List), (1000,100))
#print(tab)


#Prepare for dataFrame

# Question 1    
infectedFrame ={
    0 : Series(infectedList[0:100]) , 1 : Series(infectedList[100:200]), 2 : Series(infectedList[200:300]),
    3 : Series(infectedList[300:400]) , 4 : Series(infectedList[400:500]), 5 : Series(infectedList[500:600]),
    6 : Series(infectedList[600:700]) , 7 : Series(infectedList[700:800]), 8 : Series(infectedList[800:900]),
    9 : Series(infectedList[900:1000]) 
}

dfInfected = DataFrame(infectedFrame)


# durée de l'épidémie(i)
# boucler les 5 simulations jusqu'à qu'il n'existe plus d'individu infecté
for cmpt in range(10):
    boolean = False
    for i in range(cmpt*100,100*(cmpt+1)):
        
        if (infectedList[i]== 0 and not boolean):
            epidemieDuration.append(i-100*cmpt)
            # valeur de test
            boolean = True
            # toute les individus sont infectés pendant toute la simulation
    if (not boolean):
        epidemieDuration.append(99)        
df= DataFrame({'durée épidémie':epidemieDuration})


#la proportion maximale de la population qui est infectée (ii)
df['proportion maximale infectés']= Series(dfInfected.max())
#df.columns.values[0]="inecté initial"

# la distribution des multi-infections (iii)

for simul in range (10) :
    for z in range (200) :
        try :
            a = []
            b = []
            
            with open('2_nb_infected.txt') as file:
                for child in file:
                    if re.match('[0-9]+', child) :
                        b.append(int(child[z])) #len(b) = 1000
            
            for c in range ( simul*100 , 100*(simul+1)) :
                a.append(b[c]) #len(a) = 100

            anew = []
            anew.append(a[0])

            for i in range (len(a)) :
                try :
                    if(a[i] != a[i+1] ) :
                        anew.append(a[i+1])
                except :
                    IndexError

            number = 0

            for j in range (len(anew)) :
                try :
                    if(anew[j] == 0 and anew[j+1] == 1) :
                        number += 1
                except :
                    IndexError

            #print(anew)
            #print("this {}th person was infected {} times".format(int((z+1)/2) +1 ,number))
            howmanynumber.append(number)
            #print("-"*30)
        except :
            ValueError

    #print("howmanynumber:", howmanynumber)
    sum = 0
    for s in range(len(howmanynumber)) :
        sum += howmanynumber[s]
    avg = sum/len(howmanynumber)
    #print("avg :", avg)
    listofavg.append(avg)
    howmanynumber.clear()
    avg = 0
#print(listofavg) #Average number of infections of people for a total of 10 simulators

df['distribution des multi-infections']=Series(listofavg)

df.index.names = ['Rang initial d’infectés']
df.to_csv('nb_infected.csv')

statList.clear()
stat2List.clear()
infectedList.clear()
epidemieDuration.clear()
infectList.clear()
multi_infections.clear()
howmanynumber.clear()
listofavg.clear()
#######################################################################################

#Question 2
with open('1_travel_distance.txt') as file:
    for child in file:
        # we could retrieve values only with show_parameters = 0 but that's help us to cut
        # each part
        if re.match('\d{1,3} \d{1,3} \d{1,3}', child):
            statList.append(child)

for line in statList:
    # second value represent infected people
    infected = line.split(' ')[1]
    infectedList.append(int(infected))

#generate file for question (iii)

with open('2_travel_distance.txt', 'r') as file:
    for child in file:
        if(re.match('[0-9]+', child)):
            values = child.split(' ')
            for i in range (100):
                stat2List.append(values[i])

# convert the list to numpy array for treatement
#  and reshape it to 1000 lines of 100 columns    
tab = numpy.reshape(numpy.array(stat2List), (1000,100))
#print(tab)

rayonMOBFrame ={    
    0 : Series(infectedList[0:100]) , 1 : Series(infectedList[100:200]), 2 : Series(infectedList[200:300]),
    3 : Series(infectedList[300:400]) , 4 : Series(infectedList[400:500]), 5 : Series(infectedList[500:600]),
    6 : Series(infectedList[600:700]) , 7 : Series(infectedList[700:800]), 8 : Series(infectedList[800:900]),
    9 : Series(infectedList[900:1000])
}    

dfRayonMOB = DataFrame(rayonMOBFrame)
#print(dfRayonMOB)

# durée de l'épidémie(i)
# boucler les 5 simulations jusqu'à qu'il n'existe plus d'individu infecté
for cmpt in range(10):
    boolean = False
    for i in range(cmpt*100,100*(cmpt+1)):
        
        if (infectedList[i]== 0 and not boolean):
            epidemieDuration.append(i-100*cmpt)
            # valeur de test
            boolean = True
            # toute les individus sont infectés pendant toute la simulation
    if (not boolean):
        epidemieDuration.append(99)        
df2= DataFrame({'durée épidémie':epidemieDuration})

#la proportion maximale de la population qui est infectée (ii)
df2['proportion maximale infectés']= Series(dfRayonMOB.max())

# la distribution des multi-infections (iii)
for simul in range (10) :
    for z in range (200) :
        try :
            a = []
            b = []
            
            with open('2_travel_distance.txt') as file:
                for child in file:
                    if re.match('[0-9]+', child) :
                        b.append(int(child[z])) #len(b) = 1000
            
            for c in range ( simul*100 , 100*(simul+1)) :
                a.append(b[c]) #len(a) = 100

            anew = []
            anew.append(a[0])

            for i in range (len(a)) :
                try :
                    if(a[i] != a[i+1] ) :
                        anew.append(a[i+1])
                except :
                    IndexError

            number = 0

            for j in range (len(anew)) :
                try :
                    if(anew[j] == 0 and anew[j+1] == 1) :
                        number += 1
                except :
                    IndexError

            #print(anew)
            #print("this {}th person was infected {} times".format(int((z+1)/2) +1 ,number))
            howmanynumber.append(number)
            #print("-"*30)
        except :
            ValueError

    #print("howmanynumber:", howmanynumber)
    sum = 0
    for s in range(len(howmanynumber)) :
        sum += howmanynumber[s]
    avg = sum/len(howmanynumber)
    #print("avg :", avg)
    listofavg.append(avg)
    howmanynumber.clear()
    avg = 0
#print(listofavg) #Average number of infections of people for a total of 10 simulators

df2['distribution des multi-infections']=Series(listofavg)

df2.index.names = ['Rang rayon mob']
df2.to_csv('travel_distance.csv')
#print(df2)

statList.clear()
stat2List.clear()
infectedList.clear()
epidemieDuration.clear()
infectList.clear()
multi_infections.clear()
howmanynumber.clear()
listofavg.clear()
##########################################################################################

#Question 3
with open('1_nb_vaccinated.txt') as file:
    for child in file:
        # we could retrieve values only with show_parameters = 0 but that's help us to cut
        # each part
        if re.match('\d{1,3} \d{1,3} \d{1,3}', child):
            statList.append(child)

for line in statList:
    # second value represent infected people
    infected = line.split(' ')[1]
    infectedList.append(int(infected))

#generate file for question (iii)

with open('2_nb_vaccinated.txt', 'r') as file:
    for child in file:
        if(re.match('[0-9]+', child)):
            values = child.split(' ')
            for i in range (100):
                stat2List.append(values[i])

# convert the list to numpy array for treatement
#  and reshape it to 1000 lines of 100 columns    
tab = numpy.reshape(numpy.array(stat2List), (1000,100))
#print(tab)


vaccinatedFrame ={
    0 : Series(infectedList[0:100]) , 1 : Series(infectedList[100:200]), 2 : Series(infectedList[200:300]),
    3 : Series(infectedList[300:400]) , 4 : Series(infectedList[400:500]), 5 : Series(infectedList[500:600]),
    6 : Series(infectedList[600:700]) , 7 : Series(infectedList[700:800]), 8 : Series(infectedList[800:900]),
    9 : Series(infectedList[900:1000])
}    

dfVaccinated = DataFrame(vaccinatedFrame)
#print(dfRayonMOB)

# durée de l'épidémie(i)
# boucler les 5 simulations jusqu'à qu'il n'existe plus d'individu infecté
for cmpt in range(10):
    boolean = False
    for i in range(cmpt*100,100*(cmpt+1)):
        
        if (infectedList[i]== 0 and not boolean):
            epidemieDuration.append(i-100*cmpt)
            # valeur de test
            boolean = True
            # toute les individus sont infectés pendant toute la simulation
    if (not boolean):
        epidemieDuration.append(99)        
df3= DataFrame({'durée épidémie':epidemieDuration})

#la proportion maximale de la population qui est infectée (ii)
df3['proportion maximale infectés']= Series(dfVaccinated.max())

# la distribution des multi-infections (iii)

for simul in range (10) :
    for z in range (200) :
        try :
            a = []
            b = []
            
            with open('2_nb_vaccinated.txt') as file:
                for child in file:
                    if re.match('[0-9]+', child) :
                        b.append(int(child[z])) #len(b) = 1000
            
            for c in range ( simul*100 , 100*(simul+1)) :
                a.append(b[c]) #len(a) = 100

            anew = []
            anew.append(a[0])

            for i in range (len(a)) :
                try :
                    if(a[i] != a[i+1] ) :
                        anew.append(a[i+1])
                except :
                    IndexError

            number = 0

            for j in range (len(anew)) :
                try :
                    if(anew[j] == 0 and anew[j+1] == 1) :
                        number += 1
                except :
                    IndexError

            #print(anew)
            #print("this {}th person was infected {} times".format(int((z+1)/2) +1 ,number))
            howmanynumber.append(number)
            #print("-"*30)
        except :
            ValueError

    #print("howmanynumber:", howmanynumber)
    sum = 0
    for s in range(len(howmanynumber)) :
        sum += howmanynumber[s]
    avg = sum/len(howmanynumber)
    #print("avg :", avg)
    listofavg.append(avg)
    howmanynumber.clear()
    avg = 0
#print(listofavg) #Average number of infections of people for a total of 10 simulators

df3['distribution des multi-infections']=Series(listofavg)

df3.index.names = ['Rang vacciné']
df3.to_csv('nb_vaccinated.csv')
#print(df2)

statList.clear()
stat2List.clear()
infectedList.clear()
epidemieDuration.clear()
infectList.clear()
multi_infections.clear()
howmanynumber.clear()
listofavg.clear()
####################################################################################

#Question 4
with open('1_vaccine_efficiency.txt') as file:
    for child in file:
        # we could retrieve values only with show_parameters = 0 but that's help us to cut
        # each part
        if re.match('\d{1,3} \d{1,3} \d{1,3}', child):
            statList.append(child)

for line in statList:
    # second value represent infected people
    infected = line.split(' ')[1]
    infectedList.append(int(infected))

#generate file for question (iii)

with open('2_vaccine_efficiency.txt', 'r') as file:
    for child in file:
        if(re.match('[0-9]+', child)):
            values = child.split(' ')
            for i in range (100):
                stat2List.append(values[i])

# convert the list to numpy array for treatement
#  and reshape it to 1000 lines of 100 columns    
tab = numpy.reshape(numpy.array(stat2List), (1000,100))
#print(tab)


vaccineFrame ={
    0 : Series(infectedList[0:100]) , 1 : Series(infectedList[100:200]), 2 : Series(infectedList[200:300]),
    3 : Series(infectedList[300:400]) , 4 : Series(infectedList[400:500]), 5 : Series(infectedList[500:600]),
    6 : Series(infectedList[600:700]) , 7 : Series(infectedList[700:800]), 8 : Series(infectedList[800:900]),
    9 : Series(infectedList[900:1000])
}    

dfVaccine = DataFrame(vaccineFrame)
#print(dfRayonMOB)

# durée de l'épidémie(i)
# boucler les 5 simulations jusqu'à qu'il n'existe plus d'individu infecté
for cmpt in range(10):
    boolean = False
    for i in range(cmpt*100,100*(cmpt+1)):
        
        if (infectedList[i]== 0 and not boolean):
            epidemieDuration.append(i-100*cmpt)
            # valeur de test
            boolean = True
            # toute les individus sont infectés pendant toute la simulation
    if (not boolean):
        epidemieDuration.append(99)        
df4= DataFrame({'durée épidémie':epidemieDuration})


#la proportion maximale de la population qui est infectée (ii)
df4['proportion maximale infectés']= Series(dfVaccine.max())


# la distribution des multi-infections (iii)
for simul in range (10) :
    for z in range (200) :
        try :
            a = []
            b = []
            
            with open('2_vaccine_efficiency.txt') as file:
                for child in file:
                    if re.match('[0-9]+', child) :
                        b.append(int(child[z])) #len(b) = 1000
            
            for c in range ( simul*100 , 100*(simul+1)) :
                a.append(b[c]) #len(a) = 100

            anew = []
            anew.append(a[0])

            for i in range (len(a)) :
                try :
                    if(a[i] != a[i+1] ) :
                        anew.append(a[i+1])
                except :
                    IndexError

            number = 0

            for j in range (len(anew)) :
                try :
                    if(anew[j] == 0 and anew[j+1] == 1) :
                        number += 1
                except :
                    IndexError

            #print(anew)
            #print("this {}th person was infected {} times".format(int((z+1)/2) +1 ,number))
            howmanynumber.append(number)
            #print("-"*30)
        except :
            ValueError

    #print("howmanynumber:", howmanynumber)
    sum = 0
    for s in range(len(howmanynumber)) :
        sum += howmanynumber[s]
    avg = sum/len(howmanynumber)
    #print("avg :", avg)
    listofavg.append(avg)
    howmanynumber.clear()
    avg = 0
#print(listofavg) #Average number of infections of people for a total of 10 simulators

df4['distribution des multi-infections']=Series(listofavg)

df4.index.names = ['Rang vaccin efficacité']
df4.to_csv('vaccine_efficiency.csv')
#print(df2)


statList.clear()
stat2List.clear()
infectedList.clear()
epidemieDuration.clear()
infectList.clear()
multi_infections.clear()
howmanynumber.clear()
listofavg.clear()
###############################################################################################

#Question 5
with open('1_infection_period.txt') as file:
    for child in file:
        # we could retrieve values only with show_parameters = 0 but that's help us to cut
        # each part
        if re.match('\d{1,3} \d{1,3} \d{1,3}', child):
            statList.append(child)

#generate file for question (iii)

with open('2_infection_period.txt', 'r') as file:
    for child in file:
        if(re.match('[0-9]+', child)):
            values = child.split(' ')
            for i in range (100):
                stat2List.append(values[i])

# convert the list to numpy array for treatement
#  and reshape it to 1000 lines of 100 columns    
tab = numpy.reshape(numpy.array(stat2List), (2000,100))
#print(tab)


for line in statList:
    # second value represent infected people
    infected = line.split(' ')[1]
    infectedList.append(int(infected))

infPeriodFrame ={
    0 : Series(infectedList[0:100]) , 1 : Series(infectedList[100:200]), 2 : Series(infectedList[200:300]),
    3 : Series(infectedList[300:400]) , 4 : Series(infectedList[400:500]), 5 : Series(infectedList[500:600]),
    6 : Series(infectedList[600:700]) , 7 : Series(infectedList[700:800]), 8 : Series(infectedList[800:900]),
    9 : Series(infectedList[900:1000]), 10 : Series(infectedList[0:100]) , 11 : Series(infectedList[100:200]), 
    12 : Series(infectedList[200:300]), 13 : Series(infectedList[300:400]) , 14 : Series(infectedList[400:500]), 
    15 : Series(infectedList[500:600]), 16 : Series(infectedList[600:700]) , 17 : Series(infectedList[700:800]), 
    18 : Series(infectedList[800:900]), 19 : Series(infectedList[900:1000])
}    

dfInfPeriod = DataFrame(infPeriodFrame)
#print(dfRayonMOB)

# durée de l'épidémie(i)
# boucler les 5 simulations jusqu'à qu'il n'existe plus d'individu infecté
for cmpt in range(20):
    boolean = False
    for i in range(cmpt*100,100*(cmpt+1)):
        
        if (infectedList[i]== 0 and not boolean):
            epidemieDuration.append(i-100*cmpt)
            # valeur de test
            boolean = True
            # toute les individus sont infectés pendant toute la simulation
    if (not boolean):
        epidemieDuration.append(99)        
df5= DataFrame({'durée épidémie':epidemieDuration})

#la proportion maximale de la population qui est infectée (ii)
df5['proportion maximale infectés']= Series(dfInfPeriod.max())

# la distribution des multi-infections (iii)
for simul in range (20) :
    for z in range (200) :
        try :
            a = []
            b = []
            
            with open('2_infection_period.txt') as file:
                for child in file:
                    if re.match('[0-9]+', child) :
                        b.append(int(child[z])) #len(b) = 1000
            
            for c in range ( simul*100 , 100*(simul+1)) :
                a.append(b[c]) #len(a) = 100

            anew = []
            anew.append(a[0])

            for i in range (len(a)) :
                try :
                    if(a[i] != a[i+1] ) :
                        anew.append(a[i+1])
                except :
                    IndexError

            number = 0

            for j in range (len(anew)) :
                try :
                    if(anew[j] == 0 and anew[j+1] == 1) :
                        number += 1
                except :
                    IndexError

            #print(anew)
            #print("this {}th person was infected {} times".format(int((z+1)/2) +1 ,number))
            howmanynumber.append(number)
            #print("-"*30)
        except :
            ValueError

    #print("howmanynumber:", howmanynumber)
    sum = 0
    for s in range(len(howmanynumber)) :
        sum += howmanynumber[s]
    avg = sum/len(howmanynumber)
    #print("avg :", avg)
    listofavg.append(avg)
    howmanynumber.clear()
    avg = 0
#print(listofavg) #Average number of infections of people for a total of 10 simulators

df5['distribution des multi-infections']=Series(listofavg)

df5.index.names = ['Rang duree infection']
df5.to_csv('infection_period.csv')
#print(df2)


statList.clear()
stat2List.clear()
infectedList.clear()
epidemieDuration.clear()
infectList.clear()
multi_infections.clear()
howmanynumber.clear()
listofavg.clear()
###############################################################################################

#Question 6
with open('1_contagion_period.txt') as file:
    for child in file:
        # we could retrieve values only with show_parameters = 0 but that's help us to cut
        # each part
        if re.match('\d{1,3} \d{1,3} \d{1,3}', child):
            statList.append(child)

#generate file for question (iii)

with open('2_contagion_period.txt', 'r') as file:
    for child in file:
        if(re.match('[0-9]+', child)):
            values = child.split(' ')
            for i in range (100):
                stat2List.append(values[i])

# convert the list to numpy array for treatement
#  and reshape it to 1000 lines of 100 columns    
tab = numpy.reshape(numpy.array(stat2List), (2000,100))
#print(tab)

for line in statList:
    # second value represent infected people
    infected = line.split(' ')[1]
    infectedList.append(int(infected))

contPeriodFrame ={
    0 : Series(infectedList[0:100]) , 1 : Series(infectedList[100:200]), 2 : Series(infectedList[200:300]),
    3 : Series(infectedList[300:400]) , 4 : Series(infectedList[400:500]), 5 : Series(infectedList[500:600]),
    6 : Series(infectedList[600:700]) , 7 : Series(infectedList[700:800]), 8 : Series(infectedList[800:900]),
    9 : Series(infectedList[900:1000]), 10 : Series(infectedList[0:100]) , 11 : Series(infectedList[100:200]), 
    12 : Series(infectedList[200:300]), 13 : Series(infectedList[300:400]) , 14 : Series(infectedList[400:500]), 
    15 : Series(infectedList[500:600]), 16 : Series(infectedList[600:700]) , 17 : Series(infectedList[700:800]), 
    18 : Series(infectedList[800:900]), 19 : Series(infectedList[900:1000])
}    

dfcontPeriod = DataFrame(contPeriodFrame)
#print(dfRayonMOB)

# durée de l'épidémie(i)
# boucler les 5 simulations jusqu'à qu'il n'existe plus d'individu infecté
for cmpt in range(20):
    boolean = False
    for i in range(cmpt*100,100*(cmpt+1)):
        
        if (infectedList[i]== 0 and not boolean):
            epidemieDuration.append(i-100*cmpt)
            # valeur de test
            boolean = True
            # toute les individus sont infectés pendant toute la simulation
    if (not boolean):
        epidemieDuration.append(99)        
df6= DataFrame({'durée épidémie':epidemieDuration})

#la proportion maximale de la population qui est infectée (ii)
df6['proportion maximale infectés']= Series(dfcontPeriod.max())

# la distribution des multi-infections (iii)
for simul in range (20) :
    for z in range (200) :
        try :
            a = []
            b = []
            
            with open('2_contagion_period.txt') as file:
                for child in file:
                    if re.match('[0-9]+', child) :
                        b.append(int(child[z])) #len(b) = 1000
            
            for c in range ( simul*100 , 100*(simul+1)) :
                a.append(b[c]) #len(a) = 100

            anew = []
            anew.append(a[0])

            for i in range (len(a)) :
                try :
                    if(a[i] != a[i+1] ) :
                        anew.append(a[i+1])
                except :
                    IndexError

            number = 0

            for j in range (len(anew)) :
                try :
                    if(anew[j] == 0 and anew[j+1] == 1) :
                        number += 1
                except :
                    IndexError

            #print(anew)
            #print("this {}th person was infected {} times".format(int((z+1)/2) +1 ,number))
            howmanynumber.append(number)
            #print("-"*30)
        except :
            ValueError

    #print("howmanynumber:", howmanynumber)
    sum = 0
    for s in range(len(howmanynumber)) :
        sum += howmanynumber[s]
    avg = sum/len(howmanynumber)
    #print("avg :", avg)
    listofavg.append(avg)
    howmanynumber.clear()
    avg = 0
#print(listofavg) #Average number of infections of people for a total of 10 simulators
df6['distribution des multi-infections']=Series(listofavg)

df6.index.names = ['Rang duree de contamination']
df6.to_csv('contagion_period.csv')
#print(df2)


statList.clear()
stat2List.clear()
infectedList.clear()
epidemieDuration.clear()
infectList.clear()
multi_infections.clear()
howmanynumber.clear()
listofavg.clear()
###############################################################################################

#Question 7
with open('1_immune_period.txt') as file:
    for child in file:
        # we could retrieve values only with show_parameters = 0 but that's help us to cut
        # each part
        if re.match('\d{1,3} \d{1,3} \d{1,3}', child):
            statList.append(child)

for line in statList:
    # second value represent infected people
    infected = line.split(' ')[1]
    infectedList.append(int(infected))

#generate file for question (iii)

with open('2_immune_period.txt', 'r') as file:
    for child in file:
        if(re.match('[0-9]+', child)):
            values = child.split(' ')
            for i in range (100):
                stat2List.append(values[i])

# convert the list to numpy array for treatement
#  and reshape it to 1000 lines of 100 columns    
tab = numpy.reshape(numpy.array(stat2List), (2000,100))
#print(tab)

immuPeriodFrame ={
    0 : Series(infectedList[0:100]) , 1 : Series(infectedList[100:200]), 2 : Series(infectedList[200:300]),
    3 : Series(infectedList[300:400]) , 4 : Series(infectedList[400:500]), 5 : Series(infectedList[500:600]),
    6 : Series(infectedList[600:700]) , 7 : Series(infectedList[700:800]), 8 : Series(infectedList[800:900]),
    9 : Series(infectedList[900:1000]), 10 : Series(infectedList[0:100]) , 11 : Series(infectedList[100:200]), 
    12 : Series(infectedList[200:300]), 13 : Series(infectedList[300:400]) , 14 : Series(infectedList[400:500]), 
    15 : Series(infectedList[500:600]), 16 : Series(infectedList[600:700]) , 17 : Series(infectedList[700:800]), 
    18 : Series(infectedList[800:900]), 19 : Series(infectedList[900:1000])
}    

dfimmuPeriod = DataFrame(immuPeriodFrame)
#print(dfRayonMOB)

# durée de l'épidémie(i)
# boucler les 5 simulations jusqu'à qu'il n'existe plus d'individu infecté
for cmpt in range(20):
    boolean = False
    for i in range(cmpt*100,100*(cmpt+1)):
        
        if (infectedList[i]== 0 and not boolean):
            epidemieDuration.append(i-100*cmpt)
            # valeur de test
            boolean = True
            # toute les individus sont infectés pendant toute la simulation
    if (not boolean):
        epidemieDuration.append(99)        
df7= DataFrame({'durée épidémie':epidemieDuration})

#la proportion maximale de la population qui est infectée (ii)
df7['proportion maximale infectés']= Series(dfimmuPeriod.max())

# la distribution des multi-infections (iii)
for simul in range (20) :
    for z in range (200) :
        try :
            a = []
            b = []
            
            with open('2_immune_period.txt') as file:
                for child in file:
                    if re.match('[0-9]+', child) :
                        b.append(int(child[z])) #len(b) = 1000
            
            for c in range ( simul*100 , 100*(simul+1)) :
                a.append(b[c]) #len(a) = 100

            anew = []
            anew.append(a[0])

            for i in range (len(a)) :
                try :
                    if(a[i] != a[i+1] ) :
                        anew.append(a[i+1])
                except :
                    IndexError

            number = 0

            for j in range (len(anew)) :
                try :
                    if(anew[j] == 0 and anew[j+1] == 1) :
                        number += 1
                except :
                    IndexError

            #print(anew)
            #print("this {}th person was infected {} times".format(int((z+1)/2) +1 ,number))
            howmanynumber.append(number)
            #print("-"*30)
        except :
            ValueError

    #print("howmanynumber:", howmanynumber)
    sum = 0
    for s in range(len(howmanynumber)) :
        sum += howmanynumber[s]
    avg = sum/len(howmanynumber)
    #print("avg :", avg)
    listofavg.append(avg)
    howmanynumber.clear()
    avg = 0
#print(listofavg) #Average number of infections of people for a total of 10 simulators
df7['distribution des multi-infections']=Series(listofavg)

df7.index.names = ['Rang duree immunité']
df7.to_csv('immune_period.csv')
#print(df2)


statList.clear()
stat2List.clear()
infectedList.clear()
epidemieDuration.clear()    
infectList.clear()
multi_infections.clear()
howmanynumber.clear()
listofavg.clear()
###############################################################################################

#Question 8
with open('1_nb_nodes.txt') as file:
    for child in file:
        # we could retrieve values only with show_parameters = 0 but that's help us to cut
        # each part
        if re.match('\d{1,3} \d{1,3} \d{1,3}', child):
            statList.append(child)

with open('2_nb_nodes.txt', 'r') as file:
    for child in file:
        if(re.match('[0-9]+', child)):
            values = child.split(' ')
            for i in range (100):
                stat2List.append(values[i])

# convert the list to numpy array for treatement
#  and reshape it to 1000 lines of 100 columns    
tab = numpy.reshape(numpy.array(stat2List), (2000,100))
#print(tab)


for line in statList:
    # second value represent infected people
    infected = line.split(' ')[1]
    infectedList.append(int(infected))

densityFrame ={
    0 : Series(infectedList[0:100]) , 1 : Series(infectedList[100:200]), 2 : Series(infectedList[200:300]),
    3 : Series(infectedList[300:400]) , 4 : Series(infectedList[400:500]), 5 : Series(infectedList[500:600]),
    6 : Series(infectedList[600:700]) , 7 : Series(infectedList[700:800]), 8 : Series(infectedList[800:900]),
    9 : Series(infectedList[900:1000]), 10 : Series(infectedList[0:100]) , 11 : Series(infectedList[100:200]), 
    12 : Series(infectedList[200:300]), 13 : Series(infectedList[300:400]) , 14 : Series(infectedList[400:500]), 
    15 : Series(infectedList[500:600]), 16 : Series(infectedList[600:700]) , 17 : Series(infectedList[700:800]), 
    18 : Series(infectedList[800:900]), 19 : Series(infectedList[900:1000])
}    

dfdensity = DataFrame(densityFrame)
#print(dfRayonMOB)

# durée de l'épidémie(i)
# boucler les simulations jusqu'à qu'il n'existe plus d'individu infecté
for cmpt in range(19):
    boolean = False
    for i in range(cmpt*100,100*(cmpt+1)):
        
        if (infectedList[i]== 0 and not boolean):
            epidemieDuration.append(i-100*cmpt)
            # valeur de test
            boolean = True
            # toute les individus sont infectés pendant toute la simulation
    if (not boolean):
        epidemieDuration.append(99)        
df8= DataFrame({'durée épidémie':epidemieDuration})

#la proportion maximale de la population qui est infectée (ii)
df8['proportion maximale infectés']= Series(dfdensity.max())

# la distribution des multi-infections (iii)
for simul in range (20) :
    for z in range (200) :
        try :
            a = []
            b = []
            
            with open('2_nb_nodes.txt') as file:
                for child in file:
                    if re.match('[0-9]+', child) :
                        b.append(int(child[z])) #len(b) = 1000
            
            for c in range ( simul*100 , 100*(simul+1)) :
                a.append(b[c]) #len(a) = 100

            anew = []
            anew.append(a[0])

            for i in range (len(a)) :
                try :
                    if(a[i] != a[i+1] ) :
                        anew.append(a[i+1])
                except :
                    IndexError

            number = 0

            for j in range (len(anew)) :
                try :
                    if(anew[j] == 0 and anew[j+1] == 1) :
                        number += 1
                except :
                    IndexError

            #print(anew)
            #print("this {}th person was infected {} times".format(int((z+1)/2) +1 ,number))
            howmanynumber.append(number)
            #print("-"*30)
        except :
            ValueError

    #print("howmanynumber:", howmanynumber)
    sum = 0
    for s in range(len(howmanynumber)) :
        sum += howmanynumber[s]
    avg = sum/len(howmanynumber)
    #print("avg :", avg)
    listofavg.append(avg)
    howmanynumber.clear()
    avg = 0
#print(listofavg) #Average number of infections of people for a total of 10 simulators
df8['distribution des multi-infections']=Series(listofavg)


df8.index.names = ['Rang densité']
df8.to_csv('nb_nodes.csv')
#print(df2)


statList.clear()
stat2List.clear()
infectedList.clear()
epidemieDuration.clear()
infectList.clear()
multi_infections.clear()
howmanynumber.clear()
listofavg.clear()
###############################################################################################
