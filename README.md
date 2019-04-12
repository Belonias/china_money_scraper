# china_money_scraper
A web scraper using json response to scrape http://www.chinamoney.com.cn/english/

## Workflow

The workflow of the [script](china_money.py) is simple and straightforward

1. Get's the date and time of the execution
2. Check if there is a file with the same datetime execution
3. If not create the file
4. With request module we "open" the url
5. We get the json data
6. Store it to a csv a file
