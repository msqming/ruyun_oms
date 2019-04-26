from django.db import models


class KcErpKccx(models.Model):
    """库存数据，ERP库存查询"""
    riqi = models.DateField(verbose_name='日期')
    spbm = models.CharField(max_length=64, verbose_name='商品编码')
    leibie = models.CharField(max_length=32, verbose_name='类别')
    pinpai = models.CharField(max_length=32, verbose_name='品牌')
    spmc = models.CharField(max_length=128, verbose_name='商品名称')
    zsl = models.IntegerField(verbose_name='总数量')
    kxs = models.FloatField(verbose_name='可销数')
    djcb = models.FloatField(verbose_name='单价成本')
    je = models.FloatField(verbose_name='金额')
    cwkc = models.IntegerField(verbose_name='财务库存')
    hsbz = models.FloatField(verbose_name='含税比重')
    hsxj = models.FloatField(verbose_name='含税限价')
    wsxj = models.FloatField(verbose_name='未税限价')
    dairu = models.FloatField(verbose_name='待入')
    daichu = models.FloatField(verbose_name='待出')
    sczt = models.FloatField(verbose_name='生产在途')
    daishen = models.FloatField(verbose_name='待审')
    huola = models.CharField(max_length=64, verbose_name='货拉')
    zl = models.FloatField(verbose_name='重量')
    xz = models.CharField(max_length=16, verbose_name='性质')
    zhcgsj = models.CharField(max_length=32, verbose_name='最后采购时间')
    hsyj = models.FloatField(verbose_name='含税预计')
    wsyj = models.FloatField(verbose_name='未税预计')


class KcErpSplr(models.Model):
    """库存数据 ERP商品利润"""
    cksj = models.CharField(max_length=32, verbose_name='出库时间')
    zfrq = models.CharField(max_length=32, verbose_name='支付日期')
    khmc = models.CharField(max_length=64, verbose_name='客户名称')
    spbm = models.CharField(max_length=128, verbose_name='商品编码')
    leibie = models.CharField(max_length=32, verbose_name='类别')
    pinpai = models.CharField(max_length=32, verbose_name='品牌')
    guige = models.CharField(max_length=512, verbose_name='规格')
    xilie = models.CharField(max_length=64, verbose_name='系列')
    xh = models.CharField(max_length=64, verbose_name='型号')
    spmc = models.CharField(max_length=256, verbose_name='商品名称')
    xz = models.IntegerField(verbose_name='性质')
    leixing = models.CharField(max_length=16, verbose_name='类型')
    danhao = models.CharField(max_length=64, verbose_name='单号')
    wddh = models.CharField(max_length=128, verbose_name='网店单号')
    hyh = models.CharField(max_length=64, verbose_name='会员号')
    daofu = models.IntegerField(verbose_name='到付')
    zhiyuan = models.CharField(max_length=64, verbose_name='职员')
    sl = models.FloatField(verbose_name='数量')
    xsdj = models.FloatField(verbose_name='销售单价')
    yjcbdj = models.FloatField(verbose_name='预计成本单价')
    xsje = models.FloatField(verbose_name='销售金额')
    spzk = models.FloatField(verbose_name='商品折扣')
    yjzcb = models.FloatField(verbose_name='预计总成本')
    yjml_hyf = models.FloatField(verbose_name='预计毛利_含运费')
    cgcb = models.FloatField(verbose_name='采购成本')
    piao = models.IntegerField(verbose_name='票')
    zhcb = models.FloatField(verbose_name='折合成本')
    cbje = models.FloatField(verbose_name='成本金额')
    mlr = models.FloatField(verbose_name='毛利润')
    mllv = models.CharField(max_length=16,verbose_name='毛利率')
    zhlr = models.FloatField(verbose_name='折合利润')
    zh_lrlv = models.CharField(max_length=16,verbose_name='折合利润率')
    yf_cb = models.FloatField(verbose_name='运费成本')
    pt_fy = models.FloatField(verbose_name='平台费用')
    fx_fy = models.FloatField(verbose_name='返现费用')
    qt_fy = models.FloatField(verbose_name='其他费用')
    yj_ml = models.FloatField(verbose_name='预计毛利')
    yj_mllv = models.CharField(max_length=16, verbose_name='预计毛利率')
    yj_jlr = models.FloatField(verbose_name='预计净利润')
    yj_jlrlv = models.CharField(max_length=16,verbose_name='预计净利润率')
    pd_sj = models.CharField(max_length=32, verbose_name='拍单时间')
    bumen = models.CharField(max_length=16, verbose_name='部门')


class KcErpYdh(models.Model):
    """ERP预到货数据"""
    cjsj = models.CharField(max_length=32, null=False, verbose_name='创建时间')
    yjdh = models.CharField(max_length=32, verbose_name='预计到货')
    cqts = models.FloatField(verbose_name='超期天数')
    danhao = models.CharField(max_length=32, verbose_name='单号')
    ks = models.CharField(max_length=64, verbose_name='客商')
    spbm = models.CharField(max_length=64, verbose_name='商品编码')
    spmc = models.CharField(max_length=256, verbose_name='商品名称')
    ywy = models.CharField(max_length=32, verbose_name='业务员')
    kds = models.IntegerField(verbose_name='开单数')
    danjia = models.FloatField(verbose_name='单价')
    jine = models.FloatField(verbose_name='金额')
    ydh = models.FloatField(verbose_name='已到货')
    wds = models.IntegerField(verbose_name='未到数')
    wdje = models.FloatField(verbose_name='未到金额')


