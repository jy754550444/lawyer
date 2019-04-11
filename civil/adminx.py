# coding=utf-8
__author__ = 'yy'

import xadmin, qrcode, json
from .models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User, Group
from django.db.models import Max
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from defendant.models import CivilAgent
from lawyer.models import UserProfile


class MaintainInline(object):
    # form_layout = (
    #     Main(
    #         TabHolder(
    #             Tab(
    #                 u"委托人",
    #                 Fieldset(
    #                     "委托人基本信息",
    #                     Row("name", "sex"),
    #                     Row("age", "nation"),
    #                     Row("occupation", "idcard"),
    #                     Row("address", "tel"),
    #                     "nail_address",
    #                     # description="some comm fields, required",
    #                 ),
    #
    #                 css_id="extend_info",
    #             ),
    #             Tab(
    #                 u"当事人",
    #                 Fieldset(
    #                     "当事人基本信息",
    #                     "party",
    #                     Row("d_sex", "d_age"),
    #                     Row("d_nation", "d_occupation"),
    #                     Row("d_code", "d_address"),
    #                     Row("d_tel", "d_nail_address"),
    #
    #
    #                 ),
    #                 css_id="base_info",
    #             ),
    #         ),
    #     ),
    # )
    model = Civils
    exclude = ('user',)
    extra = 0
    style = "accordion"


