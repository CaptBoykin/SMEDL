def url_thisistrue():
    return 'https://www.aweber.com/scripts/addlead.pl'

def headers_thisistrue():
    return {
        'Origin':'https://thisistrue.com',
        'Upgrade-Insecure-Requests':'1',
        'DNT':'1',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Sec-Fetch-User':'?1',
        'Referer':'https://thisistrue.com/'
        }

def payload_thisistrue(EMAIL):
    return {
        'meta_web_form_id':'1245921654',
        'meta_split_id':'',
        'listname':'thisistrue',
        'redirect':'https%3A%2F%2Fthisistrue.com%2Fsuccess%2F',
        'meta_redirect_onlist':'https%3A%2F%2Fthisistrue.com%2Fduplicate%2F',
        'meta_adtracking':'True+Sidebar',
        'meta_message':'1',
        'meta_required':'email',
        'meta_tooltip':'',
        'name':'asdf',
        'email':'%s' % EMAIL,
        'custom+WhereHeard':'asdf',
        'submit':'Safe+Subscribe'
        }


def url_mini_airs():
    return 'https://pairlist5.pair.net/mailman/subscribe/mini-air'

def headers_mini_airs():
    return {
        'Connection':'keep-alive',
        'Cache-Control':'max-age=0',
        'Origin':'https://www.improbable.com',
        'Upgrade-Insecure-Requests':'1',
        'DNT':'1',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Sec-Fetch-User':'?1',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site':'cross-site',
        'Sec-Fetch-Mode':'navigate',
        'Referer':'https://www.improbable.com/airchives/miniair/',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.9'
        }


def payload_mini_airs(EMAIL):
    return { 'email':'%s' % EMAIL,'email-button':'Subscribe'}

def url_lefsetz():
    return 'https://www.lefsetz.com/lists/?p=subscribe&id=1'

def headers_leftsetz():
    return {
            'authority':'www.lefsetz.com',
            'cache-control':'max-age=0',
            'origin':'https://www.lefsetz.com',
            'upgrade-insecure-requests':'1',
            'dnt':'1',
            'content-type':'application/x-www-form-urlencoded',
            'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'sec-fetch-user':'?1',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site':'same-origin',
            'sec-fetch-mode':'navigate',
            'referer':'https://www.lefsetz.com/lists/?p=subscribe&id=1',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9'
            }

def payload_lefsetz(EMAIL):
    return {
            'email':'%s' % EMAIL,
            'emailconfirm':'%s' % EMAIL,
            'htmlemail':'0',
            'list%5B2%5D':'signup',
            'listname%5B2%5D':'lefsetzletter',
            'VerificationCodeX':'',
            'subscribe':'Subscribe+to+the+LefsetzLetter'
            }

def url_wateraid(EMAIL):
    return 'https://wateraid.us19.list-manage.com/subscribe/post-json?u=223395cf5b29224c243a3e6f7&id=efddb60b77&c=jQuery19009863902272559808_1577063151402&EMAIL=%s&FNAME=asdf&MMERGE2=qwer`&PHONE[area]=987&PHONE[detail1]=654&PHONE[detail2]=3214&interestgroup_field=&gdpr[9605]=Y&b_223395cf5b29224c243a3e6f7_efddb60b77=&subscribe=Subscribe&_=1577063151403' % EMAIL

def headers_wateraid():
    return {
            'authority':'wateraid.us19.list-manage.com',
            'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'dnt':'1',
            'accept':'*/*',
            'sec-fetch-site':'cross-site',
            'sec-fetch-mode':'no-cors',
            'referer':'https://www.wateraid.org/us/join-our-mailing-list',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9'
            }


def url_smashingmag():
    return 'https://smashingmagazine.us1.list-manage.com/subscribe/post?u=16b832d9ad4b28edf261f34df&id=a1666656e0'

def headers_smashingmag():
    return {
            'authority':'smashingmagazine.us1.list-manage.com',
            'cache-control':'max-age=0',
            'origin':'https://www.smashingmagazine.com',
            'upgrade-insecure-requests':'1',
            'dnt':'1',
            'content-type':'application/x-www-form-urlencoded',
            'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'sec-fetch-user':'?1',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site':'cross-site',
            'sec-fetch-mode':'navigate',
            'referer':'https://www.smashingmagazine.com/the-smashing-newsletter/',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9'
          }

def payload_smashingmag(EMAIL):
    return {'EMAIL':'%s' % EMAIL }

