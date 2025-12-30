def normalize_salaries(salaries):
    if not salaries:
        return []
    min_sal = min(salaries)
    max_sal = max(salaries)

    if min_sal == max_sal:
        # return a list of zeroes using 'for _ in' which iterates over salaries
        return [0 for _ in salaries]
    
    normalized_Salaries = []
    for sal in salaries:
        normalized_value = (sal - min_sal) / (max_sal - min_sal)
        normalized_Salaries.append(normalized_value)
    return normalized_Salaries
    
def filter_above_threshold(data, threshold):
    filtered_data = []
    for value in data:
        if value > threshold:
            filtered_data.append(value)
    # return [value for value in data if value > threshold]
    return filtered_data

def calculate_statistics(data):
    if not data:
        return {
            "mean": None,
            "median": None,
            "variance": None
        }
    n = len(data)
    mean = sum(data) / n

    sorted_data = sorted(data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    variance = sum((x - mean) ** 2 for x in data) / n

    return {
        "mean": mean,
        "median": median,
        "variance": variance
    }

