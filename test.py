import requests



# headers = {
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
# }

json_data = {
    'pageNo': 1,
    'pageSize': 15,
    'categoryCode': 'ZcyAnnouncement10016',
    '_t': 1763709618000,
}

response = requests.post('https://zfcg.gxzf.gov.cn/portal/category', json=json_data)
print(response.text)