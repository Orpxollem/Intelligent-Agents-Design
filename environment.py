import random

def get_disaster_status():
    """
    Simulates environmental data.
    Returns a severity level: Low, Medium, or High.
    """
    # To Simulate a metric, example: the flood water level in cm
    metric = random.randint(0, 100)
    
    if metric < 30:
        return "Low", metric
    elif metric < 70:
        return "Medium", metric
    else:
        return "High", metric