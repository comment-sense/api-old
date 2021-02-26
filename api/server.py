# This is the key file for the described folder setup
# This file contains the app and routes. You would also this file to setup config values
# such as (before_request(), after_request())... basically this file configures the application
import os

from flask import Flask, session
from flask_restful import Api

from api.utils.auth import authorize, credentials_to_dict
from api.resources.comment import Comment
from api.resources.sentiment import Sentiment

app = Flask(__name__)
server = Api(app)


def print_index_table():
    return (
        "<table>"
        + '<tr><td><a href="/test">Test an API request</a></td>'
        + "<td>Submit an API request and see a formatted JSON response. "
        + "    Go through the authorization flow if there are no stored "
        + "    credentials for the user.</td></tr>"
        + '<tr><td><a href="/authorize">Test the auth flow directly</a></td>'
        + "<td>Go directly to the authorization flow. If there are stored "
        + "    credentials, you still might not be prompted to reauthorize "
        + "    the application.</td></tr>"
        + '<tr><td><a href="/revoke">Revoke current credentials</a></td>'
        + "<td>Revoke the access token associated with the current user "
        + "    session. After revoking credentials, if you go to the test "
        + "    page, you should see an <code>invalid_grant</code> error."
        + "</td></tr>"
        + '<tr><td><a href="/clear">Clear Flask session credentials</a></td>'
        + "<td>Clear the access token currently stored in the user session. "
        + '    After clearing the token, if you <a href="/test">test the '
        + "    API request</a> again, you should go back to the auth flow."
        + "</td></tr></table>"
    )


# setup operational routes
@app.route("/")
def index():
    return print_index_table()


@app.route("/clear")
def clear_credentials():
    if "credentials" in session:
        del session["credentials"]
    return "Credentials have been cleared.<br><br>" + print_index_table()


app.add_url_rule("/authorize", authorize)
app.add_url_rule("/clear", clear_credentials)


# setup resource routes
server.add_resource(Comment, "/comment", "/comment/<string:video_id>")
server.add_resource(Sentiment, "/sentiment/<string:video_id>")


if __name__ == "__main__":
    # When running locally, disable OAuthlib's HTTPs verification.
    #  TODO: Remove this in production
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Specify a hostname and port that are set as a valid redirect URI
    # for your API project in the Google API Console
    app.run("localhost", 5000, debug=True)
