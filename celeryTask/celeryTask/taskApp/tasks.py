from celery import shared_task
import requests, json
from bs4 import BeautifulSoup
from .models import Proxy

@shared_task
def scrape_proxy_data():
    url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        json_data = json.loads(text)
        proxies = json_data.get("data",[])
        for proxy in proxies:  # skipping header row
            ip = proxy.get("ip")
            port = proxy.get("port")
            protocol = proxy.get("protocols")
            country = proxy.get("country")
            uptime = proxy.get("upTime")
            Proxy.objects.create(ip=ip, port=port, protocol=protocol, country=country, uptime=uptime)
