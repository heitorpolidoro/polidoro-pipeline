import itertools

from ppipeline import Pipeline


# Define processing steps
def generate_numbers(n):
    """Generate a range of numbers"""
    return list(range(n))


def classify_number(num):
    """Classify a number as even or odd"""
    if num % 2 == 0:
        return {"type": "even", "value": num}
    else:
        return {"type": "odd", "value": num}


def process_even(item):
    """Process even numbers"""
    if item["type"] != "even":
        return None  # Skip non-even items
    return item["value"] ** 2


def process_odd(item):
    """Process odd numbers"""
    if item["type"] != "odd":
        return None  # Skip non-odd items
    return item["value"] * 3


def combine_results(item):
    """Combine results, filtering out None values"""
    if item is None:
        return []  # Return empty list to filter out None values
    return [item]


# Create the pipeline
pipeline = Pipeline(
    [
        generate_numbers,
        classify_number,
        lambda x: [process_even(x), process_odd(x)],  # Branch into two processes
        combine_results,
    ]
)

# Run the pipeline
results = list(itertools.chain.from_iterable(pipeline.run(5)))
print(results)  # [0, 3, 4, 9, 16]
