from django.db import models


class Kc_Erp_Kccx(models.Model):
    """库存数据，ERP库存查询"""
    riqi = models.DateField(null=False, verbose_name='日期')
    spbm = models.CharField(null=False, max_length=64, verbose_name='商品编码')
    leibie = models.CharField(null=False, max_length=32, verbose_name='类别')
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
    xz = models.CharField(max_length=16,verbose_name='性质')
    zhcgsj = models.CharField(max_length=32,verbose_name='最后采购时间')
    hsyj = models.FloatField(verbose_name='含税预计')
    wsyj = models.FloatField(verbose_name='未税预计')


class Kc_Erp_Splr(models.Model):
    """库存数据 ERP商品利润"""
    cksj = models.CharField(max_length=32,null=False,verbose_name='出库时间')
    zfrq = models.CharField(max_length=32,null=False,verbose_name='支付日期')
    khmc = models.CharField(max_length=32,verbose_name='客户名称')
    spbm = models.CharField(max_length=64,verbose_name='商品编码')
    leibie = models.CharField(max_length=64,verbose_name='类别')
    pinpai = models.CharField(max_length=16,verbose_name='品牌')
    guige = models.CharField(max_length=128,verbose_name='规格')
    xilie = models.CharField(max_length=64,verbose_name='系列')
    xh = models.CharField(max_length=64,verbose_name='型号')
    spmc = models.CharField(max_length=256,verbose_name='商品名称')

    xz = models.IntegerField(verbose_name='性质')
    leixing = models.CharField(max_length=32,verbose_name='类型')
    danhao = models.CharField(max_length=32,verbose_name='单号')
    wddh = models.CharField(max_length=64,verbose_name='网店单号')
    hyh = models.CharField(max_length=64,verbose_name='会员号')
    daofu = models.IntegerField(verbose_name='到付')
    zhiyuan = models.CharField(max_length=64,verbose_name='职员')
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
    mll = models.FloatField(verbose_name='毛利率')
    zhlr = models.FloatField(verbose_name='折合利润')

    zhlrl = models.FloatField(verbose_name='折合利润率')
    yfcb = models.FloatField(verbose_name='运费成本')
    ptfy = models.FloatField(verbose_name='平台费用')
    fxfy = models.FloatField(verbose_name='返现费用')
    qtfy = models.FloatField(verbose_name='其他费用')
    yjml = models.FloatField(verbose_name='预计毛利')
    yjmll = models.FloatField(verbose_name='预计毛利率')
    yjjlr = models.FloatField(verbose_name='预计净利润')
    yjjlrl = models.FloatField(verbose_name='预计净利润率')
    pdsj = models.CharField(max_length=32,verbose_name='拍单时间')
    bumen = models.CharField(max_length=32,verbose_name='部门')


class Kc_Erp_Ydh(models.Model):
    """ERP预到货数据"""
    cjsj = models.CharField(max_length=32,null=False,verbose_name='创建时间')
    yjdh = models.CharField(max_length=32,verbose_name='预计到货')
    cqts = models.FloatField(verbose_name='超期天数')
    danhao = models.CharField(max_length=32,verbose_name='单号')
    ks = models.CharField(max_length=64,verbose_name='客商')
    spbm = models.CharField(max_length=64,verbose_name='商品编码')
    spmc = models.CharField(max_length=256,verbose_name='商品名称')
    ywy = models.CharField(max_length=32,verbose_name='业务员')
    kds = models.IntegerField(verbose_name='开单数')
    danjia = models.FloatField(verbose_name='单价')
    jine = models.FloatField(verbose_name='金额')
    ydh = models.FloatField(verbose_name='已到货')
    wds = models.IntegerField(verbose_name='未到数')
    wdje = models.FloatField(verbose_name='未到金额')


class Kc_Erp_Zksp(models.Model):
    """ERP在库商品模板"""
    riqi = models.DateField(null=False, verbose_name='日期')
    zhjhrq = models.CharField(max_length=32,verbose_name='最后进货日期')
    spjdrq = models.CharField(max_length=32,verbose_name='商品建档日期')
    kufang = models.CharField(max_length=32,verbose_name='库房')
    hl = models.CharField(max_length=32,verbose_name='货拉')
    lbmc = models.CharField(max_length=64,verbose_name='类别名称')
    spbm = models.CharField(max_length=64,verbose_name='商品编码')
    spmc = models.CharField(max_length=256,verbose_name='商品名称')
    xh = models.CharField(max_length=64,verbose_name='型号')
    guige = models.CharField(max_length=256,verbose_name='规格')
    pinpai = models.CharField(max_length=64,verbose_name='品牌')
    zks = models.FloatField(verbose_name='在库数')
    qjxss = models.FloatField(verbose_name='区间销售数')


class Kc_Xh_Spbm(models.Model):
    """各平台型号与商品编码对照表"""
    pingtai = models.CharField(max_length=64,verbose_name='平台')
    xinghao = models.CharField(max_length=32,verbose_name='型号')
    spbm = models.CharField(max_length=128,verbose_name='商品编码')


class Kc_Spxx(models.Model):
    """库存商品信息表"""
    xinghao = models.CharField(max_length=32, null=False,verbose_name='型号')
    pinlei = models.CharField(max_length=68, verbose_name='品类')
    new_old = models.CharField(max_length=16, verbose_name='新旧品')
    dingwei = models.CharField(max_length=64, null=False,verbose_name='定位')
    pinming = models.CharField(max_length=128, null=False,verbose_name='品名')
    cpu = models.CharField(max_length=16, verbose_name='CPU')
    xianka = models.CharField(max_length=64, verbose_name='显卡')
    neicun = models.CharField(max_length=32, verbose_name='内存')
    ssd = models.CharField(max_length=64,verbose_name='SSD')
    hhd = models.CharField(max_length=64,verbose_name='HHD')
    model_name = models.CharField(max_length=128,verbose_name='模具名称')
    config = models.CharField(max_length=256,verbose_name='配置')
    pn = models.CharField(max_length=16, null=True,verbose_name='pn')