# 民事案件登记表
class CivilAdmin(object):
    list_display = ('case_id', 'case', 'trial_level', 'pto',)
    exclude = ( 'openid', 'subscribe',)
    inlines = [MaintainInline]
    save_as = True

    def save_models(self):

        # self.new_obj.user = self.request.user
        # super().save_models()
        print(self.new_obj.user_id, self.new_obj.case_id, '=========')
        if not self.new_obj.case_id:
            print(444444444422222222)
            if self.new_obj.consultation == False:
                print(11111111)
                yearmon = datetime.datetime.now().strftime('%Y')
                maxVal = Civil.objects.filter().aggregate(sn_max=Max("case_id"))
                max_value = maxVal['sn_max']
                if max_value is None:
                    num = '001'
                    order_id = '主' + yearmon + '民初' + num
                    self.new_obj.case_id = order_id
                    self.new_obj.pto = "uploads/civil/{0}.png".format(order_id)
                    self.new_obj.save()
                else:
                    num = str(int(max_value[-3:]) + 1).rjust(3, '0')
                    order_id = '主' + yearmon + '民初' + num
                    self.new_obj.case_id = order_id
                    self.new_obj.pto = "uploads/civil/{0}.png".format(order_id)
                    self.new_obj.save()

                # host = self.request.get_host()
                # path = reverse('bath-qrcode-ack')
                url = "http://zvsh3y.natappfree.cc/redirect/?case_id={0}".format(self.new_obj.case_id, )
                # url='http://www.baidu.com'
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_M,
                    box_size=12,
                    border=4,
                )
                qr.add_data(url)
                qr.make(fit=True)
                img = qr.make_image()
                img.save('{0}.png'.format(self.new_obj.pto))
                img.show()

            else:
                self.new_obj.case = self.new_obj.case
                self.new_obj.save()
        else:
            if not self.new_obj.case_id:
                if self.new_obj.consultation == False:
                    print(2222222222)
                    yearmon = datetime.datetime.now().strftime('%Y')
                    maxVal = Civil.objects.filter().aggregate(sn_max=Max("case_id"))
                    max_value = maxVal['sn_max']
                    if max_value is None:
                        num = '001'
                        order_id = '主' + yearmon + '民初' + num
                        self.new_obj.case_id = order_id
                        self.new_obj.pto = "uploads/civil/{0}.png".format(order_id)
                        self.new_obj.save()
                    else:
                        num = str(int(max_value[-3:]) + 1).rjust(3, '0')
                        order_id = '主' + yearmon + '民初' + num
                        self.new_obj.case_id = order_id
                        self.new_obj.pto = "uploads/civil/{0}.png".format(order_id)
                        self.new_obj.save()

                    # host = self.request.get_host()
                    # path = reverse('bath-qrcode-ack')
                    url = "http://zvsh3y.natappfree.cc/redirect/?case_id={0}".format(self.new_obj.case_id, )
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_M,
                        box_size=12,
                        border=4,
                    )
                    qr.add_data(url)
                    qr.make(fit=True)
                    img = qr.make_image()
                    img.save('{0}.png'.format(self.new_obj.pto))
                    img.show()
                else:
                    self.new_obj.save()
            else:
                # print(self.new_obj.id, 6666666666)
                self.new_obj.save()

    def save_related(self):
        change_number = self.new_obj.agency_fee
        format_word = ["分", "角", "元",
                       "拾", "百", "千", "万",
                       "拾", "百", "千", "亿",
                       "拾", "百", "千", "万",
                       "拾", "百", "千", "兆"]

        format_num = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
        if type(change_number) == str:
            # - 如果是字符串,先尝试转换成float或int.
            if '.' in change_number:
                try:
                    change_number = float(change_number)
                except:
                    ValueError, print('%s  can\'t change' % change_number)
            else:
                try:
                    change_number = int(change_number)
                except:
                    ValueError, '%s   can\'t change' % change_number

        if type(change_number) == float:
            real_numbers = []
            for i in range(len(format_word) - 3, -3, -1):
                if change_number >= 10 ** i or i < 1:
                    real_numbers.append(int(round(change_number / (10 ** i), 2) % 10))

        elif isinstance(change_number, (int,)):
            real_numbers = [int(i) for i in str(change_number) + '00']

        else:
            ValueError, '%s   can\'t change' % change_number

        zflag = 0  # 标记连续0次数，以删除万字，或适时插入零字
        start = len(real_numbers) - 3
        change_words = []
        for i in range(start, -3, -1):  # 使i对应实际位数，负数为角分
            if 0 != real_numbers[start - i] or len(change_words) == 0:
                if zflag:
                    change_words.append(format_num[0])
                    zflag = 0
                change_words.append(format_num[real_numbers[start - i]])
                change_words.append(format_word[i + 2])

            elif 0 == i or (0 == i % 4 and zflag < 3):  # 控制 万/元
                change_words.append(format_word[i + 2])
                zflag = 0
            else:
                zflag += 1

        if change_words[-1] not in (format_word[0], format_word[1]):
            # - 最后两位非"角,分"则补"整"
            change_words.append("整")

        agency_fees = ''.join(change_words)
        user = UserProfile.objects.get(user_id=int(self.new_obj.user_id))
        # print(user, self.new_obj.user_id, 'user')


        # for inst in obj.charginggun_set.all():
        #     self.save_image(inst)
        print(self.new_obj.id, '------------------')
        super(CivilAdmin, self).save_related()
        obj = Civils.objects.filter(case_id=self.new_obj.id)
        print(obj, 'obj')
        print(obj.count(), 'objcount')
        if obj.count() > 1:
            for i in obj:
                if i.choice_name == '1':
                    print(2221111678678)
                    if i.name and i.method_name == '2':
                        names = i.name
                        nation = i.nation
                        idcard = i.idcard
                        tel = i.tel
                        nail_address = i.nail_address
                    else:
                        names = i.company
                        code = i.code
                        legal = i.legal
                        tel = i.telephone
                        nail_address = i.c_address
                elif i.choice_name == '3':
                    print(555444490978)
                    if i.party and i.method_name == '2':
                        names = i.party
                        d_sex = i.d_sex
                        d_age = i.d_age
                        d_nation = i.d_nation
                        d_occupation = i.d_occupation
                        d_code = i.d_code
                        d_address = i.d_address
                        legal = None
                        tel = i.d_tel
                        nail_address = i.d_nail_address
                    else:
                        name = i.company
                        code = i.code
                        legal = i.legal
                        telephone = i.telephone
                        c_address = i.c_address

                elif i.choice_name == '2':
                    print(6776767677979)
                    if i.xd_name and i.method_name == '2':
                        name = i.xd_name
                        xd_sex = i.xd_sex
                        xd_age = i.xd_age
                        xd_nation = i.xd_nation
                        xd_occupation = i.xd_occupation
                        xd_idcard = i.xd_idcard
                        xd_address = i.xd_address
                        xd_tel = i.xd_tel
                        xd_nail_address = i.xd_nail_address
                    else:
                        name = i.company
                        code = i.code
                        legal = i.legal
                        tel = i.telephone
                        nail_address = i.c_address
            # data = CivilAgent.objects.get(civil_id=self.new_obj.id)
            # if data:
            defaults = {'agency_fee': change_number, 'agency_fees': agency_fees, 'nail_name': names,
                        'b_tel': user.law.tel, 'nail_tel': tel, 'law': user.law.name, 'b_legal': user.law.f_name,
                        'b_address': user.law.address, 'nail_address': nail_address, 'nail_legal': legal,
                        'name': name, 'court': self.new_obj.case_office,'Trial_level': self.new_obj.trial_level,'case':self.new_obj.case,'user_id':self.new_obj.user_id}
            obj, created = CivilAgent.objects.update_or_create(civil_id=self.new_obj.id,defaults=defaults,)

        else:
            pass
                # self.form_obj.save_m2m()


xadmin.site.register(Civil, CivilAdmin)


# 人员信息登记表
class CivilsAdmin(object):
    list_display = ('name',)

    exclude = ('user',)
    model_icon = 'fa fa-shield fa-flip-horizontal'

    # def ui_operate(self, obj):
    #     return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    #
    # ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(CivilsAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Civils, CivilsAdmin)