class KcErpZksp(models.Model):
    """ERP在库商品模板"""
    riqi = models.DateField(null=False, verbose_name='日期')
    zhjhrq = models.CharField(max_length=32, verbose_name='最后进货日期')
    spjdrq = models.CharField(max_length=32, verbose_name='商品建档日期')
    kufang = models.CharField(max_length=32, verbose_name='库房')
    hl = models.CharField(max_length=32, verbose_name='货拉')
    lbmc = models.CharField(max_length=64, verbose_name='类别名称')
    spbm = models.CharField(max_length=64, verbose_name='商品编码')
    spmc = models.CharField(max_length=256, verbose_name='商品名称')
    xh = models.CharField(max_length=64, verbose_name='型号')
    guige = models.CharField(max_length=256, verbose_name='规格')
    pinpai = models.CharField(max_length=64, verbose_name='品牌')
    zks = models.FloatField(verbose_name='在库数')
    qjxss = models.FloatField(verbose_name='区间销售数')


class KcXhSpbm(models.Model):
    """各平台型号与商品编码对照表"""
    pingtai = models.CharField(max_length=64, verbose_name='平台')
    xinghao = models.CharField(max_length=32, verbose_name='型号')
    spbm = models.CharField(max_length=128, verbose_name='商品编码')


class KcSpxx(models.Model):
    """库存商品信息表"""
    xinghao = models.CharField(max_length=32, null=False, verbose_name='型号')
    pinlei = models.CharField(max_length=68, verbose_name='品类')
    new_old = models.CharField(max_length=16, verbose_name='新旧品')
    dingwei = models.CharField(max_length=64, null=False, verbose_name='定位')
    pinming = models.CharField(max_length=128, null=False, verbose_name='品名')
    cpu = models.CharField(max_length=16, verbose_name='CPU')
    xianka = models.CharField(max_length=64, verbose_name='显卡')
    neicun = models.CharField(max_length=32, verbose_name='内存')
    ssd = models.CharField(max_length=64, verbose_name='SSD')
    hhd = models.CharField(max_length=64, verbose_name='HHD')
    model_name = models.CharField(max_length=128, verbose_name='模具名称')
    config = models.CharField(max_length=256, verbose_name='配置')
    pn = models.CharField(max_length=16, null=True, verbose_name='pn')


class CwJqcb(models.Model):
    """财务数据，机器成本"""
    riqi = models.DateField(verbose_name="日期")
    erp_name = models.CharField(max_length=256, verbose_name='ERP名称')
    chenben = models.FloatField(verbose_name='成本')


class CwBjbTopM(models.Model):
    """财务笔记本top月度KPI"""
    comm_id = models.BigIntegerField(verbose_name='商品ID')
    shijian = models.CharField(max_length=32, verbose_name='年月')
    mbzfjs = models.IntegerField(verbose_name='月目标支付件数')
    mbuv = models.IntegerField(verbose_name='月目标UV')
    bmzhl = models.FloatField(verbose_name='月目标转化率')


class CwBjbTopW(models.Model):
    """财务笔记本top周度KPI"""
    comm_id = models.BigIntegerField(verbose_name='商品ID')
    hdzq = models.CharField(max_length=32, verbose_name='活动周期')
    mbzfjs = models.IntegerField(verbose_name='当前活动目标总支付件数')
    mbuv = models.IntegerField(verbose_name='当前活动目标总UV')
    bmzhl = models.FloatField(verbose_name='当前活动目标转化率')


class CwBjbXlW(models.Model):
    """财务笔记本系列周度KPI"""
    shijian = models.CharField(max_length=32, verbose_name='年月周')
    bjbxl = models.CharField(max_length=32, verbose_name='笔记本系列')
    mbxse = models.BigIntegerField(verbose_name='周目标销售额')
    mbxl = models.IntegerField(verbose_name='周目标销量')


class CwGplM(models.Model):
    """财务各品类月度KPI"""
    shijian = models.CharField(max_length=32, verbose_name='年月周')
    pinlei = models.CharField(max_length=32, verbose_name='品类')
    mbxse = models.BigIntegerField(verbose_name='月度目标销售额')
    mbxl = models.IntegerField(verbose_name='月度目标销量')


class CwGplW(models.Model):
    """财务各品类周度KPI"""
    shijian = models.CharField(max_length=32, verbose_name='年月周')
    pinlei = models.CharField(max_length=32, verbose_name='品类')
    huod = models.CharField(max_length=128, verbose_name='运营活动')
    mbxse = models.BigIntegerField(verbose_name='周度目标销售额')
    mbxl = models.IntegerField(verbose_name='周度目标销量')


