def give_bmi(height: list[int | float], weight: list[int | float])\
      -> list[int | float]:
    """Calculates the BMI of a list of people given their height and weight.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same size")

    bmi_values = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError("Height and weight must be integers or floats")
        if h <= 0 or w <= 0:
            raise ValueError("Height and weight must be positive values")

        # Calculate BMI using the formula: BMI = weight (kg) / height (m)^2
        bmi = w / (h ** 2)
        bmi_values.append(bmi)

    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(limit, int):
        raise ValueError("Limit must be an integer")

    return [b > limit for b in bmi]
