import types
import urllib.request
import json
import time
# def registerUrl():
url ="http://10.10.0.106/c001zt/jsongen/"
weatherHtml = urllib.request.urlopen(url)
weatherHtml1=weatherHtml.read()
# print(weatherHtml1)
weatherJSON=json.loads(weatherHtml1)
# print(weatherJSON['AMRT300'])
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
# def main():   
#     from polls.models import Mujuv2    
#     for i in weatherJSON:
#     	Mujuv2.objects.get_or_create(
#             muju_wo=i['AMRT300'],muju_date=str(i['AMRT300_DATE']),muju_empe=i['AMRT300_BY_NAME'],muju_source_code=i['资源编号']
#                 ,muju_source_code_name=i['资源名称'],muju_seq=i['SEQ'],muju_Reason=i['报修原因']
#                 )

# if __name__ == "__main__":
# 	main()

# 	print("done")
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,20);
while 1==1:
    time.sleep(second);
    def main(): 
    	from polls.models import Mujuv2
    	for i in weatherJSON:
    		Mujuv2.objects.get_or_create(
                muju_wo=i['AMRT300'],muju_date=str(i['AMRT300_DATE']),muju_empe=i['AMRT300_BY_NAME'],muju_source_code=i['资源编号']
                    ,muju_source_code_name=i['资源名称'],muju_seq=i['SEQ'],muju_Reason=i['报修原因']
                    )
    if __name__ == "__main__":
	    main()
	    print("done")

    print ("do action")


	# print(i['AMRT300'])


# jsonstr=json.dumps(weatherJSON)
# print(jsonstr)
# for i in weatherJSON
# print(weatherJSON['AMRT300'])
        # print(weatherJSON["data"]["list"][0])