#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkimageenhan.request.v20190930.AssessExposureRequest import AssessExposureRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = AssessExposureRequest()

request.set_accept_format('json')

request.set_ImageURL("http://viapi-test.oss-cn-shanghai.aliyuncs.com/sanjiye-meizi/4%E6%9C%88%E6%96%B0%E5%A2%9E/%E6%9B%9D%E5%85%89%E5%BA%A6.jpg")

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))