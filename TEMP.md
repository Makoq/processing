# exe 调度中间件

import os
def execute(process_path,params):
    os.chdir(process_path) #跳转到exe所在路径
    r_v = os.system(params)#在exe所在路径下执行命令行
    print(r_v) 
    return True
if __name__ == '__main__':
    #-test case 
    path='C:\\Users\\91308\\Desktop\\p\\Model\\AERMOD\AERMAP\\aermap_testcase\\aermap_testcase\\AK-MixedDEM_CrossUTM'
    par='aermap aermap_AK-MixedDEM_CrossUTM.inp aermap_AK-MixedDEM_CrossUTM.out'
    # path exe所在路径，不包含exe子集
    # par exe调用一系列参数，包含exe本身及其参数
    if execute(path,par) is True:
        print("ok")
