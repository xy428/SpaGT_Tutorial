# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SpaGT'
copyright = '2024, lalala'
author = 'lalala'
release = 'l'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['nbsphinx',]

templates_path = ['_templates']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
}


html_context = {
    "display_github": True,
    "github_user": "xy428",  # GitHub 用户名
    "github_repo": "SpaGT_Tutorial",  # 仓库名称
    "github_version": "main",  # 分支名，比如 'main' 或 'master'
    "conf_py_path": "/source/",  # conf.py 文件相对于仓库根目录的路径，如果文件在 'docs/' 目录中
}