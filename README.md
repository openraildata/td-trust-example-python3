# Python3/stomp.py TD/TRUST demo script
This is a short demonstration script which outputs C-class messages from
Network Rail's TD feed, or basic information from the train movements
feed.

It does not currently display S-class messages from TD.

## Setup (publicdatafeeds)
You must [register an account](https://publicdatafeeds.networkrail.co.uk/ntrod/create-account)
for the Network Rail data feeds.

Once your account is verified and active, continue to the section below.

## Setup
Create a file named `secrets.json` in the same directory as `main.py`. This
file should consist of a JSON array containing your registered email and
password. For example, if your email address was "user@example.com" and your
password was "hunter2", the contents of the file would be:
```json
["user@example.com", "hunter2"]
```

Make sure you install the dependencies in requirements.txt. You can do this
by opening a terminal in your local copy of this repository, and running the
following commands. Using a virtual environment is good practice, but you can
skip these steps if you wish.

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage
Open a terminal in your local copy of this repository

```shell
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
reconnect, which reduces the risk you'll miss messages.

CACI (the contractor responsible for the Network Rail open data feeds) had
previously implemented a firewall rule which banned IP addresses for an hour
if an ERROR frame was issued to them; this could happen under certain
circumstances with a durable subscription. This is no longer the case.

For this reason, this example does not use durable subscriptions by default,
although you can pass the argument `--durable` if you wish to do so. 

See [here](https://wiki.openraildata.com/index.php?title=About_the_Network_Rail_feeds#Durable_subscriptions_via_STOMP)
for more information.

## Licence
This is licensed under the "MIT No Attribution" licence, a variant of the MIT
licence which removes the attribution clause. There is no obligation to provide
attribution; it would nevertheless be appreciated. See LICENCE.txt for more
information.

# Further information
* [TD](https://wiki.openraildata.com/index.php?title=TD)
* [TRUST](https://wiki.openraildata.com/index.php?title=Train_Movements)
* [Durable subscriptions](https://wiki.openraildata.com/index.php?title=Durable_Subscription)
