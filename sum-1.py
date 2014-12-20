def getmid(start, end):
  return start + (end-start)/2

def constructSumUtil(arr, start, end, sum_array, sum_index):
  if start==end:
    sum_array[sum_index] = arr[start]
    return arr[start]
  
  mid = getmid(start, end)
  #This operation can be abstracted
  sum_array[sum_index] = constructSumUtil(arr, start, mid, sum_array, sum_index*2+1)+
                          constructSumUtil(arr, mid+1, end, sum_array, sum_index*2+2)
  return sum_array[sum_index]

def constructSum(arr):
  sum_array = [0 for x in range(0, 2*len(arr))]
  constructSumUtil(arr, 0, len(arr)-1, sum_array, 0)
  return (arr, sum_array)

def getsumutil(sum_array, start, end, qstart, qend, index):
  if qstart<=start and qend>=end:
    return sum_array[index]
  
  if end<qstart or start>qend:
    return 0
  
  mid = getmid(start, end)
  #Operation which can be abstracted
  return getsumutil(sum_array, start, mid, qstart, qend, 2*index+1)+
          getsumutil(sum_array, mid+1, end, qstart, qend, 2*index+2)

def getsum(sum_array, n, qstart, qend):
  if qstart<0 or qend>n-1 or qstart>qend:
    print "Invalid range"
    return -1
  
  getsumutil(sum_array, 0, n-1, qstart, qend, 0)

def updateutil(sum_array, start, end, diff, i, index):
  if i<start or i>end:
    return
  
  #Operation which can be abstracted
  s[index] += diff
  
  if start != end:
    mid = getmid(start,end)
    updateutil(sum_array, start, mid, diff, i, 2*index+1)
    updateutil(sum_array, mid+1, end, diff, i, 2*index+2)

def update(arr, sum_array, i, new_val)
  if i<0 or i>=len(arr):
    print "Invalid range"
    return
  #Operation which can be abstracted
  diff = new_val - arr[i]
  arr[i] = new_val
  updateutil(sum_array, 0, len(arr)-1, diff, i, 0)

def main():
  #This will be an interactive application
  print "Enter the number of elements in the array"
  n = len(raw_input())
  
  print "Enter the elements separated by spaces"
  
  print "Now, entering into loop"
  print "To exit, press q/Q"
  print "To query, press G <start range> <end range>"
  print "To update, press U <index> <new value>"
  
  exit = False
  while not exit:
    print "Enter the operation and index"
    

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
