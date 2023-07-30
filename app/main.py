import os
import requests
import json
import time


while True:
    # Set IAM_TOKEN environment variable using yc CLI
    output = os.popen("/root/yandex-cloud/bin/yc iam create-token").read().strip()
    IAM_TOKEN = output.split()[-1]

    # Set IAM_TOKEN environment variable
    os.environ["IAM_TOKEN"] = IAM_TOKEN

    # Send GET request with Authorization header
    url = "https://billing.api.cloud.yandex.net/billing/v1/billingAccounts/"

    headers = {"Authorization": f"Bearer {IAM_TOKEN}"}
    response = requests.get(url, headers=headers)

    # Save response to file
    balance = response.json()['billingAccounts'][0]['balance']
    new_data_json = {'balance': balance}

    # Write the new JSON object to a new file
    with open('/yc_balance/new_response.json', 'w') as f:
        json.dump(new_data_json, f, indent=4)

    # Sleep for 11 hours
    time.sleep(11*60*60)
