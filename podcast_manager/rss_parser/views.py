import requests
import xml.etree.ElementTree as ET
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ModelParser


class ParsRssFeed(APIView):
    def get(self, request):
        url = request.query_params.get('url')
        if not url:
            return Response({'error': 'URL parameter is missing'}, status=400)
        response = requests.get(url)
        root = ET.fromstring(response.content)
        items = []
        for item in root.iter('item'):
            title = item.find('title').text
            description = item.find('description').text
            link = item.find('link')
            itunes_author = item.find('.//{http://www.itunes.com/dtds/podcast-1.0.dtd}author')
            itunes_duration = item.find('.//{http://www.itunes.com/dtds/podcast-1.0.dtd}:duration')
            itunes_images = item.find('.//{http://www.itunes.com/dtds/podcast-1.0.dtd}:image')
            rss_feed_item = ModelParser(
                title=title,
                description=description,
                link=link,
                itunes_author=itunes_author.text if itunes_author is not None else None,
                itunes_duration=itunes_duration.text if itunes_duration is not None else None,
                )
            rss_feed_item.save()
            items.append({
            'title': title,
            'description': description,
            'link': link,
            'itunes_author': itunes_author.text if itunes_author is not None else None,
            'itunes_duration': itunes_duration.text if itunes_duration is not None else None,
            'itunes_image': itunes_images.text if itunes_images is not None else None,
        })
        return Response(items)