class DpGk(models.Model):
    """店铺概况105指标"""
    tjrq = models.CharField(max_length=32, verbose_name='统计日期')
    pc_fk = models.CharField(max_length=32, verbose_name='PC端访客数')
    pc_ll = models.CharField(max_length=32, verbose_name='PC端浏览量')
    fks = models.CharField(max_length=32, verbose_name='访客数')
    wx_fk = models.CharField(max_length=32, verbose_name='无线端访客数')
    lll = models.CharField(max_length=32, verbose_name='浏览量')
    wx_ll = models.CharField(max_length=32, verbose_name='无线端浏览量')
    sp_fks = models.CharField(max_length=32, verbose_name='商品访客数')
    wx_sp_fk = models.CharField(max_length=32, verbose_name='无线端商品访客数')
    pc_sp_fk = models.CharField(max_length=32, verbose_name='PC端商品访客数')
    sp_ll = models.CharField(max_length=32, verbose_name='商品浏览量')
    wx_sp_ll = models.CharField(max_length=32, verbose_name='无线端商品浏览量')
    pc_sp_ll = models.CharField(max_length=32, verbose_name='PC端商品浏览量')
    pjtlsc = models.CharField(max_length=32, verbose_name='平均停留时长')
    wx_pj_tlsc = models.CharField(max_length=32, verbose_name='无线端平均停留时长')
    pc_pj_tlsc = models.CharField(max_length=32, verbose_name='PC端平均停留时长')
    tsl = models.CharField(max_length=32, verbose_name='跳失率')
    wx_tsl = models.CharField(max_length=32, verbose_name='无线端跳失率')
    pc_tsl = models.CharField(max_length=32, verbose_name='PC端跳失率')
    sp_scmj = models.CharField(max_length=32, verbose_name='商品收藏买家数')
    wx_sp_scmj = models.CharField(max_length=32, verbose_name='无线端商品收藏买家')
    pc_sp_scmj = models.CharField(max_length=32, verbose_name='PC端商品收藏买家数')
    sp_sccs = models.CharField(max_length=32, verbose_name='商品收藏次数')
    wx_sp_sccs = models.CharField(max_length=32, verbose_name='无线端商品收藏次数')
    pc_sp_sccs = models.CharField(max_length=32, verbose_name='PC端商品收藏次数')
    jgrs = models.CharField(max_length=32, verbose_name='加购人数')
    wx_jgrs = models.CharField(max_length=32, verbose_name='无线端加购人数')
    pc_jgrs = models.CharField(max_length=32, verbose_name='PC端加购人数')
    zfje = models.CharField(max_length=32, verbose_name='支付金额')
    pc_zfje = models.CharField(max_length=32, verbose_name='PC端支付金额')
    wx_zfje = models.CharField(max_length=32, verbose_name='无线端支付金额')
    zfmjs = models.CharField(max_length=32, verbose_name='支付买家数')
    pc_zfmjs = models.CharField(max_length=32, verbose_name='PC端支付买家数')
    wx_zfmjs = models.CharField(max_length=32, verbose_name='无线端支付买家数')
    zfzdds = models.CharField(max_length=32, verbose_name='支付子订单数')
    pc_zfzdds = models.CharField(max_length=32, verbose_name='PC端支付子订单数')
    wx_zfzdds = models.CharField(max_length=32, verbose_name='无线端支付子订单数')
    zfjs = models.CharField(max_length=32, verbose_name='支付件数')
    pc_zfjs = models.CharField(max_length=32, verbose_name='PC端支付件数')
    wx_zfjs = models.CharField(max_length=32, verbose_name='无线端支付件数')
    xdje = models.CharField(max_length=32, verbose_name='下单金额')
    pc_xdje = models.CharField(max_length=32, verbose_name='PC端下单金额')
    mwx_xdje = models.CharField(max_length=32, verbose_name='无线端下单金额')
    xdmjs = models.CharField(max_length=32, verbose_name='下单买家数')
    pc_xdmjs = models.CharField(max_length=32, verbose_name='PC端下单买家数')
    wx_xdmjs = models.CharField(max_length=32, verbose_name='无线端下单买家数')
    xdjs = models.CharField(max_length=32, verbose_name='下单件数')
    pc_xdjs = models.CharField(max_length=32, verbose_name='PC端下单件数')
    wx_xdjs = models.CharField(max_length=32, verbose_name='无线端下单件数')
    rjlll = models.CharField(max_length=32, verbose_name='人均浏览量')
    pc_rjll = models.CharField(max_length=32, verbose_name='PC端人均浏览量')
    wx_rjll = models.CharField(max_length=32, verbose_name='无线端人均浏览量')
    xdzhl = models.CharField(max_length=32, verbose_name='下单转化率')
    pc_xdzhl = models.CharField(max_length=32, verbose_name='PC端下单转化率')
    wx_xdzhl = models.CharField(max_length=32, verbose_name='无线端下单转化率')
    zfzhl = models.CharField(max_length=32, verbose_name='支付转化率')
    pc_zfzhl = models.CharField(max_length=32, verbose_name='PC端支付转化率')
    wx_zfzhl = models.CharField(max_length=32, verbose_name='无线端支付转化率')
    kdj = models.CharField(max_length=32, verbose_name='客单价')
    pc_kdj = models.CharField(max_length=32, verbose_name='PC端客单价')
    wx_kdj = models.CharField(max_length=32, verbose_name='无线端客单价')
    uvjz = models.CharField(max_length=32, verbose_name='UV价值')
    pc_uvjz = models.CharField(max_length=32, verbose_name='PC端UV价值')
    wx_uvjz = models.CharField(max_length=32, verbose_name='无线端UV价值')
    old_fks = models.CharField(max_length=32, verbose_name='老访客数')
    new_fks = models.CharField(max_length=32, verbose_name='新访客数')
    wx_old_fks = models.CharField(max_length=32, verbose_name='无线端老访客数')
    wx_new_fks = models.CharField(max_length=32, verbose_name='无线端新访客数')
    pc_old_fks = models.CharField(max_length=32, verbose_name='PC端老访客数')
    pc_new_fks = models.CharField(max_length=32, verbose_name='PC端新访客数')
    jgjs = models.CharField(max_length=32, verbose_name='加购件数')
    pc_jgjs = models.CharField(max_length=32, verbose_name='PC端加购件数')
    wx_jgjs = models.CharField(max_length=32, verbose_name='无线端加购件数')
    zf_old_mjs = models.CharField(max_length=32, verbose_name='支付老买家数')
    pc_zf_old_mjs = models.CharField(max_length=32, verbose_name='PC端支付老买家数')
    wx_zf_old_mjs = models.CharField(max_length=32, verbose_name='无线端支付老买家数')
    old_mj_zfje = models.CharField(max_length=32, verbose_name='老买家支付金额')
    ztc_xh = models.CharField(max_length=32, verbose_name='直通车消耗')
    zsz_xh = models.CharField(max_length=32, verbose_name='钻石展位消耗')
    tbk_yj = models.CharField(max_length=32, verbose_name='淘宝客佣金')
    cgtk_je = models.CharField(max_length=32, verbose_name='成功退款金额')
    pjs = models.CharField(max_length=32, verbose_name='评价数')
    yt_pjs = models.CharField(max_length=32, verbose_name='有图评价数')
    zm_pjs = models.CharField(max_length=32, verbose_name='正面评价数')
    fm_pjs = models.CharField(max_length=32, verbose_name='负面评价数')
    old_mj_zm_pjs = models.CharField(max_length=32, verbose_name='老买家正面评价数')
    old_mj_fm_pjs = models.CharField(max_length=32, verbose_name='老买家负面评价数')
    zf_fdds = models.CharField(max_length=32, verbose_name='支付父订单数')
    ls_bgs = models.CharField(max_length=32, verbose_name='揽收包裹数')
    fh_bgs = models.CharField(max_length=32, verbose_name='发货包裹数')
    ps_bgs = models.CharField(max_length=32, verbose_name='派送包裹数')
    qscg_bgs = models.CharField(max_length=32, verbose_name='签收成功包裹数')
    pjzf_qs_sc = models.CharField(max_length=32, verbose_name='平均支付_签收时长(秒)')
    msxf_pf = models.CharField(max_length=32, verbose_name='描述相符评分')
    wlfw_pf = models.CharField(max_length=32, verbose_name='物流服务评分')
    wftd_pf = models.CharField(max_length=32, verbose_name='服务态度评分')
    xd_zf_zhl = models.CharField(max_length=32, verbose_name='下单-支付转化率')
    pc_xd_zf_zhl = models.CharField(max_length=32, verbose_name='PC端下单-支付转化率')
    wx_xd_zf_zhl = models.CharField(max_length=32, verbose_name='无线端下单-支付转化率')
    zf_sps = models.CharField(max_length=32, verbose_name='支付商品数')
    pc_zf_sps = models.CharField(max_length=32, verbose_name='PC端支付商品数')
    wx_zf_sps = models.CharField(max_length=32, verbose_name='无线端支付商品数')
    dp_sc_mjs = models.CharField(max_length=32, verbose_name='店铺收藏买家数')
    pc_dp_sc_mjs = models.CharField(max_length=32, verbose_name='PC端店铺收藏买家数')
    wx_dp_sc_mjs = models.CharField(max_length=32, verbose_name='无线端店铺收藏买家数')


