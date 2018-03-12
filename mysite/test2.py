import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import sqlite3 as lite
import sys
# from django.shortcuts import get_object_or_404

df = pd.read_excel('File.xlsx', sheet_name='生产排程')

print("Column headings:")
print(df.columns)



# for i in df.index:
   
#     print(df['2018-02-24白班'][i])
    # print(df['品名'][i])
    # print(df['材质'][i])
    # print(df['周期'][i])
    # print(df['穴数'][i])
    # print(df['产能     /11H'][i])
    # print(df['天(D)'][i])
    # print(df['计划/ 产出'][i])
    # print(df['已产出'][i])
    # print(df['白班'][i])

    # print(df['2018/2/24'][i])
    # print(df['周期'][i])
    # print(df['周期'][i])
    # print(df['周期'][i])




# with con:
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
#     # cur = con.cursor()    
#     # cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
def main():   
    from polls.models import Yazhupc 
#     # con = lite.connect('db.sqlite3')
#     # blogList=get_object_or_404(Blogs)
    x=1
    for i in df.index:
        Yazhupc.objects.get_or_create(machine=df['机台 '][i],prod=df['品名'][i],material=df['材质'][i],cycle=df['周期'][i]
                ,xueshu=df['穴数'][i],chann=df['产能     /11H'][i],renshu=df['人数'][i],ddanliang=df['订单量'][i]
                ,day=df['天(D)'][i],jh_or_cchu=df['计划/ 产出'][i],baiban1=df['2018-02-23 白班'][i],wanban1=df['2018-02-23 晚班'][i],baiban2=df['2018-02-24白班'][i],wanban2=df['2018-02-24 晚班'][i]
                ,baiban3=df['2018-02-25 白班'][i],wanban3=df['2018-02-25 晚班'][i],baiban4=df['2018-02-26 白班'][i],wanban4=df['2018-02-26 晚班'][i],baiban5=df['2018-02-27 白班'][i],wanban5=df['2018-02-27 晚班'][i]
                ,baiban6=df['2018-02-28 白班'][i],wanban6=df['2018-02-28 晚班'][i],baiban7=df['2018-03-01 白班'][i],wanban7=df['2018-03-01 晚班'][i],baiban8=df['2018-03-02 白班'][i],wanban8=df['2018-03-02 晚班'][i]
                ,zhoupai=df['周排程量      （8/4~8/10）'][i],shebeigongshi=df['设备工时'][i],rengongognshi=df['人工工时'][i],jadonglv=df['机台    稼动率'][i],beizhu=df['备注'][i],)
#         # if Blogs.objects.get(title__in=[df['模具维修工单'][i]]):
            
#         # Blogs.objects.get_or_create(title=df['模具维修工单'][i],content='').distinct()
        
#         # print(models.Student.objects.filter(name="Frank"))
#         # print(Blogs.objects.get('title'))
# #         # print( Blog.objects.get_value['title'])
        # print(df['机台 '][i])
if __name__ == "__main__":
	main()

	print("done")


