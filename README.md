# Jupyter Notebooks for Altair

This repository contains tutorial and example Jupyter Notebooks for Altair.

[Examples Index](notebooks/Index.ipynb)

You can browse static version of these notebooks here on GitHub, or click one of
the badges below to run these notebooks on either [Binder](https://mybinder.org/) or [Colab](http://colab.research.google.com).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/altair-viz/altair_notebooks/master?urlpath=lab/tree/notebooks/Index.ipynb)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/altair-viz/altair_notebooks/blob/master/notebooks/Index.ipynb)
[![Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](http://deepnote.com/launch?url=https%3A%2F%2Fgithub.com%2Faltair-viz%2Faltair_notebooks%2Fblob%2Fmaster%2Fnotebooks%2FIndex.ipynb)

## Example

Here is an example using Altair to quickly visualize and display a dataset with the native Vega-Lite renderer in the JupyterLab:

```python
import altair as alt

# load a simple dataset as a pandas DataFrame
from vega_datasets import data
cars = data.cars()

alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)
```

![Altair Visualization](images/cars.png?raw=true)
