# Python Basic Configuration

## Pre-requisities to run Selenium with Python
In order to run the program you would need
- Python 3
- install dependencies
- Google Chrome / Chromium (need to check this one)
- ChromeDriver - WebDriver for Chrome - https://sites.google.com/a/chromium.org/chromedriver/downloads (Follow the instructions in the website)
	- or you can visit https://sites.google.com/a/chromium.org/chromedriver/getting-started

## Creating Virtual Environment

Resources: https://docs.python.org/3/tutorial/venv.html

Extract:
```
# To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

python -m venv ~/envs/target
source ~/envs/target/bin/activate

```

You can alternative run `source ~/envs/target-env/bin/activate` for this you have to create a folder named `envs` 

## Install Dependencies
Run below command 
```
python -m pip install -r requirements.txt
```

## Issues

- On macOS you might need to accept manually to run `chromedriver` on your computer using the Security & Privacy under General tab.
- You would have to expose the `chromedriver` file to PATH so it's accessible for execution



## Notes
`chromedriver` direct link for mac - https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_mac64.zip

Sending email:
Use this link to enable "less secure" access to a gmail account
this feature is only avaiable if MFA is disabled.
https://myaccount.google.com/lesssecureapps

Full tutorial https://realpython.com/python-send-email/

# Running the script
```sh
export EMAIL_TO = "email@domain.com"
export EMAIL_SOURCE = "<your-email@gmail.com>"
read -s EMAIL_SOURCE_PASSWORD
```

then

```sh
export EMAIL_SOURCE_PASSWORD
```

And finally launch the script
```sh
python launcher.py
```

You can set a cron job and trigger the script, remember to set the environment vairables before running the script.
