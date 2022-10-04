# Student Install Guide Windows

### Windows / PC

> Skip this section if you're on MAC or Linux.

- Install `gitbash` (32-bit or 64-bit depending on your version of windows): <https://www.youtube.com/watch?v=rWboGsc6CqI>

From here on out, you have 2 options. It's recommended that you use Anaconda for Windows, and you can install it using the Python 3.6 graphical installer here (use 64 or 32 bit depending on your flavor of Windows):

<https://www.anaconda.com/download/#windows>

After you install Anaconda, and Gitbash, follow the original guide that is designed for MAC. In a nutshell, the abridged version of the Anaconda setup for Windows (while in a Gitbash session), should be:

Create your conda environment

```
conda create -n dsi python=3.6.5 anaconda
```

Activate your `dsi` environment

```
activate dsi
```

Install additional packages

```
conda install nb_conda=2.2.1 statsmodels=0.8.0 widgetsnbextension=3.0.3 spacy nltk gensim seaborn=0.7.1 scikit-image=0.13.1 scikit-learn=0.19.1 psycopg2 plotly bokeh ipywidgets flask django beautifulsoup4
```

Then, just install [Chrome](https://www.google.com/chrome/) web browser.

## (Optional) Install Docker for Windows

Another option you can consider, is using Docker. Basically, you can be up and running within a very short period of time if your windows system doesn't have too many Firewalls or anti-virus applications to modify. This is nice to have, but if you can't get it to work within an hour, use the preferred Anaconda setup.

- Please see the guidelines for installing [Docker](https://git.generalassemb.ly/DSI-US-7/course-info/wiki/Installing-Docker-Locally).

After you've successfully installed Docker, simply create the container using the following from `gitbash`. This will create a virtual machine instance called `dsi` that you can start and stop in the future.

1. Create Docker container for `dsi` environment, then start jupyter notebook.

   ```
   docker run -d -p 8888:8888 -v `pwd`:/home/jovyan --name dsi jupyter/scipy-notebook
   ```

2. Get the url of your running jupyter server on your `dsi` container, which includes the token necessary to get access:

   ```
   docker exec dsi jupyter notebook list
   ```

3. To access jupyter paste the url from your terminal that looks like `http://localhost:8888/?token=b6965133171f7f5fccc788cf4f55f3a4917a07f0e816a48a` into your browser. Replace the token parameter with the reference from step 2.

### Troubleshooting Windows Docker Problems

- If the "Docker" command doesn't respond, make sure you have installed Docker correctly and that it's in the path. It's also necessary if you run the docker command via gitbash rather than DOS.
- Can't connect to your notebook via web browser? Check that your firewalls are allowing access, or turn them off. This is a common problem but unfortunately, not all configurations are the same so this may take some research in order to work correctly. Please be patient because Windows machines aren't the easiest to support due to the market adaptation of Unix based systems for the development environment data science prefers.