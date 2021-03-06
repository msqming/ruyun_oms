from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from upload import models as up_models
from auth_mage import models as auth_models
from django.utils.decorators import method_decorator
import os
import requests
import json

import pandas as pd


class OperData(object):

    def kc_splr(self,file_obj):
        """ERP商品利润"""
        response = s.post(url=api2_url, headers=headers2)
        # if api_data.status_code == 200:
        #     return api_data.json()['data']
        result = response.json()['data']

        res_list = []
        for data_itmes in result:
            res_list.append(up_models.Erp_Stock(
                create_time=data_itmes['create_time'] if data_itmes['create_time'] else 0,
                customer_name=data_itmes['customer_name'] if data_itmes['customer_name'] else 0,
                c_sku=data_itmes['c_sku'] if data_itmes['c_sku'] else 0,
                c_series=data_itmes['c_series'] if data_itmes['c_series'] else 0,
                c_brand=data_itmes['c_brand'] if data_itmes['c_brand'] else 0,
                c_category=data_itmes['c_category'] if data_itmes['c_category'] else 0,
                c_goods_name=data_itmes['c_goods_name'] if data_itmes['c_goods_name'] else 0,
                c_ean13=data_itmes['c_ean13'] if data_itmes['c_ean13'] else 0,
                sales_billcode=data_itmes['sales_billcode'] if data_itmes['sales_billcode'] else 0,
                c_source_billcode=data_itmes['c_source_billcode'] if data_itmes['c_source_billcode'] else 0,
                n=data_itmes['n'] if data_itmes['n'] else 0,
                d_price=data_itmes['d_price'] if data_itmes['d_price'] else 0,
                d_amount=data_itmes['d_amount'] if data_itmes['d_amount'] else 0,
                d_cost=data_itmes['d_cost'] if data_itmes['d_cost'] else 0,
                d_amount_cost=data_itmes['d_amount_cost'] if data_itmes['d_amount_cost'] else 0,
                d_discount=data_itmes['d_discount'] if data_itmes['d_discount'] else 0,
                d_fare_display=data_itmes['d_fare_display'] if data_itmes['d_fare_display'] else 0,
                d_fee_platform_display=data_itmes['d_fee_platform_display'] if data_itmes['d_fee_platform_display'] else 0,
                d_back=data_itmes['d_back'] if data_itmes['d_back'] else 0,
                d_fee_charge=data_itmes['d_fee_charge'] if data_itmes['d_fee_charge'] else 0,
                t_send=data_itmes['t_send'] if data_itmes['t_send'] else 0,
                t_pay_estimate=data_itmes['t_pay_estimate'] if data_itmes['t_pay_estimate'] else 0,
                c_vip_code=data_itmes['c_vip_code'] if data_itmes['c_vip_code'] else 0,
                emp_name=data_itmes['emp_name'] if data_itmes['emp_name'] else 0,
                dept_name=data_itmes['dept_name'] if data_itmes['dept_name'] else 0,
            ))

    def kc_splr1(self, file_obj):
        """处理库存商品利润的模板"""
        df = pd.read_excel(file_obj)
        # # 遍历所有列名，排除不需要的
        cols = [i for i in df.columns if i not in ['单位', '订单标记']]
        df1 = df[cols]
        df2 = df1.fillna(0)

        res_list = []
        for n in range(df2.shape[0]):
            res_list.append(models.KcErpSplr(
                cksj=df2.iloc[n][0],
                zfrq=df2.iloc[n][1],
                khmc=df2.iloc[n][2],
                spbm=df2.iloc[n][3],
                leibie=df2.iloc[n][4],
                pinpai=df2.iloc[n][5],
                guige=df2.iloc[n][6],
                xilie=df2.iloc[n][7],
                xh=df2.iloc[n][8],
                spmc=df2.iloc[n][9],
                xz=df2.iloc[n][10],
                leixing=df2.iloc[n][11],
                danhao=df2.iloc[n][12],
                wddh=df2.iloc[n][13],
                hyh=df2.iloc[n][14],
                daofu=df2.iloc[n][15],
                zhiyuan=df2.iloc[n][16],
                sl=df2.iloc[n][17],
                xsdj=df2.iloc[n][18],
                yjcbdj=df2.iloc[n][19],
                xsje=df2.iloc[n][20],
                spzk=df2.iloc[n][21],
                yjzcb=df2.iloc[n][22],
                yjml_hyf=df2.iloc[n][23],
                cgcb=df2.iloc[n][24],
                piao=df2.iloc[n][25],
                zhcb=df2.iloc[n][26],
                cbje=df2.iloc[n][27],
                mlr=df2.iloc[n][28],
                mllv=str(df2.iloc[n][29]).replace(',', ''),
                zhlr=df2.iloc[n][30],
                zh_lrlv=str(df2.iloc[n][31]).replace(',', ''),
                yf_cb=df2.iloc[n][32],
                pt_fy=df2.iloc[n][33],
                fx_fy=df2.iloc[n][34],
                qt_fy=df2.iloc[n][35],
                yj_ml=df2.iloc[n][36],
                yj_mllv=str(df2.iloc[n][37]).replace(',', ''),
                yj_jlr=df2.iloc[n][38],
                yj_jlrlv=str(df2.iloc[n][39]).replace(',', ''),
                pd_sj=df2.iloc[n][40],
                bumen=df2.iloc[n][41],
            ))
            if len(res_list) == 100:
                models.KcErpSplr.objects.bulk_create(res_list)
                del res_list[:]  # 每一次插入完清空列表，释放内存

        # 循环最后一次不够数量的时候再执行插入一次
        if res_list:
            models.KcErpSplr.objects.bulk_create(res_list)
            del res_list[:]

    def kc_kccx(self, file_obj):
        """获取库存 api数据"""

        login_url = 'http://gzry.3cerp.com/_login'
        payload = {
            '_username': '陈志彬',
            '_password': '379f78c2073e7f800eb1782977174edc',
            '_device': 'false',
            '_checked': 'false'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': 'DWRSESSIONID=vH6~xcUig5eLXnT3Yt~CgOieNdDvQ1t5YDm; UM_distinctid=169fc3d1e7e5e6-02b6a8a0a79b-36697e04-1fa400-169fc3d1e7f7d0; Hm_lvt_7567a7c24a073c4d5983affb6409356d=1554715058; Hm_lpvt_7567a7c24a073c4d5983affb6409356d=1554870729; _jzqa=1.2600623370342070000.1554878190.1554878190.1554878190.1; _jzqc=1; _jzqx=1.1554878190.1554878190.1.jzqsr=test%2Esrerp%2E3cwdb%2Ecom|jzqct=/index%2Ejsp.-; JSESSIONID=57F1A201C94743D2790974F6B05DE8A2',
            'Host': 'gzry.3cerp.com',
            'Origin': 'http://gzry.3cerp.com',
            'Referer': 'http://gzry.3cerp.com/login.jsp',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }
        headers2 = {
            'Host': 'gzry.3cerp.com',
            'Origin': 'http://gzry.3cerp.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }

        s = requests.session()
        s.post(url=login_url, data=payload, headers=headers)
        api_url = 'http://gzry.3cerp.com/pages/stock/searchGoodsExtend.htm?pageSize=100'

        res2 = s.post(url=api_url, headers=headers2)
        total = res2.json()['total']
        print(total)

        api2_url = 'http://gzry.3cerp.com/pages/stock/searchGoodsExtend.htm?totalCount={0}&pageSize=2000&pageIndex=0'.format(
            total)

        response = s.post(url=api2_url, headers=headers2)
        # if api_data.status_code == 200:
        #     return api_data.json()['data']
        result = response.json()['data']

        res_list = []
        for data_itmes in result:
            res_list.append(up_models.Erp_Stock(
                b_c_sku=data_itmes['b_c_sku'] if data_itmes['b_c_sku'] else 0,
                b_c_name=data_itmes['b_c_name'] if data_itmes['b_c_name'] else 0,
                d_c_bom_type=data_itmes['d_c_bom_type'] if data_itmes['d_c_bom_type'] else 0,
                b_c_brand=data_itmes['b_c_brand'] if data_itmes['b_c_brand'] else 0,
                category_name=data_itmes['category_name'] if data_itmes['category_name'] else 0,
                c_series=data_itmes['c_series'] if data_itmes['c_series'] else 0,
                n_finance=data_itmes['n_finance'] if data_itmes['n_finance'] else 0,
                n_able=data_itmes['n_able'] if data_itmes['n_able'] else 0,
                n_purchase=data_itmes['n_purchase'] if data_itmes['n_purchase'] else 0,
                n_sale=data_itmes['n_sale'] if data_itmes['n_sale'] else 0,
                n_sale_net=data_itmes['n_sale_net'] if data_itmes['n_sale_net'] else 0,
                n_production=data_itmes['n_production'] if data_itmes['n_production'] else 0,
                d_cost=data_itmes['d_cost'] if data_itmes['d_cost'] else 0,
                kc_d_amount=data_itmes['kc_d_amount'] if data_itmes['kc_d_amount'] else 0,
                d_cost_estimate_tax=data_itmes['d_cost_estimate_tax'] if data_itmes['d_cost_estimate_tax'] else 0,
                d_cost_estimate_untax=data_itmes['d_cost_estimate_untax'] if data_itmes['d_cost_estimate_untax'] else 0,
                d_cost_sale_tax=data_itmes['d_cost_sale_tax'] if data_itmes['d_cost_sale_tax'] else 0,
                d_cost_sale_untax=data_itmes['d_cost_sale_untax'] if data_itmes['d_cost_sale_untax'] else 0,
                d_rate_tax=data_itmes['d_rate_tax'] if data_itmes['d_rate_tax'] else 0,
                d_weight=data_itmes['d_weight'] if data_itmes['d_weight'] else 0,
                t_last_purchase=data_itmes['t_last_purchase'] if data_itmes['t_last_purchase'] else 0,
                goods_id=data_itmes['goods_id'] if data_itmes['goods_id'] else 0,
            ))

            if len(res_list) == 100:
                up_models.Erp_Stock.objects.bulk_create(res_list)
                del res_list[:]  # 每一次插入完清空列表，释放内存

        # 循环最后一次不够数量的时候再执行插入一次
        if res_list:
            up_models.Erp_Stock.objects.bulk_create(res_list)
            del res_list[:]

    def kc_ydh(self, file_obj):
        """ERP采购分析"""
        response = s.post(url=api2_url, headers=headers2)
        # if api_data.status_code == 200:
        #     return api_data.json()['data']
        result = response.json()['data']

        res_list = []
        for data_itmes in result:
            res_list.append(up_models.Erp_Stock(
                create_time=data_itmes['create_time'] if data_itmes['create_time'] else 0,
                t_get_estimate=data_itmes['t_get_estimate'] if data_itmes['t_get_estimate'] else 0,
                d_cq=data_itmes['d_cq'] if data_itmes['d_cq'] else 0,
                c_billcode=data_itmes['c_billcode'] if data_itmes['c_billcode'] else 0,
                c_name=data_itmes['c_name'] if data_itmes['c_name'] else 0,
                c_sku=data_itmes['c_sku'] if data_itmes['c_sku'] else 0,
                goodsName=data_itmes['goodsName'] if data_itmes['goodsName'] else 0,
                kd_n=data_itmes['n'] if data_itmes['n'] else 0,
                d_price=data_itmes['d_price'] if data_itmes['d_price'] else 0,
                goods_d_amount=data_itmes['goods_d_amount'] if data_itmes['goods_d_amount'] else 0,
                n_get=data_itmes['n_get'] if data_itmes['n_get'] else 0,
                goods_n_noget=data_itmes['goods_n_noget'] if data_itmes['goods_n_noget'] else 0,
                goods_d_noget=data_itmes['goods_d_noget'] if data_itmes['goods_d_noget'] else 0,
                goods_id=data_itmes['goods_id'] if data_itmes['goods_id'] else 0,
                business_name=data_itmes['c_handing_emp_org_name'] if data_itmes['c_handing_emp_org_name'] else 0,
            ))

    def kc_ydh1(self, file_obj):
        """处理库存 预到货表格模板"""
        df = pd.read_excel(file_obj)
        df2 = df.fillna(0)

        res_list = []
        for n in range(df2.shape[0]):
            res_list.append(models.KcErpYdh(
                cjsj=df2.iloc[n][0],
                yjdh=df2.iloc[n][1],
                cqts=df2.iloc[n][2],
                danhao=df2.iloc[n][3],
                ks=df2.iloc[n][4],
                spbm=df2.iloc[n][5],
                spmc=df2.iloc[n][6],
                ywy=df2.iloc[n][7],
                kds=df2.iloc[n][8],
                danjia=df2.iloc[n][9],
                jine=df2.iloc[n][10],
                ydh=df2.iloc[n][11],
                wds=df2.iloc[n][12],
                wdje=df2.iloc[n][13],
            ))

            if len(res_list) == 100:
                models.KcErpYdh.objects.bulk_create(res_list)
                del res_list[:]  # 每一次插入完清空列表，释放内存

        # 循环最后一次不够数量的时候再执行插入一次
        if res_list:
            models.KcErpYdh.objects.bulk_create(res_list)
            del res_list[:]

    def kc_zksp(self, file_obj):
        """库存，在库商品分析模板"""
        df = pd.read_excel(file_obj)
        # # 遍历所有列名，排除不需要的
        cols = [i for i in df.columns if i not in ['商品条码']]
        df1 = df[cols]
        df2 = df1.fillna(0)

        riqi = file_obj.name[6:14]
        rq = riqi[:4] + '-' + riqi[4:6] + '-' + riqi[6:8]

        res_list = []
        for n in range(df2.shape[0]):
            res_list.append(models.KcErpZksp(
                riqi=rq,
                zhjhrq=df2.iloc[n][0],
                spjdrq=df2.iloc[n][1],
                kufang=df2.iloc[n][2],
                hl=df2.iloc[n][3],
                lbmc=df2.iloc[n][4],
                spbm=df2.iloc[n][5],
                spmc=df2.iloc[n][6],
                xh=df2.iloc[n][7],
                guige=df2.iloc[n][8],
                pinpai=df2.iloc[n][9],
                zks=df2.iloc[n][10],
                qjxss=df2.iloc[n][11],
            ))
            if len(res_list) == 100:
                models.KcErpZksp.objects.bulk_create(res_list)
                del res_list[:]  # 每一次插入完清空列表，释放内存

        # 循环最后一次不够数量的时候再执行插入一次
        if res_list:
            models.KcErpZksp.objects.bulk_create(res_list)
            del res_list[:]

    def Kc_spxx(self, file_obj):
        """库存商品基础信息"""
        df = pd.read_excel(file_obj)
        df2 = df.fillna(0)
        res_list = []
        for n in range(df2.shape[0]):
            res_list.append(models.KcSpxx(
                xinghao=df2.iloc[n][0],
                pinlei=df2.iloc[n][1],
                new_old=df2.iloc[n][2],
                dingwei=df2.iloc[n][3],
                pinming=df2.iloc[n][4],
                cpu=df2.iloc[n][5],
                xianka=df2.iloc[n][6],
                neicun=df2.iloc[n][7],
                ssd=df2.iloc[n][8],
                hhd=df2.iloc[n][9],
                model_name=df2.iloc[n][10],
                config=df2.iloc[n][11],
                pn=df2.iloc[n][12],
            ))
            if len(res_list) == 100:
                models.KcSpxx.objects.bulk_create(res_list)
                del res_list[:]  # 每一次插入完清空列表，释放内存

        # 循环最后一次不够数量的时候再执行插入一次
        if res_list:
            models.KcSpxx.objects.bulk_create(res_list)
            del res_list[:]

    def kc_xhbm(self, file_obj):
        """各平台型号与商品编码对照模板"""
        df = pd.read_excel(file_obj)
        df2 = df.fillna(0)

        res_list = []
        for n in range(df2.shape[0]):
            res_list.append(models.KcXhSpbm(
                pingtai=df2.iloc[n][0],
                xinghao=df2.iloc[n][1],
                spbm=df2.iloc[n][2],
            ))
            if len(res_list) == 100:
                models.KcXhSpbm.objects.bulk_create(res_list)
                del res_list[:]  # 每一次插入完清空列表，释放内存

        # 循环最后一次不够数量的时候再执行插入一次
        if res_list:
            models.KcXhSpbm.objects.bulk_create(res_list)
            del res_list[:]

    def cw_jqcb(self, file_obj):
        """财务数据，机器成本模板"""
        df = pd.read_excel(file_obj)
        cols = [i for i in df.columns]
        df1 = df[cols]
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['riqi'] = df2.iloc[n][0]
            res_data['erp_name'] = df2.iloc[n][1]
            res_data['chenben'] = df2.iloc[n][2]

            models.CwJqcb.objects.create(**res_data)

    def cw_bjbtop_m(self, file_obj):
        df = pd.read_excel(file_obj)
        cols = [i for i in df.columns]
        df1 = df[cols]
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['comm_id'] = df2.iloc[n][0]
            res_data['shijian'] = df2.iloc[n][1]
            res_data['mbzfjs'] = df2.iloc[n][2]
            res_data['mbuv'] = df2.iloc[n][3]
            res_data['bmzhl'] = round((res_data['mbzfjs'] / res_data['mbuv'] * 100), 2)

            models.CwBjbTopM.objects.create(**res_data)

    def cw_bjbtop_w(self, file_obj):
        df = pd.read_excel(file_obj)
        cols = [i for i in df.columns]
        df1 = df[cols]
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['comm_id'] = df2.iloc[n][0]
            res_data['hdzq'] = df2.iloc[n][1]
            res_data['mbzfjs'] = df2.iloc[n][2]
            res_data['mbuv'] = df2.iloc[n][3]
            res_data['bmzhl'] = round((res_data['mbzfjs'] / res_data['mbuv'] * 100), 2)

            models.CwBjbTopW.objects.create(**res_data)

    def cw_bjbxl_w(self, file_obj):
        df = pd.read_excel(file_obj)
        cols = [i for i in df.columns]
        df1 = df[cols]
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['shijian'] = df2.iloc[n][0]
            res_data['bjbxl'] = df2.iloc[n][1]
            res_data['mbxse'] = df2.iloc[n][2]
            res_data['mbxl'] = df2.iloc[n][3]

            models.CwBjbXlW.objects.create(**res_data)

    def cw_gpl_m(self, file_obj):
        df = pd.read_excel(file_obj)
        cols = [i for i in df.columns]
        df1 = df[cols]
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['shijian'] = df2.iloc[n][2]
            res_data['pinlei'] = df2.iloc[n][3]
            res_data['mbxse'] = int(df2.iloc[n][4])
            res_data['mbxl'] = int(df2.iloc[n][5])

            models.CwGplM.objects.create(**res_data)

    def cw_gpl_w(self, file_obj):
        df = pd.read_excel(file_obj)
        cols = [i for i in df.columns]
        df1 = df[cols]
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['shijian'] = df2.iloc[n][0]
            res_data['pinlei'] = df2.iloc[n][1]
            res_data['huod'] = df2.iloc[n][2]
            res_data['mbxse'] = int(df2.iloc[n][3])
            res_data['mbxl'] = int(df2.iloc[n][4])

            models.CwGplW.objects.create(**res_data)

    def dp_gq_gk(self, file_obj):
        df = pd.read_excel(file_obj)

        cols = list(df.iloc[6])
        df1 = df.drop([0, 1, 2, 3, 4, 5, 6])
        df1.columns = cols
        print(df1)
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['tjrq'] = df2.iloc[n][0].replace(',', '')
            res_data['pc_fk'] = df2.iloc[n][1].replace(',', '')
            res_data['pc_ll'] = df2.iloc[n][2].replace(',', '')
            res_data['fks'] = df2.iloc[n][3].replace(',', '')
            res_data['wx_fk'] = df2.iloc[n][4].replace(',', '')
            res_data['lll'] = df2.iloc[n][5].replace(',', '')
            res_data['wx_ll'] = df2.iloc[n][6].replace(',', '')
            res_data['sp_fks'] = df2.iloc[n][7].replace(',', '')
            res_data['wx_sp_fk'] = df2.iloc[n][8].replace(',', '')
            res_data['pc_sp_fk'] = df2.iloc[n][9].replace(',', '')
            res_data['sp_ll'] = df2.iloc[n][10].replace(',', '')
            res_data['wx_sp_ll'] = df2.iloc[n][11].replace(',', '')
            res_data['pc_sp_ll'] = df2.iloc[n][12].replace(',', '')
            res_data['pjtlsc'] = df2.iloc[n][13].replace(',', '')
            res_data['wx_pj_tlsc'] = df2.iloc[n][14].replace(',', '')
            res_data['pc_pj_tlsc'] = df2.iloc[n][15].replace(',', '')
            res_data['tsl'] = df2.iloc[n][16].replace(',', '')
            res_data['wx_tsl'] = df2.iloc[n][17].replace(',', '')
            res_data['pc_tsl'] = df2.iloc[n][18].replace(',', '')
            res_data['sp_scmj'] = df2.iloc[n][19].replace(',', '')
            res_data['wx_sp_scmj'] = df2.iloc[n][20].replace(',', '')
            res_data['pc_sp_scmj'] = df2.iloc[n][21].replace(',', '')
            res_data['sp_sccs'] = df2.iloc[n][22].replace(',', '')
            res_data['wx_sp_sccs'] = df2.iloc[n][23].replace(',', '')
            res_data['pc_sp_sccs'] = df2.iloc[n][24].replace(',', '')
            res_data['jgrs'] = df2.iloc[n][25].replace(',', '')
            res_data['wx_jgrs'] = df2.iloc[n][26].replace(',', '')
            res_data['pc_jgrs'] = df2.iloc[n][27].replace(',', '')
            res_data['zfje'] = df2.iloc[n][28].replace(',', '')
            res_data['pc_zfje'] = df2.iloc[n][29].replace(',', '')
            res_data['wx_zfje'] = df2.iloc[n][30].replace(',', '')
            res_data['zfmjs'] = df2.iloc[n][31].replace(',', '')
            res_data['pc_zfmjs'] = df2.iloc[n][32].replace(',', '')
            res_data['wx_zfmjs'] = df2.iloc[n][33].replace(',', '')
            res_data['zfzdds'] = df2.iloc[n][34].replace(',', '')
            res_data['pc_zfzdds'] = df2.iloc[n][35].replace(',', '')
            res_data['wx_zfzdds'] = df2.iloc[n][36].replace(',', '')
            res_data['zfjs'] = df2.iloc[n][37].replace(',', '')
            res_data['pc_zfjs'] = df2.iloc[n][38].replace(',', '')
            res_data['wx_zfjs'] = df2.iloc[n][39].replace(',', '')
            res_data['xdje'] = df2.iloc[n][40].replace(',', '')
            res_data['pc_xdje'] = df2.iloc[n][41].replace(',', '')
            res_data['mwx_xdje'] = df2.iloc[n][42].replace(',', '')
            res_data['xdmjs'] = df2.iloc[n][43].replace(',', '')
            res_data['pc_xdmjs'] = df2.iloc[n][44].replace(',', '')
            res_data['wx_xdmjs'] = df2.iloc[n][45].replace(',', '')
            res_data['xdjs'] = df2.iloc[n][46].replace(',', '')
            res_data['pc_xdjs'] = df2.iloc[n][47].replace(',', '')
            res_data['wx_xdjs'] = df2.iloc[n][48].replace(',', '')
            res_data['rjlll'] = df2.iloc[n][49].replace(',', '')
            res_data['pc_rjll'] = df2.iloc[n][50].replace(',', '')
            res_data['wx_rjll'] = df2.iloc[n][51].replace(',', '')
            res_data['xdzhl'] = df2.iloc[n][52].replace(',', '')
            res_data['pc_xdzhl'] = df2.iloc[n][53].replace(',', '')
            res_data['wx_xdzhl'] = df2.iloc[n][54].replace(',', '')
            res_data['zfzhl'] = df2.iloc[n][55].replace(',', '')
            res_data['pc_zfzhl'] = df2.iloc[n][56].replace(',', '')
            res_data['wx_zfzhl'] = df2.iloc[n][57].replace(',', '')
            res_data['kdj'] = df2.iloc[n][58].replace(',', '')
            res_data['pc_kdj'] = df2.iloc[n][59].replace(',', '')
            res_data['wx_kdj'] = df2.iloc[n][60].replace(',', '')
            res_data['uvjz'] = df2.iloc[n][61].replace(',', '')
            res_data['pc_uvjz'] = df2.iloc[n][62].replace(',', '')
            res_data['wx_uvjz'] = df2.iloc[n][63].replace(',', '')
            res_data['old_fks'] = df2.iloc[n][64].replace(',', '')
            res_data['new_fks'] = df2.iloc[n][65].replace(',', '')
            res_data['wx_old_fks'] = df2.iloc[n][66].replace(',', '')
            res_data['wx_new_fks'] = df2.iloc[n][67].replace(',', '')
            res_data['pc_old_fks'] = df2.iloc[n][68].replace(',', '')
            res_data['pc_new_fks'] = df2.iloc[n][69].replace(',', '')
            res_data['jgjs'] = df2.iloc[n][70].replace(',', '')
            res_data['pc_jgjs'] = df2.iloc[n][71].replace(',', '')
            res_data['wx_jgjs'] = df2.iloc[n][72].replace(',', '')
            res_data['zf_old_mjs'] = df2.iloc[n][73].replace(',', '')
            res_data['pc_zf_old_mjs'] = df2.iloc[n][74].replace(',', '')
            res_data['wx_zf_old_mjs'] = df2.iloc[n][75].replace(',', '')
            res_data['old_mj_zfje'] = df2.iloc[n][76].replace(',', '')
            res_data['ztc_xh'] = df2.iloc[n][77].replace(',', '')
            res_data['zsz_xh'] = df2.iloc[n][78].replace(',', '')
            res_data['tbk_yj'] = df2.iloc[n][79].replace(',', '')
            res_data['cgtk_je'] = df2.iloc[n][80].replace(',', '')
            res_data['pjs'] = df2.iloc[n][81].replace(',', '')
            res_data['yt_pjs'] = df2.iloc[n][82].replace(',', '')
            res_data['zm_pjs'] = df2.iloc[n][83].replace(',', '')
            res_data['fm_pjs'] = df2.iloc[n][84].replace(',', '')
            res_data['old_mj_zm_pjs'] = df2.iloc[n][85].replace(',', '')
            res_data['old_mj_fm_pjs'] = df2.iloc[n][86].replace(',', '')
            res_data['zf_fdds'] = df2.iloc[n][87].replace(',', '')
            res_data['ls_bgs'] = df2.iloc[n][88].replace(',', '')
            res_data['fh_bgs'] = df2.iloc[n][89].replace(',', '')
            res_data['ps_bgs'] = df2.iloc[n][90].replace(',', '')
            res_data['qscg_bgs'] = df2.iloc[n][91].replace(',', '')
            res_data['pjzf_qs_sc'] = df2.iloc[n][92].replace(',', '')
            res_data['msxf_pf'] = df2.iloc[n][93].replace(',', '')
            res_data['wlfw_pf'] = df2.iloc[n][94].replace(',', '')
            res_data['wftd_pf'] = df2.iloc[n][95].replace(',', '')
            res_data['xd_zf_zhl'] = df2.iloc[n][96].replace(',', '')
            res_data['pc_xd_zf_zhl'] = df2.iloc[n][97].replace(',', '')
            res_data['wx_xd_zf_zhl'] = df2.iloc[n][98].replace(',', '')
            res_data['zf_sps'] = df2.iloc[n][99].replace(',', '')
            res_data['pc_zf_sps'] = df2.iloc[n][100].replace(',', '')
            res_data['wx_zf_sps'] = df2.iloc[n][101].replace(',', '')
            res_data['dp_sc_mjs'] = df2.iloc[n][102].replace(',', '')
            res_data['pc_dp_sc_mjs'] = df2.iloc[n][103].replace(',', '')
            res_data['wx_dp_sc_mjs'] = df2.iloc[n][104].replace(',', '')

            models.DpGk.objects.create(**res_data)

    def dp_gq_tg_pxb(self, file_obj):
        df1 = pd.read_excel(file_obj)
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['riqi'] = df2.iloc[n][0]
            res_data['zxl'] = df2.iloc[n][1]
            res_data['djl'] = df2.iloc[n][2]
            res_data['djlv'] = df2.iloc[n][3]
            res_data['huafei'] = df2.iloc[n][4]
            res_data['zxcb'] = df2.iloc[n][5]
            res_data['djdj'] = df2.iloc[n][6]
            res_data['tz_djdj'] = df2.iloc[n][6]
            res_data['zs_cjbs'] = df2.iloc[n][7]
            res_data['zs_cjje'] = df2.iloc[n][8]
            res_data['bbscs'] = df2.iloc[n][9]
            res_data['dpscs'] = df2.iloc[n][10]
            res_data['bbjgs'] = df2.iloc[n][11]
            res_data['zs_hbl'] = df2.iloc[n][12]
            res_data['dj_hbl'] = df2.iloc[n][13]
            res_data['dj_cjbs'] = df2.iloc[n][14]
            res_data['dj_cjje'] = df2.iloc[n][15]
            res_data['cd_fks'] = df2.iloc[n][16]
            res_data['cd_new_fks'] = df2.iloc[n][17]
            res_data['dj_fks'] = df2.iloc[n][18]
            res_data['zx_zhl'] = df2.iloc[n][19]
            res_data['dj_zhl'] = df2.iloc[n][20]

            models.DpTgPxb.objects.create(**res_data)

    def dp_gq_tg_ztc(self, file_obj):
        df1 = pd.read_csv(file_obj)
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['reqi'] = df2.iloc[n][0]
            res_data['tg_jhmc'] = df2.iloc[n][1]
            res_data['bb_mc'] = df2.iloc[n][2]
            res_data['bb_lx'] = df2.iloc[n][3]
            res_data['sp_id'] = df2.iloc[n][4]
            res_data['ss_lx'] = df2.iloc[n][5]
            res_data['ll_ly'] = df2.iloc[n][6]
            res_data['zxl'] = df2.iloc[n][7]
            res_data['djl'] = df2.iloc[n][8]
            res_data['hf'] = df2.iloc[n][9]
            res_data['djlv'] = df2.iloc[n][10]
            res_data['pj_dj_hf'] = df2.iloc[n][11]
            res_data['qc_zx_hf'] = df2.iloc[n][12]
            res_data['dj_zhl'] = df2.iloc[n][13]
            res_data['zj_cj_je'] = df2.iloc[n][14]
            res_data['zj_cj_bs'] = df2.iloc[n][15]
            res_data['jj_cj_je'] = df2.iloc[n][16]
            res_data['jj_cj_bs'] = df2.iloc[n][17]
            res_data['z_cj_je'] = df2.iloc[n][18]
            res_data['z_cj_bs'] = df2.iloc[n][19]
            res_data['bb_scs'] = df2.iloc[n][20]
            res_data['dp_scs'] = df2.iloc[n][21]
            res_data['z_scs'] = df2.iloc[n][22]
            res_data['tr_ccb'] = df2.iloc[n][23]
            res_data['zj_gwcs'] = df2.iloc[n][24]
            res_data['jj_gwcs'] = df2.iloc[n][25]
            res_data['z_gwcs'] = df2.iloc[n][26]

            models.DpTgZtc.objects.create(**res_data)

    def dp_gq_tg_zz(self, file_obj):
        df1 = pd.read_excel(file_obj)
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['jhxx'] = df2.iloc[n][0]
            res_data['shijian'] = df2.iloc[n][1]
            res_data['zhanxian'] = df2.iloc[n][2]
            res_data['dianji'] = df2.iloc[n][3]
            res_data['xiaohao'] = df2.iloc[n][4]
            res_data['djlv'] = df2.iloc[n][5]
            res_data['djdj'] = df2.iloc[n][6]
            res_data['qczxcb'] = df2.iloc[n][7]
            res_data['fk'] = df2.iloc[n][8]
            res_data['sdjdl'] = df2.iloc[n][9]
            res_data['fw_sc'] = df2.iloc[n][10]
            res_data['fw_ym'] = df2.iloc[n][11]
            res_data['sc_bb'] = df2.iloc[n][12]
            res_data['sc_dp'] = df2.iloc[n][13]
            res_data['tj_gwc'] = df2.iloc[n][14]
            res_data['px_ddl'] = df2.iloc[n][15]
            res_data['px_ddje'] = df2.iloc[n][16]
            res_data['cj_ddl'] = df2.iloc[n][17]
            res_data['cj_ddje'] = df2.iloc[n][18]
            res_data['dj_zhlv'] = df2.iloc[n][19]
            res_data['tz_hblv'] = df2.iloc[n][20]
            res_data['xd_l'] = df2.iloc[n][21]
            res_data['xd_cb'] = df2.iloc[n][22]

            models.DpTgZz.objects.create(**res_data)

    def dp_gq_kjcw(self, file_obj):
        df1 = pd.read_excel(file_obj)
        df2 = df1.fillna(0)
        # print(df2.dtypes)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['dd_bh'] = df2.iloc[n][0]
            res_data['mj_hym'] = df2.iloc[n][1]
            res_data['dd_zt'] = df2.iloc[n][2]
            res_data['sf_je'] = df2.iloc[n][3]
            res_data['sf_yf'] = df2.iloc[n][4]
            res_data['hp_cb'] = df2.iloc[n][5]
            res_data['kdf'] = df2.iloc[n][6]
            res_data['bzf'] = df2.iloc[n][7]
            res_data['zpf'] = df2.iloc[n][8]
            res_data['ts_yj'] = df2.iloc[n][9]
            res_data['lirun'] = df2.iloc[n][10]
            res_data['ktgs'] = df2.iloc[n][11]
            res_data['ydh'] = df2.iloc[n][12]
            res_data['sh_dz'] = df2.iloc[n][13]
            res_data['dd_cj_sj'] = df2.iloc[n][14]
            res_data['dd_fk_sj'] = df2.iloc[n][15]
            res_data['dd_fh_sj'] = df2.iloc[n][16]
            res_data['dd_js_sj'] = df2.iloc[n][17]
            res_data['bb_bt'] = df2.iloc[n][18]
            res_data['bb_id'] = df2.iloc[n][19]
            res_data['bb_sj_bm'] = df2.iloc[n][20]
            res_data['sx_id'] = df2.iloc[n][21]
            res_data['sx_sj_bm'] = df2.iloc[n][22]
            res_data['bb_zl'] = df2.iloc[n][23]
            res_data['bb_zsl'] = df2.iloc[n][24]
            res_data['mj_fwf_1'] = df2.iloc[n][25]
            res_data['mf_fwf_2'] = df2.iloc[n][26]
            res_data['qizhi'] = df2.iloc[n][27]
            res_data['hulue'] = df2.iloc[n][28]

            models.DpGqKjcw.objects.create(**res_data)

    def dp_gq_lsgc(self, file_obj):
        df = pd.read_excel(file_obj)

        cols = list(df.iloc[4])
        df1 = df.drop([0, 1, 2, 3, 4])
        df1.columns = cols
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['ll_ly'] = df2.iloc[n][0]
            res_data['ly_mx'] = df2.iloc[n][1]
            res_data['fks'] = df2.iloc[n][2].replace(',', '')
            res_data['fks_bh'] = df2.iloc[n][3].replace(',', '')
            res_data['xd_je'] = df2.iloc[n][4].replace(',', '')
            res_data['xd_je_bh'] = df2.iloc[n][5].replace(',', '')
            res_data['xd_mjs'] = df2.iloc[n][6].replace(',', '')
            res_data['xd_mjs_bh'] = df2.iloc[n][7].replace(',', '')
            res_data['xd_zhlv'] = df2.iloc[n][8].replace(',', '')
            res_data['xd_zhlv_bh'] = df2.iloc[n][9].replace(',', '')
            res_data['zf_je'] = df2.iloc[n][10].replace(',', '')
            res_data['zf_je_bh'] = df2.iloc[n][11].replace(',', '')
            res_data['zf_mjs'] = df2.iloc[n][12].replace(',', '')
            res_data['zf_mjs_bh'] = df2.iloc[n][13].replace(',', '')
            res_data['zf_zhlv'] = df2.iloc[n][14].replace(',', '')
            res_data['zf_zhlv_bh'] = df2.iloc[n][15].replace(',', '')
            res_data['kdj'] = df2.iloc[n][16].replace(',', '')
            res_data['kdj_bh'] = df2.iloc[n][17].replace(',', '')
            res_data['uv_jz'] = df2.iloc[n][18].replace(',', '')
            res_data['uv_jz_bh'] = df2.iloc[n][19].replace(',', '')
            res_data['gz_dp_mjs'] = df2.iloc[n][20].replace(',', '')
            res_data['gz_dp_mjs_bh'] = df2.iloc[n][21].replace(',', '')
            res_data['sc_sp_mjs'] = df2.iloc[n][22].replace(',', '')
            res_data['sc_sp_mjs_bh'] = df2.iloc[n][23].replace(',', '')
            res_data['jg_rs'] = df2.iloc[n][24].replace(',', '')
            res_data['jg_rs_bh'] = df2.iloc[n][25].replace(',', '')
            res_data['x_fk'] = df2.iloc[n][26].replace(',', '')
            res_data['x_fk_bh'] = df2.iloc[n][27].replace(',', '')
            res_data['zj_zf_mjs'] = df2.iloc[n][28].replace(',', '')
            res_data['scsp_zf_mj'] = df2.iloc[n][29].replace(',', '')
            res_data['fs_zf_mjs'] = df2.iloc[n][30].replace(',', '')
            res_data['jg_sp_zfmj'] = df2.iloc[n][31].replace(',', '')

            models.DpGqLlgc.objects.create(**res_data)

    def dp_gq_plsj(self, file_obj):
        df = pd.read_excel(file_obj)

        cols = list(df.iloc[4])
        df1 = df.drop([0, 1, 2, 3, 4])
        df1.columns = cols
        df2 = df1.fillna(0)
        # print(df2.dtypes)
        res_data = {}
        for n in range(df2.shape[0]):
            res_data['tjrq'] = df2.iloc[n][0]
            res_data['yj_lm_mc'] = df2.iloc[n][1]
            res_data['ej_lm_mc'] = df2.iloc[n][2]
            res_data['lm_mc'] = df2.iloc[n][3]
            res_data['sp_fks'] = df2.iloc[n][4].replace(',', '')
            res_data['sp_lll'] = df2.iloc[n][5].replace(',', '')
            res_data['yfk_sps'] = df2.iloc[n][6].replace(',', '')
            res_data['yzf_sps'] = df2.iloc[n][7].replace(',', '')
            res_data['sp_jgs'] = df2.iloc[n][8].replace(',', '')
            res_data['sp_jg_js'] = df2.iloc[n][9].replace(',', '')
            res_data['sp_sc_rs'] = df2.iloc[n][10].replace(',', '')
            res_data['fw_sc_zhlv'] = df2.iloc[n][11].replace(',', '')
            res_data['fw_jg_zhlv'] = df2.iloc[n][12].replace(',', '')
            res_data['xd_mjs'] = df2.iloc[n][13].replace(',', '')
            res_data['xd_js'] = df2.iloc[n][14].replace(',', '')
            res_data['xd_je'] = df2.iloc[n][15].replace(',', '')
            res_data['xd_zhlv'] = df2.iloc[n][16].replace(',', '')
            res_data['zf_mjs'] = df2.iloc[n][17].replace(',', '')
            res_data['zf_js'] = df2.iloc[n][18].replace(',', '')
            res_data['zf_je'] = df2.iloc[n][19].replace(',', '')
            res_data['zf_zhlv'] = df2.iloc[n][20].replace(',', '')
            res_data['m_lj_zfje'] = df2.iloc[n][21].replace(',', '')
            res_data['y_lj_zfje'] = df2.iloc[n][22].replace(',', '')
            res_data['jhs_zfje'] = df2.iloc[n][23].replace(',', '')
            res_data['zf_xmj'] = df2.iloc[n][24].replace(',', '')
            res_data['zf_lmj'] = df2.iloc[n][25].replace(',', '')
            res_data['lmj_zfje'] = df2.iloc[n][26].replace(',', '')
            res_data['kdj'] = df2.iloc[n][27].replace(',', '')
            res_data['fk_pj_jz'] = df2.iloc[n][28].replace(',', '')
            res_data['sh_tkje'] = df2.iloc[n][29].replace(',', '')

            models.DpGqPlsj.objects.create(**res_data)

    def dp_gq_sc_hyqs_d(self, file_obj):
        df1 = pd.read_csv(file_obj)
        df2 = df1.fillna(0)
        # print(df2.columns)
        cols = list(df2.columns)
        if '客单价' in cols:
            res_data = {}
            for n in range(df2.shape[0]):
                res_data['lm_name'] = df2.iloc[n][0]
                res_data['riqi'] = df2.iloc[n][1]
                res_data['ss_rs'] = df2.iloc[n][2]
                res_data['ss_cs'] = df2.iloc[n][3]
                res_data['fks'] = df2.iloc[n][4]
                res_data['lll'] = df2.iloc[n][5]
                res_data['sc_rs'] = df2.iloc[n][6]
                res_data['sc_cs'] = df2.iloc[n][7]
                res_data['jg_rs'] = df2.iloc[n][8]
                res_data['jg_cs'] = df2.iloc[n][9]
                res_data['zf_rs'] = df2.iloc[n][10]
                res_data['jy_je'] = df2.iloc[n][11]
                res_data['kdj'] = df2.iloc[n][12]

                models.DpGqScHyqsD.objects.create(**res_data)
        else:
            res_data = {}
            for n in range(df2.shape[0]):
                res_data['lm_name'] = df2.iloc[n][0]
                res_data['riqi'] = df2.iloc[n][1]
                res_data['ss_rs'] = 0
                res_data['ss_cs'] = 0
                res_data['fks'] = df2.iloc[n][2]
                res_data['lll'] = df2.iloc[n][3]
                res_data['sc_rs'] = df2.iloc[n][4]
                res_data['sc_cs'] = df2.iloc[n][5]
                res_data['jg_rs'] = df2.iloc[n][6]
                res_data['jg_cs'] = df2.iloc[n][7]
                res_data['zf_rs'] = 0
                res_data['jy_je'] = 0
                res_data['kdj'] = 0

                models.DpGqScHyqsD.objects.create(**res_data)

    def dp_gq_sc_hyqs_m(self, file_obj):
        df1 = pd.read_excel(file_obj)
        df2 = df1.fillna(0)
        # print(df2.dtypes)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['jtpl'] = df2.iloc[n][0]
            res_data['riqi'] = df2.iloc[n][3]
            res_data['fkl'] = df2.iloc[n][4]
            res_data['lll'] = df2.iloc[n][5]
            res_data['sc_rs'] = df2.iloc[n][6]
            res_data['sc_cs'] = df2.iloc[n][7]
            res_data['jg_rs'] = df2.iloc[n][8]
            res_data['jg_cs'] = df2.iloc[n][9]
            res_data['zf_js'] = df2.iloc[n][10]
            res_data['kdj'] = df2.iloc[n][11]
            res_data['jy_zs'] = df2.iloc[n][12]
            res_data['ss_dj_rs'] = df2.iloc[n][13]
            res_data['bzf_mjs'] = df2.iloc[n][14]
            res_data['zhlv'] = df2.iloc[n][15]
            res_data['jye'] = df2.iloc[n][16]

            models.DpGqScHyqsM.objects.create(**res_data)

    def gq_scph_bjb_dp_gjy(self, file_obj):
        df1 = pd.read_csv(file_obj)
        df2 = df1.fillna(0)
        print(df2.dtypes)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['dp_xx'] = df2.iloc[n][0]
            res_data['riqi'] = df2.iloc[n][1]
            res_data['hy_pm'] = df2.iloc[n][2]
            res_data['jy_je'] = df2.iloc[n][3]
            res_data['jy_zz_fd'] = df2.iloc[n][4]
            res_data['zf_zhlv'] = df2.iloc[n][5]

            models.Scph_dp_gjy.objects.create(**res_data)

    def gq_scph_bjb_dp_gll(self, file_obj):
        df1 = pd.read_csv(file_obj)
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['dp_xx'] = df2.iloc[n][0]
            res_data['riqi'] = df2.iloc[n][1]
            res_data['hy_pm'] = df2.iloc[n][2]
            res_data['fk_rs'] = df2.iloc[n][3]
            res_data['ss_rs'] = df2.iloc[n][4]
            res_data['ss_zb'] = df2.iloc[n][5]
            res_data['jy_je'] = df2.iloc[n][6]
            res_data['uv_jz'] = df2.iloc[n][7]

            models.Scph_dp_gll.objects.create(**res_data)

    def gq_scph_bjb_pp_gjy(self, file_obj):
        df1 = pd.read_csv(file_obj)
        df2 = df1.fillna(0)
        print(df2.dtypes)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['pinp_xinx'] = df2.iloc[n][0]
            res_data['riqi'] = df2.iloc[n][1]
            res_data['hy_pm'] = df2.iloc[n][2]
            res_data['jy_je'] = df2.iloc[n][3]
            res_data['jy_zz_fd'] = df2.iloc[n][4]
            res_data['zf_zhlv'] = df2.iloc[n][5]

            models.Scph_pp_gjy.objects.create(**res_data)

    def gq_scph_bjb_pp_gll(self, file_obj):
        df1 = pd.read_csv(file_obj)
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['dp_xx'] = df2.iloc[n][0]
            res_data['riqi'] = df2.iloc[n][1]
            res_data['hy_pm'] = df2.iloc[n][2]
            res_data['fk_rs'] = df2.iloc[n][3]
            res_data['ss_rs'] = df2.iloc[n][4]
            res_data['ss_zb'] = df2.iloc[n][5]
            res_data['jy_je'] = df2.iloc[n][6]
            res_data['uv_jz'] = df2.iloc[n][7]

            models.Scph_pp_gll.objects.create(**res_data)

    def gq_scph_bjb_sp_gjy(self, file_obj):
        df1 = pd.read_csv(file_obj)
        df2 = df1.fillna(0)
        print(df2.dtypes)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['dp_xx'] = df2.iloc[n][0]
            res_data['dp_mc'] = df2.iloc[n][1]
            res_data['sp_id'] = df2.iloc[n][2]
            res_data['riqi'] = df2.iloc[n][3]
            res_data['hy_pm'] = df2.iloc[n][4]
            res_data['jy_je'] = df2.iloc[n][5]
            res_data['jy_zz_fd'] = df2.iloc[n][6]
            res_data['zf_zhlv'] = df2.iloc[n][7]

            models.Scph_sp_gjy.objects.create(**res_data)

    def gq_scph_bjb_sp_gll(self, file_obj):
        df1 = pd.read_csv(file_obj)
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['dp_xx'] = df2.iloc[n][0]
            res_data['dp_mc'] = df2.iloc[n][1]
            res_data['sp_id'] = df2.iloc[n][2]
            res_data['riqi'] = df2.iloc[n][3]
            res_data['hy_pm'] = df2.iloc[n][4]
            res_data['fk_rs'] = df2.iloc[n][5]
            res_data['ss_rs'] = df2.iloc[n][6]
            res_data['ss_zb'] = df2.iloc[n][7]
            res_data['jy_je'] = df2.iloc[n][8]
            res_data['uv_jz'] = df2.iloc[n][9]

            models.Scph_sp_gll.objects.create(**res_data)

    def gq_scph_bjb_sp_gyx(self, file_obj):
        df1 = pd.read_csv(file_obj)
        df2 = df1.fillna(0)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['dp_xx'] = df2.iloc[n][0]
            res_data['dp_mc'] = df2.iloc[n][1]
            res_data['sp_id'] = df2.iloc[n][2]
            res_data['riqi'] = df2.iloc[n][3]
            res_data['hy_pm'] = df2.iloc[n][4]
            res_data['sc_rs'] = df2.iloc[n][5]
            res_data['jg_rs'] = df2.iloc[n][6]
            res_data['jy_je'] = df2.iloc[n][7]

            models.Scph_sp_gyx.objects.create(**res_data)

    def dp_gq_sc_sxdc_d(self, file_obj):
        df1 = pd.read_excel(file_obj)
        df2 = df1.fillna(0)
        print(df2.dtypes)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['riqi'] = df2.iloc[n][0]
            res_data['sx'] = df2.iloc[n][1]
            res_data['sxz'] = df2.iloc[n][2]
            res_data['jy_zs'] = df2.iloc[n][3]
            res_data['zf_js'] = df2.iloc[n][4]
            res_data['caozuo'] = df2.iloc[n][5]

            models.Scdp_Sxdc_d.objects.create(**res_data)

    def dp_gq_sc_sxdc_m(self, file_obj):
        df1 = pd.read_excel(file_obj)
        df2 = df1.fillna(0)
        print(df2.dtypes)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['jt_pl'] = df2.iloc[n][0]
            res_data['tj_sj'] = df2.iloc[n][1]
            res_data['sx'] = df2.iloc[n][2]
            res_data['sxz'] = df2.iloc[n][3]
            res_data['jy_zs'] = df2.iloc[n][4]
            res_data['zf_js'] = df2.iloc[n][5]
            res_data['caozuo'] = df2.iloc[n][6]

            models.Scdp_Sxdc_m.objects.create(**res_data)

    def dp_gq_sc_ssph(self, file_obj):
        pass

    def dp_gq_mc_bb(self, file_obj):
        df1 = pd.read_csv(file_obj, encoding='gbk')
        df2 = df1.fillna(0)
        print(df2.dtypes)

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['dd_bh'] = df2.iloc[n][0]
            res_data['title'] = df2.iloc[n][1]
            res_data['jiage'] = df2.iloc[n][2]
            res_data['gm_sl'] = df2.iloc[n][3]
            res_data['wb_xt_bh'] = df2.iloc[n][4]
            res_data['sp_sx'] = df2.iloc[n][5]
            res_data['tc_xx'] = df2.iloc[n][6]
            res_data['beizhu'] = df2.iloc[n][7]
            res_data['dd_zt'] = df2.iloc[n][8]
            res_data['sj_bm'] = df2.iloc[n][9]

            models.Gq_Mcbb_bb.objects.create(**res_data)

    def dp_gq_mc_dd(self, file_obj):
        df1 = pd.read_csv(file_obj, encoding='gbk')
        df2 = df1.fillna(0)
        print(df2.dtypes)

        # res_data = {}
        # for n in range(df2.shape[0]):
        #     pass


def auth(func):
    """
    装饰器功能，登录验证,erp登录保存session
    :param func:
    :return:
    """
    def inner(request,*args,**kwargs):
        return func(request,*args,**kwargs)
    return inner


class DataUpload(View):
    """数据上传模块"""

    @method_decorator(auth)
    def dispatch(self, request, *args, **kwargs):
        return super(DataUpload, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'data_upload.html')

    def post(self, request):
        """数据上传处理方法"""
        msg = {'code': None}

        table_lx = request.POST.get('leixing')
        file_obj = request.FILES.get('file')
        print(file_obj.name, table_lx)

        if hasattr(OperData, table_lx):  # 利用反射
            func = getattr(OperData, table_lx)
            func(table_lx, file_obj)

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
