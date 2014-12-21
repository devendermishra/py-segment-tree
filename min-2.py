
import seg_tree
#Implement RMQ using SegmentTree
def use_val(left, right):
  if left<right:
    return left
  return right

def update_val(result, old_val, new_val):
  if new_val<result:
    result = new_val


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
  
  segtree = seg_tree.SegmentTree(use_val, update_val, 10000000)
  segtree.construct(arr)
  
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
      ans = segtree.getresult(start, end)
      print ans
      print "Min in ["+str(start)+","+str(end)+"] is "+str(ans)
    elif inp[0]=='U':
      ptw = map(int, inp[2:].split())
      index = ptw[0]
      new_val = ptw[1]
      segtree.update(index, new_val)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
