# 导入smtplib模块
import smtplib

# 从email.mime.multipart中导入MIMEMultipart类
from email.mime.multipart import MIMEMultipart

# 从email.header中导入Header类
from email.header import Header

# 从email.mime.text中导入MIMEText类
from email.mime.text import MIMEText

# 从email.mime.image中导入MIMEImage类
from email.mime.image import MIMEImage

# 连接邮箱服务器：使用smtplib模块的类SMTP_SSL，创建一个实例对象qqMail
qqMail = smtplib.SMTP_SSL("smtp.qq.com", 465)
mailUser = "smtp@qq.com"
mailPass = "授权码"
qqMail.login(mailUser, mailPass)

# 设置发件人和收件人
sender = "aLing@qq.com"
receiver = "aFei@qq.com"

# 使用类MIMEMultipart，创建一个实例对象message
message = MIMEMultipart()

# 将主题写入 message["Subject"],message["Subject"]，就是用于接收邮件的主题信息。
# 右侧使用Header类创建一个实例对象，括号内传入"团队合照"作为主题信息。
message["Subject"] = Header("团队合照")

# 将发件人信息写入 message["From"],用于接收发件人信息。
# 右侧使用Header类创建一个实例对象，括号内使用格式化的方式传入了发件人信息。
message["From"] = Header(f"aling<{sender}>")

# 将收件人信息写入 message["To"],用于接收收件人信息。
# 右侧使用Header类创建一个实例对象，括号内使用格式化的方式传入了收件人信息。
message["To"] = Header(f"阿飞<{receiver}>")

# 设置邮件的内容，赋值给变量textContent
textContent = "阿飞，这是插画同学绘制的团队合照，望查收~"

# 编辑邮件正文：使用类MIMEText，创建一个实例对象mailContent
mailContent = MIMEText(textContent, "plain", "utf-8")

# 将文件路径，赋值给filePath,获取了图片文件的路径
filePath = r"\Users\aLing\team.png"

# 使用with open() as语句以rb的方式，打开路径为filePath的图片，并赋值给imageFile;使用open()函数和with…as语句打开图片
# open(文件路径, 打开方式)
# "rb"是Read Binary的缩写，表示以二进制形式读取文件的内容。
# with open() as，先执行with后的open()函数，将open()函数的返回值，赋值给as后面的变量。
with open(filePath, "rb") as imageFile:

    # 使用read()函数读取文件内容，赋值给fileContent
    fileContent = imageFile.read()

# 设置邮件附件：使用类MIMEImage，创建一个实例对象attachment
attachment = MIMEImage(fileContent)

# 调用add_header()方法，设置附件标题
attachment.add_header("Content-Disposition", "attachment", filename="团队合照.png")

# 添加正文：调用对象message的attach()方法，传入正文对象mailContent作为参数
message.attach(mailContent)

# 添加附件：调用对象message的attach()方法，传入附件对象attachment作为参数
message.attach(attachment)

# 发送邮件：使用对象qqMail的sendmail方法发送邮件,通过对象名.方法名()的格式使用
# 使用as_string()方法将对象message变为字符串类型
qqMail.sendmail(sender, receiver, message.as_string())

# 输出"发送成功"
print("发送成功")