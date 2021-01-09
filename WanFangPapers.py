# -*- coding:utf-8 -*-

from pymongo import *
from datetime import datetime
import json


class WanFangPaperDAO(object):
    def __init__(self):
        self.host = '10.214.199.159'
        self.port = 27017
        # 创建mongodb客户端
        self.client = MongoClient(self.host, self.port)
        # 创建数据库
        self.db = self.client.data
        # 创建集合
        now = datetime.now().year
        _set = "wanfang" + str(now) + "_papers"
        self.collection = self.db[_set]

    # 判断paper的年份是哪一年
    def judge_year(self, _dict):
        now = datetime.now().year
        for i in range(2019, now):
            if _dict["year"] == str(i):
                _set = "wanfang" + str(i) + "_papers"
                self.collection = self.db[_set]
                break

    # 写入数据库
    def insert(self, _dict):
        self.judge_year(_dict)
        try:
            self.collection.update_one({'_id': _dict["id"]}, {'$set': _dict}, upsert=True)
            print('写入成功')
        except Exception as e:
            print(e)

    # 根据_id查找paper是否在数据库里
    def find(self, _id):
        now = datetime.now().year
        _set = "wanfang" + str(now) + "_papers"
        self.collection = self.db[_set]
        try:
            result = self.collection.find_one({"_id": _id})
            if result is None:
                print("Not Found.")
            else:
                print("The paper already exists.")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    wfpaper = WanFangPaperDAO()
    _dict = {"org": "\u5317\u4eac\u5927\u5b66", "year": "2018", "download_timeout": 180.0, "depth": 1, "page": 1,
              "resource_type": "\u671f\u520a\u8bba\u6587", "num_of_cited": "77", "num_of_download": "10", "title":
                  "\u8bba\u68c0\u5bdf\u673a\u5173\u7684\u6cd5\u5f8b\u804c\u80fd", "title_en":
                  "The Legal Function of the Prosecution", "download_url": "",
              "summary": "\u53f8\u6cd5\u6539\u9769\u7684\u6df1\u5165\u63a8\u8fdb,\u4f7f\u68c0\u5bdf\u5236\u5ea6\u9762\u4e34\u4e25\u5cfb\u7684\u6311\u6218,\u540c\u65f6\u4e5f\u7ed9\u68c0\u5bdf\u673a\u5173\u5e26\u6765\u4e86\u65b0\u7684\u673a\u9047.\u4f5c\u4e3a\u56fd\u5bb6\u5229\u76ca\u548c\u793e\u4f1a\u516c\u5171\u5229\u76ca\u7684\u4ee3\u8868,\u68c0\u5bdf\u673a\u5173\u901a\u8fc7\u884c\u4f7f\u8bc9\u8bbc\u804c\u80fd\u548c\u76d1\u7763\u804c\u80fd,\u6765\u7ef4\u62a4\u56fd\u5bb6\u6cd5\u5f8b\u7684\u7edf\u4e00\u5b9e\u65bd.\u5728\u8fd9\u4e24\u9879\u804c\u80fd\u53d1\u751f\u5206\u79bb\u7684\u60c5\u51b5\u4e0b,\u68c0\u5bdf\u673a\u5173\u7684\u8bc9\u8bbc\u804c\u80fd\u4e3b\u8981\u4f53\u73b0\u5728\u63d0\u8d77\u5211\u4e8b\u516c\u8bc9\u548c\u63d0\u8d77\u516c\u76ca\u8bc9\u8bbc\u8fd9\u4e24\u4e2a\u65b9\u9762,\u5176\u76d1\u7763\u804c\u80fd\u5219\u4e0d\u518d\u5305\u62ec\u4f20\u7edf\u610f\u4e49\u4e0a\u7684\u201c\u5211\u4e8b\u6cd5\u5f8b\u76d1\u7763\u6743\u201d,\u800c\u4e3b\u8981\u4fdd\u7559\u4e86\u201c\u884c\u653f\u76d1\u7763\u201d\u4e0e\u201c\u8bc9\u8bbc\u76d1\u7763\u201d\u8fd9\u4e24\u79cd\u5f62\u6001.\u5728\u884c\u4f7f\u8bc9\u8bbc\u804c\u80fd\u548c\u76d1\u7763\u804c\u80fd\u4e4b\u4f59,\u68c0\u5bdf\u673a\u5173\u8fd8\u4fdd\u7559\u4e86\u53f8\u6cd5\u5ba1\u67e5\u804c\u80fd,\u4e5f\u5c31\u662f\u4ee3\u8868\u56fd\u5bb6\u548c\u793e\u4f1a\u5bf9\u4fa6\u67e5\u673a\u5173\u7684\u5f3a\u5236\u63aa\u65bd\u548c\u5f3a\u5236\u6027\u5904\u5206\u884c\u4e3a\u8fdb\u884c\u5408\u6cd5\u6027\u5ba1\u67e5\u7684\u6743\u529b.\u76ee\u524d,\u8fd9\u79cd\u804c\u80fd\u5df2\u7ecf\u9010\u6e10\u671d\u53f8\u6cd5\u5316\u65b9\u5411\u53d1\u5c55,\u4f46\u4ecd\u7136\u6709\u8f83\u5927\u7684\u53d1\u5c55\u7a7a\u95f4.", "doi": "http://dx.chinadoi.cn/10.3969/j.issn.1000-0208.2018.01.001", "keywords": ["\u68c0\u5bdf\u76d1\u7763", "\u63d0\u8d77\u516c\u5171\u8bc9\u8bbc", "\u884c\u653f\u76d1\u7763", "\u8bc9\u8bbc\u76d1\u7763", "\u53f8\u6cd5\u5ba1\u67e5"], "keywords_en": [], "authors": ["\u9648\u745e\u534e"],
              "authors_link": ["http://trend.wanfangdata.com.cn/scholarsBootPage/toIndex.do?scholarName=%E9%99%88%E7%91%9E%E5%8D%8E&unitName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6"], "authors_en": ["Chen Ruihua"], "organizations": ["\u5317\u4eac\u5927\u5b66"], "journal": "\u653f\u6cd5\u8bba\u575b", "journal_link": "http://www.wanfangdata.com.cn/perio/detail.do?perio_id=zflt-zgzfdxxb&perio_title=%E6%94%BF%E6%B3%95%E8%AE%BA%E5%9D%9B", "journal_en": "Tribune of Political Science and Law", "journal_year": "2018", "journal_volume": ["36", ""], "journal_issue": "1", "journal_column": "\u4e3b\u9898\u63a2\u8ba8", "class_code": ["D92", "DF8"], "fund_list": "", "publish_date_online": "", "num_of_pages": "15", "page_num": "3-17", "reference_list": ["5675b7fead3e54b434eb5f67c2edf5f5", "399b0c08594d5a8a27f31511d3b9dc4f", "59c2481d025eed8a43b4216ded3adc29", "1d69f5f2c24746a3078086b3212fd1c5", "5e15d904615c56938775e24fcaae73d9", "a7c61a0387d2bfa969c25eb275f08ebb", "7c494bec657a89e51e2a8ba64156bb98", "8544a58f38e551cf624d373e1e41bcf3", "a194174410ea7d61b77c87c9148dcd12"], "cite_list": ["59cae7b500df9857883a846554acc71d", "1165228bada4811e225d8faa4a825fc6", "c6ac56c9957ee8f4523388141aa11cc0", "529120276d7dcfb91cade1dfcb9a7ed5", "35154e44e79c6359d31ad0f5a986349f", "9fab758a0087644adda22648b41473b7", "0caf2c6134f3df87197723149e87d004", "325ae3f6c747bfa0034a529f4da2528e", "3f5d40b7542e32d89fcb706a244391ea", "35e536fea113e8aa46db9aacbf0a977f"], "id": "1"}
    #wfpaper.insert(_dict)
    wfpaper.find("2")