class DpTgPxb(models.Model):
    """店铺，付费推广/品销宝"""
    riqi = models.DateField(verbose_name='日期')
    zxl = models.BigIntegerField(verbose_name='展现量')
    djl = models.BigIntegerField(verbose_name='点击量')
    djlv = models.FloatField(verbose_name='点击率')
    huafei = models.FloatField(verbose_name='花费')
    zxcb = models.FloatField(verbose_name='千次展现成本')
    djdj = models.FloatField(verbose_name='点击单价')
    tz_djdj = models.FloatField(verbose_name='跳转点击单价')
    zs_cjbs = models.BigIntegerField(verbose_name='展示成交笔数')
    zs_cjje = models.FloatField(verbose_name='展示成交金额')
    bbscs = models.BigIntegerField(verbose_name='宝贝收藏数')
    dpscs = models.BigIntegerField(verbose_name='店铺收藏数')
    bbjgs = models.BigIntegerField(verbose_name='宝贝加购数')
    zs_hbl = models.FloatField(verbose_name='展示回报率')
    dj_hbl = models.FloatField(verbose_name='点击回报率')
    dj_cjbs = models.BigIntegerField(verbose_name='点击成交笔数')
    dj_cjje = models.FloatField(verbose_name='点击成交金额')
    cd_fks = models.BigIntegerField(verbose_name='触达访客数')
    cd_new_fks = models.BigIntegerField(verbose_name='触达新访客数')
    dj_fks = models.BigIntegerField(verbose_name='点击访客数')
    zx_zhl = models.FloatField(verbose_name='展现转化率')
    dj_zhl = models.FloatField(verbose_name='点击转化率')


