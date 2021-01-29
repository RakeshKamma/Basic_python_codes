
import csv
#creating a list of dictionaries
States_Of_India = [{"name":"Andhra_Pradesh",
                                         "Population":10000,
                                         "Rank_based_on_area":7},
                       {"name":"Karnataka",
                                    "Population":100000,
                                    "Rank_based_on_area":6},
                       ]
#finding the column names of our output csv file
keys=States_Of_India[0].keys()
#opening the csv file and writing the details of states_of_india into it with its keys
with open('first.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(States_Of_India)



