# -*- coding: UTF-8 -*-
 
from tkinter import *
from tkinter import ttk

#选择仪器
def creat_instrument_selection(root):
	frame_instrument_selection = Frame(root, height=80,width=100,bd=5)#, bg='#ff3399')
	frame_instrument_selection.pack(anchor=W) 
	#选择仪器示意文字：
	lb_instrument_name = Label(frame_instrument_selection, text = "预约仪器：")
	lb_instrument_name.grid(column = 0, row = 0, padx = 10, pady = 4)
	#设置下拉框（选择仪器）
	value_instrument = StringVar()
	comboxlist_instrument_name = ttk.Combobox(frame_instrument_selection, textvariable=value_instrument)
	#下拉框可选值&默认值
	instrument_name = (
			'BD FACS CantoII流式细胞分析仪',
			'BD Influx流式细胞分选仪',
			'BD LSRFortessa流式细胞分析仪',
			'BD LSRII数字化分析型流式细胞仪',
			'latest BD FACS AriaIII流式细胞分选仪',
			'new BD FACS AriaIII流式细胞分选仪',
			'old BD FACS AriaIII流式细胞分选仪',
			'Bioruptor plus超声破碎仪'
		)
	comboxlist_instrument_name["values"] = instrument_name
	comboxlist_instrument_name.current(0)
	comboxlist_instrument_name['state'] = 'readonly'
	#下拉框位置&尺寸
	comboxlist_instrument_name.grid(column=1, row=0)
	comboxlist_instrument_name['width'] = 50
	return root, value_instrument


#选择日期
def creat_date_selection(root):
	frame_date_selection = Frame(root, height=80,width=100,bd=5)#, bg='#ff3399')
	frame_date_selection.pack(anchor=W) 
	date_selection_row = 0
	#选择日期示意文字：
	lb_date_selection = Label(frame_date_selection, text = "日期：")
	lb_date_selection.grid(column = 0, row = date_selection_row, padx = 22, pady = 4)
	lb_year = Label(frame_date_selection, text = "年")
	lb_year.grid(column = 2, row = date_selection_row, padx = 8, pady = 4)
	lb_month = Label(frame_date_selection, text = "月")
	lb_month.grid(column = 4, row = date_selection_row, padx = 8, pady = 4)
	lb_day = Label(frame_date_selection, text = "日")
	lb_day.grid(column = 6, row = date_selection_row, padx = 8, pady = 4)
	
	#设置下拉框（选择年）
	value_year = StringVar()
	comboxlist_year = ttk.Combobox(frame_date_selection, textvariable=value_year)
	#下拉框可选值&默认值
	comboxlist_year["values"] = ('2018', '2019', '2020', '2021', '2022', '2023', '2024',)
	comboxlist_year.current(0)
	comboxlist_year['state'] = 'readonly'
	#下拉框位置&尺寸
	comboxlist_year.grid(column=1, row=date_selection_row)
	comboxlist_year['width'] = 4
	
	#设置下拉框（选择月）
	value_month = StringVar()
	comboxlist_month = ttk.Combobox(frame_date_selection, textvariable=value_month)
	#下拉框可选值&默认值
	comboxlist_month["values"] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',)
	comboxlist_month.current(0)
	comboxlist_month['state'] = 'readonly'
	#下拉框位置&尺寸
	comboxlist_month.grid(column=3, row=date_selection_row)
	comboxlist_month['width'] = 2
	
	#设置下拉框（选择日）
	value_day = StringVar()
	comboxlist_day = ttk.Combobox(frame_date_selection, textvariable=value_day)
	#下拉框可选值&默认值
	comboxlist_day["values"] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', )
	comboxlist_day.current(0)
	comboxlist_day['state'] = 'readonly'
	#下拉框位置&尺寸
	comboxlist_day.grid(column=5, row=date_selection_row)
	comboxlist_day['width'] = 2
	return root, value_year, value_month, value_day
	


def main():
	root = Tk()
	#设置窗口的大小宽x高+偏移量
	root.geometry('500x300+500+200')
	#窗口标题
	root.title("InstrumentBooking")
	#设置窗口图标
	root.iconbitmap('pic/Cbi.ico')
	root, value_instrument = creat_instrument_selection(root)
	root, value_year, value_month, value_day = creat_date_selection(root)
	def rtnkey(event=None):
		print(e.get())
		print(value_instrument.get())
		print(value_year.get())
		print(value_month.get())
		print(value_day.get())
	e = StringVar()
	entry = Entry(root, validate='key', textvariable=e, width=50)
	entry.pack()
	entry.bind('<Return>', rtnkey)
	# 进入消息循环
	root.mainloop()
	return 0

if __name__ == '__main__':
	main()
