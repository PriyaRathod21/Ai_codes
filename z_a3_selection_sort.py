def selectionSort(a, n):
	for i in range(n-1):
		mini = i
		for j in range(i+1,n):
			if(a[j]<a[mini]):
				mini = j
		a[i],a[mini] = a[mini],a[i]
	print("After Selection sort: ", a)

def main():
	a = []
	n = int(input("Enter no. of elements in array: "))
	for i in range(n):
		e = int(input("Enter element: "))
		a.append(e)
	print("\nOriginal Array: ", a)
	selectionSort(a, n)
main()

