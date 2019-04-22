from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from upload import models
import os
import json
import pandas as pd


class OperData(object):

    def kc_splr(self, file_obj):
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

            models.KcErpSplr.objects.create(**res_data)

    def kc_kccx(self, file_obj):
        """处理库存/库存查询的模板"""
        df = pd.read_excel(file_obj)
        # # 遍历所有列名，排除不需要的
        cols = [i for i in df.columns if i not in ['分库数', '调拨', '拆装', '来源', '单位', '供货商 ']]
        df1 = df[cols]
        df2 = df1.fillna(0)

        riqi = file_obj.name[4:12]
        rq = riqi[:4] + '-' + riqi[4:6] + '-' + riqi[6:8]

        res_data = {}
        for n in range(df2.shape[0]):
            res_data['riqi'] = rq
            res_data['spbm'] = df2.iloc[n][0]
            res_data['leibie'] = df2.iloc[n][1]
            res_data['pinpai'] = df2.iloc[n][2]
            res_data['spmc'] = df2.iloc[n][3]
            res_data['zsl'] = df2.iloc[n][4]
            res_data['kxs'] = df2.iloc[n][5]
            res_data['djcb'] = df2.iloc[n][6]
            res_data['je'] = df2.iloc[n][7]
            res_data['cwkc'] = df2.iloc[n][8]
            res_data['hsbz'] = df2.iloc[n][9]
            res_data['hsxj'] = df2.iloc[n][10]
            res_data['wsxj'] = df2.iloc[n][11]
            res_data['dairu'] = df2.iloc[n][12]
            res_data['daichu'] = df2.iloc[n][13]
            res_data['sczt'] = df2.iloc[n][14]
            res_data['daishen'] = df2.iloc[n][15]
            res_data['huola'] = df2.iloc[n][16]
            res_data['zl'] = df2.iloc[n][17]
            res_data['xz'] = df2.iloc[n][18]
            res_data['zhcgsj'] = df2.iloc[n][19]
            res_data['hsyj'] = df2.iloc[n][20]
            res_data['wsyj'] = df2.iloc[n][21]

            models.KcErpKccx.objects.create(**res_data)

    def kc_ydh(self, file_obj):
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

            models.KcErpYdh.objects.create(**res_data)

    def kc_zksp(self, file_obj):
        """库存，在库商品分析模板"""
        df = pd.read_excel(file_obj)
        # # 遍历所有列名，排除不需要的
        cols = [i for i in df.columns if i not in ['商品条码']]
        df1 = df[cols]
        df2 = df1.fillna(0)

        riqi = file_obj.name[6:14]
        rq = riqi[:4] + '-' + riqi[4:6] + '-' + riqi[6:8]

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

            models.KcErpZksp.objects.create(**res_data)

    def kc_spxx(self, file_obj):
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

            models.KcSpxx.objects.create(**res_data)

    def kc_xhbm(self, file_obj):
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

            models.KcXhSpbm.objects.create(**res_data)

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
            res_data['tjrq'] = df2.iloc[n][0].replace(',','')
            res_data['pc_fk'] = df2.iloc[n][1].replace(',','')
            res_data['pc_ll'] = df2.iloc[n][2].replace(',','')
            res_data['fks'] = df2.iloc[n][3].replace(',','')
            res_data['wx_fk'] = df2.iloc[n][4].replace(',','')
            res_data['lll'] = df2.iloc[n][5].replace(',','')
            res_data['wx_ll'] = df2.iloc[n][6].replace(',','')
            res_data['sp_fks'] = df2.iloc[n][7].replace(',','')
            res_data['wx_sp_fk'] = df2.iloc[n][8].replace(',','')
            res_data['pc_sp_fk'] = df2.iloc[n][9].replace(',','')
            res_data['sp_ll'] = df2.iloc[n][10].replace(',','')
            res_data['wx_sp_ll'] = df2.iloc[n][11].replace(',','')
            res_data['pc_sp_ll'] = df2.iloc[n][12].replace(',','')
            res_data['pjtlsc'] = df2.iloc[n][13].replace(',','')
            res_data['wx_pj_tlsc'] = df2.iloc[n][14].replace(',','')
            res_data['pc_pj_tlsc'] = df2.iloc[n][15].replace(',','')
            res_data['tsl'] = df2.iloc[n][16].replace(',','')
            res_data['wx_tsl'] = df2.iloc[n][17].replace(',','')
            res_data['pc_tsl'] = df2.iloc[n][18].replace(',','')
            res_data['sp_scmj'] = df2.iloc[n][19].replace(',','')
            res_data['wx_sp_scmj'] = df2.iloc[n][20].replace(',','')
            res_data['pc_sp_scmj'] = df2.iloc[n][21].replace(',','')
            res_data['sp_sccs'] = df2.iloc[n][22].replace(',','')
            res_data['wx_sp_sccs'] = df2.iloc[n][23].replace(',','')
            res_data['pc_sp_sccs'] = df2.iloc[n][24].replace(',','')
            res_data['jgrs'] = df2.iloc[n][25].replace(',','')
            res_data['wx_jgrs'] = df2.iloc[n][26].replace(',','')
            res_data['pc_jgrs'] = df2.iloc[n][27].replace(',','')
            res_data['zfje'] = df2.iloc[n][28].replace(',','')
            res_data['pc_zfje'] = df2.iloc[n][29].replace(',','')
            res_data['wx_zfje'] = df2.iloc[n][30].replace(',','')
            res_data['zfmjs'] = df2.iloc[n][31].replace(',','')
            res_data['pc_zfmjs'] = df2.iloc[n][32].replace(',','')
            res_data['wx_zfmjs'] = df2.iloc[n][33].replace(',','')
            res_data['zfzdds'] = df2.iloc[n][34].replace(',','')
            res_data['pc_zfzdds'] = df2.iloc[n][35].replace(',','')
            res_data['wx_zfzdds'] = df2.iloc[n][36].replace(',','')
            res_data['zfjs'] = df2.iloc[n][37].replace(',','')
            res_data['pc_zfjs'] = df2.iloc[n][38].replace(',','')
            res_data['wx_zfjs'] = df2.iloc[n][39].replace(',','')
            res_data['xdje'] = df2.iloc[n][40].replace(',','')
            res_data['pc_xdje'] = df2.iloc[n][41].replace(',','')
            res_data['mwx_xdje'] = df2.iloc[n][42].replace(',','')
            res_data['xdmjs'] = df2.iloc[n][43].replace(',','')
            res_data['pc_xdmjs'] = df2.iloc[n][44].replace(',','')
            res_data['wx_xdmjs'] = df2.iloc[n][45].replace(',','')
            res_data['xdjs'] = df2.iloc[n][46].replace(',','')
            res_data['pc_xdjs'] = df2.iloc[n][47].replace(',','')
            res_data['wx_xdjs'] = df2.iloc[n][48].replace(',','')
            res_data['rjlll'] = df2.iloc[n][49].replace(',','')
            res_data['pc_rjll'] = df2.iloc[n][50].replace(',','')
            res_data['wx_rjll'] = df2.iloc[n][51].replace(',','')
            res_data['xdzhl'] = df2.iloc[n][52].replace(',','')
            res_data['pc_xdzhl'] = df2.iloc[n][53].replace(',','')
            res_data['wx_xdzhl'] = df2.iloc[n][54].replace(',','')
            res_data['zfzhl'] = df2.iloc[n][55].replace(',','')
            res_data['pc_zfzhl'] = df2.iloc[n][56].replace(',','')
            res_data['wx_zfzhl'] = df2.iloc[n][57].replace(',','')
            res_data['kdj'] = df2.iloc[n][58].replace(',','')
            res_data['pc_kdj'] = df2.iloc[n][59].replace(',','')
            res_data['wx_kdj'] = df2.iloc[n][60].replace(',','')
            res_data['uvjz'] = df2.iloc[n][61].replace(',','')
            res_data['pc_uvjz'] = df2.iloc[n][62].replace(',','')
            res_data['wx_uvjz'] = df2.iloc[n][63].replace(',','')
            res_data['old_fks'] = df2.iloc[n][64].replace(',','')
            res_data['new_fks'] = df2.iloc[n][65].replace(',','')
            res_data['wx_old_fks'] = df2.iloc[n][66].replace(',','')
            res_data['wx_new_fks'] = df2.iloc[n][67].replace(',','')
            res_data['pc_old_fks'] = df2.iloc[n][68].replace(',','')
            res_data['pc_new_fks'] = df2.iloc[n][69].replace(',','')
            res_data['jgjs'] = df2.iloc[n][70].replace(',','')
            res_data['pc_jgjs'] = df2.iloc[n][71].replace(',','')
            res_data['wx_jgjs'] = df2.iloc[n][72].replace(',','')
            res_data['zf_old_mjs'] = df2.iloc[n][73].replace(',','')
            res_data['pc_zf_old_mjs'] = df2.iloc[n][74].replace(',','')
            res_data['wx_zf_old_mjs'] = df2.iloc[n][75].replace(',','')
            res_data['old_mj_zfje'] = df2.iloc[n][76].replace(',','')
            res_data['ztc_xh'] = df2.iloc[n][77].replace(',','')
            res_data['zsz_xh'] = df2.iloc[n][78].replace(',','')
            res_data['tbk_yj'] = df2.iloc[n][79].replace(',','')
            res_data['cgtk_je'] = df2.iloc[n][80].replace(',','')
            res_data['pjs'] = df2.iloc[n][81].replace(',','')
            res_data['yt_pjs'] = df2.iloc[n][82].replace(',','')
            res_data['zm_pjs'] = df2.iloc[n][83].replace(',','')
            res_data['fm_pjs'] = df2.iloc[n][84].replace(',','')
            res_data['old_mj_zm_pjs'] = df2.iloc[n][85].replace(',','')
            res_data['old_mj_fm_pjs'] = df2.iloc[n][86].replace(',','')
            res_data['zf_fdds'] = df2.iloc[n][87].replace(',','')
            res_data['ls_bgs'] = df2.iloc[n][88].replace(',','')
            res_data['fh_bgs'] = df2.iloc[n][89].replace(',','')
            res_data['ps_bgs'] = df2.iloc[n][90].replace(',','')
            res_data['qscg_bgs'] = df2.iloc[n][91].replace(',','')
            res_data['pjzf_qs_sc'] = df2.iloc[n][92].replace(',','')
            res_data['msxf_pf'] = df2.iloc[n][93].replace(',','')
            res_data['wlfw_pf'] = df2.iloc[n][94].replace(',','')
            res_data['wftd_pf'] = df2.iloc[n][95].replace(',','')
            res_data['xd_zf_zhl'] = df2.iloc[n][96].replace(',','')
            res_data['pc_xd_zf_zhl'] = df2.iloc[n][97].replace(',','')
            res_data['wx_xd_zf_zhl'] = df2.iloc[n][98].replace(',','')
            res_data['zf_sps'] = df2.iloc[n][99].replace(',','')
            res_data['pc_zf_sps'] = df2.iloc[n][100].replace(',','')
            res_data['wx_zf_sps'] = df2.iloc[n][101].replace(',','')
            res_data['dp_sc_mjs'] = df2.iloc[n][102].replace(',','')
            res_data['pc_dp_sc_mjs'] = df2.iloc[n][103].replace(',','')
            res_data['wx_dp_sc_mjs'] = df2.iloc[n][104].replace(',','')

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
            res_data['fks'] = df2.iloc[n][2].replace(',','')
            res_data['fks_bh'] = df2.iloc[n][3].replace(',','')
            res_data['xd_je'] = df2.iloc[n][4].replace(',','')
            res_data['xd_je_bh'] = df2.iloc[n][5].replace(',','')
            res_data['xd_mjs'] = df2.iloc[n][6].replace(',','')
            res_data['xd_mjs_bh'] = df2.iloc[n][7].replace(',','')
            res_data['xd_zhlv'] = df2.iloc[n][8].replace(',','')
            res_data['xd_zhlv_bh'] = df2.iloc[n][9].replace(',','')
            res_data['zf_je'] = df2.iloc[n][10].replace(',','')
            res_data['zf_je_bh'] = df2.iloc[n][11].replace(',','')
            res_data['zf_mjs'] = df2.iloc[n][12].replace(',','')
            res_data['zf_mjs_bh'] = df2.iloc[n][13].replace(',','')
            res_data['zf_zhlv'] = df2.iloc[n][14].replace(',','')
            res_data['zf_zhlv_bh'] = df2.iloc[n][15].replace(',','')
            res_data['kdj'] = df2.iloc[n][16].replace(',','')
            res_data['kdj_bh'] = df2.iloc[n][17].replace(',','')
            res_data['uv_jz'] = df2.iloc[n][18].replace(',','')
            res_data['uv_jz_bh'] = df2.iloc[n][19].replace(',','')
            res_data['gz_dp_mjs'] = df2.iloc[n][20].replace(',','')
            res_data['gz_dp_mjs_bh'] = df2.iloc[n][21].replace(',','')
            res_data['sc_sp_mjs'] = df2.iloc[n][22].replace(',','')
            res_data['sc_sp_mjs_bh'] = df2.iloc[n][23].replace(',','')
            res_data['jg_rs'] = df2.iloc[n][24].replace(',','')
            res_data['jg_rs_bh'] = df2.iloc[n][25].replace(',','')
            res_data['x_fk'] = df2.iloc[n][26].replace(',','')
            res_data['x_fk_bh'] = df2.iloc[n][27].replace(',','')
            res_data['zj_zf_mjs'] = df2.iloc[n][28].replace(',','')
            res_data['scsp_zf_mj'] = df2.iloc[n][29].replace(',','')
            res_data['fs_zf_mjs'] = df2.iloc[n][30].replace(',','')
            res_data['jg_sp_zfmj'] = df2.iloc[n][31].replace(',','')

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
            res_data['sp_fks'] = df2.iloc[n][4].replace(',','')
            res_data['sp_lll'] = df2.iloc[n][5].replace(',','')
            res_data['yfk_sps'] = df2.iloc[n][6].replace(',','')
            res_data['yzf_sps'] = df2.iloc[n][7].replace(',','')
            res_data['sp_jgs'] = df2.iloc[n][8].replace(',','')
            res_data['sp_jg_js'] = df2.iloc[n][9].replace(',','')
            res_data['sp_sc_rs'] = df2.iloc[n][10].replace(',','')
            res_data['fw_sc_zhlv'] = df2.iloc[n][11].replace(',','')
            res_data['fw_jg_zhlv'] = df2.iloc[n][12].replace(',','')
            res_data['xd_mjs'] = df2.iloc[n][13].replace(',','')
            res_data['xd_js'] = df2.iloc[n][14].replace(',','')
            res_data['xd_je'] = df2.iloc[n][15].replace(',','')
            res_data['xd_zhlv'] = df2.iloc[n][16].replace(',','')
            res_data['zf_mjs'] = df2.iloc[n][17].replace(',','')
            res_data['zf_js'] = df2.iloc[n][18].replace(',','')
            res_data['zf_je'] = df2.iloc[n][19].replace(',','')
            res_data['zf_zhlv'] = df2.iloc[n][20].replace(',','')
            res_data['m_lj_zfje'] = df2.iloc[n][21].replace(',','')
            res_data['y_lj_zfje'] = df2.iloc[n][22].replace(',','')
            res_data['jhs_zfje'] = df2.iloc[n][23].replace(',','')
            res_data['zf_xmj'] = df2.iloc[n][24].replace(',','')
            res_data['zf_lmj'] = df2.iloc[n][25].replace(',','')
            res_data['lmj_zfje'] = df2.iloc[n][26].replace(',','')
            res_data['kdj'] = df2.iloc[n][27].replace(',','')
            res_data['fk_pj_jz'] = df2.iloc[n][28].replace(',','')
            res_data['sh_tkje'] = df2.iloc[n][29].replace(',','')

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

    def gq_scph_bjb_dp_gjy(self,file_obj):
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

    def gq_scph_bjb_dp_gll(self,file_obj):
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

    def gq_scph_bjb_pp_gjy(self,file_obj):
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

    def gq_scph_bjb_pp_gll(self,file_obj):
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

    def gq_scph_bjb_sp_gjy(self,file_obj):
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

    def gq_scph_bjb_sp_gll(self,file_obj):
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

    def gq_scph_bjb_sp_gyx(self,file_obj):
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
        df1 = pd.read_csv(file_obj,encoding='gbk')
        df2 = df1.fillna(0)
        print(df2.dtypes)

        # res_data = {}
        # for n in range(df2.shape[0]):
        #     pass


class DataUpload(View):
    """数据上传模块"""

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
