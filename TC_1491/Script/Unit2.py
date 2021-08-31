

def Test1():
    #Clicks the 'BrowserWindow' object.
    Aliases.browser.BrowserWindow.Click(1901, 61)
    #Simulates one or several keypresses.
    Aliases.browser.pageNewtab.Keys("Ctrl+p")

def GiftCard():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://smartstore.alertsite.com/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'imageGiftCardsPngSize250' control.
    Aliases.browser.pageShop.sectionContent.article2.linkGiftCards.imageGiftCardsPngSize250.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageGiftCards.sectionContent.textnode5000ExclTax object equals '$5.00 excl tax'.
    aqObject.CheckProperty(Aliases.browser.pageGiftCards.sectionContent.textnode5000ExclTax, "contentText", cmpEqual, "$5.00 excl tax")
    #Closes the 'BrowserWindow' window.
    Aliases.browser.BrowserWindow.Close()
