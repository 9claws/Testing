import requests

def create_folder(name_folder):
    token = "y0_AgAAAAAETjVHAADLWwAAAAD8F8NGAADzmCquv-VDHaD9E0wAv-0zv7UxVA"
    url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Authorization': f'OAuth {token}'
               }
    params = {'path': name_folder}
    response = requests.put(url=url_create_folder, headers=headers, params=params)
    return response.status_code

