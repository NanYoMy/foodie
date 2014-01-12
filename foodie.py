__author__ = 'NanYoMy'
import urllib,urllib2,cookielib,re
#create a opener
def createCookieOpener():
    #the http post data
    #build a cookie opener for meituan.com
    MTcookie = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(MTcookie)
    return opener

def login(phoneNumber,password):

    post_data={
        "email": phoneNumber,
        "password": password,
        "remember_username":"1"
    }

    #send the login info
    request=urllib2.Request("https://passport.meituan.com/account/login",urllib.urlencode(post_data))
    opener = createCookieOpener()
    html=opener.open(request).read()
    #write for test the loging method
    #fp=open("meituan.html",'w')
    #fp.write(html)
    #print html
    return opener

def order(id,opener):
    #quantity-8824672=1&dealid%5B%5D=8824672&cardcode=&mobile=158****3952
    #http://xa.meituan.com/deal/buy/8824672

    requestURL="http://xa.meituan.com/deal/buy/"+id
    #it must access this url first
    request=urllib2.Request(requestURL)
    opener.open(request)
    #fp=open("result.html",'w')
    #fp.write(html)

    quantityIDName="quantity-"+id
    post_data={
        quantityIDName:2,
        "dealid[]": id,
        "cardcode":"",
        "mobile":"158****3952"
    }
    request=urllib2.Request(requestURL,urllib.urlencode(post_data))
    opener.open(request)
    '''
    fp=open("result2.html",'w')
    fp.write(html)
    '''

def main():
    '''
    @phoneNumber:type your id
    @password:type your password
    '''
    phoneNumber="*****@**.**"
    password="******"
    opener=login(phoneNumber,password)
    #8824672
    #6700604
    i=2
    while i:
        i=i-1
        print "order: "+str(i)
        order("8824672",opener)
main()

