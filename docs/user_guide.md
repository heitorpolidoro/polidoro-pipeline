# User Guide

This guide provides detailed information on using Polidoro Pipeline for parallel data processing.

## Pipeline Concept

A pipeline is a sequence of processing steps where the output of one step becomes the input to the next. Polidoro Pipeline implements this concept with automatic parallelization, making it easy to process data efficiently.

## Creating a Pipeline

There are two ways to create a pipeline:

### Method 1: Provide Steps at Initialization

```python
from ppipeline import Pipeline

def step1(data):
    return data + 1

def step2(data):
    return data * 2

# Create pipeline with steps
pipeline = Pipeline([step1, step2])
```

### Method 2: Add Steps Incrementally

```python
from ppipeline import Pipeline

# Create empty pipeline
pipeline = Pipeline()

# Add steps one by one
pipeline.add_step(step1)
pipeline.add_step(step2)
```

## Running the Pipeline

The `run` method executes the pipeline on the provided data:

```python
# Process a single value
result = list(pipeline.run(5))

# Process multiple values
results = list(pipeline.run([1, 2, 3, 4, 5]))
```

### Important Notes:

1. The `run` method returns an iterator, so you need to convert it to a list to get all results at once.
2. When processing a list of values, each value is processed independently and in parallel.

## Controlling Parallelization

You can control the number of worker threads used for parallel processing:

### Fixed Thread Count

```python
# Limit to 4 worker threads
pipeline = Pipeline([step1, step2], thread_count=4)
```

### Dynamic Thread Count Based on CPU Cores

```python
# Use 2x the number of CPU cores
pipeline = Pipeline([step1, step2], thread_count="x2")
```

## How Data Flows Through the Pipeline

1. Each item in the input data is processed through all steps in sequence.
2. If a step returns a list, each item in that list is processed independently in subsequent steps.
3. The final results are collected and returned as an iterator.

### Example:

```python
def step1(x):
    return [x, x+10]  # Returns two values for each input

def step2(x):
    return x * 2

pipeline = Pipeline([step1, step2])
results = list(pipeline.run(5))
# Results: [10, 30]
# Explanation:
# 5 -> step1 -> [5, 15] -> step2 -> [10, 30]
```

## Error Handling

If an error occurs during processing, it will be raised when you try to access the results:

```python
def failing_step(x):
    if x == 3:
        raise ValueError("Error processing value 3")
    return x

pipeline = Pipeline([failing_step])

# This will raise ValueError when processing the value 3
try:
    results = list(pipeline.run([1, 2, 3, 4]))
except ValueError as e:
    print(f"Error: {e}")
```

## Best Practices

1. **Function Design**: Design your step functions to be pure and independent, avoiding side effects.
2. **Thread Safety**: Ensure any shared resources accessed by your step functions are thread-safe.
3. **Error Handling**: Implement proper error handling in your step functions or when consuming pipeline results.
4. **Memory Management**: For large datasets, consider processing results as they become available instead of collecting all results at once.

## Performance Considerations

1. **CPU-bound vs IO-bound**: ThreadPoolExecutor works best for IO-bound tasks. For CPU-bound tasks, consider using ProcessPoolExecutor instead.
2. **Thread Count**: Setting the optimal thread count depends on your specific workload. For IO-bound tasks, you might benefit from more threads than CPU cores.
3. **Step Complexity**: If some steps are much more complex than others, consider splitting your pipeline to balance the workload.
