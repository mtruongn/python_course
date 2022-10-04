# Student Install Guide

## ![img](https://snag.gy/CPB5di.jpg) Step 1: Anaconda and Python

> Linux users do not do this. Your setup is complete in terms of development environment.

In our class, we'll be working closely with tools that utilize the Python programming language. [Anaconda](https://docs.continuum.io/anaconda/index) is a popular cross-platform tool that helps install and manage python-related data science libraries. While you may have set this up prior to the class, perhaps as instructed by our prework platform, it's important that we're all setup with the same version for class.

> **Previously Installed Anaconda?**
>
> Please refer to your local instructor for guidance.

1. [Download Anaconda](https://www.anaconda.com/download/#macos) and follow the installation instructions package for your operating system. For MAC, use the 64-bit macOS graphical installer, with the Python 3.7 Anaconda package file.

![img](https://snag.gy/sVFwkQ.jpg)

1. Agree to the terms and let Anaconda go through its default installation.

![img](https://snag.gy/gamr9V.jpg)

1. Anaconda should install several packages by default, including:

- **python**: a programming language very popular with data scientists
- **jupyter**: an interface for creating interactive python notebooks, great for sharing analyses
- **matplotlib**: a plotting library for python
- **nltk**: a toolkit for natural language processing
- **numpy**: a linear algebra library
- **pip** & **setuptools**: software to manage and install python packages
- **scikit-learn**: a toolkit for machine learning algorithms
- **scipy** and **statsmodels**: statistical packages for python
- **sqlite**: a popular, easy to use database

1. We will be using Conda virtual environments. "But why" you might ask?! Everyone has different versions of libraries, system tools, and underlying operating system resources. Using a Conda virtual environment helps mitigate the differences everyone's system brings, with a consistent baseline development environment. This is the proper way to manage your Python environment.

**IMPORT FIRST STEP!** 
Verify that `conda` is setup and in your path. If you're getting a `command not found`, when you type `conda` in your terminal, double check that you installed Anaconda, and your paths are setup correctly (`source ~/.bash_profile` or opening a **new** terminal window are common solutions). You might need to start a new terminal session because `conda` may not be in your path until you reload your shell configuration which includes your updated path environmental variable that refers to where Anaconda is installed.

```
conda install nb_conda
```

The previous command, should install the `nb_conda` package in your root system. This enables Jupyter notebook to use **conda environments** from the **"kernel"** menu. The **conda environment**we will be creating and using for our class will be available after we create it shortly.

**Creating and activating the conda environment**
This command will create an "Anaconda Environment" called `dsi`, which isolates a specific directory on your computer with a specific version of Python (**3.6.5**), and associated Python libraries that can be contextually used for development of data science projects. This contextual isolation allows us to install and use specific libraries and dependencies for projects we will build in class, without impacting your base system, or other "Anaconda Environments" we may want to configure and use in the future. Using these types of environments are supported industry best practices for managing Python projects.

```
conda create -n dsi python=3.6.5 anaconda
```

Before we do anything in class with Python, or Jupyter notebook, please don't forget to activate your environment. This puts our development environment in context to be used.

```
source activate dsi
```

**Update your packages to the latest**

In any terminal, regardless of which directory you are in, you can install the python packages using the `conda install [package name]` command.

Install the following packages:

```
conda install nb_conda=2.2.1 statsmodels=0.8.0 widgetsnbextension=3.0.2 spacy nltk gensim seaborn=0.9.0 scikit-image=0.13.1 scikit-learn=0.19.1 psycopg2 plotly bokeh ipywidgets flask django beautifulsoup4
```

You should be prompted to install these packages, and you should say "y" for yes to install them. This should install successfully.

> **Additional Python / Conda Packages** 
> *As we need more packages, please use the conda system at all costs, before using pip to install packages. When you're not sure, ask an instructor.* 
> *Are you already familiar with pip? Check out these equivalent Conda commands.*

### ![img](https://snag.gy/CPB5di.jpg) Install Brew + Git

[brew.sh](http://brew.sh/) *OSX Only. Linux students will use apt-get for package management. Windows / Linux users do not need to install brew.*

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Instructions are straight forward and listed on site. Brew is a package management system for OSX. Skip this if you are on Windows.

```
brew install git
```



## ![img](https://snag.gy/CPB5di.jpg) Step 2: Confirm Your Python Installation

1. When you've made it this far, open up a terminal and enter the Python interpreter:

> Don't forget to `source activate dsi` first!

```
$ python
```

Depending on your operating system, your terminal should return something like this:

```
Python 3.6.5 | packaged by conda-forge | (default, Apr  6 2018, 13:44:09) 
[GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.53)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

1. Next, make sure that the necessary packages are installed. For example, to check that `matplotlib` is installed, type in your terminal:

> These versions may have changed slightly since our last install guide iteration. This should be an issue as long as the versions are newer than what's listed.

```
>>>> import matplotlib
>>>> print(matplotlib.__version__)
1.5.1
```

You may see another version (which is OK). If you get an error like this:

```
$ import matplotlib
ImportError: No module named matplotlib
```

then you'll need to try to install the Python packages again.

## Additional Software

1. We'll be using [Slack](https://slack.com/), a popular messaging platform, for our class communications.

- Click on the [installation instructions for your platform](https://slack.com/downloads) to install the Slack desktop app. You can also sign into Slack using a web interface or via their mobile app!

> Note: Add additional market & cohort-specific channel instructions here, as needed.

1. [Chrome](https://www.google.com/chrome/) is Google's popular web browser, and it comes with a complete set of developer tools built-in. We'll use Chrome to examine code, debug scripts, and view back-end processes. If you don't already have Chrome, make sure to download and install it now.
2. (Optional) [Tmate.io](https://tmate.io/) is a terminal sharing application.

- Go to the site and follow the directions.

## ![img](https://snag.gy/CPB5di.jpg) Additional Text Editors

A data scientist frequently writes scripts to process data, perform analysis, and create visualizations, webpages, and other end products, so you'll need a good text editor. If you don't already have a preference, try [Atom](https://atom.io/) or [Sublime](http://www.sublimetext.com/). Both editors are available for most platforms. If you have your own preferences, these are only suggestions and are optional pieces of software.

> Instructors should modify these options based on their preferences.

If you are on a Mac, you can install Atom with

```
$ brew cask install atom
```

Or Sublime Text with

```
$ brew cask install sublime-text
```

1. Download the editor of your choice from their website.
2. Install the package by double clicking the file icon or from the command line
3. Run your editor from the applications menu, or from the command line, like so:

```
$ subl
$ atom
```

This example would open up Sublime or Atom, respectively. Whichever editor you choose, be sure to practice using it!



## ![img](https://snag.gy/CPB5di.jpg) Configure Git with your Text Editor

Finally, you'll want to tell `git` which editor it should use for your commits.

- If you choose to use Sublime, you would type:

```
$ git config --global core.editor "subl --wait --new-window"
```

- If you choose to use Atom, you would type:

```
$ git config --global core.editor "atom --wait"
```

## ![img](https://snag.gy/CPB5di.jpg) SSH Setup

Check that you have an ssh key setup first. The follow command should output the contents of your public SSH key to your terminal:

```
cat ~/.ssh/id_rsa.pub
```

If you are getting a file not found error, perhaps you don't yet have an SSH key setup yet. Use the following command to setup your ssh key:

```
$ ssh-keygen -t rsa
```

Use all defaults, no password, for all prompts. This is a necessary step to allow tmate.io sessions, AWS connectivity, or password-less Github Enterprise interactivity or any future interconnectivity with secure shell sessions.



##  ![img](https://snag.gy/CPB5di.jpg)Max's Stuff

- [Hydrogen](https://atom.io/packages/hydrogen)
- [Hyper](https://hyper.is/)
- [Typora](https://typora.io/)