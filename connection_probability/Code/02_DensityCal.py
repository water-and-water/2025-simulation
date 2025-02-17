## 用于计算文件中每个节点的长度和所在区域
import os,math,shutil
import time
from multiprocessing import Pool


def FileInfoGet(par):
    path,file,write_path=par[0],par[1],par[2]
    new_contents=[]
    with open(os.path.join(path,file)) as file_object:
        contents = file_object.readlines()
        print(len(contents))
        file_object.close()
    while contents[0][0]=='#':# 删除注释
        del contents[0]
    for lineid in range(0,len(contents)):
        x=contents[lineid]
        x=x.strip("\n")
        t1=x.split( )
        t1=list(map(float,t1))
        if t1[1]!=0 and t1[1]!=-1: #不统计空白点和soma的位置
            # 计算到上一节点的长度
            t2=contents[int(t1[9])-1].split( )
            t2=list(map(float,t2))
            linelen=math.sqrt((t1[2]-t2[2])*(t1[2]-t2[2])+(t1[3]-t2[3])*(t1[3]-t2[3])+(t1[4]-t2[4])*(t1[4]-t2[4]))
            ## 给定坐标返回值
            temp=str(int(t1[1]))+' '+str(int(t1[10]))+' '+str(linelen)+'\n'
            new_contents.append(temp)
    new_file=file.split('.')[0]+'.swc'
    f=open(os.path.join(write_path, new_file),'w+')
    f.writelines(new_contents)
    f.close()
            
def run__pool():  # main process
    cpu_worker_num = 2
    time_start = time.time()  # 记录开始时间

    path='./File_Temp'
    write_path='./File_Info'

    # 清空文件夹
    if not os.path.exists(write_path):
        os.mkdir(write_path)
    else:
        shutil.rmtree(write_path)  
        os.mkdir(write_path)
    par_list=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            par_list.append([path,file,write_path])
    with Pool(cpu_worker_num) as p:
        p.map(FileInfoGet, par_list)
       
    time_end = time.time()  # 记录结束时间
    time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
    print('File Info Get time: '+str(time_sum))  

if __name__ =='__main__':
    run__pool()