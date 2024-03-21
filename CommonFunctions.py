

class CommonFunctions():
    def do_login(self,sb,url,username,password):
        sb.open(url)
        sb.type("#username", username)
        sb.click("#continue")
        sb.type("#password", password)
        sb.click("#submit")

    def do_logout(selfb,sb):
        sb.click(".right-nav-item.profile-link")
        sb.click("#basics-tab")
        sb.click("button.log-out-button")

    def do_get_active_tmpl_name(self,sb):
        sb.click(".right-nav-item.profile-link", timeout = 15)
        sb.click("#templates-tab", timeout=10)
        sb.wait_for_element_present(".v-card__title.cardTitleForViewer",timeout=15)
        name = sb.find_element(".v-card__title.cardTitleForViewer",timeout=10)
        print("Selected Template is: " + name.text)

