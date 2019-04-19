from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from upload import models
import os
import json
import pandas as pd

class Data_Upload(View):
    """数据上传模块"""

    def leix_kc_splr(self, file_obj):
        """处理库存商品利润的模板"""
        df = pd.read_excel(file_obj)
        # # 遍历所有列名，排除不需要的
        cols = [i for i in df.columns if i not in ['单位', '订单标记']]
        df1 = df[cols]
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['cksj'] = df2.iloc[n][0]
            res_data['zfrq'] = df2.iloc[n][1]
            res_data['khmc'] = df2.iloc[n][2]
            res_data['spbm'] = df2.iloc[n][3]
            res_data['leibie'] = df2.iloc[n][4]
            res_data['pinpai'] = df2.iloc[n][5]
            res_data['guige'] = df2.iloc[n][6]
            res_data['xilie'] = df2.iloc[n][7]
            res_data['xh'] = df2.iloc[n][8]
            res_data['spmc'] = df2.iloc[n][9]
            res_data['xz'] = df2.iloc[n][10]
            res_data['leixing'] = df2.iloc[n][11]
            res_data['danhao'] = df2.iloc[n][12]
            res_data['wddh'] = df2.iloc[n][13]
            res_data['hyh'] = df2.iloc[n][14]
            res_data['daofu'] = df2.iloc[n][15]
            res_data['zhiyuan'] = df2.iloc[n][16]
            res_data['sl'] = df2.iloc[n][17]
            res_data['xsdj'] = df2.iloc[n][18]
            res_data['yjcbdj'] = df2.iloc[n][19]
            res_data['xsje'] = df2.iloc[n][20]
            res_data['spzk'] = df2.iloc[n][21]
            res_data['yjzcb'] = df2.iloc[n][22]
            res_data['yjml_hyf'] = df2.iloc[n][23]
            res_data['cgcb'] = df2.iloc[n][24]
            res_data['piao'] = df2.iloc[n][25]
            res_data['zhcb'] = df2.iloc[n][26]
            res_data['cbje'] = df2.iloc[n][27]
            res_data['mll'] = df2.iloc[n][28]
            res_data['zhlr'] = df2.iloc[n][29]
            res_data['zhlrl'] = df2.iloc[n][30]
            res_data['yfcb'] = df2.iloc[n][31]
            res_data['ptfy'] = df2.iloc[n][32]
            res_data['fxfy'] = df2.iloc[n][33]
            res_data['qtfy'] = df2.iloc[n][34]
            res_data['yjml'] = df2.iloc[n][35]
            res_data['yjmll'] = df2.iloc[n][36]
            res_data['yjjlr'] = df2.iloc[n][37]
            res_data['yjjlrl'] = df2.iloc[n][38]
            res_data['pdsj'] = df2.iloc[n][39]
            res_data['bumen'] = df2.iloc[n][40]

            # print(res_data)
            models.Kc_Erp_splr.objects.create(**res_data)

            # break

    def leix_kc_kccx(self, file_obj):
        """处理库存/库存查询的模板"""
        df = pd.read_excel(file_obj)
        # # 遍历所有列名，排除不需要的
        cols = [i for i in df.columns if i not in ['分库数', '调拨', '拆装', '来源', '单位', '供货商 ']]
        df1 = df[cols]
        df2 = df1.fillna(0)

        riqi = file_obj.name[4:12]
        rq = riqi[:4]+'-'+riqi[4:6]+'-'+riqi[6:8]


        res_data = {}
        for n in range(df2.shape[0]):
            res_data['riqi']=rq
            res_data['spbm']=df2.iloc[n][0]
            res_data['leibie']=df2.iloc[n][1]
            res_data['pinpai']=df2.iloc[n][2]
            res_data['spmc']=df2.iloc[n][3]
            res_data['zsl']=df2.iloc[n][4]
            res_data['kxs']=df2.iloc[n][5]
            res_data['djcb']=df2.iloc[n][6]
            res_data['je']=df2.iloc[n][7]
            res_data['cwkc']=df2.iloc[n][8]
            res_data['hsbz']=df2.iloc[n][9]
            res_data['hsxj']=df2.iloc[n][10]
            res_data['wsxj']=df2.iloc[n][11]
            res_data['dairu']=df2.iloc[n][12]
            res_data['daichu']=df2.iloc[n][13]
            res_data['sczt']=df2.iloc[n][14]
            res_data['daishen']=df2.iloc[n][15]
            res_data['huola']=df2.iloc[n][16]
            res_data['zl']=df2.iloc[n][17]
            res_data['xz']=df2.iloc[n][18]
            res_data['zhcgsj']=df2.iloc[n][19]
            res_data['hsyj']=df2.iloc[n][20]
            res_data['wsyj']=df2.iloc[n][21]

            models.Kc_Erp_Kccx.objects.create(**res_data)

    def leix_kc_ydh(self, file_obj):
        """处理库存 预到货表格模板"""
        df = pd.read_excel(file_obj)
        df2 = df.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['cjsj'] = df2.iloc[n][0]
            res_data['yjdh'] = df2.iloc[n][1]
            res_data['cqts'] = df2.iloc[n][2]
            res_data['danhao'] = df2.iloc[n][3]
            res_data['ks'] = df2.iloc[n][4]
            res_data['spbm'] = df2.iloc[n][5]
            res_data['spmc'] = df2.iloc[n][6]
            res_data['ywy'] = df2.iloc[n][7]
            res_data['kds'] = df2.iloc[n][8]
            res_data['danjia'] = df2.iloc[n][9]
            res_data['jine'] = df2.iloc[n][10]
            res_data['ydh'] = df2.iloc[n][11]
            res_data['wds'] = df2.iloc[n][12]
            res_data['wdje'] = df2.iloc[n][13]

            models.Kc_Erp_Ydh.objects.create(**res_data)

    def leix_kc_zksp(self, file_obj):
        """库存，在库商品分析模板"""
        df = pd.read_excel(file_obj)
        # # 遍历所有列名，排除不需要的
        cols = [i for i in df.columns if i not in ['商品条码']]
        df1 = df[cols]
        df2 = df1.fillna(0)

        riqi = file_obj.name[6:14]
        rq = riqi[:4]+'-'+riqi[4:6]+'-'+riqi[6:8]

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['riqi'] = rq
            res_data['zhjhrq'] = df2.iloc[n][0]
            res_data['spjdrq'] = df2.iloc[n][1]
            res_data['kufang'] = df2.iloc[n][2]
            res_data['hl'] = df2.iloc[n][3]
            res_data['lbmc'] = df2.iloc[n][4]
            res_data['spbm'] = df2.iloc[n][5]
            res_data['spmc'] = df2.iloc[n][6]
            res_data['xh'] = df2.iloc[n][7]
            res_data['guige'] = df2.iloc[n][8]
            res_data['pinpai'] = df2.iloc[n][9]
            res_data['zks'] = df2.iloc[n][10]
            res_data['qjxss'] = df2.iloc[n][11]

            models.Kc_Erp_Zksp.objects.create(**res_data)

    def leix_kc_Kc_Spxx(self,file_obj):
        """库存商品基础信息"""
        df = pd.read_excel(file_obj)
        df2 = df.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['xinghao'] = df2.iloc[n][0]
            res_data['pinlei'] = df2.iloc[n][1]
            res_data['new_old'] = df2.iloc[n][2]
            res_data['dingwei'] = df2.iloc[n][3]
            res_data['pinming'] = df2.iloc[n][4]
            res_data['cpu'] = df2.iloc[n][5]
            res_data['xianka'] = df2.iloc[n][6]
            res_data['neicun'] = df2.iloc[n][7]
            res_data['ssd'] = df2.iloc[n][8]
            res_data['hhd'] = df2.iloc[n][9]
            res_data['model_name'] = df2.iloc[n][10]
            res_data['config'] = df2.iloc[n][11]
            res_data['pn'] = df2.iloc[n][12]

            models.Kc_Spxx.objects.create(**res_data)


    def leix_kc_xhbm(self,file_obj):
        """各平台型号与商品编码对照模板"""
        df = pd.read_excel(file_obj)

        cols = [i for i in df.columns]
        df1 = df[cols]
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['pingtai'] = df2.iloc[n][0]
            res_data['xinghao'] = df2.iloc[n][1]
            res_data['spbm'] = df2.iloc[n][2]

            models.Kc_Xh_Spbm.objects.create(**res_data)

    def get(self,request):

        return render(request, 'data_upload.html')

    def post(self,request):
        """数据上传处理方法"""
        msg = {'code': None}

        table_lx = request.POST.get('leixing')

        file_obj = request.FILES.get('file')
        print(file_obj.name,table_lx)
        if table_lx == 'kc_splr':
            if file_obj:
                self.leix_kc_splr(file_obj)
        elif table_lx == 'kc_kccx':
            if file_obj:
                self.leix_kc_kccx(file_obj)
        elif table_lx == 'kc_ykh':
            if file_obj:
                self.leix_kc_ydh(file_obj)
        elif table_lx == 'kc_zksp':
            if file_obj:
                self.leix_kc_zksp(file_obj)
        elif table_lx == 'Kc_Spxx':
            if file_obj:
                self.leix_kc_Kc_Spxx(file_obj)
        elif table_lx == 'kc_xhbm':
            if file_obj:
                self.leix_kc_xhbm(file_obj)

        msg['code'] = 0
        s = json.dumps(msg)
        return HttpResponse(s)

        # new_file = os.path.join('upload/excel_data', file_obj.name)
        # with open(new_file, 'wb') as f:
        #
        #     for file in file_obj.chunks():
        #         f.write(file)

    def put(self):
        pass

    def delete(self):
        pass