class DpTgZtc(models.Model):
    """店铺，付费推广/直通车"""
    reqi = models.CharField(max_length=32, verbose_name='日期')
    tg_jhmc = models.CharField(max_length=128, verbose_name='推广计划名称')
    bb_mc = models.CharField(max_length=256, verbose_name='宝贝名称')
    bb_lx = models.CharField(max_length=64, verbose_name='宝贝类型')
    sp_id = models.FloatField(verbose_name='商品id')
    ss_lx = models.CharField(max_length=32, verbose_name='搜索类型')
    ll_ly = models.CharField(max_length=64, verbose_name='流量来源')
    zxl = models.BigIntegerField(verbose_name='展现量')
    djl = models.BigIntegerField(verbose_name='点击量')
    hf = models.IntegerField(verbose_name='花费(分)')
    djlv = models.FloatField(verbose_name='点击率')
    pj_dj_hf = models.FloatField(verbose_name='平均点击花费(分)')
    qc_zx_hf = models.FloatField(verbose_name='千次展现花费(分)')
    dj_zhl = models.FloatField(verbose_name='点击转化率')
    zj_cj_je = models.FloatField(verbose_name='直接成交金额(分)')
    zj_cj_bs = models.FloatField(verbose_name='直接成交笔数')
    jj_cj_je = models.FloatField(verbose_name='间接成交金额(分)')
    jj_cj_bs = models.FloatField(verbose_name='间接成交笔数')
    z_cj_je = models.FloatField(verbose_name='总成交金额(分)')
    z_cj_bs = models.FloatField(verbose_name='总成交笔数')
    bb_scs = models.FloatField(verbose_name='宝贝收藏数')
    dp_scs = models.FloatField(verbose_name='店铺收藏数')
    z_scs = models.FloatField(verbose_name='总收藏数')
    tr_ccb = models.FloatField(verbose_name='投入产出比')
    zj_gwcs = models.FloatField(verbose_name='直接购物车数')
    jj_gwcs = models.FloatField(verbose_name='间接购物车数')
    z_gwcs = models.FloatField(verbose_name='总购物车数')


class DpTgZz(models.Model):
    """店铺，付费推广，钻展"""
    jhxx = models.CharField(max_length=256, verbose_name='计划基本信息')
    shijian = models.DateField(verbose_name='时间')
    zhanxian = models.BigIntegerField(verbose_name='展现')
    dianji = models.BigIntegerField(verbose_name='点击')
    xiaohao = models.FloatField(verbose_name='消耗')
    djlv = models.CharField(max_length=16, verbose_name='点击率( %)')
    djdj = models.FloatField(verbose_name='点击单价(元)')
    qczxcb = models.FloatField(verbose_name='千次展现成本(元)')
    fk = models.BigIntegerField(verbose_name='访客')
    sdjdl = models.FloatField(verbose_name='深度进店量')
    fw_sc = models.FloatField(verbose_name='访问时长')
    fw_ym = models.FloatField(verbose_name='访问页面数')
    sc_bb = models.FloatField(verbose_name='收藏宝贝量')
    sc_dp = models.FloatField(verbose_name='收藏店铺量')
    tj_gwc = models.FloatField(verbose_name='添加购物车量')
    px_ddl = models.FloatField(verbose_name='拍下订单量')
    px_ddje = models.FloatField(verbose_name='拍下订单金额')
    cj_ddl = models.FloatField(verbose_name='成交订单量')
    cj_ddje = models.FloatField(verbose_name='成交订单金额')
    dj_zhlv = models.CharField(max_length=16, verbose_name='点击转化率(%)')
    tz_hblv = models.FloatField(verbose_name='投资回报率')
    xd_l = models.FloatField(verbose_name='行动量')
    xd_cb = models.FloatField(verbose_name='行动成本')


class DpGqKjcw(models.Model):
    """店铺，天猫官旗，会计财务"""
    dd_bh = models.BigIntegerField(verbose_name='订单编号')
    mj_hym = models.CharField(max_length=64, verbose_name='买家会员名')
    dd_zt = models.CharField(max_length=32, verbose_name='订单状态')
    sf_je = models.FloatField(verbose_name='实付金额')
    sf_yf = models.IntegerField(verbose_name='实付邮费')
    hp_cb = models.FloatField(verbose_name='货品成本')
    kdf = models.IntegerField(verbose_name='快递费')
    bzf = models.IntegerField(verbose_name='包装费')
    zpf = models.IntegerField(verbose_name='赠品费')
    ts_yj = models.IntegerField(verbose_name='特殊佣金')
    lirun = models.FloatField(verbose_name='利润')
    ktgs = models.CharField(max_length=64, verbose_name='快递公司')
    ydh = models.CharField(max_length=64, verbose_name='运单号')
    sh_dz = models.CharField(max_length=128, verbose_name='收货地址')
    dd_cj_sj = models.DateField(verbose_name='订单创建时间')
    dd_fk_sj = models.DateField(verbose_name='订单付款时间')
    dd_fh_sj = models.CharField(max_length=32, verbose_name='订单发货时间')
    dd_js_sj = models.CharField(max_length=32, verbose_name='订单结束时间')
    bb_bt = models.CharField(max_length=512, verbose_name='宝贝标题')
    bb_id = models.CharField(max_length=128, verbose_name='宝贝ID')
    bb_sj_bm = models.CharField(max_length=128, verbose_name='宝贝商家编码')
    sx_id = models.CharField(max_length=128, verbose_name='属性ID')
    sx_sj_bm = models.CharField(max_length=128, verbose_name='属性商家编码')
    bb_zl = models.IntegerField(verbose_name='宝贝种类')
    bb_zsl = models.IntegerField(verbose_name='宝贝总数量')
    mj_fwf_1 = models.IntegerField(verbose_name='卖家货到付款服务费')
    mf_fwf_2 = models.IntegerField(verbose_name='买家货到付款服务费')
    qizhi = models.CharField(max_length=32, verbose_name='旗帜')
    hulue = models.FloatField(verbose_name='是否已忽略')


