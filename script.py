import mwclient
site = mwclient.Site('en.wikipedia.org')

PLAYERSFILE = 'players.txt'
#PLAYERSFILE = 'sampleplayers.txt'
DISAMBIGS = 'disambigs.txt'
NEEDSPAGE = 'needspage.txt'
NEEDSIMAGE = 'needsimage.txt'


def name(page):
    # We should only have objects that have a .name,
    # but this seems broken on python3
    # https://github.com/mwclient/mwclient/issues/106
    try:
        return page['title']
    except TypeError:
        # cool, we actually have a Page
        return page.name


def isBoring(imagename):
    # Flags, Increase2.svg, Decrease2.svg
    return imagename.endswith('.svg')


def hasImage(page):
    # TODO: Does this page exist in other languages?
    # Do any of them have an image?
    images = page.images()
    imgnames = [name(image) for image in images]
    interestingImages = [imgname for imgname in imgnames
                         if not isBoring(imgname)]
    return bool(interestingImages)


def isDisambiguation(page):
    cats = page.categories()
    disambigCat = 'Category:All disambiguation pages'
    return disambigCat in [name(cat) for cat in cats]


def getPage(name):
    page = site.Pages[name].resolve_redirect()
    if not page.exists:
        return
    return page


def normaliseName(name):
    last, first = name.strip().split(', ')
    return ' '.join([first, last])


def main():
    hasimage = []

    with open(PLAYERSFILE) as players, open(DISAMBIGS, 'w') as disambigs, open(NEEDSPAGE, 'w') as needspage, open(NEEDSIMAGE, 'w') as needsimage:
        for player in players:
            print(".", end='', flush=True)
            forwardname = normaliseName(player)
            page = getPage(forwardname)
            if not page:
                print(forwardname, file=needspage)
                continue

            if isDisambiguation(page):
                # TODO try to get the right page from here!
                print(name(page), file=disambigs)
            elif hasImage(page):
                hasimage.append(name(page))
            else:
                print(name(page), file=needsimage)
            
    print("\nHas image:", len(hasimage))
    print("See {}, {} and {} for further work!".format(DISAMBIGS, NEEDSPAGE, NEEDSIMAGE))


if __name__ == "__main__":
    main()
