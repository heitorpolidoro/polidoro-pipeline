# Quick Start

This guide will help you get started with Polidoro Pipeline quickly. We'll cover the basics of creating a pipeline and processing data through it.

## Basic Usage

### Creating a Simple Pipeline

```python
from ppipeline import Pipeline

# Define processing steps as functions
def add_1(x):
    return x + 1

def multiply_by_2(x):
    return x * 2

# Create a pipeline with steps
pipeline = Pipeline([add_1, multiply_by_2])
```

### Processing a Single Value

```python
# Process a single value
result = list(pipeline.run(1))
print(result)  # Output: [4]
```

The value `1` is processed through the pipeline:
1. `add_1` function: 1 + 1 = 2
2. `multiply_by_2` function: 2 * 2 = 4

### Processing Multiple Values

```python
# Process multiple values in parallel
results = list(pipeline.run([1, 2, 3]))
print(results)  # Output: [4, 6, 8]
```

Each value is processed independently and in parallel:
- 1 → add_1 → 2 → multiply_by_2 → 4
- 2 → add_1 → 3 → multiply_by_2 → 6
- 3 → add_1 → 4 → multiply_by_2 → 8

## Adding Steps Incrementally

You can also create an empty pipeline and add steps incrementally:

```python
pipeline = Pipeline()
pipeline.add_step(add_1)
pipeline.add_step(multiply_by_2)

result = list(pipeline.run(2))
print(result)  # Output: [6]
```

## Controlling Thread Count

You can control the number of worker threads used for parallel processing:

```python
# Limit to 4 worker threads
pipeline = Pipeline([add_1, multiply_by_2], thread_count=4)
results = list(pipeline.run([1, 2, 3, 4, 5]))

# Use a multiple of CPU count (e.g., 2x CPU cores)
pipeline = Pipeline([add_1, multiply_by_2], thread_count="x2")
results = list(pipeline.run([1, 2, 3, 4, 5]))
```

## Next Steps

For more detailed information on using Polidoro Pipeline, check out the [User Guide](user_guide.md) and [API Reference](api_reference.md).
