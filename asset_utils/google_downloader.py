import sys
import requests
import json

class CloudUtils:
    def download_file_from_google_drive(self, id, destination):
        URL = "https://docs.google.com/uc?export=download&confirm=1"

        session = requests.Session()

        response = session.get(URL, params={"id": id}, stream=True)
        token = self.get_confirm_token(response)

        if token:
            params = {"id": id, "confirm": token}
            response = session.get(URL, params=params, stream=True)

        self.save_response_content(response, destination)


    def get_confirm_token(self, response):
        for key, value in response.cookies.items():
            if key.startswith("download_warning"):
                return value

        return None


    def save_response_content(self, response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)


    def download(self, file_id, dest ):
        if len(sys.argv) >= 3:
            file_id = sys.argv[1]
            destination = sys.argv[2]
        else:
            file_id = file_id
            destination = dest
        print(f"dowload {file_id} to {destination}")
        self.download_file_from_google_drive(file_id, destination)


if __name__ == "__main__":

    with open("asset_info.json","r") as file:
        data = json.load(file)

    #file_id = data["asset1"]["link"]
    dest = "/Users/felipepesantez/Library/Mobile Documents/com~apple~CloudDocs/Documents/development/python/dev/production_assets"
    e1 = CloudUtils()

    for asset in data.values():
        e1.download(asset["link"], dest + "/{}".format(asset["name"]) + ".abc")


    #e1.download(file_id, dest)


