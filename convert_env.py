import os, json

secrets = {
    "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID"),
    "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY"),
    # Add more secrets as needed
}

with open("config.json", "w") as f:
  json.dump(secrets, f , indent = 3)
