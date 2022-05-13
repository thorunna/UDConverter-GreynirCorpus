# Treebank format converter
Version 1.0

A Python module for converting the [GreynirCorpus](https://github.com/mideind/GreynirCorpus) treebank to the [Universal Dependencies](https://universaldependencies.org/) framework. The module has been adapted from [UDConverter](https://github.com/thorunna/UDConverter).

The resulting UD treebank will be included in UD version 2.11.

## Setup

Install all requirements by running: 

`pip install -r requirements.txt`

## Usage

Scripts to run are in the `scripts` folder.

_In all examples below, the_ `--output` _flag is used to write to files in the_ `/CoNLLU/` _output folder. Otherwise prints to standard output._

*Convert single file or directory of files:*

> `convert.py -N -i path/to/corpus/file.psd --output --post_process`

> `convert.py -N -i path/to/corpus/* --output --post_process`

_For further usage, input files must be placed in a folder within the_ `corpora` _folde:r_

*Convert single tree in treebank using sentence ID (only prints to standard output):*

> `convert.py -C FOLDER_NAME -id SENTENCE_ID`

*Convert single file in treebank*

> `convert.py -C FOLDER_NAME -f FILE_NAME --output --post_process`


## Acknowledgements

This converter was adapted as part of the Language Technology Programme for Icelandic 2019-2023. The programme, which is managed and coordinated by Almannarómur (https://almannaromur.is/), is funded by the Icelandic Ministry of Education, Science and Culture.
