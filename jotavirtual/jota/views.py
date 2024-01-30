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
            '_vwo_uuid_v2':'DD73518466238977642B4CD0E32C9E373|45bbcc36468ae3567231c5c04da332e8',
            ' _vwo_uuid':'DD73518466238977642B4CD0E32C9E373',
            '_vwo_ds':'3%3Aa_0%2Ct_0%3A0%241700046564%3A69.93065289%3A%3A%3A4_0%2C3_0%3A5',
            'apple_analytics':'web-direct; cbar_uid=621862532989',
            'SESSvl':'en',
            'cookie_consent_v3':'%7B%22version%22%3A3%2C%22strictlyNecessary%22%3Atrue%2C%22custom%22%3A%7B%22performance%22%3Atrue%2C%22functionality%22%3Atrue%2C%22targeting%22%3Atrue%7D%7D',
            '_mkto_trk':'id:911-LXO-192&token:_mch-matterport.com-1700455732495-32277',
            '_scid':'0d6daa5d-096d-4658-9b53-c078e62d08bc',
            '_rdt_uuid':'1700455733659.1bfe7bac-9b33-4988-98e9-dcaf03e2da91',
            '_fbp':'fb.1.1700455733828.1860351439',
            '_yjsu_yjad':'1700455733.85005910-fa52-4fca-9b02-0e5e2d3dbb49',
            '_pin_unauth':'dWlkPU9HRmpaR1EwTXpZdFpqRTJOQzAwWlRkakxUZzBaVGd0Wm1FNU5UTXlOVGd3TTJZNA',
            '_gcl_au':'1.1.1423864634.1700455734',
            '_sctr':'1%7C1700418600000',
            '_hjSessionUser_928272':'eyJpZCI6IjNmOWM4NjFjLWY4ZjAtNWZjNS05NDc1LTdhZDE5Y2FhYjM4YSIsImNyZWF0ZWQiOjE3MDA0NTU3MzM4NzAsImV4aXN0aW5nIjp0cnVlfQ==',
            '_gid':'GA1.2.1081463536.1700555483',
            'intercom-device-id-toxdrc11':'24fdf2be-16c1-4364-a421-32a2d4011509',
            'intercom-id-toxdrc11':'32a16b6b-7a98-4fb7-94fc-d65aab8f1fae',
            '_vis_opt_exp_21_combi':'2',
            '_tt_enable_cookie':'1',
            '_ttp':'0YV2iQNx1TGwKbPDVoe2XZ_yuP1',
            '_vis_opt_exp_35_combi':'1',
            '_vis_opt_exp_31_combi':'1',
            '__q_state_oerwbSnkKEjaiD3g':'eyJ1dWlkIjoiN2FlNTQzNTktZjMzYi00MDU0LWI5OTgtNTNlZmRmODExY2JjIiwiY29va2llRG9tYWluIjoibWF0dGVycG9ydC5jb20iLCJtZXNzZW5nZXJFeHBhbmRlZCI6ZmFsc2UsInByb21wdERpc21pc3NlZCI6ZmFsc2UsImNvbnZlcnNhdGlvbklkIjoiMTI3NDEyNjc0NjI4NTg4MzY1OCJ9',
            '_clck':'1bykxwj%7C2%7Cfgz%7C0%7C1419',
            '_vis_opt_s':'8%7C',
            '_vis_opt_test_cookie':'1',
            'cbar_sess':'3',
            '_scid_r':'0d6daa5d-096d-4658-9b53-c078e62d08bc',
            '_uetsid':'b4b94fc0885f11eeb1e215926a6b8f87|1q700fb|2|fgz|0|1420',
            '_uetvid':'1b0c6f20876011eea1ffcba9176d58bb|1npvv0l|1700802999710|2|1|bat.bing.com/p/insights/c/o',
            '_clsk':'4tmr7o%7C1700803534426%7C3%7C1%7Co.clarity.ms%2Fcollect',
            '_ga_Y48QX5W4WM':'GS1.1.1700801940.15.1.1700803548.0.0.0',
            'cbar_lvt':'1700805334',
            'domain_token':'d910cf745dc2453380d8f6ab1b6aa901',
            'authn_token':'e3574a5144d141da98e10bb7d74a7500',
            '_vis_opt_exp_21_goal_2':'1',
            '_vis_opt_exp_31_goal_2':'1',
            'cbar_sess_pv':'5',
            'mprtlmid':'6GwFy8GVNn3m*7zabwpMc',
            'ajs_user_id':'DAZHrSkYcyM',
            'ajs_group_id':'u8jHzqYf2aB',
            'ajs_anonymous_id':'d5d60f20-e7b0-489e-904f-d98e3a685b02',
            '_ga_W66Y5HELXX':'GS1.1.1700797047.5.1.1700816483.51.0.0',
            '_ga':'GA1.2.386849141.1700455734',
            '_gat':'1',
            'intercom-session-toxdrc11':'ZjRNVkM2RytPNjV6NlFibHpMNVRNazgvZHk0L29tbkc5MzlZK0gzOEdDdGNmMkZZbjc5S29ndTUvN3k1NmhQcS0tN1pBREFGSkhKUG84VmZ3Tm1ac3VTZz09--313b5343022f5a2e98f06bce7587fb2e233cdc4a',
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

def editspace_view(request):
    return render(request, 'editspace.html')

def brand_view(request):
    return render(request, 'branding.html')

def whitelabel_view(request):
    return render(request, 'whitelabeling.html')


