import wx
import re

SKILL_POWER = 100  # 技能倍率
MIN_HURT = 0.0  # 面板小伤
MAX_HURT = 0.0  # 面板大伤
MAIN_ATTRIBUTE = 0.0  # 主属性
COMBAT_POWER = 0.0  # 战斗力
CRIT_HURT = 0.0  # 暴击伤害
CRIT_RATE = 0.0  # 暴击率
EQUIP_UP = 0.0  # 装备额外提升
SKILL_UP = 0.0  # 技能额外提升
INJURY_REDUCE = 10.0  # 敌实际减伤率
FIRE_ATT = 0.0  # 属性攻击
PASS = 0.0  # 穿透

RESULTS_MIN_UNCRIT = 0.0  # 小伤不爆
RESULTS_MAX_UNCRIT = 0.0  # 大伤不爆
RESULTS_MIN_AVR_CRIT = 0.0  # 小伤暴击期望
RESULTS_MAX_AVR_CRIT = 0.0  # 大伤暴击期望
RESULTS_MIN_CRIT = 0.0  # 小伤暴击
RESULTS_MAX_CRIT = 0.0  # 大伤暴击

RESULTS_UP_UNCRIT = 100.0  # 不计算暴击的提升
RESULTS_UP_YUQI = 100.0  # 暴击期望的提升
RESULTS_UP_CRIT = 100.0  # 计算暴击的提升


