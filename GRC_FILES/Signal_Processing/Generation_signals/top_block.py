#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Jul 17 11:02:01 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab1")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab2")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab3")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab4")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab5")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab6")
        self.Add(self.notebook_0)
        self.wxgui_scopesink2_5 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(3).GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(3).Add(self.wxgui_scopesink2_5.win)
        self.wxgui_scopesink2_4 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(2).GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(2).Add(self.wxgui_scopesink2_4.win)
        self.wxgui_scopesink2_3 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(5).GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(5).Add(self.wxgui_scopesink2_3.win)
        self.wxgui_scopesink2_2 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(4).GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(4).Add(self.wxgui_scopesink2_2.win)
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(0).GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_scopesink2_1.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_scopesink2_0.win)
        self.analog_sig_source_x_5 = analog.sig_source_c(samp_rate, analog.GR_TRI_WAVE, 1000, 1, 0)
        self.analog_sig_source_x_4 = analog.sig_source_c(samp_rate, analog.GR_SAW_WAVE, 1000, 1, 0)
        self.analog_sig_source_x_3 = analog.sig_source_c(samp_rate, analog.GR_SQR_WAVE, 1000, 1, 0)
        self.analog_sig_source_x_2 = analog.sig_source_c(samp_rate, analog.GR_CONST_WAVE, 1000, 1, 0)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 1000, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.wxgui_scopesink2_1, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.wxgui_scopesink2_4, 0))
        self.connect((self.analog_sig_source_x_3, 0), (self.wxgui_scopesink2_5, 0))
        self.connect((self.analog_sig_source_x_4, 0), (self.wxgui_scopesink2_3, 0))
        self.connect((self.analog_sig_source_x_5, 0), (self.wxgui_scopesink2_2, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_5.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_4.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_3.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_2.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_5.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_4.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
