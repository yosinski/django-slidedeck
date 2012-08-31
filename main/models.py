import os
from bs4 import UnicodeDammit

from django.db import models
from django.contrib import admin
from django.db.models.signals import pre_save, post_save

from util.helper import runCmd, randomString, DuckStruct
from util.storage import OverwriteStorage
import settings



class Slidedeck(models.Model):
    dateCreated    = models.DateTimeField(auto_now_add = True)
    ref            = models.CharField(max_length=32, default = lambda : randomString(6))
    order          = models.FloatField()

    title          = models.TextField(help_text = 'Unformatted')
    presenter      = models.TextField(help_text = 'Formatted')
    abstract       = models.TextField()
    
    # Uploaded
    pdf            = models.FileField(upload_to = 'slides', storage=OverwriteStorage(), blank = True)

    # Filled in automatically after upload
    slug           = models.CharField(max_length=256, blank = True)
    text           = models.TextField(blank = True, help_text = 'Automatically filled in on save.')
    pages          = models.IntegerField(default = -1,
                                         help_text = ('Automatically filled in on save. -1 if no ' +
                                                      'data exists, if > 0, implies that images have been saved.'))

    def getImageBasePath(self):
        if self.pdf is not None:
            if self.pdf.path[-4:] != '.pdf':
                raise Exception('Expected path ending in .pdf')
            return self.pdf.path[:-4]

    def getImageBaseUrl(self):
        if self.pdf is not None:
            if self.pdf.url[-4:] != '.pdf':
                raise Exception('Expected url ending in .pdf')
            return self.pdf.url[:-4]

    def getImageUrls(self, thumb = False):
        baseUrl = self.getImageBaseUrl()
        if baseUrl and self.pages > 0:
            thumbstr = '.thumb' if thumb else ''
            return ['%s_%03d%s.png' % (baseUrl, ii+1, thumbstr) for ii in xrange(self.pages)]

    def getImageThumbUrls(self):
        return self.getImageUrls(thumb = True)

    def getSlides(self):
        '''Gets a list of slide objects'''

        slideTranscriptions = self.text.strip(u'\x0c').split(u'\x0c')
        if self.pages > 0 and len(slideTranscriptions) != self.pages:
            raise Exception('Expected transcriptions of length %d but got %d' % (self.pages, len(slideTranscriptions)))

        ret = []
        for imgUrl, imgThumbUrl, slideText in zip(self.getImageUrls(), self.getImageThumbUrls(), slideTranscriptions):
            ret.append(DuckStruct(imgUrl = imgUrl,
                                  imgThumbUrl = imgThumbUrl,
                                  text = slideText))
        return ret

    def __unicode__(self):
        return 'Slidedeck(pk=%s, title=%s)' % (self.pk if self.pk is not None else 'None',
                                               repr(self.title))



def slidedeckPreSave(sender, instance, **kwargs):
    pass



def slidedeckPostSave(sender, instance, **kwargs):
    print 'slidedeckPostSave:', instance.pdf, instance.pdf.path
    print 'slidedeckPostSave:', sender
    print 'slidedeckPostSave:', instance
    print 'slidedeckPostSave:', kwargs

    if instance.pdf:
        # still need to process

        modified = False
        
        if instance.pages == -1:
            out,err = runCmd(('gs', '-q', '-dNODISPLAY', '-c',
                              '(%s) (r) file runpdfbegin pdfpagecount = quit' % instance.pdf.path))
            print 'Pages:', out
            try:
                instance.pages = int(out)
            except:
                raise Exception('expected int but got %s' % repr(out))

            print 'trying', settings.SITE_BASE_DIR + '/scripts/pdf2pngs',
            basepath = instance.getImageBasePath()
            print 'trying', settings.SITE_BASE_DIR + '/scripts/pdf2pngs',
            runCmd((settings.SITE_BASE_DIR + '/scripts/pdf2pngs',
                    instance.pdf.path,
                    basepath,
                    '2000', '400', '.thumb'), verbose = True)
            modified = True
            
        if instance.text == '':
            # extract text
            randFile = '/tmp/%s.tmp' % randomString(6)
            runCmd(('pdftotext', '-enc', 'UTF-8', instance.pdf.path, randFile))
            with open(randFile, 'r') as ff:
                uu = UnicodeDammit(ff.read())
            textUnicode = uu.unicode_markup
            instance.text = textUnicode.encode('ascii', 'ignore')
            modified = True
            print 'got text: %s...' % instance.text[:100]

        if instance.slug == '':
            instance.slug = os.path.split(instance.getImageBasePath())[-1]
            modified = True
            print 'set slug to:', instance.slug

        if modified:
            print 'saving'
            instance.save()



pre_save.connect(slidedeckPreSave,   Slidedeck, dispatch_uid = 'SlidedeckPreSave')
post_save.connect(slidedeckPostSave, Slidedeck, dispatch_uid = 'SlidedeckPostSave')

