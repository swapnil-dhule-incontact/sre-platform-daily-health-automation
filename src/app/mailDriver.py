import boto3
import sys
from datetime import datetime, timedelta,date
import json
import os

now = datetime.now()         
startTime=now -timedelta(days=1)


def buildTable(result):
    
    flag=0
    
    outHTML="<table id='customers'> <tr> <th> Metric <th>Value<th>Unit<th>Range<th>Status</tr>"
    
    for k,v in result.items():
        
        if v['output']['status'] == "PASS":
            statusColor="a9fc03"
        else:
            statusColor="f44336"
        
        outHTML+="\n<tr><td><a style=font-weight:bold href={}>{}</a><td>{}<td>{}<td>{} - {}<td style=font-weight:bold;color:#{}>{}</tr>".format(v['output']['link'],k,v['output']['value'],v['output']['unit'],v['output']['minval'],v['output']['maxval'],statusColor,v['output']['status'])

    else:
        outHTML+="</table>"
    
    return outHTML


def sendMail(rawData):
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "SRE-Platform@niceincontact.com"

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    RECIPIENT = ["swapnil.dhule@nice.com"]

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the 
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    #CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-west-2"

    # The subject line for the email.
    SUBJECT = "Automated Health Check Report| ICPune - Pre-Release"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("This is health check report for icpune account "
                )
                
    # The HTML body of the email.
    cssTxt=r''' <style>
    
    #customers {
      font-family: Courier New;
      border-collapse: collapse;
      text-align: left;
      border-style: dashed;
      border-color: white;
      border-width: thin;
    }
    
    th, td {
      padding: 10px;
      border: 1px dashed white;
    }
    
    body {
        font-family: Courier New;
        font-size: 14px;
        background-color: black;
        color: white;
    }
    
    hr {
        border-top: 1px dashed white;
    }
    
   a:link {
  color: white;
  
}

a:visited {
 color: white;
}

a:hover {
   color: white;
}

a:active {
  color: white;
}
    </style>'''
    
    BODY_HTML = """<html>
    <head>
   {}
    </head>
    <body>
        <p>
        Greetings from NiC Site Reliability Engineering Team!<br>
        <br>
        <b>Region:</b> ICPune (Oregon)<br>
        <b>Report Generation Date:</b> {}<br>
        <b>Report Observation Period:</b> {} to {}
        <br><br>
        
        </p>
         {}<br><br>
         <hr style='border: 1px dashed white;'>
         <small>This automated report is brought to you by Platform SRE Team.</small>
    </body>
    
    </html>
                """.format(cssTxt,date.today().strftime("%B %d, %Y"),startTime,now,buildTable(rawData))            

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses':RECIPIENT,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )


    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])