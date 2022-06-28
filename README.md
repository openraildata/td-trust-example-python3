# Python3/stomp.py TD demo script
This is a short demonstration script which outputs C-class messages from
Network Rail's TD feed.

## Setup
You must [register an account](https://datafeeds.networkrail.co.uk/ntrod/login)
for the Network Rail data feeds.
When your account is active, you can enable the TD feed - log in, go to "my feeds",
and click on the "TD" link on the left of the page. Select "All Signalling Areas"
in the "Available" list, move it into "Selected", then save.

Create a file named `secrets.json` in the same directory as `td.py`. This
file should consist of a JSON array containing your registered email and
password(_not_ your security token).
For example, if your email address was "user@example.com" and your password
was "hunter2", the contents of the file would be:
```text
["user@example.com", "hunter2"]
```

Make sure you install the dependencies in requirements.txt. You can do this
by opening a terminal in your local copy of this repository, and running the
following commands. Using a virtual environment is good practice, but you can
skip these steps if you wish.

```text
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage
Open a terminal in your local copy of this repository

```text
source venv/bin/activate
./td.py
```

You should now see the printed C-class messages in your terminal.

## Licence
This is licensed under the "MIT No Attribution" licence, a variant of the MIT
licence which removes the attribution clause. See LICENCE.txt for
more information.

# Further information
* [TD](https://wiki.openraildata.com/index.php?title=TD)
* [Durable subscriptions](https://wiki.openraildata.com/index.php?title=Durable_Subscription)
