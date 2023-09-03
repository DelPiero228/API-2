import requests
import json
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = file_path
        headers = {"Content-Type": "application/json", "Authorization": "OAuth {}".format(self.token)}
        params = {"path": f"Загрузки/{file_name}", "overwrite": "true"}
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

    f_name = "123.png"

    path_to_file = os.path.join(os.getcwd(), f_name)

    token = " "
    uploader = YaUploader(token)

    print(f"Загружаем файл {path_to_file} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)
