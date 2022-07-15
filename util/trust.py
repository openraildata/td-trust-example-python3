TOCS = {}

MESSAGES = {
    "0001": "activation",
    "0002": "cancellation",
    "0003": "movement",
    "0004": "_unidentified",
    "0005": "reinstatement",
    "0006": "origin change",
    "0007": "identity change",
    "0008": "_location change"
    }


def print_trust_frame(parsed):
    for a in parsed:
        body = a["body"]

        toc = a["body"].get("toc_id", '')
        platform = a["body"].get("platform", '')
        loc_stanox = "@" + body.get("loc_stanox", "")

        summary = "{} ({} {}) {:<13s} {:2s} {:<6s} {:3s}".format(
            body["train_id"], body["train_id"][2:6], body["train_id"][6],
            MESSAGES[a["header"]["msg_type"]], toc, loc_stanox, platform)

        print(summary)
