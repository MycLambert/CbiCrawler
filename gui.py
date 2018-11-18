# -*- coding: UTF-8 -*-
 
from tkinter import *
from InstrumentBooking import *
from tkinter import ttk
import time
import threading

threads = []
booking_flag = False
circle_times = 0
value_input = {
		'instrument': '',
		'year': '',
		'month': '',
		'day': '',
		'start_time': '',
		'stop_time': '',
		}

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
	comboxlist_month["values"] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',)
	comboxlist_month.current(0)
	comboxlist_month['state'] = 'readonly'
	#下拉框位置&尺寸
	comboxlist_month.grid(column=3, row=date_selection_row)
	comboxlist_month['width'] = 2
	
	#设置下拉框（选择日）
	value_day = StringVar()
	comboxlist_day = ttk.Combobox(frame_date_selection, textvariable=value_day)
	#下拉框可选值&默认值
	comboxlist_day["values"] = (
			'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 
			'11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
			'21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', 
		)
	comboxlist_day.current(0)
	comboxlist_day['state'] = 'readonly'
	#下拉框位置&尺寸
	comboxlist_day.grid(column=5, row=date_selection_row)
	comboxlist_day['width'] = 2
	return root, value_year, value_month, value_day
	

#选择时间
def creat_time_selection(root):
	frame_time_selection = Frame(root, height=80,width=100,bd=5)#, bg='#ff3399')
	frame_time_selection.pack(anchor=W) 
	#选择开始时间示意文字：
	lb_start_time_name = Label(frame_time_selection, text = "开始时间：")
	lb_start_time_name.grid(column = 0, row = 0, padx = 10, pady = 4)
	#设置下拉框（选择开始时间）
	value_start_time = StringVar()
	comboxlist_start_time = ttk.Combobox(frame_time_selection, textvariable=value_start_time)
	#下拉框可选值&默认值
	time_value = (
			'08:30',
			'09:00', '09:30',
			'10:00', '10:30',
			'11:00', '11:30',
			'12:00', '12:30',
			'13:00', '13:30',
			'14:00', '14:30',
			'15:00', '15:30',
			'16:00', '16:30',
			'17:00', '17:30',
			'18:00', '18:30',
			'19:00', '19:30',
			'20:00', '20:30',
			'21:00', '21:30',
			'22:00', '22:30',
			'23:00', '23:30',
		)
	comboxlist_start_time["values"] = time_value
	comboxlist_start_time.current(0)
	comboxlist_start_time['state'] = 'readonly'
	#下拉框位置&尺寸
	comboxlist_start_time.grid(column=1, row=0)
	comboxlist_start_time['width'] = 50
	
	#选择结束时间示意文字：
	lb_stop_time_name = Label(frame_time_selection, text = "结束时间：")
	lb_stop_time_name.grid(column = 0, row = 1, padx = 10, pady = 4)
	#设置下拉框（选择结束时间）
	value_stop_time = StringVar()
	comboxlist_stop_time = ttk.Combobox(frame_time_selection, textvariable=value_stop_time)
	comboxlist_stop_time["values"] = time_value
	comboxlist_stop_time.current(6)
	comboxlist_stop_time['state'] = 'readonly'
	#下拉框位置&尺寸
	comboxlist_stop_time.grid(column=1, row=1)
	comboxlist_stop_time['width'] = 50
	
	return root, value_start_time, value_stop_time


#选择模式
def creat_mode_selection(root):
	frame_mode_selection = Frame(root, height=80,width=100,bd=5)#, bg='#ff3399')
	frame_mode_selection.pack(anchor=W) 
	#选择仪器示意文字：
	lb_mode_name = Label(frame_mode_selection, text = "预定模式：")
	lb_mode_name.grid(column = 0, row = 0, padx = 10, pady = 4)
	#设置下拉框（选择仪器）
	value_mode = StringVar()
	comboxlist_mode = ttk.Combobox(frame_mode_selection, textvariable=value_mode)
	#下拉框可选值&默认值
	comboxlist_mode["values"] = ('持续预定', '单次预定')
	comboxlist_mode.current(0)
	comboxlist_mode['state'] = 'readonly'
	#下拉框位置&尺寸
	comboxlist_mode.grid(column=1, row=0)
	comboxlist_mode['width'] = 10
	return root, value_mode

	
def gui_main():
	root = Tk() 
	#设置窗口的大小宽x高+偏移量
	root.geometry('500x300+500+200')
	#窗口标题
	root.title("InstrumentBooking")
	#设置窗口图标
	root.iconbitmap('pic/Cbi.ico')
	
	#创建选择下拉框界面
	root, value_instrument = creat_instrument_selection(root)
	root, value_year, value_month, value_day = creat_date_selection(root)
	root, value_start_time, value_stop_time = creat_time_selection(root)
	root, value_mode = creat_mode_selection(root)
	
	def confirm_event():
		global booking_flag, circle_times, value_input
		print('\n\n------------------------')
		booking_flag = True
		value_input['instrument'] = value_instrument.get()
		value_input['year'] = value_year.get()
		value_input['month'] = value_month.get()
		value_input['day'] = value_day.get()
		value_input['start_time'] = value_start_time.get()
		value_input['stop_time'] = value_stop_time.get()
		print(value_input)
		if value_mode.get() == '持续预定':
			print('持续预定')
			circle_times = -1
		else:
			print('单次预定')
			circle_times = 1
		
	def cancel_event():
		global booking_flag
		print('\nCancel mission...')
		booking_flag = False
	confirm_button = Button(root,text='Confirm',command=confirm_event, width=10)
	confirm_button.pack()
	cancel_button = Button(root,text='Cancel',command=cancel_event, width=10)
	cancel_button.pack()
	root.mainloop()
	return 0


def book_api():
	print('start book_api')
	global booking_flag, circle_times, value_input
	while True:
		time.sleep(1)
		if booking_flag:
			booking(value_input['instrument'], value_input['year'], value_input['month'], value_input['day'], value_input['start_time'], value_input['stop_time'], 1)
			if circle_times == 1:
				booking_flag = False
			else:
				print('\nTrying booking again...')
				time.sleep(0.2)
	print('stop book_api')


t1 = threading.Thread(target=book_api,args=())
threads.append(t1)


def main():
	global threads
	for t in threads:
		print(t)
		t.setDaemon(True)
		t.start()
	gui_main()
	


if __name__ == '__main__':
	main()
