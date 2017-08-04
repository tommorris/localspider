# localspider

localspider is a very simple Scrapy-based spider for sites on `localhost` to check that the internal links all work.

## Installation

Currently, localspider is not packaged for PyPI. You can install it locally for development as follows.

You'll need to have `virtualenv` and `virtualenvwrapper` set up.

````
git clone git@github.com:tommorris/localspider.git
cd localspider
mkvirtualenv localspider
pip install -r requirements.txt
````

Then run it by passing the port number in as an environment variable:

````
PORT=3000 scrapy runspider spider.py --output=fails.json
````

This will run localspider against `localhost:3000` and put any failures it finds into `fails.json`

## Development

Feel free to improve this. It's an itch-scratching project: I got bored of manually checking internal links on websites so I created something that would do it for me.

* License: MIT
* Be excellent to each another.
