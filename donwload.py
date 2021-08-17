import requests
import os
from tqdm import tqdm
url = 'https://www.oia.ncu.edu.tw/index.php/en/download/category/164-%E6%96%87%E5%AD%B8%E9%99%A2.html?download=382:%E4%B8%AD%E6%96%87%E7%B3%BB'



#path = r'C:\Users\Hardy\Desktop\downloadfile\downloadfile\word.doc'
def download_file(url,filename):
    path = r'C:\Users\Hardy\Desktop\downloadfile\downloadfile' + r'/' + filename
    
    try:
        r = requests.get(url, stream = True,verify=False)
        total_size_in_bytes= int(r.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(path, 'wb') as f:
            for data in r.iter_content(block_size):
            #for data in r:
                progress_bar.update(len(data))
                f.write(data)

    except:
        print(url,':    download error')   
    

urls = []
filenames = []
with open(os.getcwd()+r'/data/urls.txt',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    urls.append(line.split(' ')[1])
    filenames.append(line.split(' ')[0])

print(urls)
print(filenames)


for url,filename in zip(urls,filenames):
    
    download_file(url,filename)


#download_file(url)
#print(os.getcwd()+r'\data\url.txt')

