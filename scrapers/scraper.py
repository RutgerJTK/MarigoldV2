def handler(event, context):  # ✅ This matches your serverless.yml
    print("Handler started - this will appear in CloudWatch logs!")
    return {"statusCode": 200, "body": "Test Function executed successfully"}