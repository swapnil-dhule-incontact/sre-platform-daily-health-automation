from datetime import datetime
from datetime import date, timedelta
from mailDriver import *
from statsDriver import *

def lambda_handler(event,context):
        now = datetime.now() 
        startTime=now -timedelta(days=1)
        print(startTime,now)
        
        #Max CPU
        
        RDSWriterCPUmaxParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'CPUUtilization',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'WRITER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Maximum',
            ],
            'Unit':'Percent'
        }
        RDSReaderCPUmaxParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'CPUUtilization',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'READER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Maximum',
            ],
            'Unit':'Percent'
        }
        
        #Max DB Connections
        
        RDSWriterDBConnmaxParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'DatabaseConnections',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'WRITER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Maximum',
            ],
        }
        RDSReaderDBConnmaxParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'DatabaseConnections',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'READER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Maximum',
            ],
        }
        
       #Max Freeable Memory
        
        RDSWriterMemorymaxParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'FreeableMemory',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'WRITER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Minimum',
            ],
            'Unit':'Bytes'
        }
        RDSReaderMemorymaxParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'FreeableMemory',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'READER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Minimum',
            ],
            'Unit':'Bytes'
        }
        
        #Avg Select Latency
        
        RDSWriterSelectLatencyAvgParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'SelectLatency',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'WRITER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Average',
            ],
            'Unit':'Milliseconds'
        }
        RDSReaderSelectLatencyAvgParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'SelectLatency',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'READER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Average',
            ],
            'Unit':'Milliseconds'        
        }
        
        #Total Queries
        
        RDSWriterQueriesParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'Queries',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'WRITER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Sum',
            ],
        }
        RDSReaderQueriesParam={
            'Namespace':'AWS/RDS',
            'MetricName' : 'Queries',
            'Dimensions' : [
                {
                'Name': 'DBClusterIdentifier',
                'Value': 'icpune-perf-shared-storage-auroraclusterrdsdb-c6o6w6b5kvv8'
                },
                                {
                'Name': 'Role',
                'Value': 'READER'
                },
            ],
             
            'StartTime':startTime,
            'EndTime':now,
            'Period':60,
            'Statistics':[
                'Sum',
            ],
        }
        
        import json
        out = {
        'RDS Max CPU Utilization - Writer' : get_custom_metrics(RDSWriterCPUmaxParam,'max',0,80,"Percent","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),
        'RDS Max CPU Utilization - Reader' : get_custom_metrics(RDSReaderCPUmaxParam,'max',0,80,"Percent","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),
        'RDS Max DB Connections - Writer' : get_custom_metrics(RDSWriterDBConnmaxParam,'max',0,400,"Count","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),
        'RDS Max DB Connections - Reader' : get_custom_metrics(RDSReaderDBConnmaxParam,'max',0,400,"Count","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),
        'RDS Min Freeable Memory - Writer' : get_custom_metrics(RDSWriterMemorymaxParam,'min',3000000000,10000000000,"Bytes","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),
        'RDS Min Freeable Memory - Reader' : get_custom_metrics(RDSReaderMemorymaxParam,'min',3000000000,10000000000,"Bytes","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),   
        'RDS Avg Select Latency - Writer' : get_custom_metrics(RDSWriterSelectLatencyAvgParam,'avg',0,2,"milisecond","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),
        'RDS Avg Select Latency - Reader' : get_custom_metrics(RDSReaderSelectLatencyAvgParam,'avg',0,2,"milisecond","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),      
        'RDS Max Queries - Writer' : get_custom_metrics(RDSWriterQueriesParam,'max',0,10000,"Count/Second","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),
        'RDS Max Queries - Reader' : get_custom_metrics(RDSReaderQueriesParam,'max',0,10000,"Count/Second","https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=RDS-Test"),     
        }
        
        print(out)
        
        sendMail(out)
        
        return out