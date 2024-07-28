#infinite num to text convertor
import time
list1=('','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
list2=('', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Ninteen')
list3=('', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninty')
list4=('', "Hundred", 'Thousand', 'Lakh', 'Crore')
def num2text(num, recursion=0):
	if num==0:
		return 'Zero'
	else:
		num_list=[]
		count=0
		num_text=()
		
		while (num!=0):
			num_list.append(num%10)
			num//=10
		num_list.reverse()
			
		while len(num_list)!=0:
			if count==0 and len(num_list)>0:
				'''for first to digit 0-99'''
				if len(num_list)==1:
					num_list.insert(0, 0)
				num_text=digits2text(num_list[-2:])+num_text
				count+=1
				num_list=num_list[:-2]
				
			elif (count==1 and len(num_list)>0):
				'''for 100th number'''
				num_text=(Hundrade(num_list[-1]))+num_text
				count+=1
				num_list=num_list[:-1]
				
			elif count>=2 and count<=4 and len(num_list)>0:
				"This calculate over 1000 number "
				if len(num_list)==1:
					num_list.insert(0, 0)
				num_text=digits2text(num_list[-2:])+(list4[count],)+num_text
				num_list=num_list[:-2]
				count+=1
			
			elif count>=5 and len(num_list)>0:
				num2=0
				for i in num_list:
					num2=(num2*10)+i
				num_text=num2text(num2, 1)+(list4[count-4],)+num_text
				num_list.clear()
				count+=1
		if recursion==1:
			return num_text
		else:
			return ' '.join(num_text)

def digits2text( digits: list ) -> str :
	if digits[0]==0 and digits[1]!=0:
		return (list1[digits[1]],)
	elif digits[0]==1 and digits[1]!=0:
		return (list2[digits[1]],)
	elif digits[0]>0 and digits[1]==0 :
		return (list3[digits[0]],)
	elif digits[0]>=2 and digits[1]!=0 :
		return list3[digits[0]], list1[digits[1]]
	else:
		return ('',)
		
def Hundrade(digit:list)-> str:
	if digit==0:
		return ('',)
	else:
		return list1[digit], list4[1]

if __name__=='__main__':
	start=time.time()
	#for num in range(19899):
		#print(num, num2text(num))
		
	num=11111111111111111111111483474862342374523462354324234234119908765432 #19, 90, 87, 65, 4, 32
	print(num, num2text(num))
	print((time.time())-start)