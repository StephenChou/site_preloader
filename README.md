
# Site Pre-Loader

Multiple hosting sites load sites very slowly if they haven't been accessed in a certain period of time. This is present in many free-tier hosting sites. When ran, this script can act as a cron job to ensure that a website is quick to load every time a user visits it by sending a simple get request to the site. This is useful if your site does not have normal traffic.

## Usage:

First install the required dependencies:
```
pip install -r requirements.txt
```

Then, open ```urls.txt``` and paste each url on a newline. For example, the ```urls.txt``` file can look like:
```
https://surprisify.me 
https://stephenchou.onrender.com
```

Finally, run:
```
python reload_site.py
```

## Cron/GitHub Actions

In ```.github/workflows/github_actions.yml ``` there is a cron expression that can be used to run the script through GitHub Actions. Currently it's set to every 15 minutes but can be set by the user.




