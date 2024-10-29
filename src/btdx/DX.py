import requests
import json
from datetime import datetime, timedelta, timezone
import urllib.parse

class DX:
    def __init__(self, api_key:str, feed_id:str, version:float=1, delta:float=0):
        """
        Initializes the DX class.

        :param api_key: Required. API key for authentication.
        :param feed_id: Required. Feed ID for the data feed.
        :param version: Optional. Version of the API. Default is 1.
        :param delta: Optional. Time difference for event time. Default is 0 minutes.
        """
        self.api_key = api_key
        self.feed_id= feed_id
        self.version = version if version else 1
        self.url = "https://api.mkdx.btcsp.co.uk/data-service/sensors/feeds/"
        self.header = {
            "accept": "application/json",
            "x-api-key": f"{self.api_key}",
            "Content-Type": "application/json"
        }
        
        self.delta = timedelta(minutes=delta) if delta is not None else timedelta(minutes=0)
            
    def get_current_time(self):
        """Return the current time in the required format."""
        return (datetime.now(timezone.utc) + self.delta).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


    def post(self, stream_id:int, data:str):
        """
        Sends a POST request to the ingestion URL.

        :param stream_id: Required. Stream ID to send the data.
        :param data: Required. The data to be posted.
        """
        self.post_stream_id = stream_id
        self.data = data
        if not self.api_key:
            print("Please enter your API key.")
            return None
        
        self.ingest_url= f"https://ing.mkdx.btcsp.co.uk/datahub-adapter/sensors/feeds/{self.feed_id}/{self.version}"
        self.time_now = self.get_current_time()
        # Create the JSON payload
        self.json = {
            "data": [
                {
                    "streamId": self.post_stream_id,  # Use the streamId
                    "value": self.data,
                    "eventTime": self.time_now
                }
            ]
        }

        try:
            response = requests.post(self.ingest_url, headers=self.header, json=self.json)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
        
    def get(self, stream_id:str, start:str=None, end:str=None, agregate:bool=False, display:bool=False):
        """
        Sends a GET request to fetch the data stream.

        :param stream_id: Required. Stream ID to fetch the data.
        :param start: Optional. Start date for data range in YYYY-MM-DD format.
        :param end: Optional. End date for data range in YYYY-MM-DD format.
        :param aggregate: Optional. If True, aggregate the data. Default is False.
        :param display: Optional. If True, display the fetched data. Default is False.
        """
        self.get_stream_id = stream_id
        try:
            start_iso = urllib.parse.quote(datetime.strptime(start, "%Y-%m-%d").isoformat() + 'Z') if start else None
            end_iso = urllib.parse.quote(datetime.strptime(end, "%Y-%m-%d").isoformat() + 'Z') if end else None
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

        self.base_url = f"https://api.mkdx.btcsp.co.uk/data-service/sensors/feeds/{self.feed_id}/{self.version}/datastream/{self.get_stream_id}"
        
        if not self.api_key:
            print("Please enter your API key.")
            return None
        self.agregate = agregate if agregate is not None else False
        if self.agregate:
            if(start and end ):
                self.get_url = f"{self.base_url}/datapoints?start={start_iso}&end={end_iso}&limit=100"
            else:
                self.get_url = f"{self.base_url}/datapoints?limit=100"

        else:
            self.get_url = self.base_url

        try:
            response = requests.get(self.get_url, headers=self.header)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            if display:
                self.display_data(response.json())
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
    
    def display_data(self, data):
        """Prints the pollution data in a readable format."""
        if data:
            print(json.dumps(data, indent=4))  # Pretty print the JSON data
        else:
            print("No data to display.")
