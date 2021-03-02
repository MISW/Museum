import slackweb
import datetime
from django.conf import settings


ALERT_CHANNELS = [
    "inquiry",
    "development"
]

ALERT_URL = {
    "inquiry": settings.SLACK_WEBHOOK_URL_INQUIRY,
    "development": settings.SLACK_WEBHOOK_URL_DEVELOPMENT
}

ALERT_COLOR = {
    "inquiry": "#ffff00",
    "development": {
        "create": "#00ffff",
        "update": "#00ff00"
    },
}

ALERT_FALLBACK = {
    "inquiry": "This is inquiry notification attachment",
    "development": "This is notification of creation and update of developments attachment",
}

def create_variable_attachment(pretext: str, title: str, title_link: str, author_name: str, ts) -> dict:
    if not isinstance(ts, datetime.datetime):
        return {}

    variable_attachment = {
        "pretext": pretext,
        "title": title,
        "title_link": title_link,
        "author_name": author_name,
        "ts": str(int(ts.timestamp()))
    }
    return variable_attachment


# TODO: logを出す
def send_alert_to_channel(channel: str, mode: str, variable_attachment: dict):
    # パラメータが正確に設定されているか
    for value in ALERT_URL.values():
        if not value:
            return

    url = None
    for base_channel in ALERT_CHANNELS:
        if channel == base_channel:
            url = ALERT_URL[channel]
    if not url:
        return


    slack = slackweb.Slack(url=url)

    attachment = {
        "fallback": ALERT_FALLBACK[channel],
        "color": ALERT_COLOR[channel] if not mode else ALERT_COLOR[channel][mode],
        "footer": "send by MISW Museum",
    }
    attachment.update(variable_attachment)

    slack.notify(attachments=[attachment,])

