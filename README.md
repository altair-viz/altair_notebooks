# Jupyter Notebooks for Altair

This repository contains tutorial and example Jupyter Notebooks for Altair.

You can browse static version of these notebooks here on GitHub, or click the `binder`
badge below to launch of live Jupyter Notebook server with the notebooks in this 
repo.

[![Binder](https://beta.mybinder.org/badge.svg)](https://beta.mybinder.org/v2/gh/altair-viz/altair_notebooks/master)

## Example

Here is an example of an Altair visualization:

```python
import altair as alt

# Uncomment/run this line to enable Altair in JupyterLab/nteract:
# alt.enable_mime_rendering()

# load data as a pandas DataFrame
cars = alt.load_dataset('cars')

alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)
```

![Altair Visualization](images/cars.png?raw=true)
