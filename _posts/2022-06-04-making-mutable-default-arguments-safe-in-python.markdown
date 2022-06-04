---
layout: post
title:  "Making mutable default arguments safe in Python"
date:   2022-06-04 13:38:00 -0400
categories: technical
---

_Note: this is just a silly hack. Do not take this seriously._

Recently, my colleague remarked that handling nulls (or `None`) in Python is awkward, yet frequently unavoidable.
For instance, when setting default arguments in functions, it is unsafe to set the defaults to mutable types such as lists or dictionaries.
This is because the defaults are initialized _once_ and baked in at the time the function is defined; if the argument is modified inside the function, then those modifications will stick around in future function calls.

```python
def unsafe(a=[]):
    a.append("default")
    print(a)

unsafe()
# ['default']

unsafe()
# ['default', 'default']

unsafe()
# ['default', 'default', 'default']
```

The accepted workaround is to set the default to `None` and then initialize accordingly inside the function.

```python
def safe_but_awkward(a=None):
    if a is None:
        a = []

    a.append("default")
    print(a)

safe_but_awkward()
# ['default']

safe_but_awkward()
# ['default']
```

If you're used to Python then maybe it doesn't seem so bad, but it is certainly inelegant and makes the function signature a bit less self-documenting.

Unfortunately, I can't create any syntactic sugar for nulls that's any more pleasant than a SQL `coalesce()`, and perhaps at this point nobody can change the way function definition works.

But Python has powerful reflection/introspection capabilities, so maybe we can "fix" this oversight post-hoc. We can write a function decorator to detect the case where unsafe default arguments are used, and then ensure that a fresh copy is passed in every time the function is called.

I did exactly that, and this is what it looks like:

```python
@safe_defaults
def unsafe(a=[]):
    a.append("default")
    print(a)

unsafe()
# ['default']

unsafe()
# ['default']

unsafe()
# ['default']
```

How does it work?
By using the `inspect` module, we can figure out which parameters have default values.

```python
import inspect

sig = inspect.signature(unsafe)

sig.parameters["a"].default
# []
```

For parameters with no defaults, there is a special indicator value, `inspect._empty`.

The next step is to cache a copy of the default for any mutable parameters.
I've used `deepcopy` out of an abundance of caution.

```python
from copy import deepcopy

default_values = {}

for param_name, param in sig.parameters.items():
    if type(param.default) in (list, set, dict):
        default_values[param_name] = deepcopy(param.default)
```

Now we can define our wrapped version of `unsafe`.
One very neat piece of functionality here is [sig.bind](https://docs.python.org/3/library/inspect.html#inspect.Signature.bind), which fully maps all of the supplied `*args` and `**kwds` to the function signature.
It makes it easy to check if the defaults are going to get invoked (at which point we leap in and inject our cached copy into `**kwds`).

[bound.apply_defaults](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.apply_defaults) fills in the remaining gaps (e.g., if there were normal `int` defaults that we didn't need to wrap).

```python
def wrapped_unsafe(*args, **kwds):
    bound = sig.bind(*args, **kwds)
    
    for param_name, param_value in default_values.items():
        if param_name not in bound.arguments:
            kwds[param_name] = deepcopy(param_value)
    
    bound.apply_defaults()
    
    return unsafe(*args, **kwds)

wrapped_unsafe()
# ['default']

wrapped_unsafe()
# ['default']

wrapped_unsafe()
# ['default']
```

For better ergonomics, we can package the whole thing up as a decorator so it's easy to use.
You can find the full source [on Github](https://gist.github.com/metavee/42b394601dc0014da53d195b7e06cd1b) or at the bottom of this page.

Overall, this was a fun exercise.
I can't say I will be using it seriously, but knowing more about `inspect` will certainly come in handy for future hacks.
Maybe it's enough to win over my colleague.

Thanks to [Stack Overflow user Lucas Wiman](https://stackoverflow.com/users/303931/lucas-wiman) for showing me [how to properly inspect default arguments](https://stackoverflow.com/a/69170441) and providing the starting point for the code.

---

```python
from copy import deepcopy
from functools import wraps
import inspect
from typing import Callable


def safe_defaults(f: Callable) -> Callable:
    """
    Decorate a function to allow safe usage of mutable default parameters.
    
    Each time the function is invoked with defaults, a fresh copy of the mutable arguments will be passed.
    
    Lists, dicts and sets are supported.
    
    E.g., instead of this:
    
    >>> def my_function(arg: Optional[List] = None):
    ...     if arg is None:
    ...         arg = []
    ...     
    ...     pass
        
    You can write:
    
    >>> @safe_defaults
    ... def my_function(arg: List = []):
    ...    pass
    
    Adapted from this Stack Overflow answer by @303931/lucas-wiman
    https://stackoverflow.com/a/69170441
    
    Parameters
    ----------
    f: Callable
        Function to decorate.
        
    Returns
    -------
    Callable
        Wrapped function.
    """
    
    sig = inspect.signature(f)
    default_values = {}
    
    # inspect defaults in type signature
    for param_name, param in sig.parameters.items():
        if type(param.default) in (list, set, dict):
            # save a copy that will never be modified
            default_values[param_name] = deepcopy(param.default)
    
    @wraps(f)
    def wrapper(*args, **kwds):
        bound = sig.bind(*args, **kwds)
        
        for param_name, param_value in default_values.items():
            # copy over our default value if not specified by caller
            if param_name not in bound.arguments:
                kwds[param_name] = deepcopy(param_value)
        
        bound.apply_defaults()
        
        return f(*args, **kwds)

    return wrapper
```
