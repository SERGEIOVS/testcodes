"""import os
for i in range(4):
    i+=1
    os.system('echo 123 >>  My1/test_.txt')"""
    
import os
for i in range(4):
    i+=1
    os.system('echo 123 >>  My1/test_'+str(i)+'."txt')