# Import necessary packages
import sys
import getopt
import pandas as pd

# Setup the file details for processing
inputfile = ''
outputfile = ''
allcols = False
samplerate = "30s"
usageText = "FormatCSV.py -i <inputfile> -o <outputfile> [-a -s <samplerate>]\r\n-a will return all columns in input CSV -s 30s"

try:
    opts, args = getopt.getopt(sys.argv[1:], "hai:o:s:")
except getopt.GetoptError:
    print (usageText)
    sys.exit(2)
if len(opts) < 2:
    print (usageText)
    sys.exit()

for opt, arg in opts:
    if opt == "-h":
        print (usageText)
        sys.exit()
    elif opt in ("-i"):
        inputfile = arg
    elif opt in ("-o"):
        outputfile = arg
    elif opt in ("-s"):
        samplerate = arg
    elif opt in ("-allcols"):
        allcols = True

print ("Input file: ", inputfile)
print ("Output file: ", outputfile)
print ("all columns: ", allcols)
print ("sample rate: ", samplerate)

#filename = "data\\2022-02-12 17-02-18" # omit .csv
index = 'time' # Name of the date/time index column in the CSV

# Read the CSV into a dataframe "df" with date/time processing
df = pd.read_csv("%s" % inputfile, index_col=index, parse_dates=[index])

# Diagnostic to check dataframe shape and start/end times
print("Dataframe shape: ", df.shape)
dt = (df.index[-1] - df.index[0])
print("Number of hours between start and end time: ", round(dt.total_seconds()/3600,3))

# Create a rolling average to fill the gaps, and then resample to 1 seconds, load into "df2"
df2 = df.rolling(8, min_periods=1).median()
df2 = df2.resample(samplerate).median()
df2 = df2.interpolate(method='linear')

# Create column for HV charge power (we don't need to do this, the data is in "Hybrid/EV Charger Power (kW)")
#df2["HV Charger Output Power (kW)"] = df2["HV Charger Output Voltage (V)"] * df2["HV Charger Output Current Measured (A)"] / 1000

if not allcols:
    # Drop any columns we don't need
    df2.drop(df2.filter(regex="Absolute pedal"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Distance"),axis=1, inplace=True)
    #df2.drop(df2.filter(regex="Engine"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Primary"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Secondary"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Vehicle"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Average"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="fuel"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Fuel"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="GPS"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Unnamed"),axis=1, inplace=True)
    #df2.drop(df2.filter(regex="Hybrid"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="LVB"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="ODB"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="(kPa)"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Engine R"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="# warm-ups since codes cleared ()"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="A/C Compressor"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Accelerator"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Aux 12V"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="BCM"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Brake"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Calculated engine"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Control"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="EV Instant"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="EVSE"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Grill Shutter"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV AC Charger Input"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Lateral"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Steering"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Yaw"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Coolant Heater"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV Charger Maximum Power (kW)"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV Contactor"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV Current"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV DC Charger"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV Leakage"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV Negative"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV Positive"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HVB"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="Transmission temp"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV Charger Proximity Status"),axis=1, inplace=True)
    df2.drop(df2.filter(regex="HV Charger Voltage Requested"),axis=1, inplace=True)
    df2.drop(df2.filter(like="Engine coolant temperature (℉)"),axis=1, inplace=True)
    df2.drop(df2.filter(like="Engine coolant temperature (A) (℉)"),axis=1, inplace=True)
    df2.drop(df2.filter(like="HV AC Charger Coupler Temperature (℉)"),axis=1, inplace=True)
    df2.drop(df2.filter(like="HV Charger Current Requested (A)"),axis=1, inplace=True)
    df2.drop(df2.filter(like="HV Charger Output Reduction Temperature (%)"),axis=1, inplace=True)
    df2.drop(df2.filter(like="HV Charger Pilot Duty Cycle (%)"),axis=1, inplace=True)
    df2.drop(df2.filter(like="Hybrid/EV Battery System Current (A)"),axis=1, inplace=True)
    df2.drop(df2.filter(like="OBD Module Voltage (V)"),axis=1, inplace=True)
    df2.drop(df2.filter(like="Hybrid/EV Battery Power (kW)"),axis=1, inplace=True)
    df2.drop(df2.filter(like="Hybrid/EV Battery System Voltage (V)"),axis=1, inplace=True)

# Output a cleaned up and resampled CSV to the original file name plus "-merged"
# df2.to_csv("%s-converted.csv" % filename)
df2.to_csv(outputfile)