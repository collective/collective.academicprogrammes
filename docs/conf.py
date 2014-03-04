# -*- coding: utf-8 -*-
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinxcontrib_robotframework',
]

# Enable Robot Framework tests during Sphinx compilation
sphinxcontrib_robotframework_enabled = True

# Hide all Robot Framework syntax by default
sphinxcontrib_robotframework_quiet = True

# Configure Robot Frameowrk tests to use Firefox
sphinxcontrib_robotframework_variables = {
    'BROWSER': 'PhantomJS'
}

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'collective.academicprogrammes'
copyright = 'collective.github.com'

# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinxcontrib_robotframework']

# General information about the project.

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['robot.rst', '*.txt', '*.GPL']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'pyramid'

# Output file base name for HTML help builder.
htmlhelp_basename = 'collective.academicprogrammes'
