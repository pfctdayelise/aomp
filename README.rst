A script to figure out which Wikipedia articles for tennis players at the 2016 Australian Open need freely licensed photos!

Github can render the notebook directly, but the formatting looks slightly better `on nbviewer <https://nbviewer.jupyter.org/github/pfctdayelise/aomp/blob/master/How%20many%20Australian%20Open%20players%20need%20photos%20in%20Wikipedia%3F.ipynb>`_.

To run the code yourself:

- You need python 3, pip(==pip3), virtualenv
- Clone the repo
- Make a virtualenv with python 3 (With virtualenvwrapper: ``mkvirtualenv -p `which python3` aomp``)
- Install the requirements: ``pip install -r requirements.txt``
- Run the script: ``python script.py`` (Be sure you want to check all 546 players before you do this, maybe!)

To run the notebook:

- ``pip install jupyter``
- Launch the notebook server: ``jupyter notebook``
- This should pop open a browser tab which will have a link to the notebook. From there you can modify the cells and re-run them to your heart's content!
