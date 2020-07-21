# --* coding=utf-8 *--
from cStringIO import StringIO
from pymongo import MongoClient
import gridfs
import os
import matplotlib.pyplot as plt
import matplotlib.image as iming
import bson.binary
import numpy as np
if __name__ == '__main__':
        connect = MongoClient('106.14.173.166', 27017)  # 创建连接点
        db = connect.mydb
        print db.collection_names()
        imgput = gridfs.GridFS(db)
        dirs = r'C:\Users\61980\Desktop\pic'
        files = os.listdir(dirs)
        for file in files:
                filesname = dirs + '\\' + file
                print filesname
                imgfile=iming.imread(filesname)
                # iming.imsave('s.jpg',imgfile)
                # print type(imgfile),imgfile
                # imgfile.shape()
                plt.imshow(imgfile)
                plt.axis('off')
                plt.show()
                f=file.split('.')
                print f
                datatmp=open(filesname,'rb')
                data=StringIO(datatmp.read())
                content=bson.binary.Binary(data.getvalue())
                # print content
                insertimg=imgput.put(data,content_type=f[1],filename=f[0])
                datatmp.close()