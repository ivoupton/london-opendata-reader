import requests
from sheet2dict import Worksheet

LONDON_PT_URL = "<URL>"
STATS_NAME = ""
API_URL = "<URL>"
public_transportation_stats = LONDON_PT_URL + "/public/data/export/csv/" + STATS_NAME

csv_export = requests.get(public_transportation_stats, timeout=10).content

ws = Worksheet()
ws_items = ws.xlsx_to_dict(path=csv_export)
ws.csv_to_dict(csv_file=csv_export, delimiter=";")
ws_items = ws.sanitize_sheet_items

for row in ws_items:
    print("STATS ROW:", row)
    try:
        response = requests.post(json=row, timeout=2)
        print("API OK", response.status_code, response.text)
    except Exception as e:
        print("API problem:", e)

