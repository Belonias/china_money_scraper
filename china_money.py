import argparse
import sys
import requests
import os
import datetime
import csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-output_folder', '--of', type=str,
                        help='output folder selection', required=True)
    args = parser.parse_args()
    print('This is the input argument ' + args.of)

    now = datetime.datetime.now()
    # original job_execution_time = now.strftime("%Y-%m-%d %H:%M:%S")
    job_execution_time = now.strftime("%Y/%m/%d/%H%M%S")
    file_path = args.of + '/' + job_execution_time + '/'

    print('This is the file path ' + file_path)

    try:
        directory = os.path.dirname(file_path)
        os.makedirs(directory)
    except OSError:
        print('OSError')

    url = 'http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/ccpr.json'
    print('The urls is ', url)

    r = requests.get(url)
    data = r.json()
    print(len(data['records']))

    if len(data['records']) == 24:
        print('comple')
    else:
        print('System.exit[0]')

    for i in data['records']:
        print(i['vrtEName'], i['price'], i['bpDouble'])

    with open(file_path + 'table.csv', 'w+', newline='') as csvfile:
        row_writer = csv.writer(csvfile, delimiter=',')
        row_writer.writerow(['currency', 'rate', 'change'])
        for i in data['records']:
            row_writer.writerow([i['vrtEName'], i['price'], i['bpDouble']])
        csvfile.close()
        print('The file table.csv created')


if __name__ == '__main__':
    main()
