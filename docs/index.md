# Welcome to st-undp

A utility package that helps build Streamlit apps in line with [UNDP Design System](https://design.undp.org). Bootstrap
your app development with `st-undp`!

## Installation

Currently, the package is distributed via GitHub only. You can install it with `pip`:

```bash
# latest version from the default branch (not recommended)
pip install git+https://github.com/undp-data/st-undp.git

# specific version from a tagged release (recommended) 
pip install git+https://github.com/undp-data/st-undp.git@v0.1.0
```

You can also add it to your `requirements.txt`:

```requirements
st-undp @ git+https://github.com/undp-data/st-undp.git@0.1.0
```

See [VCS Support](https://pip.pypa.io/en/stable/topics/vcs-support/#vcs-support) for more details.

## Usage

The package is intended to make styling a breeze. The most basic usage involves only two simple steps.

First, use the CLI to set up the recommended theme in `.streamlit/config.toml`:

```shell
python -m st_undp configure
```

This will edit the theme section in the file if it exists or create it if it doesn't.
Then, call `apply_style` function inside your application entry point, typically `app.py`: 

```python
# app.py or an equivalent module
import streamlit as st
import st_undp

st_undp.apply_style()
st.header("Hello world!")  # now UNDP-styled
```