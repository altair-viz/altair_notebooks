"""Build example notebooks from JSON specs in altair.examples"""

import os
import sys
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))

import nbformat
from nbformat.v4.nbbase import new_markdown_cell, new_code_cell, new_notebook
from nbconvert.preprocessors import ExecutePreprocessor
from jupyter_client.kernelspec import KernelSpecManager

from altair import *
from altair.vegalite.v2.examples import iter_examples

INDEX_TEXT = """# Auto-Generated Altair Examples

All the following notebooks are auto-generated from the example specifications
in the [Vega-Lite](http://vega.github.io/vega-lite/) project.
"""


def get_kernelspec(name):
    ksm = KernelSpecManager()
    kernelspec = ksm.get_kernel_spec(name).to_dict()
    kernelspec['name'] = name
    kernelspec.pop('argv')
    return kernelspec


def write_notebook(cells, outputfile, execute=True, kernel='python3'):
    kernelspec = get_kernelspec(kernel)
    notebook = new_notebook(cells=cells,
                            metadata={'language': 'python',
                                      'kernelspec': kernelspec})

    if execute:
        ep = ExecutePreprocessor(timeout=600, kernelname='python3')
        ep.preprocess(notebook,
                      {'metadata': {'path': os.path.dirname(outputfile)}})

    nbformat.write(notebook, outputfile)


def create_example_notebook(example, notebook_directory,
                            execute=True, kernel='python3', verbose=True,
                            index_dict=None):
    filename = example['filename']
    name = example['name']
    outputfile = os.path.join('..','..', name + '.ipynb')
    outputfile_full = os.path.join(notebook_directory, outputfile)

    if verbose:
        print(filename)
        print(" -> {0}".format(outputfile_full))

    title = name.replace('_', ' ').title()

    # index_entry = "[{0}]({1}): *{2}*".format(title, outputfile, description)
    # if index_dict is not None:
    #     index_dict[filename] = index_entry

    with open(filename) as f:
        source_code = f.readlines()

    def cells():
        yield new_code_cell(source_code)

    write_notebook(list(cells()), outputfile_full,
                   execute=execute, kernel=kernel)


def write_index(notebook_directory, index_dict, kernel='python3'):
    index_listing = '\n'.join('- ' + entry
                              for key, entry in sorted(index_dict.items()))

    cells = [new_markdown_cell(INDEX_TEXT),
             new_markdown_cell(index_listing)]

    write_notebook(cells, os.path.join(notebook_directory, 'Index.ipynb'),
                   execute=False, kernel=kernel)


def write_all_examples(execute=True):
    notebook_directory = os.path.join(os.path.dirname(__file__),
                                      '..', 'notebooks',
                                      'examples')
    
    # Remove old examples before starting again
    if not os.path.exists(notebook_directory):
        os.makedirs(notebook_directory)

    for example in os.listdir(notebook_directory):
        if os.path.splitext(example)[1] == '.ipynb':
            os.remove(os.path.join(notebook_directory, example))

    index_dict = {}
    for example in iter_examples():
        create_example_notebook(example, notebook_directory,
                                execute=execute, index_dict=index_dict)

    print("writing Index.ipynb")
    write_index(notebook_directory, index_dict)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate Altair example notebooks.')
    parser.add_argument('-e', '--execute', action='store_true',
                        help='Automatically execute all notebooks')

    args = parser.parse_args()
    write_all_examples(execute=args.execute)


if __name__ == '__main__':
    main()
