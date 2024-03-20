import matplotlib as mpl
import matplotlib.pyplot as plt
changes_plot=[]
temp_plot=[]

# Constants
## albedo
a = 0.3
#solar constant
sc = 1367
# initial temp in kelvin
ti = 288
# emissivity
e = 0.7
## EarthSurface area
sa = 5.1*10**14
## Radius
r = 6371000

# Surface Capacity
shc = 4*10**8

## Sigma
sigma = 5.67*10**-8

'''
def pop(incoming_energy, years, current_temp, outgoing_energy):
    if years == 0:
        return incoming_energy
         #return incoming_sys.exit()energy
    else:
        changes = pop(incoming_energy,years-1,current_temp,outgoing_energy)
        print(changes)
        changes_plot.append(changes)
        return changes + (1-changes/outgoing_energy)

pop(600,80,0.1,20000)
plt.plot(changes_plot)
plt.show()

0.5
3
0.1
288
15

'''


initial_temp=int(input('initial temperature in kelvin: ' + '\n'))
number_of_years=int(input('estimatede number of years:' + '\n'))
input_increase=int(input('percentage from 0-10% increase for the initial year in incoming energy: '))

def simple_simulator(surface_temp,years,increase):
    outgoing = incoming = sigma*surface_temp**4
    time_delta=60*60*24*365
    temp_plot.append(surface_temp)
    incoming = incoming * (100 + increase) / 100
    while years > 0:
        outgoing=surface_temp**4*sigma
        temp_delta=(incoming-outgoing)/shc*time_delta
        surface_temp+=temp_delta
        years -= 1
        temp_plot.append(surface_temp)

simple_simulator(initial_temp,number_of_years,input_increase)
print(temp_plot)
plt.plot(temp_plot)
plt.show()
