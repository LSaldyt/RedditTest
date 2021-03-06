#!/usr/bin/env python3

from fetch        import fetch_reddit, fetch_gutenberg, fetch_google, fetch_wikipedia
from multiprocess import Pool, TimeoutError
    #fetch_google({'https://en.wikipedia.org/wiki/Spider'})
    #fetch_wikipedia({'spiders'})

if __name__ == '__main__':
    pool    = Pool(processes=4)
    futures = []
    def launch(f, args=()):
        futures.append(pool.apply_async(f, args))
        print('Launched %s' % f.__name__)
    launch(fetch_google, ({'https://en.wikipedia.org/wiki/Spider'}, '../log/google'))
    launch(fetch_reddit, ('../log/reddit'))
    launch(fetch_wikipedia, ({'spiders'}, '../log/wiki'))
    launch(fetch_gutenberg, ('../log/guten'))
    
    for future in futures:
        future.get()


