import os
import sys
def execute(input,output):
    fileList = os.listdir(input)
    #挑出shp数据 
    for file in fileList:
        if(file.split('.')[1]== 'inp'):
            inp=file
            break
    exe_program= 'aermap '+input+'/'+inp+' '+output+'/out'
    os.chdir('C:\\Users\\91308\\Desktop\\p\\Model\\AERMOD\AERMAP\\aermap_testcase\\aermap_testcase\\AK-MixedDEM_CrossUTM') #跳转到exe所在路径
    os.system(exe_program)#在exe所在路径下执行命令行
if __name__ == '__main__':
    #-test case 
    # inp='C:\\Users\\91308\\Desktop\\p\\Model\\AERMOD\AERMAP\\aermap_testcase\\aermap_testcase\\AK-MixedDEM_CrossUTM\\'
    # out='C:\\Users\\91308\\Desktop\\p\\Model\\AERMOD\AERMAP\\aermap_testcase\\aermap_testcase\\out_tep\\'
    # inp 输入数据集文件路径
    # par 输入数据集文件路径
    execute(sys.argv[1],sys.argv[2])
