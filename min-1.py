def getmid(start, end):
  return start + (end-start)/2

def constructMinUtil(arr, start, end, min_array, min_index):
  if start==end:
    min_array[min_index] = arr[start]
    return arr[start]

  mid = getmid(start, end)
  #This operation can be abstracted
  left_min = constructMinUtil(arr, start, mid, min_array, min_index*2+1)
  right_min = constructMinUtil(arr, mid+1, end, min_array, min_index*2+2)
  if left_min<right_min:
    min_array[min_index]  = left_min
  else:
    min_array[min_index]  = right_min

  return min_array[min_index]

def constructMin(arr):
  from math import ceil, log
  min_array = [0 for x in range(2*(pow(2, int(ceil(log(len(arr), 2))))) - 1)]
  constructMinUtil(arr, 0, len(arr)-1, min_array, 0)
  return (arr, min_array)

def getminutil(min_array, start, end, qstart, qend, index):
  if qstart<=start and qend>=end:
    return min_array[index]

  if end<qstart or start>qend:
    return float('inf')

  mid = getmid(start, end)
  #Operation which can be abstracted
  left = getminutil(min_array, start, mid, qstart, qend, 2*index+1)
  right = getminutil(min_array, mid+1, end, qstart, qend, 2*index+2)
  if left<right:
    return left
  else:
    return right
  return float('inf')

def getmin(min_array, n, qstart, qend):
  if qstart<0 or qend>n-1 or qstart>qend:
    print "Invalid range"
    return -1

  return getminutil(min_array, 0, n-1, qstart, qend, 0)

def updateutil(min_array, start, end, new_val, i, index):
  if i<start or i>end:
    return

  #Operation which can be abstracted
  if new_val<min_array[index]:
    min_array[index] = new_val

  if start != end:
    mid = getmid(start,end)
    updateutil(min_array, start, mid, new_val, i, 2*index+1)
    updateutil(min_array, mid+1, end, new_val, i, 2*index+2)

def update(arr, min_array, i, new_val):
  if i<0 or i>=len(arr):
    print "Invalid range"
    return
  #Operation which can be abstracted
  arr[i] = new_val
  updateutil(min_array, 0, len(arr)-1, new_val, i, 0)

def main():
  #This will be an interactive application
  print "Enter the number of elements in the array."
  n = int(raw_input())
  i = 0
  print "Enter the elements separated by spaces. Press Enter after each input."
  arr = []
  while i<n:
    num = int(raw_input())
    arr.append(num)
    i +=1

  print "Now, entering into loop"
  print "To exit, press q/Q"
  print "To query, press G <start range> <end range>"
  print "To update, press U <index> <new value>"

  (myarr,s) = constructMin(arr)

  exit = False
  while not exit:
    print "Enter the operation and index"
    inp = raw_input()
    if str(inp) == 'q' or str(inp)=='Q':
      exit = True
    if inp[0]=='G':
      ptw = map(int, inp[2:].split())
      start = ptw[0]
      end = ptw[1]
      ans = getmin(s, len(myarr), start, end)
      print ans
      print "Min in ["+str(start)+","+str(end)+"] is "+str(ans)
    elif inp[0]=='U':
      ptw = map(int, inp[2:].split())
      index = ptw[0]
      new_val = ptw[1]
      update(myarr, s, index, new_val)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
