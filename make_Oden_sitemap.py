
import re
import requests

target_url = 'https://researchdata.se/en/catalogue/collection/icebreaker-oden'
output_file = 'sitemap.xml'

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

try:
   with requests.get(target_url, headers=headers, timeout=5) as f:
      s = f.text
except Exception as err:
   print(f"Unexpected {err=}, {type(err)=}")
   raise

regex = '/en/catalogue/dataset/[^"]*'
match = re.findall(regex, s)

header = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xsi="http://www.w3.org/2001/XMLSchema-instance" schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
'''

footer = '''</urlset>
'''

print("Writing to file " + output_file)

with open(output_file, 'w', encoding='utf-8') as f_out:
  f_out.write(header)
  for m in match:
    f_out.write('<url><loc>'+'https://researchdata.se'+m+'</loc></url>'+ '\n')
  f_out.write(footer)
