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
    ingredient_pattern = r'chil[ie]+s?'

    filtered_recipes = data[data['ingredients'].str.contains(ingredient_pattern, case=False, regex=True)]
    
    return filtered_recipes


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
