# API Reference

This page provides detailed documentation for the Polidoro Pipeline API.

## Pipeline Class

```{eval-rst}
.. autoclass:: ppipeline.Pipeline
   :members:
   :special-members: __init__
```

## Exceptions

```{eval-rst}
.. autoexception:: ppipeline.pipeline.EmptyPipelineError
   :members:

.. autoexception:: ppipeline.pipeline.InvalidThreadCountError
   :members:
```

## Helper Functions

```{eval-rst}
.. autofunction:: ppipeline.pipeline._to_list
```

## Type Variables

- `T = TypeVar("T")` - Type variable used for generic typing in the pipeline module.
