import re
import pandas as pd

sample_data = {
    'Name': ['Hannah Thompson','Bob Thomas','Paul Johnson','Julia Martin','Nina Moore'],
    'ID' : ['R4604489@data.pl','K5832875','Y4939317@data.pl','P1290000@data.pl','Y4821158 Y4821158']
}

tabela = pd.DataFrame(sample_data)
tabela['user_id'] = ''

def get_uid(text):
    uid = re.findall(r"^[A-Z]{1}[0-9]{7}", text)
    return uid[0]                    

for i in range(len(tabela)):
    text = tabela['ID'][i]
    tabela['user_id'][i]= get_uid(text)


print(tabela)