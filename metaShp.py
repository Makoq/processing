import os
import json
import shapefile  #导入模块

def execute(input,output):
    fileList = os.listdir(input)
    #挑出shp数据 
    for file in fileList:
        if(file.split('.')[1]== 'shp'):
            shp_file=file
            break
    sf = shapefile.Reader(input+'/'+shp_file) #shp路径，读入shp文件
    metaDict={'Shape Type':sf.shapeTypeName,'Elements Number':len(sf.shapes()),'Bounding Box':sf.bbox}
    fieldsName=[]
    for field in sf.fields:
        if(isinstance(field,list)):
            fieldsName.append(field[0])
    metaDict['fields']=fieldsName
    size = 0
    for root, dirs, files in os.walk(input):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    metaDict['size']=str(size)+'bytes'
    print(metaDict)      
    return True
if __name__=='__main__':
    i='D:\Projects\processing\input\shp\china'
    o='D:\Projects\processing\output\shp\china'
    if execute(i,o) is True:
        print('ok')