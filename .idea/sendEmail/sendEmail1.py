__author__ = 'User'

import smtplib
from email.mime.text import MIMEText
mailto_list = ['18210262865@163.com']
mail_host = 'smtp.163.com'
mail_user = '18210262865'
mail_pass = 'gao@367985'
mail_postfix = '163.com'

def send_mail(to_list,sub,content):
    me = 'hello ' + '<' + mail_user + '@' + mail_postfix + '>'
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ';'.join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me,to_list,msg.as_string())
        server.close()
        return True
    except Exception,e :
        print str(e)
        return False

if __name__ == '__main__' :
    if send_mail(mailto_list,"hello","hello world！"):
        print "发送成功"
    else:
        print "发送失败"
