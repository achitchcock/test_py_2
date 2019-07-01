import cPickle
import os

def build_data(size):
    data = {}
    for i in xrange(size):
        data['PLMN-S2OSS/RNC-1607/WBTS-1002/MRBTS-1/RET-{}'.format(i)] = i
    return data

def pickle_data(entries=0):
    file_name = 'tilt_data'
    tilts = build_data(entries)
    with open(file_name, 'wb') as t_data:
        cPickle.dump(tilts, t_data, protocol=-1)

    size = os.path.getsize(os.path.join(os.path.curdir, file_name))
    print('Number of entries: {} \n\tFile size: {} bytes\n\tFile size: {} KB\n\tFile_size: {} MB'.format(
            entries,
            size,
            size/1024.0,
            size/1024.0/1024.0)
          )

if __name__ == "__main__":
    for i in [10000,1000,100,10]:
        pickle_data(i)