class DpGqLlgc(models.Model):
    """店铺官旗流量构成"""
    ll_ly = models.CharField(max_length=64, verbose_name='流量来源')
    ly_mx = models.CharField(max_length=128, verbose_name='来源明细')
    fks = models.CharField(max_length=64, verbose_name='访客数')
    fks_bh = models.CharField(max_length=64, verbose_name='访客数变化')
    xd_je = models.CharField(max_length=64, verbose_name='下单金额')
    xd_je_bh = models.CharField(max_length=64, verbose_name='下单金额变化')
    xd_mjs = models.CharField(max_length=64, verbose_name='下单买家数')
    xd_mjs_bh = models.CharField(max_length=64, verbose_name='下单买家数变化')
    xd_zhlv = models.CharField(max_length=64, verbose_name='下单转化率')
    xd_zhlv_bh = models.CharField(max_length=64, verbose_name='下单转化率变化')
    zf_je = models.CharField(max_length=64, verbose_name='支付金额')
    zf_je_bh = models.CharField(max_length=64, verbose_name='支付金额变化')
    zf_mjs = models.CharField(max_length=64, verbose_name='支付买家数')
    zf_mjs_bh = models.CharField(max_length=64, verbose_name='支付买家数变化')
    zf_zhlv = models.CharField(max_length=64, verbose_name='支付转化率')
    zf_zhlv_bh = models.CharField(max_length=64, verbose_name='支付转化率变化')
    kdj = models.CharField(max_length=64, verbose_name='客单价')
    kdj_bh = models.CharField(max_length=64, verbose_name='客单价变化')
    uv_jz = models.CharField(max_length=64, verbose_name='UV价值')
    uv_jz_bh = models.CharField(max_length=64, verbose_name='uv价值变化')
    gz_dp_mjs = models.CharField(max_length=64, verbose_name='关注店铺买家数')
    gz_dp_mjs_bh = models.CharField(max_length=64, verbose_name='关注店铺买家数变化')
    sc_sp_mjs = models.CharField(max_length=64, verbose_name='收藏商品买家数')
    sc_sp_mjs_bh = models.CharField(max_length=64, verbose_name='收藏商品买家数变化')
    jg_rs = models.CharField(max_length=64, verbose_name='加购人数')
    jg_rs_bh = models.CharField(max_length=64, verbose_name='加购人数变化')
    x_fk = models.CharField(max_length=64, verbose_name='新访客')
    x_fk_bh = models.CharField(max_length=64, verbose_name='新访客变化')
    zj_zf_mjs = models.CharField(max_length=64, verbose_name='直接支付买家数')
    scsp_zf_mj = models.CharField(max_length=64, verbose_name='收藏商品_支付买家')
    fs_zf_mjs = models.CharField(max_length=64, verbose_name='粉丝支付买家数')
    jg_sp_zfmj = models.CharField(max_length=64, verbose_name='加购商品_支付买家')


