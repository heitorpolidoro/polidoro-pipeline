import os

import pytest
from ppipeline import Pipeline
from ppipeline.pipeline import EmptyPipelineError, InvalidThreadCountError


def add_1(x):
    print("add", x)
    return x + 1


def mul_2(x):
    print("mul", x)
    return x * 2


def test_simple_run():
    pipeline = Pipeline([add_1, mul_2])
    assert list(pipeline.run(1)) == [4]


def test_run_with_lists():
    pipeline = Pipeline([add_1, mul_2])
    assert set(pipeline.run([1, 2, 3])) == {4, 6, 8}

def test_add_step():
    pipeline = Pipeline()
    pipeline.add_step(add_1)
    pipeline.add_step(mul_2)
    assert list(pipeline.run(2)) == [6]

def test_without_steps():
    pipeline = Pipeline()
    with pytest.raises(EmptyPipelineError, match="Cannot run pipeline without steps"):
        list(pipeline.run(1))

def test_when_error():
    def failing_function(_x):
        raise ValueError("Test error")

    # Create a pipeline with just the failing function
    pipeline = Pipeline([failing_function])

    # Verify that the error is propagated
    with pytest.raises(ValueError, match="Test error"):
        next(pipeline.run(1))

def test_passing_thread_count_as_str():
    pipeline = Pipeline([add_1, mul_2], thread_count="x2")
    assert pipeline.thread_count == 2 * os.cpu_count()

def test_passing_invalid_thread_count_as_str():
    with pytest.raises(InvalidThreadCountError, match="Invalid thread count string"):
        Pipeline([add_1, mul_2], thread_count="10")