def url_aimsurplus():
    return 'https://subscribe.rndpxl.net/subscribe/22ba545cdacea84d2a5b14532a196a14/c20ebca9c86089b243752b8c70bb9b41'


def headers_aimsurplus():
    return {
            'Connection':'keep-alive',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Origin':'https://aimsurplus.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'DNT':'1',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Sec-Fetch-Site':'cross-site',
            'Sec-Fetch-Mode':'cors',
            'Referer':'https://aimsurplus.com/',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-US,en;q=0.9'
            }

def payload_aimsurplus(EMAIL):
    return {'contact[name]':'Aasdf','email':'%s'%EMAIL }
    
def url_katespade(EMAIL):
    return 'https://www.katespade.com/on/demandware.store/Sites-Shop-Site/en_US/Account-EmailSignup?email=%s&source=ksny online account mailing list&email=&postal=&source=ksny+online+footer' % EMAIL

def headers_katespade():
    return {
          'authority':'www.katespade.com',
          'accept':'application/json, text/javascript, */*; q=0.01',
          'dnt':'1',
          'x-requested-with':'XMLHttpRequest',
          'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
          'sec-fetch-site':'same-origin',
          'sec-fetch-mode':'cors',
          'referer':'https://www.katespade.com/join-mailing-list.html',
          'accept-encoding':'gzip, deflate, br',
          'accept-language':'en-US,en;q=0.9'
          }
        
def url_naa():
    return 'https://nationalautismassociation.org/wp-admin/admin-ajax.php'

def headers_naa():
    return {
            'authority':'nationalautismassociation.org',
            'accept':'application/json, text/javascript, */*; q=0.01',
            'origin':'https://nationalautismassociation.org',
            'x-requested-with':'XMLHttpRequest',
            'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'dnt':'1',
            'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-fetch-site':'same-origin',
            'sec-fetch-mode':'cors',
            'referer':'https://nationalautismassociation.org/get-involved/join-our-mailing-list/',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9'
            }

def payload_naa(EMAIL):
    return {'action':'et_pb_submit_subscribe_form',
            'et_frontend_nonce':'fd8442eb6a',
            'et_list_id':'1',
            'et_firstname':'Asdf',
            'et_lastname':'Lasdf',
            'et_email':'%s'%EMAIL,
            'et_provider':'constant_contact',
            'et_account':'NAAMail',
            'et_ip_address':'true',
            'token':''
            }
            
def url_23eats():
    return 'https://www.23eats.com/join-our-mailing-list/'

def headers_23eats():
    return {
            'authority':'www.23eats.com',
            'cache-control':'max-age=0',
            'origin':'http://www.23eats.com',
            'upgrade-insecure-requests':'1',
            'dnt':'1',
            'content-type':'application/x-www-form-urlencoded',
            'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'sec-fetch-user':'?1',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site':'cross-site',
            'sec-fetch-mode':'navigate',
            'referer':'http://www.23eats.com/join-our-mailing-list/',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9'
            }


def payload_23eats(EMAIL):
    return {
            'first_name___185b795264e09a98fe0f4e47e70e8e90':'asdf',
            'last_name___7844763b59c9491b69645b716220aad7':'qwer',
            'email___ecd412e904309dcce66177488240b016':'%s' % EMAIL,
            'ctct-opt-in':'2077471341',
            'ctct_usage_field':'',
            'ctct-id':'129',
            'ctct-verify':'8IplPnpX0kM7rRguMJcBT8Zmm',
            'ctct_time':'1577063790',
            'ctct-submitted':'Join+Our+Mailing+List',
            'ctct_form':'93165b9be5',
            '_wp_http_referer':'%2Fjoin-our-mailing-list%2F',
            'ctct_must_opt_in':'yes'
            }

def url_worldcare():
    return 'https://visitor2.constantcontact.com/api/signup'

def headers_worldcare():
    return {
            'Connection':'keep-alive',
            'Accept':'*/*',
            'Origin':'https://www.worldcare.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'DNT':'1',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Sec-Fetch-Site':'cross-site',
            'Sec-Fetch-Mode':'cors',
            'Referer':'https://www.worldcare.com/join-email-list/',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-US,en;q=0.9'
            }

def payload_worldcare(EMAIL):
    return {
            'ca':'e6ac934c-b3f5-42c0-9f98-ec84e4930efd',
            'list':'1072061486',
            'source':'EFD',
            'required':'list,email,first_name,last_name,company',
            'email':'%s' % EMAIL,
            'first_name':'AAAA',
            'last_name':'LLLL',
            'company':'CCCC'
            }
