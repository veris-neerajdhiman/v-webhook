
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView

# Create your views here.


class SampleView(APIView):
    """

    """
    def post(self, request):
        originalRequest =request.data.get('originalRequest')
        appname = request.data.get('result').get('parameters').get('appName')

        if originalRequest.get('source') == 'slack':
            attachments = []
            for app in appname:
                attchment = {
                    "title": app,
                    "title_link": "http://app.veris.in",
                    "color": "#36a64f",
                    "attachment_type": "default",

                    "fields": [
                            {
                                "title": "Sub Text comes here",
                                "value": 'value 1',
                                "short": "false"
                            },
                            {
                                "title": "Another text comes here",
                                "value": 'value 2',
                                "short": "true"
                            },

                        ],

                        "thumb_url": "https://media.giphy.com/media/xTiQyI4ZqiLbb7FgE8/giphy.gif"
                }
                attachments.append(attchment)

            if attachments:
                dataText = {
                    "text": 'Matched apps are as follows : ',
                    "attachments": attachments
                }
            else:
               dataText = {
                   "text": 'NO Matched apps found, matched keyword is {0}'.format(appname),
               }
        else:
            dataText = {
                'text': 'app names are {0}'.format(appname)
            }

        response = ({
            'speech': 'app names are {0}'.format(appname),
            'displayText': 'sample displayText',
            'data': {
                "slack": dataText
            },
            'contextOut': [
                {
                    'test context': True
                }
            ],
            'source': 'sample source',
            'followupEvent': {
                'event': 'sample followupEvent'
            }
        })
        return Response(response, status=status.HTTP_200_OK)