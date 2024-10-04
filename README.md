# BTDX Library

[![PyPI Latest Release](https://img.shields.io/pypi/v/btdx.svg)](https://pypi.org/project/btdx/)

The **btdx** library is designed to interact with the **Milton Keynes' BT Data Exchange Platform**. This README provides a guide on how to install, set up, and effectively use the `DX`.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [1. Initialization](#1-initialization)
  - [2. Posting Data](#2-posting-data)
  - [3. Getting Data](#3-getting-data)
- [Contributing](#contributing)
- [License](#license)



## Installation

- From PyPI (Python Package Index) 

    You can install the `btdx` library using pip. Make sure you have `python >= 3.8` and pip installed on your machine, then,:

    ```bash
    pip install btdx
    ```
- From source

    To install btdx from source, clone the repository from [here](https://github.com/ShobhitManiar/data-exchange). You will also need [requests](https://pypi.org/project/requests/) to install `btdx`. In your terminal type:

    ```sh 
    pip install requests
    ```
    , and then, 
    ```sh
    pip install .
    ```

    or in editable mode
    ```sh 
    pip install -e .
    ```

## Usage 

To use the `btdx`, you need to create an instance of `DX` first. Then use either `post` method to ingest data or `get` method to retrieve data

1. **Initialization** To create an instance of DX, provide your API key, feed ID, and optionally a version number..
   
   ```python
   from btdx import DX  # Make sure to import the DX class from the module
   api_key = "your_api_key"     # Your API key
   feed_id = "your_feed_id"     # The feed ID you want to interact with
   version = 1                  # Optional: Version number (default is 1)
   DX = DX(api_key, feed_id, version)
   ```

2. **Posting Data** You can post data to a specific stream by calling the post method. You need to provide the stream ID and the data you want to post.

    ```python
    stream_id = "100"           # The ID of the stream you want to post data to
    data =  "AQI: 2"         # The value you want to post
    DX.post(stream_id=stream_id, data=data)
    ```

3. **Getting Data** To retrieve data from a specific stream, use the get method. You can specify the stream ID and whether you want to display the data. You can also pass optional parameters such as agregate.

    ```python
    stream_id = "100"           # The ID of the stream you want to get data from
    # Retrieve and display data
    DX.get(stream_id=stream_id, display=True)
    # Retrieve last 100 values and display data
    DX.get(stream_id=stream_id, display=True, agregate=True)
    ``` 
## Contributing

 Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.

## License
 This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

[Go to Top](#table-of-contents)