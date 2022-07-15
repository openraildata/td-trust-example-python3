# Python3/stomp.py TD/TRUST demo script
This is a short demonstration script which outputs C-class messages from
Network Rail's TD feed, or basic information from the train movements
feed.

## Setup
You must [register an account](https://datafeeds.networkrail.co.uk/ntrod/login)
for the Network Rail data feeds.
When your account is active, you can enable the feeds - log in, go to "my feeds",
and click on the "TD" link on the left of the page. Select "All Signalling Areas"
in the "Available" list, move it into "Selected", then save. For TRUST, the
process is the same, except you'll need to click on "Train Movements", and
select "All TOCs".

Create a file named `secrets.json` in the same directory as `main.py`. This
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

# To show TD messages
./main.py --td
# To show TRUST messages
./main.py --trust
```

You should now see the printed messages in your terminal.

## Durable subscriptions
Durable subscriptions have certain advantages - with a durable subscription,
the message queue server will hold messages for a short duration while you
reconnect, which reduces the risk you'll miss messages. Unfortunately, while
this property is quite desirable, it carries certain availability risks while
interacting with the Network Rail feeds via STOMP, due to the interaction
between a bug where ActiveMQ may not detect that the STOMP client has
disconnected, and an overzealous firewall rule which will block you for
several hours if it believes you've attempted to connect while already
connected.

For this reason, this example does not use durable subscriptions by default,
although you can pass the argument `--durable` if you wish to do so. If you
bridge the feed to your own message queue server, no such constraint exists
and there's no reason not to use durable subscriptions with STOMP.

See [here](https://wiki.openraildata.com/index.php?title=About_the_Network_Rail_feeds#Durable_subscriptions_via_STOMP)
for more information.

## Licence
This is licensed under the "MIT No Attribution" licence, a variant of the MIT
licence which removes the attribution clause. See LICENCE.txt for
more information.

# Further information
* [TD](https://wiki.openraildata.com/index.php?title=TD)
* [TRUST](https://wiki.openraildata.com/index.php?title=Train_Movements)
* [Durable subscriptions](https://wiki.openraildata.com/index.php?title=Durable_Subscription)
