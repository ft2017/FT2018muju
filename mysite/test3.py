import pandas as pd
import numpy as np
import math
from pandas import ExcelWriter
from pandas import ExcelFile
import sqlite3 as lite
import sys
# from django.shortcuts import get_object_or_404

df = pd.read_excel('File.xlsx', sheet_name='列表')
# math.isnan(df)
print("Column headings:")
print(df.columns)






# with con:
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
#     # cur = con.cursor()    
#     # cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
def main():   
    from polls.models import Mujuv2 
#     # con = lite.connect('db.sqlite3')
#     # blogList=get_object_or_404(Blogs)
    
    for i in df.index:
        # df.replace("","1")
        # print(df['项次'][i])
        # df['项次'].replace("nan","")
        Mujuv2.objects.get_or_create(
            muju_wo=df['模具维修工单'][i],muju_date=str(df['AMRT300日期'][i]),muju_empe=df['维修人员'][i],muju_source_code=df['资源编号'][i]
                ,muju_source_code_name=df['资源名称'][i],muju_seq=df['项次'][i],muju_Reason=df['报修原因'][i]
                )
        
if __name__ == "__main__":
	main()

	print("done")


