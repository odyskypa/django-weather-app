from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import boto3
import os



def get_url_quicksight():
    # Replace these values with your own
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_SESSION_TOKEN = os.environ.get('AWS_SESSION_TOKEN')
    AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME')


    # Connect to QuickSight
    # quicksight = boto3.client('quicksight',
    #                           aws_access_key_id=AWS_ACCESS_KEY_ID,
    #                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    #                           aws_session_token=AWS_SESSION_TOKEN,
    #                           region_name=AWS_REGION_NAME
    #                           )

    # Get the AWS account ID
    aws_account_id = boto3.client('sts',
                                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                  aws_session_token=AWS_SESSION_TOKEN,
                                  region_name=AWS_REGION_NAME
                                  ).get_caller_identity().get('Account')

    # Get list of dashboards
    # response = quicksight.list_dashboards(AwsAccountId=aws_account_id)

    # Generate URL for the first dashboard
    # dashboard = response['DashboardSummaryList']
    # if dashboard:
    #     dashboard_id = dashboard[0]['DashboardId']
    #     url = quicksight.get_dashboard_embed_url(
    #         AwsAccountId=aws_account_id,
    #         DashboardId=dashboard_id,
    #         IdentityType='IAM',
    #         SessionLifetimeInMinutes=60,
    #         UndoRedoDisabled=True
    #     )['EmbedUrl']
    #     return url

    # return None
    return "https://publuu.com/"


def index(request):
    dashboard_url= get_url_quicksight()
    
    if dashboard_url:
        return render(request, 'weatherapp/index.html', {'dashboard_url': dashboard_url})
    return None