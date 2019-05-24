# Job Ofert Fetcher
This is a simple script that downloads job offers from pracuj.pl/praca and every of its subpage. When script downloaded data then lightly clean it up of unnecessary informations and then save this data into output.json file. The script also contains its own log module that records information about downloaded data and errors, this logs will be stored in log.txt file.



## Requirements
For proper operation of the script, the following requirements must be met:
1. Python version >= 3.6
2. bs4 version >= 4.7
3. requests version >= 2.22