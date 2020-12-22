#! /usr/bin/env python

import sys
import urllib.request, urllib.error, urllib.parse



pdfs = [
    #['http://stat.wharton.upenn.edu/~rakhlin/ml_summer_school.pdf', 'Rakhlin-Statistical-Learning-Theory'],
    #['https://www.dropbox.com/s/qxedx9oj37gyjgf/srl-mlss.pdf', 'Domingos-Statistical-Relational-Learning'],
    ['https://dl.dropbox.com/s/qxedx9oj37gyjgf/srl-mlss.pdf?dl=1', 'Domingos-Statistical-Relational-Learning'],
    #['https://dl.dropbox.com/u/11277113/mlss_tsuda_mining_chapter1.pdf', 'Tsuda-Graph-Mining1'],
    #['https://dl.dropbox.com/u/11277113/mlss_tsuda_learning_chapter2.pdf', 'Tsuda-Graph-Mining2'],
    #['https://dl.dropbox.com/u/11277113/mlss_tsuda_kernel_chapter3.pdf', 'Tsuda-Graph-Mining3'],
    ['http://www.ee.ucla.edu/~vandenbe/shortcourses/mlss12-convexopt.pdf', 'Vandenberghe-Convex-Optimization'],
    ['https://www.dropbox.com/s/g3ycjuiybbiwzib/Kyoto-muller-bbci_12.pdf', 'Muller-Brain-Computer-Interfacing'],
    ['http://www.cs.princeton.edu/~schapire/talks/mlss12.pdf', 'Schapire-Theory-and-Applications-of-Boosting'],
    ['http://www.csie.ntu.edu.tw/~cjlin/talks/mlss_kyoto.pdf', 'Lin-Machine-Learning-Software'],
    #['', ''],
    #['', ''],
    ]



def main():
    for pdfUrl, pdfBaseName in pdfs:
        pdfFilename = 'MLSS-2012-%s.pdf' % pdfBaseName

        print('Fetching %s to %s...' % (pdfUrl, pdfFilename), end=' ')
        sys.stdout.flush()
        with open(pdfFilename, 'w') as ff:
            page = urllib.request.urlopen(pdfUrl)
            ff.write(page.read())
        print('done.')



main()

