# Project Name

 Pitch Application

## Author

 Collins Kiprutoh

# Description

This is an application that allows users to sign in or sign up and post one minute pitches.It also allows them comment, view other people comments  to vote on different pitches.

## User Story

- Comment on the different pitches posted py other uses.
- See the pitches posted by other uses.
- Vote on pitch they have viwed by giving it a upvote or a downvote.
- Register to be allowed to log in to the application
- View pitches from the different categories.
- Submit a pitch to a specific category of their choice.

## BDD

| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           |                               Get all posts, Select between signup and signin |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app pitches based on categories and commenting section |
| Select comment button |             **Comment**             |                                             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments tamplate with your comment and other comments |

## Development Installation

To get the code..

1. Cloning the repository:

```bash
https://github.com/wizzicollo/Profile-Pitching-App
```

2. Move to the folder and install requirements

```bash
cd Profile-Pitching-App
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application

```bash
python3.6 app.py server

chmod a+x start.sh
./start.sh
```

Open the application on your browser `127.0.0.1:5000`.

## Technology used

- [Python3.6](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Heroku](https://heroku.com)

## Contact Information

kiprutohcollo@gmail.com

## Live Link To Project




## License
 
 Licensed under[MIT license](license)


