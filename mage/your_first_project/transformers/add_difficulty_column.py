if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import re


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    print(data['prepTime'].unique())
    print(data['cookTime'].unique())

    def parse_iso_duration(duration):
        """
        Parse an ISO 8601 duration string into hours and minutes.
        """
        # where duration is only 'PT'
        if duration == "PT":
            return 0, 0

        # use regex to match the hours and mins
        hour_min = re.match(r'^PT(?:(\d+)H)?(?:(\d+)M)?$', duration)
        if hour_min is False:
            return 0, 0

        # extract hours and minutes
        hours = int(hour_min.group(1)) if hour_min.group(1) else 0
        minutes = int(hour_min.group(2)) if hour_min.group(2) else 0
        return hours, minutes

    def calculate_difficulty(row):
        """
        Calculate the difficulty of a recipe based on prepTime and cookTime
        """
        try:
            prep_time = row.get("prepTime", "PT0M")
            cook_time = row.get("cookTime", "PT0M")

            # parse the prepTime and cookTime into hours and mins
            prep_hours, prep_minutes = parse_iso_duration(prep_time)
            cook_hours, cook_minutes = parse_iso_duration(cook_time)
            total_mins = (prep_hours * 60 + prep_minutes) + (cook_hours * 60 + cook_minutes)

            # determine the difficulty level based on total minutes
            if total_mins > 60:
                return "Hard"
            elif 30 <= total_mins <= 60:
                return "Medium"
            elif total_mins < 30:
                return "Easy"
            else:
                return "Unknown"
        except Exception:
            return "Unknown"

    data['difficulty'] = data.apply(calculate_difficulty, axis=1)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'