# st-undp

A utility package that styles Streamlit apps according to [UNDP Design System](https://design.undp.org).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

Currently, the package is distributed via GitHub only. You can install with `pip` with:

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

First, copy the below template to your `.streamlit/config.toml`:

```toml
[theme]

# The preset Streamlit theme that your custom theme inherits from.
# One of "light" or "dark".
base = "light"

# Primary accent color for interactive elements.
primaryColor = "#d12800"  # dark-red

# Background color for the main content area.
backgroundColor = "#FFFFFF"

# Background color used for the sidebar and most interactive widgets.
secondaryBackgroundColor = "#F7F7F7"  # gray-200

# Color used for almost all text.
textColor = "#000000"

# Font family for all text in the app, except code blocks. One of "sans serif",
# "serif", or "monospace".
font = "sans serif"
```

Then, call `apply_style` function inside your application entry point, typically `app.py`: 

```python
# app.py or an equivalent module
import streamlit as st
import st_undp

st_undp.apply_style()
st.header("Hello world!")  # now UNDP-styled
```

To launch an example app that showcases the style and components, run:

```shell
python -m streamlit run app.py
```
## Features

This package is currently in the early stages of development. Main features include:

- `ProximaNova` fonts
- CSS styles for most Streamlit input components
- Basic custom components like Stats Card

## Contributing

Guidelines for contributing to your project. This can include how to report issues, submit pull requests, and coding standards.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

All contributions must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
The codebase is formatted with `black` and `isort`. Use the provided [Makefile](./Makefile) for these
routine operations.

## License

This project is licensed under the BSD 3-Clause License. However, entities or individuals not affiliated with UNDP 
are strictly prohibited from using this package or any of its components to create, share, publish, or distribute works 
that resemble, claim affiliation with, or imply endorsement by UNDP.

UNDP’s name, emblem and its abbreviation are the exclusive property of UNDP and are protected under international law. 
Their unauthorized use is prohibited, and they may not be reproduced or used in any manner without UNDP’s prior written permission. 

## Contact

This project is part of [Data Futures Exchange (DFx)](https://data.undp.org) at UNDP.
If you are facing any issues or would like to make some suggestions, feel free to 
[open an issue](https://github.com/undp-data/st-undp/issues/new/choose). 

For enquiries about DFx, visit [Contact Us](https://data.undp.org/contact-us).
