# influencR

To help fight back.  
Influenced by the [article by Andy Moon](https://medium.com/@andymoon/how-we-can-fight-back-c1c3605c57ad#.jch2zel09).

Goal: Create a simple Heroku app to serve user's contact information 
for their representatives, current issues in that state/district, and 
a script that the user can use to call their representatives.

[Data sources in wiki](https://github.com/cstoafer/influencR/wiki) 
(so we don't have to commit to repo to add data sources)


## Contributing - Getting Started

Clone the repo

```
git clone https://github.com/cstoafer/influencR.git
```

Install requirements

```
cd influencR
pip install -r requirements.txt
```

Initiate the database

```
mkdir data
sqlite3 data/db.db < schema.sql
```

Run the server

```
python main.py
```

Navigate to [localhost:5000](http://localhost:5000/) in your browser.


## Getting Started - new with Heroku

- https://realpython.com/blog/python/flask-by-example-part-1-project-setup/
- autoenv for env and environmental variables
- postgres install
- heroku install
