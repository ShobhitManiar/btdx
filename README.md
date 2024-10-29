# BTDX Library

[![PyPI Latest Release](https://img.shields.io/pypi/v/btdx.svg)](https://pypi.org/project/btdx/)

The **btdx** library is designed to interact with the **Milton Keynes' BT Data Exchange Platform**. This README provides a guide on how to install, set up, and effectively use the `DX` class.

<div align="center" >🤝 Show your support - give a ⭐️ if you find this library useful</div>

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [1. Initialization](#initialization)
  - [2. Posting Data](#posting-data)
  - [3. Getting Data](#getting-data)
- [Contributing](#contributing)
- [License](#license)



## Installation

- From PyPI (Python Package Index) 

    You can install the `btdx` library using pip. Make sure you have `python >= 3.8` and pip installed on your machine, then,

    ```bash
    pip install btdx
    ```
- From source

    To install btdx from source, clone the repository from [here](https://github.com/ShobhitManiar/data-exchange). In your terminal type:

    ```sh
    pip install .
    ```
    or in editable mode
    ```sh 
    pip install -e .
    ```
    You will also need [requests](https://pypi.org/project/requests/) to use `btdx`
    ```sh 
    pip install requests
    ``` 

## Usage 

To use the `btdx`, you need to create an instance of `DX` first. Then use either `post` method to ingest data or `get` method to retrieve data

1. #### Initialization
      To create an instance of DX, provide your API key, feed ID, and optionally a version number.
   
     ``` python
     from btdx import DX  # Make sure to import the DX class from the module
     api_key = "your_api_key"     # Your API key
     feed_id = "your_feed_id"     # The feed ID you want to interact with
     version = 1                  # Optional: Version number (default is 1)
     response = DX(api_key, feed_id, version)
     ```

2. #### Posting Data
    You can post data to a specific stream by calling the post method. You need to provide the stream ID and the data you want to post.
   
    ```python
    stream_id = "100"           # The ID of the stream you want to post data to
    data =  "AQI: 2"         # The value you want to post
    response.post(stream_id=stream_id, data=data)
    ```

5. #### Getting Data
     To retrieve data from a specific stream, use the get method. You can specify the stream ID and whether you want to display the data. 

    ```python
    stream_id = "100"           # The ID of the stream you want to get data from
    # Retrieve and display data
    response.get(stream_id=stream_id, display=True)
    ```
   You can also pass optional parameters such as agregate.
   ```python
    # Retrieve last 100 values between a date range and display data, if no range is provided last 100 values from current time will be obtained.

    start="YYYY-MM-DD"
    end="YYYY-MM-DD"
    response.get(stream_id=stream_id, start=start, end=end, display=True, agregate=True)
    ``` 
## Contributing

 Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.

## License
 This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

[Go to Top](#table-of-contents)
