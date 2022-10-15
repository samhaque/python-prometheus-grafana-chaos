import random
import re
import time
import httpx
import prometheus_client
from bs4 import BeautifulSoup
from flask import Response, Flask
from prometheus_client import Summary, Counter, Histogram, Info

app = Flask(__name__)

_INF = float("inf")
graphs = {'c': Counter('python_request_operations_total', 'The total number of processed requests'),
          'h': Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.',
                         buckets=(1, 2, 5, 6, 10, _INF)),
          's': Summary('python_request_processing_seconds', 'Time spent processing request'),
          'info': Info('my_build_version', 'Description of info')}


@app.route("/", methods=['GET'])
def get_prime_mortgage_rate():
    # start the clock
    start = time.time()
    graphs['c'].inc()
    # simple http GET call to fetch the RBC Prime Rate
    r = httpx.get('https://www.rbcroyalbank.com/mortgages/mortgage-rates.html')
    # Parse the rate from the HTML
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find('table', attrs={'id': 'collapsible-swipe-table9'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    extracted_percentage = re.findall('\\d*\\.?\\d+', rows[0].text)[0]
    # time how long it took to parse the info
    # to demonstrate variability in transaction speeds in demo we will randomly sleep
    time.sleep(random.uniform(0, 1))
    end = time.time()
    # feed the stats to our graphs so that prometheus can consume the metrics
    graphs['s'].observe(end - start)
    graphs['h'].observe(end - start)
    # return today's RBC prime rate
    return Response(f"RBC Prime Rate: {extracted_percentage}%", mimetype="text/plain")


@app.route("/metrics")
def requests_count():
    res = []
    # structure our graph data using the prometheus client in a format that prometheus understands
    for k, v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
