year=int(input())
if year>=1900 and year<=10**5:
	def leap(year):

		if year%4==0 and year%100!=0 or year%400==0:
			return True
		else:
			return False
	print(leap(year))

