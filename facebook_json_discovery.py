import sys
import json
import csv
import os

json_file_path = "D:\sample_FB_json.json"
csv_file_path  =  "result.csv"

def second_level_nodes(json_file_path,csv_file_path):

    # Function takes the json file and csv file paths.
    # Loops through the json content and outputs all the second level nodes in the root node 'data' (taking data as the first level node)
    #The output is routed to a csv file (taken as one of the input parameters).

    L2_nodes = []
    try:
        fp = open(json_file_path, 'r+')
        print("json file opened")
        #read the file content
        json_value = fp.read()
        #Loading the json content
        raw_data = json.loads(json_value)
        #take the list named 'data', which is a list of dictionaries
        data = raw_data['data']
        #loop through each dictionary in the list
        for i in data:
            for k, v in i.items():
                #avoiding repeated keys in each loop
                if not k in L2_nodes:
                    #append the second level nodes to the list L2_nodes
                    L2_nodes.append(k)

    except IOError as e:
        #catches any errors in opening and reading the file

        print("I/O error({0}): {1}".format(e.errno, e.strerror))


    #calculate number of Level-2 nodes
    length = len(L2_nodes)

    try:
        #open the csv file with file pointer as 'fp'
        with open(csv_file_path, 'w') as fp:
            print("csv file opened")

            #create writer object with file pointer
            writer = csv.writer(fp)
            print("csv file running")

            #writes row to the csv file

            writer.writerow(L2_nodes)
            writer.writerow(['number of nodes:',length])
            print("values appended to the csv file")

    except IOError as e:
        #catch any errors in opening the file and writing to it
        print("I/O error({0}): {1}".format(e.errno, e.strerror))


    print(L2_nodes)
    print("Number of first level nodes :")
    print(len(L2_nodes))

second_level_nodes(json_file_path,csv_file_path)
