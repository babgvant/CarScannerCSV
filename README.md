# CarScannerCSV
 
This script converts/cleans up Car Scanner CSV files. It is based on the work of Sam (phidauex) from the Mach-E Forums who was nice enough to share his parsing script with me.

Usage:

FormatCSV.py -i <inputfile> -o <outputfile> [-a -s <samplerate>]

-a will return all columns in input CSV (the default is to remove columns that aren't relevant to looking at the charge curve)
-s specify the sample rate that the data will be compressed to, the default is 30s