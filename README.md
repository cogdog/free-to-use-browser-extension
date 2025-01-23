# Free to Use Browser Extension

![Library of Congress Labs Free to Use Browser Extension](https://code.cog.dog/shared/free-to-use.jpg "Library of Congress Labs Free to Use Browser Extension")

This is a slightly updated version of [the extension created at the Library of Congress](https://labs.loc.gov/work/experiments/free-to-use-browser-extension/) that displays a random public domain image from the Library of Congress every time you open a new browser tab/window.

I just love this tool and over the years have made minor changes to one file to keep it working. This repo is just to make my working version available to anyone else.

The original version was created in 2018 by Flynn Shannon-- see his blog post [Explore Historical Images through the Library of Congress Free to Use Browser Extension](https://blogs.loc.gov/thesignal/2018/08/explore-historical-images-through-the-library-of-congress-free-to-use-browser-extension/).

## Blogged
* [Instead of Nothingness, Every New Open Tab Becomes a Public Domain Image Doorway of Curiosity](https://cogdogblog.com/2018/09/instead-of-nothingness/) (Sep 18 2018)
* [Public Domain as the Opener of Glorious Rabbit Holes](https://cogdogblog.com/2021/01/opener-of-rabbit-holes/) (Jan 4 2021)
* [Knitting a Quick Fix for the Free to Use Browser Extension](https://cogdogblog.com/2023/01/knitting-quick-fix/) (Jan 11 2023)
* [Weil & Braun (& CogDog) Trick: Fixing Tech I Don’t Understand](https://cogdogblog.com/2023/11/weil-braun-cogdog-trick/) (Nov 23, 2023)


## How to Install 

1. Download [this repo as a zip file](https://github.com/cogdog/free-to-use-browser-extension/archive/refs/heads/master.zip) and open it.
2. In Chrome, enter chrome://extensions into the search bar.
3. Turn on developer mode.
4. Click 'Load unpacked extension'.
5. Select the folder created when you opened the zip file.
6. Open those tabs! (load time can sometimes be slow)
7. Don't forget to turn off developer mode!


## My Work Flow
If an image catches my eye, these are my steps for going from the image in my browser tab to ultimately find them in the [Flickr Commons](https://flickr.com/commons) (I can do more with Flickr, like use my [Flickr CC Attribution Helper](https://code.cog.dog/flickr-cc-helper/), plus see informative comments)

This requires use of a [browser bookmarklet](https://en.wikipedia.org/wiki/Bookmarklet) that searches flickr commons for any selected or entered text.

1. Drag this link for [Flickr Commons](javascript:(function() %7Bs%3Dwindow.getSelection()%2B%27%27%3Bif(!s) s%3Dprompt(%27Search Flickr Commons public domain licensed Images for...%27,%27%27)%3B if (s) w%3Dwindow.open(%27https://www.flickr.com/search/%3Fw%3Dcommons%26q%3D%27%2BencodeURIComponent(s))%3B%7D)()) to your browser's bookmarks bar
2. When you find an image that shows up with Free to Use Extension, hover over the image, and click it's title in the bottom left.
3. This opens up the record in the Library of Congress. This maybe be fine for mos people, but I go further.
4. Select the key name of people or places in the title.
5. Click the Flickr Commons bookmarklet
6. The search results may include one image or several, but most likely you will find the same image.

Go from there.


## Updates
* v 1.2 delete browser_action{} from manifest.json
* v 1.1 bumped manifest version in manifest.json from 2 to 3
* v 1.0 original version from Library of Congress

## Original READme from version 1.0

This extension is meant to encourage interaction with the Library of Congress collections of images that are free to use and reuse by the public.

The Library of Congress Free to Use extension provides a way to explore historic images from digital collections that are free to use and reuse. The images displayed are either in the public domain, have no known copyright, or have been cleared by the copyright owner for public use. This is just a small sample of the Library of Congress digital collections that are free to use and reuse. The digital collections comprise millions of items including books, newspapers, manuscripts, prints and photos, maps, musical scores, films, sound recordings and more. Explore away!

The extension works by overriding the default new tab used by Chrome and replacing it with [newtab.html](newtab.html). The file [client.js](client.js) reads a JSON file in an Amazon Web Services S3 Bucket. A local copy of this file can be found [here](pythonEnv/local.json). More information about how the JavaScript works can be found [here](jsExplained.md). The JSON file was written using a few Python scripts. They are explained [here](pyExplained.md)

This extension makes use of a [Python implementation of the Flickr API](https://github.com/alexis-mignon/python-flickr-api), as well as the [Library's own API](https://github.com/LibraryOfCongress/data-exploration), to display just a small number of [over one million photos](https://www.loc.gov/search/?fa=online-format:image%7Caccess-restricted:false) that the Library has made available online, and a [Bootstrap template](https://startbootstrap.com/template-overviews/the-big-picture/).

To install this extension on your machine,
1. Download and open the zip file (remember where you opened it)
1. Enter [chrome://extensions](chrome://extensions) into the search bar
1. Turn developer mode on
1. Click "load unpacked"
1. Select the folder created when you opened the zip file

Originally created August 1, 2018

Created by [Flynn Shannon](https://github.com/flynnshannon), Junior Fellow, Library of Congress.

