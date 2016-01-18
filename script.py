import mwclient
site = mwclient.Site('en.wikipedia.org')

# PLAYERSFILE = 'players.txt'
PLAYERSFILE = 'sampleplayers.txt'


def isBoring(imagename):
    # Flags, Increase2.svg, Decrease2.svg
    return imagename.endswith('.svg')


def hasImage(page):
    # TODO: Does this page exist in other languages?
    # Do any of them have an image?
    images = page.images()
    imgnames = [image.name for image in images]
    interestingImages = [imgname for imgname in imgnames
                         if not isBoring(imgname)]
    return bool(interestingImages)


def isDisambiguation(page):
    cats = page.categories()
    disambigCat = u'Category:All disambiguation pages'
    return disambigCat in [cat.name for cat in cats]


def getPage(name):
    page = site.Pages[name].resolve_redirect()
    if not page.exists:
        return
    return page


def normaliseName(name):
    last, first = name.split(', ')
    return ' '.join([first, last])


def main():
    needspage = []
    disambigs = []
    hasimage = []
    needsimage = []

    with open(PLAYERSFILE) as players:
        for player in players:
            name = normaliseName(player.strip())
            page = getPage(name)
            if not page:
                needspage.append(name)
                continue

            if isDisambiguation(page):
                # TODO try to get the right page from here!
                disambigs.append(name)
            elif hasImage(page):
                hasimage.append(name)
            else:
                needsimage.append(name)
            
    print "Has image:", hasimage
    print "Disambig:", disambigs
    print "Needs image:", needsimage
    print "No page:", needspage


if __name__ == "__main__":
    main()
