"""Build example notebooks from JSON specs in altair.examples"""

import base64
import os
import sys
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))

import nbformat
from nbformat.v4.nbbase import new_markdown_cell, new_code_cell, new_notebook
from jupyter_client.kernelspec import KernelSpecManager


def export_png(notebook_path, png_path):
    """Find the first png in a notebook, and export to a file.
    
    Parameters
    ==========
    notebook_path: str
        Full path to the input notebook file.
    png_path: str
        Full path to the output png file.
    """
    with open(notebook_path, 'r') as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)
    for cell in nb.cells:
        if hasattr(cell, 'outputs'):
            for output in cell.outputs:
                if hasattr(output, 'output_type') and output.output_type == 'display_data':
                    if hasattr(output, 'data') and 'image/png' in output.data:
                        image_data = base64.b64decode(output.data['image/png'])
                        print('Exporting png data for {}'.format(notebook_path))
                        with open(png_path, 'wb') as f_png:
                            f_png.write(image_data)


def export_all_example_pngs():
    """Export the pngs from all the example notebooks."""
    example_directory = os.path.join(os.path.dirname(__file__),
                                      '..', 'notebooks',
                                      'examples')

    png_directory = os.path.join(os.path.dirname(__file__),
                                      '.', 'example_images')

    # Remove old pngs before starting again
    if not os.path.exists(png_directory):
        os.makedirs(png_directory)
    for png in os.listdir(png_directory):
        if os.path.splitext(png)[1] == '.png':
            os.remove(os.path.join(png_directory, png))

    for example in os.listdir(example_directory):
        if example.endswith('.ipynb'):
            file_stem = os.path.splitext(example)[0]
            notebook_path = os.path.join(example_directory, file_stem + '.ipynb')
            png_path = os.path.join(png_directory, file_stem + '.png')
            export_png(notebook_path, png_path)


_description = """Export pngs saved in example notebooks.

This script assumes that the example notebooks in ``notebooks/examples`` have been run
interactively and have the png data embedded in the output of the cell with the
displayed chart.

Output png files will be put into the ``./example_images`` directory with the same file prefix.
"""

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Export pngs saved in example notebooks.')
    args = parser.parse_args()
    export_all_example_pngs()


if __name__ == '__main__':
    main()
