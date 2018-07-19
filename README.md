Slack.io status plugin for Buildbot
===================================

This Buildbot plugin sends messages to a Slack.io channel when each build finishes with a handy link to the build results.

This plugin is based on the buildbot-status-hipchat plugin created by the dev team at http://www.pricingassistant.com/ ; Contributions are welcome!

## Install

### via pip

```sh
pip install -e 'git+https://github.com/mindmatters/buildbot-status-slack#egg=slack'
```

### manual

Copy `slack.py` next to your master.cfg file


## Setup

Create a new Incomming Webhook in your slack account.

Then in your master.cfg, add the following:

```py
import buildbot_status_slack
c['status'].append(buildbot_status_slack.SlackStatusPush("YOUR_SLACK_WEBURL"))
```

### Additional Options:
```py
  localhost_replace = False
  builder_name = False
  username = None
  icon = None
  notify_on_success = True
  notify_on_failure = True
```

### Complete Example:

```py
import buildbot_status_slack
c['status'].append(buildbot_status_slack.SlackStatusPush("YOUR_SLACK_WEBURL", "http://ci.mindmatters.de", "mindmatters Builder", None, None, False, True)
```

Enjoy!