# 自定义窗口类MyFrame
class Frame(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, parent=superior, title=u'地城之光伤害计算器')
        # self.Centre()
        self.SetSize(1000, 600)

        panel = wx.Panel(self, -1)
        # 添加静态文本控件
        label_skill_power = wx.StaticText(parent=panel, id=101, label=u"技能威力 ：")
        label_min_hurt = wx.StaticText(parent=panel, id=102, label=u"面板小伤 ：")
        label_max_hurt = wx.StaticText(parent=panel, id=103, label=u"面板大伤 ：")
        label_main_attribute = wx.StaticText(parent=panel, id=104, label=u'主属性 ：')
        label_combat_power = wx.StaticText(parent=panel, id=105, label=u'战斗力 ：')
        label_crit_hurt = wx.StaticText(parent=panel, id=106, label=u'暴击伤害 %：')
        label_crit_rate = wx.StaticText(parent=panel, id=107, label=u'暴击率 %：')
        label_equit_up = wx.StaticText(parent=panel, id=108, label=u'装备提升 %：')
        label_skill_up = wx.StaticText(parent=panel, id=109, label=u'技能提升 %：')
        label_injury_reduce = wx.StaticText(parent=panel, id=110, label=u'敌减伤率 %：')

        label_results_min_uncrit = wx.StaticText(parent=panel, id=111, label=u'小伤不爆 ：')
        label_results_max_uncrit = wx.StaticText(parent=panel, id=112, label=u'大伤不爆 %：')
        label_results_min_avr_crit = wx.StaticText(parent=panel, id=113, label=u'小伤暴击期望 ：')
        label_results_max_avr_crit = wx.StaticText(parent=panel, id=114, label=u'大伤暴击期望 ：')
        label_results_min_crit = wx.StaticText(parent=panel, id=115, label=u'小伤暴击 %：')
        label_results_max_crit = wx.StaticText(parent=panel, id=116, label=u'大伤暴击 %：')
        label_fire_att = wx.StaticText(parent=panel, id=117, label=u'属性攻击：')
        label_pass = wx.StaticText(parent=panel, id=118, label=u'穿透 %：')

        label_results_up_nocrit = wx.StaticText(parent=panel, id=120, label=u'不计算暴击的提升 ：')
        label_results_up_yuqi = wx.StaticText(parent=panel, id=122, label=u'暴击期望的提升 ：')
        label_results_up_crit = wx.StaticText(parent=panel, id=121, label=u'计算暴击的提升 ：')

        # 添加文本框
        self.input_skill_power = wx.TextCtrl(parent=panel, id=201, value=str(SKILL_POWER))
        self.input_min_hurt = wx.TextCtrl(parent=panel, id=202, value=str(MIN_HURT))
        self.input_max_hurt = wx.TextCtrl(parent=panel, id=203, value=str(MAX_HURT))
        self.input_main_attribute = wx.TextCtrl(parent=panel, id=204, value=str(MAIN_ATTRIBUTE))
        self.input_combat_power = wx.TextCtrl(parent=panel, id=205, value=str(COMBAT_POWER))
        self.input_crit_hurt = wx.TextCtrl(parent=panel, id=206, value=str(CRIT_HURT))
        self.input_crit_rate = wx.TextCtrl(parent=panel, id=207, value=str(CRIT_RATE))
        self.input_equit_up = wx.TextCtrl(parent=panel, id=208, value=str(EQUIP_UP))
        self.input_skill_up = wx.TextCtrl(parent=panel, id=209, value=str(SKILL_UP))
        self.input_injury_reduce = wx.TextCtrl(parent=panel, id=210, value=str(INJURY_REDUCE))

        self.input_results_min_uncrit = wx.TextCtrl(parent=panel, id=211, value=str(RESULTS_MIN_UNCRIT))
        self.input_results_max_uncrit = wx.TextCtrl(parent=panel, id=212, value=str(RESULTS_MAX_UNCRIT))
        self.input_results_min_avr_crit = wx.TextCtrl(parent=panel, id=213, value=str(RESULTS_MIN_AVR_CRIT))
        self.input_results_max_avr_crit = wx.TextCtrl(parent=panel, id=214, value=str(RESULTS_MAX_AVR_CRIT))
        self.input_results_min_crit = wx.TextCtrl(parent=panel, id=215, value=str(RESULTS_MIN_CRIT))
        self.input_results_max_crit = wx.TextCtrl(parent=panel, id=216, value=str(RESULTS_MAX_CRIT))
        self.input_fire_att = wx.TextCtrl(parent=panel, id=217, value=str(FIRE_ATT))
        self.input_pass = wx.TextCtrl(parent=panel, id=218, value=str(PASS))

        self.input_results_up_nocrit = wx.TextCtrl(parent=panel, id=220, value=str(RESULTS_UP_UNCRIT))
        self.input_results_up_yuqi = wx.TextCtrl(parent=panel, id=222, value=str(RESULTS_UP_YUQI))
        self.input_results_up_crit = wx.TextCtrl(parent=panel, id=221, value=str(RESULTS_UP_CRIT))

        # 添加按钮
        self.button_Clear = wx.Button(parent=panel, id=1, label=u'清空')
        self.button_Cou = wx.Button(parent=panel, id=2, label=u'计算')

        # 绑定事件处理函数
        self.Bind(wx.EVT_BUTTON, handler=self.OnButton_Clear, source=self.button_Clear)
        self.Bind(wx.EVT_BUTTON, self.OnButton_Back, source=self.button_Cou)

        self.panel = panel

        # 创建水平方向box布局管理器（默认水平方向）
        hbox1 = wx.BoxSizer()
        hbox1.Add(label_skill_power, 101, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox1.Add(self.input_skill_power, 201, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox1.Add(label_min_hurt, 102, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox1.Add(self.input_min_hurt, 202, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox1.Add(label_max_hurt, 103, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox1.Add(self.input_max_hurt, 203, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)

        hbox2 = wx.BoxSizer()
        hbox2.Add(label_main_attribute, 104, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox2.Add(self.input_main_attribute, 204, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox2.Add(label_combat_power, 105, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox2.Add(self.input_combat_power, 205, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox2.Add(label_fire_att, 117, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox2.Add(self.input_fire_att, 217, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)

        hbox3 = wx.BoxSizer()
        hbox3.Add(label_crit_rate, 107, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox3.Add(self.input_crit_rate, 207, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox3.Add(label_equit_up, 108, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox3.Add(self.input_equit_up, 208, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox3.Add(label_injury_reduce, 110, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox3.Add(self.input_injury_reduce, 209, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)

        hbox4 = wx.BoxSizer()
        hbox4.Add(label_crit_hurt, 106, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox4.Add(self.input_crit_hurt, 206, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox4.Add(label_skill_up, 109, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox4.Add(self.input_skill_up, 209, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox4.Add(label_pass, 118, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox4.Add(self.input_pass, 218, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)

        hbox5 = wx.BoxSizer()
        hbox5.Add(label_results_min_uncrit, 111, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox5.Add(self.input_results_min_uncrit, 211, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox5.Add(label_results_min_avr_crit, 113, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox5.Add(self.input_results_min_avr_crit, 213, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox5.Add(label_results_min_crit, 115, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox5.Add(self.input_results_min_crit, 215, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)

        hbox6 = wx.BoxSizer()
        hbox6.Add(label_results_max_uncrit, 112, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox6.Add(self.input_results_max_uncrit, 212, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox6.Add(label_results_max_avr_crit, 114, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox6.Add(self.input_results_max_avr_crit, 214, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox6.Add(label_results_max_crit, 116, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox6.Add(self.input_results_max_crit, 216, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)

        hbox7 = wx.BoxSizer()
        hbox7.Add(label_results_up_nocrit, 120, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox7.Add(self.input_results_up_nocrit, 210, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox7.Add(label_results_up_yuqi, 122, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox7.Add(self.input_results_up_yuqi, 222, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)
        hbox7.Add(label_results_up_crit, 121, wx.ALIGN_CENTER | wx.LEFT, border=10)
        hbox7.Add(self.input_results_up_crit, 221, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=10)

        hbox9 = wx.BoxSizer()
        hbox9.Add(self.button_Clear, 1, flag=wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=5)
        hbox9.Add(self.button_Cou, 1, flag=wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=5)

        # 创建垂直方向box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 将hbox添加到vbox
        vbox.Add(hbox1, proportion=1, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        vbox.Add(hbox2, proportion=1, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        vbox.Add(hbox3, proportion=1, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        vbox.Add(hbox4, proportion=1, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        vbox.Add(hbox9, proportion=1, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        vbox.Add(hbox5, proportion=1, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        vbox.Add(hbox6, proportion=1, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        vbox.Add(hbox7, proportion=1, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        # 整个界面为一个面板，面板中设置一个垂直方向的布局管理器（根布局管理器）
        panel.SetSizer(vbox)

    def OnButton_Clear(self, event):
        self.input_skill_power.SetValue(str(SKILL_POWER))
        self.input_min_hurt.SetValue(str(MIN_HURT))
        self.input_max_hurt.SetValue(str(MAX_HURT))
        self.input_main_attribute.SetValue(str(MAIN_ATTRIBUTE))
        self.input_combat_power.SetValue(str(COMBAT_POWER))
        self.input_crit_hurt.SetValue(str(CRIT_HURT))
        self.input_crit_rate.SetValue(str(CRIT_RATE))
        self.input_equit_up.SetValue(str(EQUIP_UP))
        self.input_skill_up.SetValue(str(SKILL_UP))
        self.input_injury_reduce.SetValue(str(INJURY_REDUCE))
        self.input_fire_att.SetValue(str(FIRE_ATT))
        self.input_pass.SetValue(str(PASS))

        self.input_results_min_uncrit.SetValue(str(RESULTS_MIN_UNCRIT))
        self.input_results_max_uncrit.SetValue(str(RESULTS_MAX_UNCRIT))
        self.input_results_min_avr_crit.SetValue(str(RESULTS_MIN_AVR_CRIT))
        self.input_results_max_avr_crit.SetValue(str(RESULTS_MAX_AVR_CRIT))
        self.input_results_min_crit.SetValue(str(RESULTS_MIN_CRIT))
        self.input_results_max_crit.SetValue(str(RESULTS_MAX_CRIT))

        self.input_results_up_nocrit.SetValue(str(RESULTS_UP_UNCRIT))
        self.input_results_up_crit.SetValue(str(RESULTS_UP_CRIT))

        event.Skip()

    def OnButton_Back(self, event):
        self.input_skill_power.SetValue(str(int(self.input_skill_power.GetValue())))
        self.input_min_hurt.SetValue(str(float(self.input_min_hurt.GetValue())))
        self.input_max_hurt.SetValue(str(float(self.input_max_hurt.GetValue())))
        self.input_main_attribute.SetValue(str(float(self.input_main_attribute.GetValue())))
        self.input_combat_power.SetValue(str(float(self.input_combat_power.GetValue())))
        self.input_crit_hurt.SetValue(str(float(self.input_crit_hurt.GetValue())))
        self.input_crit_rate.SetValue(str(float(self.input_crit_rate.GetValue())))
        self.input_equit_up.SetValue(str(float(self.input_equit_up.GetValue())))
        self.input_skill_up.SetValue(str(float(self.input_skill_up.GetValue())))
        self.input_injury_reduce.SetValue(str(float(self.input_injury_reduce.GetValue())))
        self.input_fire_att.SetValue(str(float(self.input_fire_att.GetValue())))
        self.input_pass.SetValue(str(float(self.input_pass.GetValue())))

        min_uncrit_1 = float(self.input_results_min_uncrit.GetValue())
        max_uncrit_1 = float(self.input_results_max_uncrit.GetValue())
        min_avr_crit_1 = float(self.input_results_min_avr_crit.GetValue())
        max_avr_crit_1 = float(self.input_results_max_avr_crit.GetValue())
        min_crit_1 = float(self.input_results_min_crit.GetValue())
        max_crit_1 = float(self.input_results_max_crit.GetValue())

        # print(min_uncrit_1)
        # print(max_uncrit_1)
        # print(min_crit_1)
        # print(max_crit_1)

        skill_power = int(self.input_skill_power.GetValue())
        min_hurt = float(self.input_min_hurt.GetValue())
        max_hurt = float(self.input_max_hurt.GetValue())
        main_attribut = float(self.input_main_attribute.GetValue())
        combat_power = float(self.input_combat_power.GetValue())
        crit_hurt = float(self.input_crit_hurt.GetValue())
        crit_rate = float(self.input_crit_rate.GetValue())
        equit_up = float(self.input_equit_up.GetValue())
        skill_up = float(self.input_skill_up.GetValue())
        injury_reduce = float(self.input_injury_reduce.GetValue())
        fire_att = float(self.input_fire_att.GetValue())
        pass_1 = float(self.input_pass.GetValue())

        min_uncrit = ((skill_power / 100) * min_hurt * (1 + main_attribut / 1000) + combat_power) * (
                1 + skill_up / 100) * (1 + equit_up / 100) * (1 - (
                    0.3 * (injury_reduce - pass_1) + 0.7 * (injury_reduce * (1 - pass_1 / 100))) / 100) * (
                                 1 + fire_att / 100)
        max_uncrit = ((skill_power / 100) * max_hurt * (1 + main_attribut / 1000) + combat_power) * (
                1 + skill_up / 100) * (1 + equit_up / 100) * (1 - (
                    0.3 * (injury_reduce - pass_1) + 0.7 * (injury_reduce * (1 - pass_1 / 100))) / 100) * (
                                 1 + fire_att / 100)
        min_avr_crit = ((((skill_power / 100) * min_hurt * (1 + main_attribut / 1000) + combat_power) * (
                1 + skill_up / 100) * (1 + equit_up / 100) * (1 - (
                    0.3 * (injury_reduce - pass_1) + 0.7 * (injury_reduce * (1 - pass_1 / 100))) / 100) * (
                                 crit_hurt / 100) * crit_rate) * (1 + fire_att / 100) + (
                                ((skill_power / 100) * min_hurt * (1 + main_attribut / 1000) + combat_power) * (
                                1 + skill_up / 100) * (1 + equit_up / 100) * (1 - (
                                    0.3 * (injury_reduce - pass_1) + 0.7 * (
                                        injury_reduce * (1 - pass_1 / 100))) / 100) * (
                                        100 - crit_rate)) * (1 + fire_att / 100)) / 100
        max_avr_crit = ((((skill_power / 100) * max_hurt * (1 + main_attribut / 1000) + combat_power) * (
                1 + skill_up / 100) * (1 + equit_up / 100) * (1 - (
                    0.3 * (injury_reduce - pass_1) + 0.7 * (injury_reduce * (1 - pass_1 / 100))) / 100) * (
                                 crit_hurt / 100) * crit_rate) * (1 + fire_att / 100) + (
                                ((skill_power / 100) * max_hurt * (1 + main_attribut / 1000) + combat_power) * (
                                1 + skill_up / 100) * (1 + equit_up / 100) * (1 - (
                                    0.3 * (injury_reduce - pass_1) + 0.7 * (
                                        injury_reduce * (1 - pass_1 / 100))) / 100) * (
                                        100 - crit_rate)) * (1 + fire_att / 100)) / 100
        min_crit = ((skill_power / 100) * min_hurt * (1 + main_attribut / 1000) + combat_power) * (
                1 + skill_up / 100) * (1 + equit_up / 100) * (1 - (
                    0.3 * (injury_reduce - pass_1) + 0.7 * (injury_reduce * (1 - pass_1 / 100))) / 100) * (
                               crit_hurt / 100) * (1 + fire_att / 100)
        max_crit = ((skill_power / 100) * max_hurt * (1 + main_attribut / 1000) + combat_power) * (
                1 + skill_up / 100) * (1 + equit_up / 100) * (1 - (
                    0.3 * (injury_reduce - pass_1) + 0.7 * (injury_reduce * (1 - pass_1 / 100))) / 100) * (
                               crit_hurt / 100) * (1 + fire_att / 100)

        self.input_results_min_uncrit.SetValue(str(min_uncrit))
        self.input_results_max_uncrit.SetValue(str(max_uncrit))
        self.input_results_min_avr_crit.SetValue(str(min_avr_crit))
        self.input_results_max_avr_crit.SetValue(str(max_avr_crit))
        self.input_results_min_crit.SetValue(str(min_crit))
        self.input_results_max_crit.SetValue(str(max_crit))

        if (min_uncrit_1 != 0) and max_uncrit_1 != 0:
            a = (min_uncrit + max_uncrit) / (min_uncrit_1 + max_uncrit_1) * 100
            self.input_results_up_nocrit.SetValue(str(a) + '%')
        if (min_avr_crit_1 != 0) and max_avr_crit_1 != 0:
            c = (min_avr_crit + max_avr_crit) / (min_avr_crit_1 + max_avr_crit_1) * 100
            self.input_results_up_yuqi.SetValue(str(c) + '%')
        if (min_crit_1 != 0) and max_crit_1 != 0:
            b = (min_crit + max_crit) / (min_crit_1 + max_crit_1) * 100
            self.input_results_up_crit.SetValue(str(b) + '%')

        event.Skip()


# 自定义应用程序对象
class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = Frame(None)
        frame.Show()
        return True

    def OnCloseQuery(self):
        print('应用程序退出')
        dlg = wx.MessageDialog(self, '确认返回？', '返回', wx.CANCEL | wx.OK | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_OK:
            self.Destroy()
        return 0


if __name__ == '__main__':
    app = App()  # 调用上面函数
    app.MainLoop()  # 进入主事件循环
