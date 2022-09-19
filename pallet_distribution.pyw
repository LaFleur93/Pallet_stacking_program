from tkinter import *
from Pallets_Brondby import *
from datetime import date
import time

class Pallet_distribution:
	def __init__(self, window):
        # Initializations 
		self.wind = window
		self.wind.title('Pallets distribution')
		#self.wind.iconbitmap(r'C:\Users\santi\OneDrive\Escritorio\Infarm\Pallets\Pallet program\infarm_logo.ico')
		self.wind.geometry('1200x635')
		self.wind.resizable(False, False)

		#-------------------------------------
		# Left column (messages and pallets inputs)
		#-------------------------------------
		frame_column_1 = LabelFrame(self.wind, borderwidth = '0')
		frame_column_1.place(x=10, y=0, relwidth=0.255, relheight=1)

		#-------------------------------------
		# Brondby message frame
		#-------------------------------------
		frame_msg_brondby = LabelFrame(frame_column_1, text = 'Message')
		frame_msg_brondby.grid(row = 1, column = 0, columnspan = 4, padx = 5, pady = 5)
		frame_msg_brondby.place(x=0, y=0, relwidth=.99, height=55)

		self.message_brondby = Label(frame_msg_brondby, text = 'No message')
		self.message_brondby.place(x = 10, y = 4)

		#-------------------------------------
		# Brondby pallets frame
		#-------------------------------------
		frame_brondby = LabelFrame(frame_column_1, text = 'Brøndby pallets')
		frame_brondby.grid(row = 1, column = 0, columnspan = 4, padx = 5, pady = 5)
		frame_brondby.place(x=0, y=57, relwidth=.99, height=255)

		Label(frame_brondby, text = 'TRAYSEAL', width = 20).grid(row = 1, column = 0, columnspan = 2)
		Label(frame_brondby, text = 'FLOWPACK', width = 20).grid(row = 1, column = 3, columnspan = 2)

		entry_width = 7

		Label(frame_brondby, text = 'Thyme').grid(row = 2, column = 0, sticky = E)
		ts_b_thyme = Entry(frame_brondby, width = entry_width)
		ts_b_thyme.grid(row = 2, column = 1)
		Label(frame_brondby, text = 'Flat Coriander').grid(row = 3, column = 0, sticky = E)
		ts_b_coriander = Entry(frame_brondby, width = entry_width)
		ts_b_coriander.grid(row = 3, column = 1)
		Label(frame_brondby, text = 'Rosemary').grid(row = 4, column = 0, sticky = E)
		ts_b_rosemary = Entry(frame_brondby, width = entry_width)
		ts_b_rosemary.grid(row = 4, column = 1)
		Label(frame_brondby, text = 'Green Mint').grid(row = 5, column = 0, sticky = E)
		ts_b_mint = Entry(frame_brondby, width = entry_width)
		ts_b_mint.grid(row = 5, column = 1)
		Label(frame_brondby, text = 'Sage').grid(row = 6, column = 0, sticky = E)
		ts_b_sage = Entry(frame_brondby, width = entry_width)
		ts_b_sage.grid(row = 6, column = 1)
		Label(frame_brondby, text = 'Tarragon').grid(row = 7, column = 0, sticky = E)
		ts_b_tarragon = Entry(frame_brondby, width = entry_width)
		ts_b_tarragon.grid(row = 7, column = 1)
		Label(frame_brondby, text = 'Italian Basil').grid(row = 8, column = 0, sticky = E)
		ts_b_italianbasil = Entry(frame_brondby, width = entry_width)
		ts_b_italianbasil.grid(row = 8, column = 1)
		Label(frame_brondby, text = 'Dill').grid(row = 9, column = 0, sticky = E)
		ts_b_dill = Entry(frame_brondby, width = entry_width)
		ts_b_dill.grid(row = 9, column = 1)

		Label(frame_brondby, text = 'Italian Basil').grid(row = 2, column = 3, sticky = E)
		fp_b_thyme = Entry(frame_brondby, width = entry_width)
		fp_b_thyme.grid(row = 2, column = 4)
		Label(frame_brondby, text = 'Curly Parsley').grid(row = 3, column = 3, sticky = E)
		fp_b_coriander = Entry(frame_brondby, width = entry_width)
		fp_b_coriander.grid(row = 3, column = 4)
		Label(frame_brondby, text = 'Flat Coriander').grid(row = 4, column = 3, sticky = E)
		fp_b_rosemary = Entry(frame_brondby, width = entry_width)
		fp_b_rosemary.grid(row = 4, column = 4)
		Label(frame_brondby, text = 'Green Mint').grid(row = 5, column = 3, sticky = E)
		fp_b_mint = Entry(frame_brondby, width = entry_width)
		fp_b_mint.grid(row = 5, column = 4)
		Label(frame_brondby, text = 'Thyme').grid(row = 6, column = 3, sticky = E)
		fp_b_sage = Entry(frame_brondby, width = entry_width)
		fp_b_sage.grid(row = 6, column = 4)
		Label(frame_brondby, text = 'Rosemary').grid(row = 7, column = 3, sticky = E)
		fp_b_tarragon = Entry(frame_brondby, width = entry_width)
		fp_b_tarragon.grid(row = 7, column = 4)
		Label(frame_brondby, text = 'Tarragon').grid(row = 8, column = 3, sticky = E)
		fp_b_italianbasil = Entry(frame_brondby, width = entry_width)
		fp_b_italianbasil.grid(row = 8, column = 4)

		frame_b_button = LabelFrame(frame_brondby, pady = 7, bd = 0)
		frame_b_button.grid(row =10, column = 0, columnspan = 5)

		Button(frame_b_button, text = 'Generate Brøndby distribution', relief="solid", bg = '#D3D3D3', bd = 1, width = 37, command = lambda: self.generate_brondby(ts_b_thyme.get(), ts_b_coriander.get(), ts_b_rosemary.get(), ts_b_mint.get(), ts_b_sage.get(), ts_b_tarragon.get(), ts_b_italianbasil.get(), ts_b_dill.get(), fp_b_thyme.get(), fp_b_coriander.get(), fp_b_rosemary.get(), fp_b_mint.get(), fp_b_sage.get(), fp_b_tarragon.get(), fp_b_italianbasil.get())).grid(row = 0, column = 0)

		#-------------------------------------
		# Hasselager message frame
		#-------------------------------------
		frame_msg_hasselager = LabelFrame(frame_column_1, text = 'Message')
		frame_msg_hasselager.grid(row = 11, column = 0, columnspan = 4, padx = 5, pady = 5)
		frame_msg_hasselager.place(x=0, y=315,
		 relwidth=.99, height=55)

		self.message_hasselager = Label(frame_msg_hasselager, text = 'No message')
		self.message_hasselager.place(x = 10, y = 4)

		#-------------------------------------
		# Hasselager pallets frame
		#-------------------------------------

		frame_hasselager = LabelFrame(frame_column_1, text = 'Hasselager pallets')
		frame_hasselager.grid(row = 12, column = 0, columnspan = 4, padx = 5, pady = 5)
		frame_hasselager.place(x=0, y=375, relwidth=.99, height=255)

		Label(frame_hasselager, text = 'TRAYSEAL', width = 20).grid(row = 1, column = 0, columnspan = 2)
		Label(frame_hasselager, text = 'FLOWPACK', width = 20).grid(row = 1, column = 3, columnspan = 2)

		entry_width = 7
		Label(frame_hasselager, text = 'Thyme').grid(row = 2, column = 0, sticky = E)
		ts_h_thyme = Entry(frame_hasselager, width = entry_width)
		ts_h_thyme.grid(row = 2, column = 1)
		Label(frame_hasselager, text = 'Flat Coriander').grid(row = 3, column = 0, sticky = E)
		ts_h_coriander = Entry(frame_hasselager, width = entry_width)
		ts_h_coriander.grid(row = 3, column = 1)
		Label(frame_hasselager, text = 'Rosemary').grid(row = 4, column = 0, sticky = E)
		ts_h_rosemary = Entry(frame_hasselager, width = entry_width)
		ts_h_rosemary.grid(row = 4, column = 1)
		Label(frame_hasselager, text = 'Green Mint').grid(row = 5, column = 0, sticky = E)
		ts_h_mint = Entry(frame_hasselager, width = entry_width)
		ts_h_mint.grid(row = 5, column = 1)
		Label(frame_hasselager, text = 'Sage').grid(row = 6, column = 0, sticky = E)
		ts_h_sage = Entry(frame_hasselager, width = entry_width)
		ts_h_sage.grid(row = 6, column = 1)
		Label(frame_hasselager, text = 'Tarragon').grid(row = 7, column = 0, sticky = E)
		ts_h_tarragon = Entry(frame_hasselager, width = entry_width)
		ts_h_tarragon.grid(row = 7, column = 1)
		Label(frame_hasselager, text = 'Italian Basil').grid(row = 8, column = 0, sticky = E)
		ts_h_italianbasil = Entry(frame_hasselager, width = entry_width)
		ts_h_italianbasil.grid(row = 8, column = 1)
		Label(frame_hasselager, text = 'Dill').grid(row = 9, column = 0, sticky = E)
		ts_h_dill = Entry(frame_hasselager, width = entry_width)
		ts_h_dill.grid(row = 9, column = 1)

		Label(frame_hasselager, text = 'Italian Basil').grid(row = 2, column = 3, sticky = E)
		fp_h_thyme = Entry(frame_hasselager, width = entry_width)
		fp_h_thyme.grid(row = 2, column = 4)
		Label(frame_hasselager, text = 'Curly Parsley').grid(row = 3, column = 3, sticky = E)
		fp_h_coriander = Entry(frame_hasselager, width = entry_width)
		fp_h_coriander.grid(row = 3, column = 4)
		Label(frame_hasselager, text = 'Flat Coriander').grid(row = 4, column = 3, sticky = E)
		fp_h_rosemary = Entry(frame_hasselager, width = entry_width)
		fp_h_rosemary.grid(row = 4, column = 4)
		Label(frame_hasselager, text = 'Green Mint').grid(row = 5, column = 3, sticky = E)
		fp_h_mint = Entry(frame_hasselager, width = entry_width)
		fp_h_mint.grid(row = 5, column = 4)
		Label(frame_hasselager, text = 'Thyme').grid(row = 6, column = 3, sticky = E)
		fp_h_sage = Entry(frame_hasselager, width = entry_width)
		fp_h_sage.grid(row = 6, column = 4)
		Label(frame_hasselager, text = 'Rosemary').grid(row = 7, column = 3, sticky = E)
		fp_h_tarragon = Entry(frame_hasselager, width = entry_width)
		fp_h_tarragon.grid(row = 7, column = 4)
		Label(frame_hasselager, text = 'Tarragon').grid(row = 8, column = 3, sticky = E)
		fp_h_italianbasil = Entry(frame_hasselager, width = entry_width)
		fp_h_italianbasil.grid(row = 8, column = 4)

		frame_h_button = LabelFrame(frame_hasselager, pady = 7, bd = 0)
		frame_h_button.grid(row =10, column = 0, columnspan = 5)
		
		Button(frame_h_button, text = 'Generate Hasselager distribution', relief="solid", bg = '#D3D3D3', bd = 1, width = 37, command = lambda: self.generate_hasselager(ts_h_thyme.get(), ts_h_coriander.get(), ts_h_rosemary.get(), ts_h_mint.get(), ts_h_sage.get(), ts_h_tarragon.get(), ts_h_italianbasil.get(), ts_h_dill.get(), fp_h_thyme.get(), fp_h_coriander.get(), fp_h_rosemary.get(), fp_h_mint.get(), fp_h_sage.get(), fp_h_tarragon.get(), fp_h_italianbasil.get())).grid(row = 0, column = 0)

		#-------------------------------------
		# Right column (pallet distributions)
		#-------------------------------------

		frame_column_2 = LabelFrame(self.wind, borderwidth = '0')
		frame_column_2.place(x=315, y=2, relwidth=0.73, height=630)

		self.frame_distribution_brondby = LabelFrame(frame_column_2, bg = '#FFF')
		self.frame_distribution_brondby.grid(row = 1, column = 0, columnspan = 4, padx = 5, pady = 5)
		self.frame_distribution_brondby.place(x=8, y=6, relwidth=.99, height=304)

		self.frame_distribution_brondby_title = Label(self.frame_distribution_brondby, text = 'No distribution generated', font = ("Arial", 15), bg = '#FFF')
		self.frame_distribution_brondby_title.place(x = 10, y = 6)

		self.frame_distribution_hasselager = LabelFrame(frame_column_2, bg = '#FFF')
		self.frame_distribution_hasselager.grid(row = 1, column = 1, columnspan = 4, padx = 5, pady = 5)
		self.frame_distribution_hasselager.place(x=8, y=320, relwidth=.99, height=307)

		self.frame_distribution_hasselager_title = Label(self.frame_distribution_hasselager, text = 'No distribution generated', font = ("Arial", 15), bg = '#FFF')
		self.frame_distribution_hasselager_title.place(x = 10, y = 6)

		self.pallet_color = '#481F01'
		self.trayseal_color = '#7F0000'
		self.flowpack_color = '#004A7F'

	#-------------------------------------
	# Functions
	#-------------------------------------

	def draw_distribution(self, distribution, col_x, heights, pallet_colours, boxes_colours, boxes_amounts):

		pallet_width = 130
		boxes_width = pallet_width - 10
		pallet_height = 15
		base_y = 255

		self.pallet_1 = Label(distribution, text = '.', bg = pallet_colours[0], fg = pallet_colours[0])
		self.pallet_1.place(x = col_x, y = base_y, width = pallet_width, height = pallet_height)

		self.boxes_1 = Label(distribution, text = boxes_amounts[0], bg = boxes_colours[0], fg = '#FFF')
		self.boxes_1.place(x = col_x + 5, y = base_y - heights[0], width = boxes_width, height = heights[0])

		self.pallet_2 = Label(distribution, text = '.', bg = pallet_colours[1], fg = pallet_colours[1])
		self.pallet_2.place(x = col_x, y = base_y - pallet_height*1 - heights[0], width = pallet_width, height = pallet_height)

		self.boxes_2 = Label(distribution, text = boxes_amounts[1], bg = boxes_colours[1], fg = '#FFF')
		self.boxes_2.place(x = col_x + 5, y = base_y - pallet_height*1 - sum(heights[0:2]), width = boxes_width, height = heights[1])

		self.pallet_3 = Label(distribution, text = '.', bg = pallet_colours[2], fg = pallet_colours[2])
		self.pallet_3.place(x = col_x, y = base_y - pallet_height*2 - sum(heights[0:2]), width = pallet_width, height = pallet_height)

		self.boxes_3 = Label(distribution, text = boxes_amounts[2], bg = boxes_colours[2], fg = '#FFF')
		self.boxes_3.place(x = col_x + 5, y = base_y - pallet_height*2 - sum(heights[0:3]), width = boxes_width, height = heights[2])
		
		self.pallet_4 = Label(distribution, text = '.', bg = pallet_colours[3], fg = pallet_colours[3])
		self.pallet_4.place(x = col_x, y = base_y - pallet_height*3 - sum(heights[0:3]), width = pallet_width, height = pallet_height)

		self.boxes_4 = Label(distribution, text = boxes_amounts[3], bg = boxes_colours[3], fg = '#FFF')
		self.boxes_4.place(x = col_x + 5, y = base_y - pallet_height*3 - sum(heights[0:4]), width = boxes_width, height = heights[3])

		self.pallet_5 = Label(distribution, text = '.', bg = pallet_colours[4], fg = pallet_colours[4])
		self.pallet_5.place(x = col_x, y = base_y - pallet_height*4 - sum(heights[0:4]), width = pallet_width, height = pallet_height)

		self.boxes_5 = Label(distribution, text = boxes_amounts[4], bg = boxes_colours[4], fg = '#FFF')
		self.boxes_5.place(x = col_x + 5, y = base_y - pallet_height*4 - sum(heights[0:5]), width = boxes_width, height = heights[4])


	def generate_brondby(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
		try:
			start_time = time.time()
	
			distribution = distribute_brondby(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)

			Label(self.frame_distribution_brondby, text = '.', bg = '#FFF', fg = '#FFF').place(x = 5, y = 40, relwidth = .98, relheight = .855)

			self.message_brondby['text'] = f'Distribution generated ({len(distribution)} pallets - {round(time.time() - start_time, 2)}s)'
			self.message_brondby['fg'] = '#000'
			self.message_brondby['font'] = ('Helvetica', 8, 'bold')
			self.frame_distribution_brondby_title['text'] = f'Brøndby pallets distribution - {date.today().strftime("%d/%m/%Y")}'

			distribution_heights = [[] for n in range(len(distribution))]

			for column in distribution:
				distribution_heights.append(column)

			heights = [[] for n in range(len(distribution))]
			pallet_colours = [[] for n in range(len(distribution))]
			boxes_colours = [[] for n in range(len(distribution))]
			boxes_amounts = [[] for n in range(len(distribution))]
			dif = [[] for n in range(len(distribution))]

			for i in range(len(distribution)):
				heights[i] = list(map(lambda x: x * 75, distribution[i][::2]))
				dif[i].append(5 - len(heights[i]))
				heights[i].extend([0] * dif[i][0])

				for pallet in distribution[i]:
					if type(pallet) is float:
						continue
					else:
						if pallet[0][0] == 'T':
							boxes_colours[i].append(self.trayseal_color)
						elif pallet[0][0] == 'F':
							boxes_colours[i].append(self.flowpack_color)
					boxes_amounts[i].append(pallet[0])
				boxes_amounts[i].extend(['#FFF'] * dif[i][0])
				boxes_colours[i].extend(['#FFF'] * dif[i][0])
				
				for element in heights[i]:
					if element != 0:
						pallet_colours[i].append(self.pallet_color)
					else:
						pallet_colours[i].append('#FFF')

			x = 5

			for i in range(len(distribution)):
				self.draw_distribution(self.frame_distribution_brondby, x, heights[i], pallet_colours[i], boxes_colours[i], boxes_amounts[i])
				self.frame_pos_1 = Label(self.frame_distribution_brondby, text = '[n]', font = ("Arial", 15), bg = '#FFF')
				self.frame_pos_1.place(x = (x + 105 / 2), y = 270)
				self.frame_pos_1['text'] = f'[{i+1}]'
				x += 140
		except:
			self.message_brondby['text'] = 'Please check inputs'
			self.message_brondby['fg'] = 'red'
			self.message_brondby['font'] = ('Helvetica', 8, 'bold')

	def generate_hasselager(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
		try:
			start_time = time.time()

			distribution = distribute_brondby(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)

			Label(self.frame_distribution_hasselager, text = '.', bg = '#FFF', fg = '#FFF').place(x = 5, y = 40, relwidth = .98, relheight = .855)

			self.message_hasselager['text'] = f'Distribution generated ({len(distribution)} pallets - {round(time.time() - start_time, 2)}s)'
			self.message_hasselager['fg'] = '#000'
			self.message_hasselager['font'] = ('Helvetica', 8, 'bold')
			self.frame_distribution_hasselager_title['text'] = f'Hasselager pallets distribution - {date.today().strftime("%d/%m/%Y")}'

			distribution_heights = [[] for n in range(len(distribution))]

			for column in distribution:
				distribution_heights.append(column)

			heights = [[] for n in range(len(distribution))]
			pallet_colours = [[] for n in range(len(distribution))]
			boxes_colours = [[] for n in range(len(distribution))]
			boxes_amounts = [[] for n in range(len(distribution))]
			dif = [[] for n in range(len(distribution))]

			for i in range(len(distribution)):
				heights[i] = list(map(lambda x: x * 75, distribution[i][::2]))
				dif[i].append(5 - len(heights[i]))
				heights[i].extend([0] * dif[i][0])

				for pallet in distribution[i]:
					if type(pallet) is float:
						continue
					else:
						if pallet[0][0] == 'T':
							boxes_colours[i].append(self.trayseal_color)
						elif pallet[0][0] == 'F':
							boxes_colours[i].append(self.flowpack_color)
					boxes_amounts[i].append(pallet[0])
				boxes_amounts[i].extend(['#FFF'] * dif[i][0])
				boxes_colours[i].extend(['#FFF'] * dif[i][0])
				
				for element in heights[i]:
					if element != 0:
						pallet_colours[i].append(self.pallet_color)
					else:
						pallet_colours[i].append('#FFF')

			x = 5

			for i in range(len(distribution)):
				self.draw_distribution(self.frame_distribution_hasselager, x, heights[i], pallet_colours[i], boxes_colours[i], boxes_amounts[i])
				self.frame_pos_1 = Label(self.frame_distribution_hasselager, text = '[n]', font = ("Arial", 15), bg = '#FFF')
				self.frame_pos_1.place(x = (x + 105 / 2), y = 270)
				self.frame_pos_1['text'] = f'[{i+1}]'
				x += 140

		except:
			self.message_hasselager['text'] = 'Please check inputs'
			self.message_hasselager['fg'] = 'red'
			self.message_hasselager['font'] = ('Helvetica', 8, 'bold')

if __name__ == '__main__':
    window = Tk()
    application = Pallet_distribution(window)
    window.mainloop()