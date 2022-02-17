# CarScannerCSV
 
This script converts/cleans up Car Scanner CSV files.

Usage:

FormatCSV.py -i <inputfile> -o <outputfile> [-a -s <samplerate>]

-a will return all columns in input CSV (the default is to remove columns that aren't relevant to looking at the charge curve)
-s specify the sample rate that the data will be compressed to, the default is 30s