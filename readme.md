# DataPrep
Some 
useful utlity scripts to prep data

shuffleCSV.py - A script to strip the ID column of a file, shufle the rows and re-append a ID. To ensure sensitive anonymous data sets rows are not in sequential order to minimise re-identification.

Validator/Validator.py - A script that uses the cutplace module to validate CSV files. The script has the ability to scan through a directory of incoming files.

Thresholds/Thresholds.py - scans a file and ensures values are truncated to aceptable values, to minimise the risk of identification.

EmailExtractor - A script to merge multiple email lists and remove admin emails to form a mailing list. I used this to prepare emails pulled from a powershell script of folder permissions from AD groups.

Converters - Scans a converts a entire directory of files to one format to another, supported formats (DTA to CSV - STATA to CSV,more to come)

