def ContactUs1_py():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://smartstore.alertsite.com/")
    Project.Variables.VarDataLoop.Reset()
    RecordIdx = 1
    while RecordIdx <= 4:
        #Maximizes the specified Window object.
        Aliases.browser.BrowserWindow.Maximize()
        #Clicks the 'linkContactUs' link.
        Aliases.browser.pageShop.header.nav.nav2.linkContactUs.Click()
        #Waits until the browser loads the page and is ready to accept user input.
        Aliases.browser.pageContactus.Wait()
        #Clicks the 'textboxYourName' control.
        Aliases.browser.pageContactus.sectionContent.form.textboxYourName.Click()
        #Clicks the 'textboxYourName' control.
        Aliases.browser.pageContactus.sectionContent.form.textboxYourName.Click()
        #Clicks the 'textboxYourName' control.
        Aliases.browser.pageContactus.sectionContent.form.textboxYourName.Click()
        #Sets the text KeywordTests.ContactUs1.Variables.VarDataLoop["Name"] in the 'textboxYourName' text editor.
        Aliases.browser.pageContactus.sectionContent.form.textboxYourName.SetText(Project.Variables.VarDataLoop.Value["Name"])
        #Sets the text KeywordTests.ContactUs1.Variables.VarDataLoop["Email"] in the 'textboxYourEmail' text editor.
        Aliases.browser.pageContactus.sectionContent.form.textboxYourEmail.SetText(Project.Variables.VarDataLoop.Value["Email"])
        #Clicks the 'textareaEnquiry' control.
        Aliases.browser.pageContactus.sectionContent.form.textareaEnquiry.Click()
        #Enters KeywordTests.ContactUs1.Variables.VarDataLoop["Enquiry"] in the 'textareaEnquiry' object.
        Aliases.browser.pageContactus.sectionContent.form.textareaEnquiry.Keys(Project.Variables.VarDataLoop.Value["Enquiry"])
        #Clicks the 'buttonSubmit' button.
        Aliases.browser.pageContactus.sectionContent.form.buttonSubmit.ClickButton()
        #Checks whether the 'contentText' property of the Aliases.browser.pageContactus.sectionContent.panel object equals 'Your enquiry has been successfully sent to the store owner.'.
        aqObject.CheckProperty(Aliases.browser.pageContactus.sectionContent.panel, "contentText", cmpEqual, "Your enquiry has been successfully sent to the store owner.")
        Project.Variables.VarDataLoop.Next()
        RecordIdx = RecordIdx + 1
