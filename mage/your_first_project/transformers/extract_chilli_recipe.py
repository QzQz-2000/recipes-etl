if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Transformer function to filter recipes containing specified ingredient ("Chilies" or variants).

    Args:
        data (pd.DataFrame): Input DataFrame containing recipes.

    Returns:
        pd.DataFrame: Filtered DataFrame containing recipes with the specified ingredient.
    """
    # 定义要匹配的食材关键词和其变体
    ingredient_pattern = r'chil[ie]+s?'  # 匹配 "Chilies", "Chiles", "Chile" 等
    
    # 使用正则表达式进行模糊匹配，并忽略大小写
    filtered_recipes = data[data['ingredients'].str.contains(ingredient_pattern, case=False, regex=True)]
    
    return filtered_recipes


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
