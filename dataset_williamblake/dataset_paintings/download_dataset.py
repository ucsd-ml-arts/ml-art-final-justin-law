# after generating the csv, download in folders named by csv 

# dataset is from https://www.robots.ox.ac.uk/~vgg/data/paintings/
# runtime is about 10 minutes as it has to gather thousands of paintings using the requests package
import csv
import os
import requests
from collections import Counter

# custom ABC class for counting labels
class CountLabels():
    def __init__(self):
        self.cnt = Counter()

    def add(self, label):
        self.cnt[label] += 1
        self._last_used = label

    @property
    def last_count(self):
        return self.cnt[self._last_used]

# for hyperparameters, the only thing you may need to control is whitelist and blacklist.
class HyperParameter(CountLabels):
    def __init__(self):
        super().__init__()
        # hyperparameters
        self.dataset_type = None # None, train, validation, test or a list containing a comb of these
        self.blacklist = [''] # list containing labels (see csv) in blacklist
        self.whitelist = ['dog'] # list containing labels (see csv) in whitelist
        self.filepath = 'download.csv' # filepath of csv
        self.multiprocess = True # enable 4 threads. Turn off if low performance machine.
        self.num_threads = 8 # lower if low performance machine and want multiprocess
        
def parse_csv(csvfile,hyperparam):
    reader = csv.reader(csvfile)
    
    for row in reader:
        label = row[-1].strip(" \\\'").replace(' ','_')
        link = row[0]
        
        if (label in hyperparam.blacklist) and (label not in hyperparam.whitelist) or ('http' not in link):
            continue

        if (hyperparam.dataset_type is None) or (row[-2].strip("\\\'") in hyperparam.dataset_type):
            hyperparam.add(label)
            yield (label +'/'+str(hyperparam.last_count)+'.png', link)

# https://markhneedham.com/blog/2018/07/15/python-parallel-download-files-requests/
def fetch_url(http):
    path, url = http

    directory = ''.join(path.split('/')[:1])
    directory = 'paintings/' + directory
    os.makedirs(directory, exist_ok=True)

    path = 'paintings/' + path
    if not os.path.exists(path):
        r = requests.get(url, stream=True)

        error = (r.status_code != 200)
        if not error:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
    return path

if __name__ == '__main__':
    hyperparam = HyperParameter()
    with open(hyperparam.filepath, 'r') as csvfile:
        urls = [item for item in parse_csv(csvfile,hyperparam)]

    if os.path.exists('paintings'):
        raise Exception('Dataset already exists. Delete paintings/' \
                         'if you want to download again')

    os.makedirs('paintings')

    if hyperparam.multiprocess:
        import multiprocessing
        pool = multiprocessing.Pool(processes=hyperparam.num_threads)
        pool.map(fetch_url, urls)
    else:
        for entry in urls:
            fetch_url(entry)