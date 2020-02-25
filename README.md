## Twitter 3.3
The application visualizes all the locations of the year you want on the world map.
<h2>What map shows?</h2>
    1. The world map<br>
    2. Locations of the friends you follow<br>
<h2>Installation</h2>
To run twitter_map you have to have all the libraries that are used in the 
project. So run this line in your cmd:

```
sudo pip install -r requirements.txt
```

<h2>Usage</h2>
To start the application you have to have installed python 3+ version and installed virtualenv<br>
To activate your virtualenv you have to write:
```
python -m venv venv
source venv/bin/activate

```

To run the program:

```

python flask_app.py

```

After that you will have a field in your browser:
```
Enter Twitter Account: <user name>
```

You have to enter the name of the user whom friends you want to know. After 
that you have to wait a littele bit. You have to open ./docs/index.html with
 your browser.<br>
To deactivate your virtualenv:
```
deactivate
```
 
 <h2>Result</h2>
 You have a map with the locations of some person friends. Also if you press
  the marker you will see the name of each person.
 
 <h2>Conclusion</h2>
 We can use this map to know about somebody's friends and role models.
