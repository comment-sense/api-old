# -*- coding: utf-8 -*-

from flask_restful import Resource
import googleapiclient.discovery

GOOGLE_API_KEY = "AIzaSyB3i6xQSuki2gyAHnwAVanAsz4LyoaQ5vc"


# Call the API's commentThreads.list method to list the existing comments.
def get_comments_as_dict(youtube, video_id):
    results = (
        youtube.commentThreads()
        .list(part="snippet", videoId=video_id, textFormat="plainText",)
        .execute()
    )
    return results


class Comment(Resource):
    """
    TODO: describe the resource
    """

    def get(self, video_id):
        """
        @rtype: object
        """
        api_service_name = "youtube"
        api_version = "v3"
        # client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

        # # Get credentials and create an API client
        # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        #     client_secrets_file, scopes
        # )
        # credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=GOOGLE_API_KEY
        )

        response = get_comments_as_dict(youtube, video_id)
        return response

    def post(self):
        # TODO: implement POST /comment/<video_id>
        pass
