import mwclient
site = mwclient.Site('en.wikipedia.org')

# PLAYERSFILE = 'players.txt'
PLAYERSFILE = 'sampleplayers.txt'


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
    last, first = name.split(', ')
    return ' '.join([first, last])


def main():
    needspage = []
    disambigs = []
    hasimage = []
    needsimage = []

    with open(PLAYERSFILE) as players:
        for player in players:
            forwardname = normaliseName(player.strip())
            page = getPage(forwardname)
            if not page:
                needspage.append(forwardname)
                continue

            if isDisambiguation(page):
                # TODO try to get the right page from here!
                disambigs.append(name(page))
            elif hasImage(page):
                hasimage.append(name(page))
            else:
                needsimage.append(name(page))
            
    print("Has image:", hasimage)
    print("Disambig:", disambigs)
    print("Needs image:", needsimage)
    print("No page:", needspage)


if __name__ == "__main__":
    main()