class DpGqPlsj(models.Model):
    """天猫官旗，品类数据"""
    tjrq = models.CharField(max_length=32, verbose_name='统计日期')
    yj_lm_mc = models.CharField(max_length=128, verbose_name='一级类目名称')
    ej_lm_mc = models.CharField(max_length=128, verbose_name='二级类目名称')
    lm_mc = models.CharField(max_length=128, verbose_name='类目名称')
    sp_fks = models.CharField(max_length=32, verbose_name='商品访客数')
    sp_lll = models.CharField(max_length=16, verbose_name='商品浏览量')
    yfk_sps = models.CharField(max_length=16, verbose_name='有访客商品数')
    yzf_sps = models.CharField(max_length=16, verbose_name='有支付商品数')
    sp_jgs = models.CharField(max_length=16, verbose_name='商品加购人数')
    sp_jg_js = models.CharField(max_length=16, verbose_name='商品加购件数')
    sp_sc_rs = models.CharField(max_length=16, verbose_name='商品收藏人数')
    fw_sc_zhlv = models.CharField(max_length=16, verbose_name='访问收藏转化率')
    fw_jg_zhlv = models.CharField(max_length=16, verbose_name='访问加购转化率')
    xd_mjs = models.CharField(max_length=16, verbose_name='下单买家数')
    xd_js = models.CharField(max_length=16, verbose_name='下单件数')
    xd_je = models.CharField(max_length=16, verbose_name='下单金额')
    xd_zhlv = models.CharField(max_length=16, verbose_name='下单转化率')
    zf_mjs = models.CharField(max_length=16, verbose_name='支付买家数')
    zf_js = models.CharField(max_length=16, verbose_name='支付件数')
    zf_je = models.CharField(max_length=16, verbose_name='支付金额')
    zf_zhlv = models.CharField(max_length=16, verbose_name='支付转化率')
    m_lj_zfje = models.CharField(max_length=16, verbose_name='月累计支付金额')
    y_lj_zfje = models.CharField(max_length=16, verbose_name='年累计支付金额')
    jhs_zfje = models.CharField(max_length=16, verbose_name='聚划算支付金额')
    zf_xmj = models.CharField(max_length=16, verbose_name='支付新买家数')
    zf_lmj = models.CharField(max_length=16, verbose_name='支付老买家数')
    lmj_zfje = models.CharField(max_length=16, verbose_name='老买家支付金额')
    kdj = models.CharField(max_length=16, verbose_name='客单价')
    fk_pj_jz = models.CharField(max_length=16, verbose_name='访客平均价值')
    sh_tkje = models.CharField(max_length=16, verbose_name='售中售后成功退款金额')


class DpGqScHyqsD(models.Model):
    """天猫官旗，市场大盘行业趋势,日度"""
    lm_name = models.CharField(max_length=256, verbose_name='类目名')
    riqi = models.CharField(max_length=64, verbose_name='日期')
    ss_rs = models.BigIntegerField(verbose_name='搜索人数')
    ss_cs = models.BigIntegerField(verbose_name='搜索次数')
    fks = models.BigIntegerField(verbose_name='访客数')
    lll = models.BigIntegerField(verbose_name='浏览量')
    sc_rs = models.BigIntegerField(verbose_name='收藏人数')
    sc_cs = models.BigIntegerField(verbose_name='收藏次数')
    jg_rs = models.BigIntegerField(verbose_name='加购人数')
    jg_cs = models.BigIntegerField(verbose_name='加购次数')
    zf_rs = models.BigIntegerField(verbose_name='支付人数')
    jy_je = models.BigIntegerField(verbose_name='交易金额')
    kdj = models.FloatField(verbose_name='客单价')


class DpGqScHyqsM(models.Model):
    """天猫官旗，市场大盘行业趋势,月度"""
    jtpl = models.CharField(max_length=256, verbose_name='具体品类')
    riqi = models.DateField(verbose_name='日期')
    fkl = models.FloatField(default=0, verbose_name='访客数')
    lll = models.FloatField(default=0, verbose_name='浏览量')
    sc_rs = models.FloatField(default=0, verbose_name='收藏人数')
    sc_cs = models.FloatField(default=0, verbose_name='收藏次数')
    jg_rs = models.FloatField(default=0, verbose_name='加购人数')
    jg_cs = models.FloatField(default=0, verbose_name='加购次数')
    zf_js = models.FloatField(default=0, verbose_name='支付件数')
    kdj = models.FloatField(default=0, verbose_name='客单价')
    jy_zs = models.FloatField(default=0, verbose_name='交易指数')
    ss_dj_rs = models.FloatField(default=0, verbose_name='搜索点击人数')
    bzf_mjs = models.FloatField(default=0, verbose_name='被支付卖家数')
    zhlv = models.FloatField(default=0, verbose_name='转化率')
    jye = models.FloatField(default=0, verbose_name='交易额')


class Scph_dp_gjy(models.Model):
    """天猫官旗，市场排行，笔记本店铺排行，高交易"""
    dp_xx = models.CharField(max_length=256, verbose_name='店铺信息')
    riqi = models.CharField(max_length=32, verbose_name='日期')
    hy_pm = models.CharField(max_length=16, verbose_name='行业排名')
    jy_je = models.BigIntegerField(verbose_name='交易金额')
    jy_zz_fd = models.CharField(max_length=16, verbose_name='交易增长幅度')
    zf_zhlv = models.CharField(max_length=8, verbose_name='支付转化率')


class Scph_dp_gll(models.Model):
    """天猫官旗，市场排行，笔记本店铺排行，高流量"""
    dp_xx = models.CharField(max_length=256, verbose_name='店铺信息')
    riqi = models.CharField(max_length=32, verbose_name='日期')
    hy_pm = models.CharField(max_length=16, verbose_name='行业排名')
    fk_rs = models.BigIntegerField(verbose_name='访客人数')
    ss_rs = models.BigIntegerField(verbose_name='搜索人数')
    ss_zb = models.CharField(max_length=16, verbose_name='搜索占比')
    jy_je = models.BigIntegerField(verbose_name='交易金额')
    uv_jz = models.FloatField(max_length=16, verbose_name='uv价值')


class Scph_pp_gjy(models.Model):
    """天猫官旗，市场排行，笔记本品牌排行，高交易"""
    pinp_xinx = models.CharField(max_length=256, verbose_name='品牌信息')
    riqi = models.CharField(max_length=32, verbose_name='日期')
    hy_pm = models.CharField(max_length=16, verbose_name='行业排名')
    jy_je = models.BigIntegerField(verbose_name='交易金额')
    jy_zz_fd = models.CharField(max_length=16, verbose_name='交易增长幅度')
    zf_zhlv = models.CharField(max_length=8, verbose_name='支付转化率')


