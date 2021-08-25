# Arrays

They are like trains with cars, stiff and irreplacable when fixed.

They are easily traversed, but bad at insert and prepend operations.

The space complexity of arrays with the :
Insert operation (true insert) is worst case linear as everyone needs to be shifted one space on append (o(n) time complexity I'm guessing or space)
They are also bad at prepends due to shifting (linear space) but better at suffixing as the reindexing isn't necessary

They are also better at traversing (constant time )

Arrays in pythons have amortised constant space comlpexity as they take up more space than needed and then they expand on reaching certain breaking ponts

Wait...that means the array structure by default has linear space anyways...this is just mockup. Real notes later


# Linked lists

They are much better at prepends, inserts and suffixing as they are made up of nodes with constant links regardless of size

Worse case linear runtime for traversing though.
This means things like length have linear runtime.

Tracking these values could help the operation of length so, it depends on the implementation again.

They take linear space 
