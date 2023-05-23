import requests

url = "http://localhost:8000/get_mask"

data = {
    "prompt" : [500, 475],
    "prompt_label" : 1,
    "img_path" : 'images/dog.jpg'
}
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    mask = result["mask"]
    print("mask & score: ", mask )
else:
    print("Error:", response.status_code)