class Scph_pp_gll(models.Model):
    """天猫官旗，市场排行，笔记本品牌排行，高流量"""
    dp_xx = models.CharField(max_length=256, verbose_name='店铺信息')
    riqi = models.CharField(max_length=32, verbose_name='日期')
    hy_pm = models.CharField(max_length=16, verbose_name='行业排名')
    fk_rs = models.BigIntegerField(verbose_name='访客人数')
    ss_rs = models.BigIntegerField(verbose_name='搜索人数')
    ss_zb = models.CharField(max_length=16, verbose_name='搜索占比')
    jy_je = models.BigIntegerField(verbose_name='交易金额')
    uv_jz = models.FloatField(verbose_name='uv价值')


class Scph_sp_gjy(models.Model):
    """天猫官旗，市场排行，笔记本商品排行，高交易"""
    sp_xx = models.CharField(max_length=256, verbose_name='商品信息')
    dp_mc = models.CharField(max_length=256, verbose_name='店铺名')
    sp_id = models.BigIntegerField(verbose_name='商品id')
    riqi = models.CharField(max_length=32, verbose_name='日期')
    hy_pm = models.CharField(max_length=16, verbose_name='行业排名')
    jy_je = models.BigIntegerField(verbose_name='交易金额')
    jy_zz_fd = models.CharField(max_length=16, verbose_name='交易增长幅度')
    zf_zhlv = models.CharField(max_length=8, verbose_name='支付转化率')


class Scph_sp_gll(models.Model):
    """天猫官旗，市场排行，笔记本商品排行，高流量"""
    sp_xx = models.CharField(max_length=256, verbose_name='商品信息')
    dp_mc = models.CharField(max_length=256, verbose_name='店铺名')
    sp_id = models.BigIntegerField(verbose_name='商品id')
    riqi = models.CharField(max_length=32, verbose_name='日期')
    hy_pm = models.CharField(max_length=16, verbose_name='行业排名')
    fk_rs = models.BigIntegerField(verbose_name='访客人数')
    ss_rs = models.BigIntegerField(verbose_name='搜索人数')
    ss_zb = models.CharField(max_length=16, verbose_name='搜索占比')
    jy_je = models.BigIntegerField(verbose_name='交易金额')
    uv_jz = models.FloatField(verbose_name='uv价值')


class Scph_sp_gyx(models.Model):
    """天猫官旗，市场排行，笔记本商品排行，高意向"""
    sp_xx = models.CharField(max_length=256, verbose_name='商品信息')
    dp_mc = models.CharField(max_length=256, verbose_name='店铺名')
    sp_id = models.BigIntegerField(verbose_name='商品id')
    riqi = models.CharField(max_length=32, verbose_name='日期')
    hy_pm = models.CharField(max_length=16, verbose_name='行业排名')
    sc_rs = models.BigIntegerField(verbose_name='收藏人数')
    jg_rs = models.BigIntegerField(verbose_name='加购人数')
    jy_je = models.BigIntegerField(verbose_name='交易金额')


class Scdp_Sxdc_d(models.Model):
    """市场大盘，属性洞察，日度"""
    riqi = models.DateField(verbose_name='日期')
    sx = models.CharField(max_length=32, verbose_name='属性')
    sxz = models.CharField(max_length=128, verbose_name='属性值')
    jy_zs = models.BigIntegerField(verbose_name='交易指数')
    zf_js = models.BigIntegerField(verbose_name='支付件数')
    caozuo = models.CharField(max_length=32, verbose_name='操作')


class Scdp_Sxdc_m(models.Model):
    """市场大盘，属性洞察，月度"""
    jt_pl = models.DateField(verbose_name='具体品类')
    tj_sj = models.DateField(verbose_name='统计时间')
    sx = models.CharField(max_length=32, verbose_name='属性')
    sxz = models.CharField(max_length=128, verbose_name='属性值')
    jy_zs = models.BigIntegerField(verbose_name='交易指数')
    zf_js = models.BigIntegerField(verbose_name='支付件数')
    caozuo = models.CharField(max_length=32, verbose_name='操作')


class Gq_Mcbb_bb(models.Model):
    """天猫官旗，已卖出的宝贝,宝贝报表"""
    dd_bh = models.CharField(max_length=32, verbose_name='订单编号')
    title = models.CharField(max_length=256, verbose_name='标题')
    jiage = models.FloatField(verbose_name='价格')
    gm_sl = models.IntegerField(verbose_name='购买数量')
    wb_xt_bh = models.CharField(max_length=256, verbose_name='外部系统编号')
    sp_sx = models.CharField(max_length=128, verbose_name='商品属性')
    tc_xx = models.FloatField(verbose_name='套餐信息')
    beizhu = models.CharField(max_length=128, verbose_name='备注')
    dd_zt = models.CharField(max_length=64, verbose_name='订单状态')
    sj_bm = models.CharField(max_length=256, verbose_name='商家编码')


class Gq_Mcbb_dd(models.Model):
    """天猫官旗，已卖出的宝贝,订单报表"""
    pass
