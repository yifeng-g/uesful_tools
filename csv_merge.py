import csv
import glob
import pandas as pd


def merge():
    csv_list = glob.glob(file_addres + '*' + '.csv')
    print('共发现csv文件' + str(len(csv_list)) + '个')
    for i in csv_list:
        content = open(i,'r',encoding='utf-8').read()
        with open(file_addres + 'merge.csv','a',encoding='utf-8') as f:
            f.write(content)
    print('done')

def delete(target_file):
    content = pd.read_csv(target_file,encoding='utf-8',header=0,low_memory=False)
    datalist = content.drop_duplicates()
    datalist.to_csv(target_file)

if __name__ == '__main__':
    local_df = pd.DataFrame(pd.read_csv('D:/python/pythonProject1/TandE/2019-2021/locale.csv'))
    file_addres = 'G:/data/'
    #file_addres = 'C:/Users/gyf/Desktop/paper/harvesting_silge/'
    # for i in range(len(local_df)):
    #     city = local_df['city'][i]
    merge()
    delete(file_addres + 'merge.csv')

