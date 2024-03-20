import matplotlib as mpl
import matplotlib.pyplot as plt
import decimal
temp_plot=[]
time_plot=[]
em_plot=[]
a_plot=[]

def repeat(ratio):
    def pop(temp, a,em, ac, ti, time, time_delta):
        ## Sigma
        sigma = 5.67*10**-8
        duration = 0
        # assuming that the earth is at equalibirum at year 0
        outgoing = incoming = (1-a)*sc/4*sa
        time_seconds=60*60*24*365*time_delta
        temp_plot.append(temp)
        time_plot.append(duration)
        print(outgoing)
        print(temp)
        em_plot.append(em)
        a_plot.append(a)


        # emissivity increases because blacker surface of earth
        # albedo decreases due to blacker earth

        while time>=0 and em <= 1 and a>=0 and temp>=10:
            duration += time_delta

            a=a*(100-albedo_change)/100
            incoming = (1-a)*sc/4
            em=em*(100+(ratio**(albedo_change)-1))/100
            print(temp)
            outgoing=(pow(temp,4))*em*sigma
            temp_delta=(incoming-outgoing)/shc*time_seconds
            temp+=temp_delta
            time -= time_delta
            temp_plot.append(temp)
            time_plot.append(duration)
            em_plot.append(em)
            a_plot.append(a)
            print(temp_plot, time_plot)




    # Constants
    ## albedo
    a = 0.3
    #solar constant
    sc = 1367
    # initial temp in kelvin
    ti = 288
    # emissivity
    e = 0.5
    ## EarthSurface area
    sa = 5.1*10**14
    ## Radius
    r = 6371000

    # Surface Capacity
    shc = 4*10**8



    pop(initial_temp, a, e, albedo_change, initial_temp, number_of_years, time_delta)
    print(time_plot, temp_plot)

    fig, axs = plt.subplots(2)
    fig.suptitle('temp, a&Em against time. when emissivity increase ratio per year is: ' + str(ratio**(number_of_years*time_delta)))
    axs[0].plot(time_plot, temp_plot)
    axs[1].plot(time_plot, em_plot)
    axs[1].plot(time_plot, a_plot)
    plt.show()

    '''
        temp_plot=[]
        time_plot=[]
        em_plot=[]
        a_plot=[]

    f1 = plt.plot(time_plot, temp_plot)
    f2 = plt.plot(time_plot, a_plot)
    f2 = plt.plot(time_plot, em_plot)

     f1.plot(time_plot, temp_plot)
     f1.xlabel('t in years')
     f1.ylabel('temp in kelvin [k]')

     f2.plot(time_plot, a_plot)
     f2.plot(time_plot, em_plot)

    f1.show()
    f2.show()
    '''
a=float(input('Initial albedo starts at what value between 0 and 1? \n the average on earth is around 0.3. value of albedo : '))
albedo_change=float(input('what percentage should this go down in year 0? Percentage: '))
time_delta=float(input('How often should the new values be calculated in terms of years? e.g. 0.1 [years] : '))
initial_temp=float(input('initial temperature in kelvin: ' ))
number_of_years=float(input('estimatede number of years: ' ))

for i in range(1,8):

    repeat(1+i/50)
    temp_plot=[]
    time_plot=[]
    em_plot=[]
    a_plot=[]
