def getmid(start, end):
  return start + (end-start)/2

class SegmentTree:
  def __init__(self, use_val, update_val, invalid_val):
    self.use_val = use_val
    self.update_val = update_val
    self.invalid_val = invalid_val

  def constructutil(self, arr, start, end, result_array, result_index):
    if start == end:
      print "result_index = "+str(result_index) + "  size of result_array = "+str(len(result_array))
      result_array[result_index]  = arr[start]
      return result_array[result_index]
    mid = getmid(start, end)
    print "Mid = "+str(mid) + "Childs are "+str(2*result_index+1)+" and "+str(2*result_index+2)
    left_val = self.constructutil(arr, start, mid, result_array, 2*result_index+1)
    right_val = self.constructutil(arr, mid+1, end, result_array, 2*result_index+2)
    print "result_index = "+str(result_index) + "  size of result_array = "+str(len(result_array))
    result_array[result_index]  = self.use_val(left_val, right_val)
    return result_array[result_index]

  def construct(self, arr):
    self.arr = arr
    #Get the size in the next higher power of 2
    s = 1
    slen = len(arr)
    while s < slen:
        s <<= 1

    self.result_array = [0 for x in range(0,2*s+1)]
    self.constructutil(arr, 0, len(arr)-1, self.result_array, 0)

  def getresultutil(self, start, end, qstart, qend, index):
    if qstart<=start and qend>=end:
      return self.result_array[index]
    if end<qstart or start>qend:
      return self.invalid_val
    mid = getmid(start, end)
    left = self.getresultutil(start, mid, qstart, qend, 2*index+1)
    right = self.getresultutil(mid+1, end, qstart, qend, 2*index+2)
    return self.use_val(left, right)

  def getresult(self, qstart, qend):
    if qstart<0 or qend>len(self.arr)-1 or qstart>qend:
      return self.invalid_val

    return self.getresultutil(0, len(self.arr)-1, qstart, qend, 0)

  def updateutil(self, start, end, old_val, new_val, i, index):
    if i<start or i>end:
      return

    self.update_val(self.result_array[index], old_val, new_val)
    if start !=end:
      mid = getmid(start, end)
      self.updateutil(start, mid, old_val, new_val, i, 2*index+1)
      self.updateutil(mid+1, end, old_val, new_val, i, 2*index+2)


  def update(self, i, new_val):
    if i<0 or i>=len(self.arr):
      return

    old_val = self.arr[i]
    self.arr[i] = new_val
    self.updateutil(0, len(self.arr)-1, old_val, new_val, i, 0)


def main():
  return
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
