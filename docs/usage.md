# Usage

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
