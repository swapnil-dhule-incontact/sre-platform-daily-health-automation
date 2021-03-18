import boto3
import sys
from datetime import datetime, timedelta
import json

def get_custom_metrics(JSONParam,aggregateFunc,minval,maxval,unit,link):
        metric=JSONParam['Statistics'][0]
    
        client = boto3.client('cloudwatch')
        response = client.get_metric_statistics(**JSONParam)
         
        print("checkpoint :",response)
        if aggregateFunc=="max":
            for k, v in response.items():
                if k == 'Datapoints':
                    max = 0
                    for y in v:
                        if y[metric]> max : max=y[metric]
                    out= "{0:.0f}".format(max)
        elif aggregateFunc=="avg":
            for k, v in response.items():
                if k == 'Datapoints':
                    sum = 0
                    count=0
                    for y in v:
                        sum+=y[metric]
                        count+=1
                    out= "{0:.2f}".format(sum/count)
        elif aggregateFunc=="sum":
            for k, v in response.items():
                if k == 'Datapoints':
                    sum = 0
                    for y in v:
                        sum+=y[metric]
                    out= "{0:.2f}".format(sum)
        elif aggregateFunc=="min":
            for k, v in response.items():
                if k == 'Datapoints':
                    min = 1000000000000
                    for y in v:
                        if y[metric]< min : min=y[metric]
                    out= "{0:.0f}".format(min)
                    
        if float(out)>maxval or float(out) < minval : 
            status="FAIL"
        else:
            status="PASS"
            
        return {'output':{'value':out, 'status':status, 'unit':unit,'minval':minval,'maxval':maxval,'link':link}, 'input': json.dumps(JSONParam,default=str), 'aggregateFunc':aggregateFunc}