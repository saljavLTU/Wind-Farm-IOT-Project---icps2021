import pandas as pd
from mat4py import loadmat
from mat4py import savemat

#data = loadmat('T2_traineddict.mat')
data = loadmat('check_dictionary.mat')
print(data)

df = pd.DataFrame(data)
df.to_csv('Dictionary_Data-Temp.csv') #your_data.csv final data in csv file

savemat('check_dictionary.mat',data)


###############################

pdObj = pd.read_json('Testingt1d1_samples.json', orient='index')
csvData = pdObj.to_csv(index=False)
print(csvData)
pdObj.to_csv('Experiment_Output-Temp.csv')


##############################




# with open('Testing.json') as json_file:
# 	jsondata = json.load(json_file)
#
# data_file = open('Experiment_Output_File.csv', 'w', newline='')
# csv_writer = csv.writer(jsondata)
#
# data_file.close()
