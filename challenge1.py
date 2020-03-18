from collections import Counter





class Rectangle:
	'''  All dimensoions are in sqft'''
	total_area = 1000.00 
	
	''' Here the whole area is divided into two phases
	First phase is of 500 sqft whose length is 50 ft and breadth is 10 ft
	It contains five rectangles each of 80 sqft whose each length is 10 ft and breadth is 8 sqft '''
 
	first_phase = 500.00

	first_phase_length = 50.00

	first_phase_breadth = 10.00

	number_of_rectangles = 5

	first_rectangle_area = 80.00
	

	''' second phase (500 sqft) consist of two rectangles
			one is 100 sqft , second one is 150 sqft'''

	
	
	second_phase = 500.00

	second_phase_length = 50.00

	second_phase_breadth = 10.00

	''' '''
	number_of_second_phase_of_rectangles = 5

	second_rectangle_area = 100.00

	third_rectangle_area = 150.00


	

	def first_rectangle(self):

		rectangle_phase_area_1 = []
		rectangle_1_area = []
		remaining_1_area = []

		length_1 = float(input('Enter the length of the first rectangle\n'))
		breadth_1 = float(input('Enter the length of the second rectangle\n'))

		area_1 = length_1*breadth_1

		if area_1 == Rectangle.first_rectangle_area:
			if length_1==10.00 and breadth_1==8.00:
				print('Area of the one of five rectangle is {} sqft\n'.format(area_1))
				total_area_1 = area_1 * Rectangle.number_of_rectangles
				print('The area occupied by the five rectangles are {} sqft\n'.format(total_area_1))
				
				reamainig_area_1_phase = Rectangle.first_phase - total_area_1        
				print('The unoccupied area of  is {} sqft\n'.format(reamainig_area_1_phase))
				 
				each_of_remaing_area_1 = reamainig_area_1_phase/5
				breadth_of_each_remaining_area_1 = each_of_remaing_area_1/Rectangle.first_phase_breadth

				print('Breadth of each remaining area is {} ft\n'.format(breadth_of_each_remaining_area_1))

				for _ in range(Rectangle.number_of_rectangles):
					
					if length_1==10.00 and breadth_1==8.00 and breadth_of_each_remaining_area_1==2.00 :
						
						rectangle_phase_area_1.append(str(area_1)+' sqft Rectangle')
						rectangle_1_area.append(area_1)
						rectangle_phase_area_1.append(str(each_of_remaing_area_1)+' sqft remaining space')
						remaining_1_area.append(each_of_remaing_area_1)


			else:
				print('Make sure Length is 10 sqft and breadth is 8 sqft ')


		else:
			print(f'The input area {length_1*breadth_1} sqft is not matching  with the {Rectangle.first_rectangle_area} sqft ')


				
		
		d = Counter(rectangle_phase_area_1)
		Dict = dict(d)
		
		rect_1 = Counter(rectangle_1_area)
		Dict_rect_1 = dict(rect_1)
		
		for k1, v1 in rect_1.items():
			print('There are {} rectangles of {} sqft\n'.format(v1,k1))

		rem_1 = Counter(remaining_1_area)
		Dict_rem_1 = dict(rem_1) 
		
		for k2, v2 in rem_1.items():
			print('The remaining area is {} sqft\n'.format(k2*v2))


		for k in rectangle_phase_area_1:
			print(k)



	def second_rectangle(self):
		
		area = []

		print('\nEnter the dimensions for Second rectangle\n')
		length_2 = float(input('Enter the length of the rectangle\n'))
		breadth_2 = float(input('Enter the breadth of the rectangle\n'))

		area_2 = length_2 * breadth_2 

		if area_2 == Rectangle.second_rectangle_area:
			if length_2==50 and breadth_2==2:
				print('The area of the second rectangle is {}\n'.format(area_2))

			else:
				print('Make sure that Length is 50 and Breadth is 2\n') 
		

		else:
			print(f'The input area {length_2*breadth_2} sqft is not matching  with the {Rectangle.second_rectangle_area} sqft ')
			


		print('Enter the dimensions for third rectangle\n')
		length_3 = float(input('Enter the length of the rectangle\n'))
		breadth_3 = float(input('Enter the breadth of the rectangle\n'))

		area_3 = length_3*breadth_3


		if area_3 == Rectangle.third_rectangle_area:
			if length_3==50 and breadth_3==3:
				print('The area of the third rectangle is {}\n'.format(area_3))

				total_rectangle_area = area_2+area_3
				remaining_area_2_phase = Rectangle.second_phase - total_rectangle_area

				print('Total Rectangle area of the second phase is {} sqft\n'.format(total_rectangle_area))
				print('Remaining second phase area is {} sqft :  Length is {} Breadth is {}\n'.format(remaining_area_2_phase, Rectangle.second_phase_length, remaining_area_2_phase/Rectangle.second_phase_length ))

			
				for i in range(1,Rectangle.number_of_second_phase_of_rectangles+1):
					if Rectangle.second_phase_length==50.00 and remaining_area_2_phase%i==0.00:
						breadth_of_remaining_area_1 = i
						remaining_area_1 = Rectangle.second_phase_length*breadth_of_remaining_area_1
						print('Remaining area 1 is {} sqft : Whose Length is {} and Breadth is {} \n'.format(remaining_area_1,Rectangle.second_phase_length,i))
						
						breadth_of_remaining_area_2 = (remaining_area_2_phase/Rectangle.second_phase_length) - i
						remaining_area_2 = Rectangle.second_phase_length*breadth_of_remaining_area_2
						print('Remaining area 2 is {} sqft : Whose Length is {} and Breadth is {} \n'.format(remaining_area_2,Rectangle.second_phase_length,breadth_of_remaining_area_2))
						
						area.append(str(remaining_area_1)+' sqft remaining area')
						if length_2==50 and breadth_2==2:
							area.append(str(area_2)+' sqft of Second rectangle')
						area.append(str(remaining_area_2)+' sqft remaining area')
						if length_3==50 and breadth_3==3:
							area.append(str(area_3)+' sqft of third rectangle')


						break



						
									

			

			else:
				print('Make sure that Length is 50 and Breadth is 3\n') 

		else:
			print(f'The input area {length_3*breadth_3} sqft is not matching  with the {Rectangle.third_rectangle_area} sqft ')
				

		for l in area:
			print(l)




if __name__ == '__main__':


	R = Rectangle()
	R.first_rectangle()
	R.second_rectangle()







