exe处理方法测试用例

说明：
path： exe所在路径，不包含exe子集
par： exe调用一系列参数，包含exe本身及其参数


1. SAGA数据处理程序
-test case saga exe
path='C:\\Users\\91308\\Desktop\\p\\SAGA\\saga_vc_x64\\'
par='saga_cmd.exe ta_lighting 0 -ELEVATION=D:\\Projects\\testData\\saga_data\\ASTGTM2_N27E086_dem.tif -SHADE=D:\\Projects\\testData\\saga_data\\out3.sgrd'

2. 气象数据预处理程序
-test case AERCOARE
path='C:\\Users\\91308\\Desktop\\p\\Model\\AERCOARE\\aercoare-dos-code\\dos-code\\'
par='aercoare.exe co-test3f.in'


3. 气象数据预处理程序
AERMAP处理高程数据，是AERMOD的地形预处理器
