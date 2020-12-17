# Web_Scrapping Homework.
Submission includes a notebook file, 2 python scripts and an html file.
Jupyter notebook file (mission_to_mars.ipynb) - visits all the web pages and does web scrapping and displays the output
python scripts (app.py and scrape_mars.py)
scrape_mars.py - imports splinter and beautifulsoup libraries and performs web scrapping, saves aal the scraped data into a dictionary (mars_data)
app.py - calls the scrape_mars.py and saves the mars_data info, it further saves this info into mongoDB and retrieves data from the database and displays it on index.html page
