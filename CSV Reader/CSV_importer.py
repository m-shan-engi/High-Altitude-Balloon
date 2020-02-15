""" File template for using the balloon data, imported via a *.csv file """


def import_from_csv(filename):
    "Imports the data from a *.csv file stored in the same folder as this program"

    contents = ""
    with open(filename, "r") as f:
        contents = f.read()
        f.close()
    
    split_contents = [entry.split(",") for entry in contents.split("\n") if entry != ""]

    data_dictionarys = []
    for entry in split_contents:
        new_dict = dict()
             
        new_dict["RockBLOCK Base Serial"] = entry[0]    # Base RockBLOCK serial number       
        new_dict["GPS TX Time"] = [entry[1][:4]] + [entry[1][i:i+2] for i in range(4,14,2)]  # GPS Tx Time (YYYYMMDDHHMMSS)               
        new_dict["GPS Lat"] = float(entry[2])           # GPS Lat             
        new_dict["GPS Long"] = float(entry[3])          # GPS Long         
        new_dict["GPS Alt"] = int(entry[4])             # GPS Alt           
        new_dict["GPS Speed"] = float(entry[5])         # GPS Speed             
        new_dict["GPS Heading"] = int(entry[6])         # GPS Heading             
        new_dict["GPS HDOP"] = float(entry[7])          # GPS HDOP            
        new_dict["GPS Sat"] = int(entry[8])             # GPS Satellites            
        new_dict["Pressure"] = float(entry[9])          # Pressure               
        new_dict["Humidity"] = float(entry[10])         # Humidity               
        new_dict["Temperature"] = float(entry[11])      # Temperature               
        new_dict["Battery"] = float(entry[12])          # Battery           
        new_dict["Iteration"] = int(entry[13])          # Iteration Count                       
        #new_dict["Serial Number"] = entry[14]           # RockBlock Serial No.
        data_dictionarys.append(new_dict)

    return data_dictionarys


if __name__ == "__main__":

    my_filename = "test_data_file.csv"
    data = import_from_csv(my_filename)

    ### The data variable above is a list of dictionarys - each dictionary has the data from one transmission

    ### Example code to put all the temperatures into a list:

    my_temperatures = []
    for entry in data:
        temperature = entry["Temperature"]      # Change "Temperature" here for the data you want (see above for names)
        my_temperatures.append(temperature)

    print(my_temperatures)


    ### Put your code below here
my_altitudes = []
for entry in data:
    GPS Alt = entry["Temperature"]
    my_altitudes.append(GPS Alt)
print(my_altitudes)
    
import matplotlib.pyplot as plt  #Imports the pyplot function from matplotlib, renames it plt.
import numpy  #Imports numpy.
from datetime import date as dt  #Imports the date function from datetime.

today = dt.today() #Saves the date in the variable 'today'.
day = (str(today.day)+"/").zfill(3)  #Converts the day to a string, adds a forwardslash and pads it with zeros.
month = (str(today.month)+"/").zfill(3) #Converts the month to a string, adds a forwardslash and pads it with zeros.
date = (day+month+str(today.year)) #Forms a dtring value for the date in the form dd/mm/yyyy
filedate = date.replace('/', '_')  #Removes the forward slashes from the date so that it can be used in a filename.

##Creating the graphs. This can be copied and tweaked to plot different variables against each other.

plt.plot(my_temperatures, my_altitudes, 'bo--')  #Creates a plot of Temperature vs altitude, points are marked with a blue circle and connected with a dashed line.
plt.title("Temperature vs Altitude  " + date)   #Titles the plot 'Temperature vs Altitude  dd/mm/yyyy'.
plt.xlabel('Temperature, Celsius')   #Labels the x axis 'Temperature, Celsius'.
plt.ylabel('Altitude, feet')   #Labels the y axis 'Altitude, feet'. 
fig1 = plt.gcf()  #Saves the current plot as 'fig1'
fig1.savefig('A_vs_T_'+ filedate +'.png', transparent=True, dpi=80, bbox_inches="tight") #Saves the plot as a png file named 'A_vs_T_dd_mm_yyyy.png'.




