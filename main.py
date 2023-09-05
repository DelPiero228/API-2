import requests
import json
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = file_path
        headers = {"Content-Type": "application/json", "Authorization": "y0_AgAAAAAzcazzAADLWwAAAADrGNeeZhnMDds9S1eflh0n2119y-PC2bo".format(self.token)}
        params = {"path": f"/{file_name}", "overwrite": "true"}
        upload_link = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        get_upload_url = requests.get(upload_link, headers=headers, params=params)
        get_url = get_upload_url.json()
        upload_url = get_url["href"]
        responce = requests.api.put(upload_url, data=file_path)
        responce.raise_for_status()
        if responce.status_code == 201:
            return "Ок"
        else:
            return f"Ошибка! Код ошибки: {responce.status_code}"


if __name__ == "__main__":

    BASE_PATH = os.getcwd()
    FILE = "123.png"
    FULL_PATH_TOLOG = os.path.join(BASE_PATH, FILE)

    token = " "
    uploader = YaUploader(token)

    print(f"Загружаем файл  на Яндекс.Диск")
    result = uploader.upload(FILE)
    print(result)
