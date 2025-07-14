import requests

api_key = "M1XbCrQnV47mHjZcYnpsUBOFPvDFo/PJhrSaPRNlJb4MYO0gWTQamNFIw6zn7KLCo5e4xx7aTm5dbDhSxFBJS64Qd34M8gn0/78uGxilK4Rg4MVNLVO62u18ElX59BSJJ1Pcfyar2N5TqrQMEypEOQ=="

url = "https://apihub.document360.io/v2/Drive/Folders"

headers = {
    "api_token": api_key,
}

# Task 1: GET folders
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("Drive Folders Retrieved Successfully:")
        #print(data)
        folders = data.get('data') or data.get('folders') or data
        if isinstance(folders, list):
            for folder in folders:
                print(f"Folder Name: {folder.get('title')}")
                print(f"Folder ID: {folder.get('id')}")
        else:
            print("No folder list found in response.")
    else:
        print(f"Failed to fetch folders. Status Code: {response.status_code}")
        print(response.text)
except Exception as e:
    print("Error occurred:", str(e))


# Task 2: POST create folder
headers["Content-Type"] = "application/json"
payload_create = {
    "title": "Demo_Folder_Python",
    "parentFolderId": None,
    "userId": "223e32e4-7a9f-4a69-ba9a-5f201c00dbda"
}

try:
    response = requests.post(url, headers=headers, json=payload_create)
    if response.status_code == 201:
        data = response.json()
        folder_id = data.get('id')
        print(f"Folder Created: {data.get('title')} with ID {folder_id}")
    else:
        print(f"Failed to create folder. Status Code: {response.status_code}")
        print(response.text)
        exit()
except Exception as e:
    print("Error occurred:", str(e))


# Task 3: PUT update folder name
url_update = f"https://apihub.document360.io/v2/Drive/Folders/{folder_id}"
payload_update = {
    "title": "Updated_Demo_Folder"
}

try:
    response = requests.put(url_update, headers=headers, json=payload_update)
    if response.status_code == 200:
        data = response.json()
        print(f"Folder Updated Successfully to '{data.get('title')}'")
    else:
        print(f"Failed to update folder. Status Code: {response.status_code}")
        print(response.text)
except Exception as e:
    print("Error occurred:", str(e))


# Task 4: DELETE folder
url_delete = f"https://apihub.document360.io/v2/Drive/Folders/{folder_id}"

try:
    response = requests.delete(url_delete, headers=headers)
    if response.status_code == 204:
        print("Folder Deleted Successfully.")
    else:
        print(f"Failed to delete folder. Status Code: {response.status_code}")
        print(response.text)
except Exception as e:
    print("Error occurred:", str(e))
