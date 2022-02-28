from subprocess import run


nb_infected = 2
travel_distance = 200
nb_vaccinated = 0
vaccine_efficiency = 2
infection_period = 100
contagion_period = 200
immune_period = 300
nb_nodes = 100

for i in range(10):
    # 10 simulations varying number of infected 
    #gui=0 ==> to eliminate interface snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0', '-nb_snapshots=100','show_parameters = 0',f'-nb_infected={nb_infected}'],capture_output=True)
    nb_infected += 2 
    with open ('1_nb_infected.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(10):
    # 10 simulations varying rayon mobilité (trvael distance) 
    #gui=0 ==> to eliminate interface snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-nb_snapshots=100','show_parameters = 0',f'-travel_distance={travel_distance}'],capture_output=True)
    travel_distance += 50 
    with open ('1_travel_distance.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(10):
    # 10 simulations varying number of vaccinated 
    #gui=0 ==> to eliminate interface snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-nb_snapshots=100','show_parameters = 0',f'-nb_vaccinated={nb_vaccinated}'],capture_output=True)
    nb_vaccinated += 2 
    with open ('1_nb_vaccinated.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(10):
    # 10 simulations varying vaccine_efficiency
    #gui=0 ==> to eliminate interface snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-nb_snapshots=100','show_parameters = 0',f'-vaccine_efficiency={vaccine_efficiency}'],capture_output=True)
    vaccine_efficiency += 2 
    with open ('1_vaccine_efficiency.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(20):
    # 20 simulations varying vaccine_efficiency
    #gui=0 ==> to eliminate interface snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-nb_snapshots=100','show_parameters = 0',f'-infection_period={infection_period}'],capture_output=True)
    infection_period += 50 
    with open ('1_infection_period.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(20):
    # 20 simulations varying contagion_period
    #gui=0 ==> to eliminate interface snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-nb_snapshots=100','show_parameters = 0',f'-contagion_period={contagion_period}'],capture_output=True)
    contagion_period += 50
    with open ('1_contagion_period.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(20):
    # 20 simulations varying vaccine_efficiency
    #gui=0 ==> to eliminate interface snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-nb_snapshots=100','show_parameters = 0',f'-immune_period={immune_period}'],capture_output=True)
    immune_period += 50 
    with open ('1_immune_period.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(20):
    # 20 simulations varying nb_nodes (density)
    #gui=0 ==> to eliminate interface snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-nb_snapshots=100','show_parameters = 0',f'-nb_nodes={nb_nodes}'],capture_output=True)
    nb_nodes += 50
    with open ('1_nb_nodes.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))



#####################################################################################################
###################### Plusieurs simulations pour chaque noeud de paramètres #####################
############################################ son état ###############################################
#####################################################################################################

# column : node  
# line : time    
# 0: normal 1: infected 2: immune                                                           

for i in range(10):
    # 10 simulations varying number of infected 
    #gui=0 ==> to eliminate interface printout for multiple snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-printout=2', '-nb_snapshots=100','show_parameters = 0',f'-nb_infected={nb_infected}'],capture_output=True)
    nb_infected += 2 
    with open ('2_nb_infected.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(10):
    # 10 simulations varying rayon mobilité (trvael distance) 
    #gui=0 ==> to eliminate interface printout for multiple snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-printout=2','-nb_snapshots=100','show_parameters = 0',f'-travel_distance={travel_distance}'],capture_output=True)
    travel_distance += 50 
    with open ('2_travel_distance.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(10):
    # 10 simulations varying number of vaccinated 
    #gui=0 ==> to eliminate interface printout for multiple snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-printout=2','-nb_snapshots=100','show_parameters = 0',f'-nb_vaccinated={nb_vaccinated}'],capture_output=True)
    nb_vaccinated += 2 
    with open ('2_nb_vaccinated.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(10):
    # 10 simulations varying vaccine_efficiency
    #gui=0 ==> to eliminate interface printout for multiple snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-printout=2','-nb_snapshots=100','show_parameters = 0',f'-vaccine_efficiency={vaccine_efficiency}'],capture_output=True)
    vaccine_efficiency += 2 
    with open ('2_vaccine_efficiency.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(20):
    # 20 simulations varying vaccine_efficiency
    #gui=0 ==> to eliminate interface printout for multiple snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-printout=2','-nb_snapshots=100','show_parameters = 0',f'-infection_period={infection_period}'],capture_output=True)
    infection_period += 50 
    with open ('2_infection_period.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(20):
    # 20 simulations varying contagion_period
    #gui=0 ==> to eliminate interface printout for multiple snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-printout=2','-nb_snapshots=100','show_parameters = 0',f'-contagion_period={contagion_period}'],capture_output=True)
    contagion_period += 50
    with open ('2_contagion_period.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(20):
    # 20 simulations varying vaccine_efficiency
    #gui=0 ==> to eliminate interface printout for multiple snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-printout=2','-nb_snapshots=100','show_parameters = 0',f'-immune_period={immune_period}'],capture_output=True)
    immune_period += 50 
    with open ('2_immune_period.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))

for i in range(20):
    # 20 simulations varying nb_nodes (density)
    #gui=0 ==> to eliminate interface printout for multiple snapshot ==> number of sample
    # capture_output to to capture both STDOUT and STDERR independently
    proc = run(['java','-jar','Virus.jar','-gui=0','-printout=2','-nb_snapshots=100','show_parameters = 0',f'-nb_nodes={nb_nodes}'],capture_output=True)
    nb_nodes += 50
    with open ('2_nb_nodes.txt','a') as file:
        file.write(proc.stdout.decode('utf-8'))                                                              