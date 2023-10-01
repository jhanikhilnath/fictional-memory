import requests
import argparse
import urllib.parse
import urllib3
import threading
import queue
import sys
import time


def parse_args():
    parser = argparse.ArgumentParser(description="Brute force web directories")
    parser.add_argument('-u', '--url', dest='url', help='URL to scan, will be prefixed',required=True)
    parser.add_argument('-w', '--wordlist', dest='wordlist', help='path to wordlist, one word per line', required=True)
    parser.add_argument('-p', '--proxy', dest='proxy', default=None, help='send the resource to the proxy ')
    parser.add_argument('-s', '--size', dest='size', default='2392', help='If a reply is this size, ignore it. Pass ' +'multiple values comma-separated (100,123,3123)')
    parser.add_argument('-t', '--threads', dest='threads', type=int, default=10)
    parser.add_argument('-a', '--useragent', dest='useragent', default='pybuster', help='Set User-Agent')
    parser.add_argument('-f', '--addslash', dest='addslash', default=False, action='store_true',help='append a slash to each request')
    parser.add_argument('-r', '--redirects', dest='follow', default=False, action='store_true', help='Follow redirects')
    parser.add_argument('-v', '--verbose', dest='verbose', default=False, action='store_true', help='be more verbose, not used atm.')
    return parser.parse_args()


def check_url(word_queue, args):
    while not word_queue.empty():
        try:
            word = word_queue.get_nowait()
        except queue.Empty:
            break
        url = args.url + word.lstrip('/')
        if args.addslash and not url.endswith('/'):
            url += '/'
        headers = {'User-Agent': args.useragent}
        response = requests.get(url, verify=False, allow_redirects=args.follow, headers=headers)
        if response.status_code in [200, 204, 301, 302, 307, 401, 403] and len(response.text) not in args.size:
            print(f'[{response.status_code}] {url} ({len(response.text)})')
            if args.proxy is not None:
                proxies = {'http': args.proxy, 'https': args.proxy}
                requests.get(url, verify=False, allow_redirects=args.follow, headers=headers, proxies=proxies)


def main():
    args = parse_args()
    if not args.url.endswith('/'):
        args.url = args.url + '/'

    try:
        sizelist = [int(x) for x in args.size.split(',')]
    except ValueError:
        print(f'Can not parse {args.size}.')
        sys.exit(-1)
    args.size = sizelist
    words = open(args.wordlist).readlines()
    word_queue = queue.Queue()
    for word in words:
        word_queue.put(urllib.parse.quote(word.strip()))


    threads = []
    for i in range(args.threads):
        t = threading.Thread(target=check_url, args=(word_queue, args))
        t.start()
        threads.append(t)

    while True:
        try:
            time.sleep(0.5)
            if word_queue.empty() and True not in [t.is_alive() for t in threads]:
                sys.exit(0)
        except KeyboardInterrupt:
            while not word_queue.empty():
                try:
                    word_queue.get(block=False)
                except queue.Empty:
                    pass
            sys.exit(0)


if __name__ == "__main__":
    urllib3.disable_warnings()
    main()