import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Loads JSON data from a specified API endpoint and converts it to Pandas DataFrame.
    
    Returns:
    - pd.DataFrame: DataFrame containing data from the API.
    """
    url = 'https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json'
    try:
        # 发送 GET 请求获取 JSON 数据
        response = requests.get(url)
        
        # 确保响应成功
        if response.status_code == 200:
            # 将 JSON 数据转换为 DataFrame
            df = pd.read_json(response.text, lines=True)
            return pd.DataFrame(df)
        else:
            # 如果请求失败，打印错误信息并返回 None
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        # 处理异常情况
        print(f"Error loading data from {url}: {str(e)}")
        return None


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'Loading dataset failed'
