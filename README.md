# Bitly URL shortener

Just a simple URL shortener with ability to check out shortened link clicks.

## Enviroment variables

Get token on [bitly](https://app.bitly.com/settings/integrations/) and use it in .env file as `BITLY_TOKEN=urtoken`. Then you can run it!

## How to install

Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

## Run

To run program on Windows OS you should use [this](https://www.wikihow.com/Use-Windows-Command-Prompt-to-Run-a-Python-File)

To run program on Linux head to main.py file's directory and type:

```
python main.py {url}
```

Depending on whether you give it shortened link or unshortened, it will:

- give you shortened link clicks count
- give shortened link

If program will run into an error, it will print:

- `Err while creating bitlink` if program was tring to shorten ur link
- `Err while calculating clicks` if program war tring to count clicks

## Notes

Some info about all fuctions in code

```py
def is_bitlink()
```

1. parses given link
1. gets information about link
1. returns `True` if link is shortened or `False` if link isn't  

```py
def count_clicks()
```

1. parses link
1. gets info about link and gets clicks_count from link info
1. returns it. If func runs into an error while raising for status it'll print error message

```py
def shorten_link()
```

1. uses unshortened link and tries to short it
1. raises for status, if successfully, gets link from response text and returns it
