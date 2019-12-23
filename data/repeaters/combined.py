def url_dnc():
    return 'https://actionnetwork.org/api/v2/forms/439dd665-c55c-44c5-90a1-72629885ccf7/submissions'
    
def headers_dnc():
    return  {  
              'authority':'actionnetwork.org',
              'origin':'https://democrats.org',
              'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
              'dnt':'1',
              'content-type':'application/json',
              'accept':'*/*',
              'sec-fetch-site':'cross-site',
              'sec-fetch-mode':'cors',
              'referer':'https://democrats.org/',
              'accept-encoding':'gzip, deflate, br',
              'accept-language':'en-US,en;q=0.9'
              }

def payload_dnc(EMAIL,RAND_ZIP,RAND_PHONE):
    return {
                "person":{
                "email_addresses":[{"address":"%s" % EMAIL,"status":"subscribed"}],
                "postal_addresses":[{"postal_code":"%s" % RAND_ZIP}],
                "custom_fields":{
                    "Mobile Phone":"%s" % RAND_PHONE,
                    "SMS Opt-In":"1"
                    }
                },
                "triggers":{
                "autoresponse":{
                "enabled":'true',
                    }
                }
            }
