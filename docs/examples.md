# Examples

This page provides more complex examples of using Polidoro Pipeline for various use cases.

## Example 1: Text Processing Pipeline

This example demonstrates a pipeline for processing text data:

```python
from ppipeline import Pipeline

# Define processing steps
def tokenize(text):
    """Split text into words"""
    return text.lower().split()

def remove_stopwords(words):
    """Remove common stopwords"""
    stopwords = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', 'by'}
    return [word for word in words if word not in stopwords]

def stem_words(words):
    """Simple stemming (in practice, you'd use a proper stemmer)"""
    return [word[:-1] if word.endswith('s') else word for word in words]

# Create the pipeline
text_pipeline = Pipeline([tokenize, remove_stopwords, stem_words])

# Process a single text
result = list(text_pipeline.run("The quick brown foxes jump over the lazy dogs"))
print(result)  # ['quick', 'brown', 'fox', 'jump', 'over', 'lazy', 'dog']

# Process multiple texts in parallel
texts = [
    "The quick brown fox jumps over the lazy dog",
    "A team of researchers published their findings",
    "Machine learning models require large datasets"
]
results = list(text_pipeline.run(texts))
for text, processed in zip(texts, results):
    print(f"Original: {text}")
    print(f"Processed: {processed}\n")
```

## Example 2: Image Processing Pipeline

This example shows how to create a pipeline for image processing (using a hypothetical image library):

```python
from ppipeline import Pipeline
import numpy as np
from PIL import Image
import io

# Define processing steps
def load_image(image_path):
    """Load an image from a file path"""
    return Image.open(image_path)

def resize_image(image, size=(100, 100)):
    """Resize the image"""
    return image.resize(size)

def grayscale(image):
    """Convert image to grayscale"""
    return image.convert('L')

def normalize(image):
    """Normalize pixel values to range [0, 1]"""
    img_array = np.array(image).astype(float)
    return img_array / 255.0

# Create the pipeline
image_pipeline = Pipeline([load_image, resize_image, grayscale, normalize])

# Process a single image
result = next(image_pipeline.run("path/to/image.jpg"))
print(f"Processed image shape: {result.shape}")

# Process multiple images in parallel
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
results = list(image_pipeline.run(image_paths))
```

## Example 3: Data Transformation Pipeline

This example demonstrates a pipeline for transforming and filtering data:

```python
from ppipeline import Pipeline
import json

# Define processing steps
def load_json(file_path):
    """Load JSON data from a file"""
    with open(file_path, 'r') as f:
        return json.load(f)

def extract_records(data):
    """Extract records from the JSON data"""
    return data.get('records', [])

def filter_active(records):
    """Filter only active records"""
    return [record for record in records if record.get('status') == 'active']

def transform_format(records):
    """Transform records to a different format"""
    return [{
        'id': record.get('id'),
        'name': record.get('name'),
        'score': record.get('metrics', {}).get('score', 0)
    } for record in records]

# Create the pipeline
data_pipeline = Pipeline([load_json, extract_records, filter_active, transform_format])

# Process a single file
result = next(data_pipeline.run("data.json"))
print(f"Transformed {len(result)} active records")

# Process multiple files in parallel
file_paths = ["data1.json", "data2.json", "data3.json"]
all_results = list(data_pipeline.run(file_paths))
```

## Example 4: Branching Pipeline

This example shows how to create branching in a pipeline by returning multiple items:

```python
import itertools

from ppipeline import Pipeline

# Define processing steps
def generate_numbers(n):
    """Generate a range of numbers"""
    return list(range(n))

def classify_number(num):
    """Classify a number as even or odd"""
    if num % 2 == 0:
        return {'type': 'even', 'value': num}
    else:
        return {'type': 'odd', 'value': num}

def process_even(item):
    """Process even numbers"""
    if item['type'] != 'even':
        return None  # Skip non-even items
    return item['value'] ** 2

def process_odd(item):
    """Process odd numbers"""
    if item['type'] != 'odd':
        return None  # Skip non-odd items
    return item['value'] * 3

def combine_results(item):
    """Combine results, filtering out None values"""
    if item is None:
        return []  # Return empty list to filter out None values
    return [item]

# Create the pipeline
pipeline = Pipeline([
    generate_numbers,
    classify_number,
    lambda x: [process_even(x), process_odd(x)],  # Branch into two processes
    combine_results
])

# Run the pipeline
results = list(itertools.chain.from_iterable(pipeline.run(5)))
print(results)  # [0, 3, 4, 9, 16]
```

These examples demonstrate the flexibility and power of Polidoro Pipeline for various data processing tasks.
