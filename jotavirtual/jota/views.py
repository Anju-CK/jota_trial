from rest_framework import generics
from rest_framework.response import Response
import requests
from django.shortcuts import render
from datetime import datetime
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema

class MatterportSpaceListView(generics.ListAPIView):

    # @swagger_auto_schema(openapi.Parameter('internal_id', openapi.IN_QUERY, type=openapi.TYPE_STRING))
    def get(self, request, *args, **kwargs):
        # search_term = request.query_params.get('search', None)
        search_term = 'ID1'
        if not search_term:
            return Response({"message": "Search term not provided"}, status=400)

        matterport_api_url = f'https://my.matterport.com/api/v2/search/?allowPending=true&ordering=created&organization=u8jHzqYf2aB&page=1&page_size=24&search={search_term}&type=internal_id'

        # Include your cookie data here
        cookies = {
            'domain_token':'d910cf745dc2453380d8f6ab1b6aa901',
            'authn_token':'e3574a5144d141da98e10bb7d74a7500'
        }

        # Make a GET request to the Matterport API with cookies in headers
        response = requests.get(matterport_api_url, headers={'Cookie': '; '.join([f'{name}={value}' for name, value in cookies.items()])})

        if response.status_code == 200:
            data = response.json()['results']
            # data = [
            #     {
            #         "name": "Jotaspaces1",
            #         "created": "2023-11-24T08:57:06.767740Z",
            #         "thumbnail": "https://cdn-2.matterport.com/apifs/models/prnTDzrwvA8/images/71zMbKa5AXW/71zMbKa5AXW-Photo_01.jpg?t=2-42ef6cad56b84ab4b67b811157d5fcc3486df4f5-1702530196-1&width=100&height=70&fit=crop&disable=upscale",
            #         "address": {
            #             "public_mode": "full",
            #             "address_1": "Infopark Kakkanad Kerala 682030 India"
            #         },
            #     },
            #     {
            #         "name": "Jotaspaces2",
            #         "created": "2023-11-25T08:57:06.767740Z",
            #         "thumbnail": "https://cdn-2.matterport.com/apifs/models/prnTDzrwvA8/images/71zMbKa5AXW/71zMbKa5AXW-Photo_01.jpg?t=2-42ef6cad56b84ab4b67b811157d5fcc3486df4f5-1702530196-1&width=100&height=70&fit=crop&disable=upscale",
            #         "address": {
            #             "public_mode": "full",
            #             "address_1": "Infopark Kakkanad Kerala 682030 India"
            #         },
            #     }
            # ]

            for space in data:
                # Convert ISO 8601 formatted string to datetime object
                space['created'] = datetime.strptime(space['created'], '%Y-%m-%dT%H:%M:%S.%fZ')

                # Format the date and assign it to the 'formatted_date' field
                space['formatted_date'] = space['created'].strftime('%b %d, %Y')

            url_to_share = "https://my.matterport.com/show/?m=sKRxxDcS4AZ"
            social_links = {
                "facebook": f"https://www.facebook.com/sharer/sharer.php?u={url_to_share}",
                "twitter": f"https://twitter.com/intent/tweet?url={url_to_share}",
                "linkedin": f"https://www.linkedin.com/sharing/share-offsite/?url={url_to_share}",
                "pinterest": f"https://pinterest.com/pin/create/button/?url={url_to_share}",
                "email": f"mailto:?subject=Check%20out%20this%20link&body={url_to_share}",
            }
            return render(request, 'allspace.html', {'api_data': data, 'social_links': social_links})
        else:
            return Response({"message": f"Failed to retrieve data for search term {search_term}"},
                            status=response.status_code)



def dashboard_view(request):
    books = [
        {
            "name": "Jotaspacessssss1",
            "created": "2023-11-24T08:57:06.767740Z",
            "thumbnail": "https://cdn-2.matterport.com/apifs/models/prnTDzrwvA8/images/71zMbKa5AXW/71zMbKa5AXW-Photo_01.jpg?t=2-42ef6cad56b84ab4b67b811157d5fcc3486df4f5-1702530196-1&width=100&height=70&fit=crop&disable=upscale",
            "address": {
                "public_mode": "full",
                "address_1": "Infopark Kakkanad Kerala 682030 India Kakkanad is home to the Infopark,"
                             # " a technological hub and one of the major IT parks in Kerala. It hosts numerous IT companies, "
                             # "fostering the growth of the IT sector in the region."
            },
            'space': "qqqqqqqqqqqqqqqqqqqq",
            'view': 10,
            'click': 10,
            'share': 10
        },
        {
            "name": "Jotaspaces2",
            "created": "2023-11-24T08:57:06.767740Z",
            "thumbnail": "https://cdn-2.matterport.com/apifs/models/prnTDzrwvA8/images/71zMbKa5AXW/71zMbKa5AXW-Photo_01.jpg?t=2-42ef6cad56b84ab4b67b811157d5fcc3486df4f5-1702530196-1&width=100&height=70&fit=crop&disable=upscale",
            "address": {
                "public_mode": "full",
                "address_1": "Infopark Kakkanad Kerala 682030 India"
            },
            'space': "qqqqqqqqqqqqqqqqqqq",
            'view': 10,
            'click': 10,
            'share': 10
        },
        {
            "name": "Jotaspaces3",
            "created": "2023-11-24T08:57:06.767740Z",
            "thumbnail": "https://cdn-2.matterport.com/apifs/models/prnTDzrwvA8/images/71zMbKa5AXW/71zMbKa5AXW-Photo_01.jpg?t=2-42ef6cad56b84ab4b67b811157d5fcc3486df4f5-1702530196-1&width=100&height=70&fit=crop&disable=upscale",
            "address": {
                "public_mode": "full",
                "address_1": "Infopark Kakkanad Kerala 682030 India"
            },
            'space': "qqqqqqqqqqqqqqqqqqqqqqqq",
            'view': 10,
            'click': 10,
            'share': 10
        },
        {
            "name": "Jotaspaces4",
            "created": "2023-11-24T08:57:06.767740Z",
            "thumbnail": "https://cdn-2.matterport.com/apifs/models/prnTDzrwvA8/images/71zMbKa5AXW/71zMbKa5AXW-Photo_01.jpg?t=2-42ef6cad56b84ab4b67b811157d5fcc3486df4f5-1702530196-1&width=100&height=70&fit=crop&disable=upscale",
            "address": {
                "public_mode": "full",
                "address_1": "Infopark Kakkanad Kerala 682030 India"
            },
            'space': "qqqqqqqqqqqqqqq",
            'view': 10,
            'click': 10,
            'share': 10
        }
    ]
    for book in books:
        book['created'] = datetime.strptime(book['created'], '%Y-%m-%dT%H:%M:%S.%fZ')
        book['formatted_date'] = book['created'].strftime('%b %d, %Y')
    return render(request, 'dashboard.html', {'books': books})
def settings_view(request):
    return render(request, 'settings.html')

def login_view(request):
    return render(request, 'login.html')

def landing_screen_view(request):
    return render(request, 'landing_screen.html')

def space_view(request):
    return render(request, 'space.html')

def editspace_view(request):
    return render(request, 'editspace.html')

def embed_view(request):
    return render(request, 'embed.html')

def brand_view(request):
    return render(request, 'branding.html')

def whitelabel_view(request):
    return render(request, 'whitelabeling.html')


