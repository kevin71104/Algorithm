import time
import sys

########################################
# You can add supporting functions here





########################################

def mergesort(x, count):
    ### TODO ###
    # Implement the merge sort algorithm.
    # x is a list with N elements.
    # You must return a sorted list and a counter of splitting number.
    if len(x) > 1 :
        # split x into three sublist with left > center > right
        q = int(len(x) / 3);
        r = len(x) % 3;
        #print(q,r)
        if r == 2 :
            left,   count_1 = mergesort(x[:q+1],count+1);
            center, count_2 = mergesort(x[q+1:2*q+2],count+1);
            right,  count_3 = mergesort(x[2*q+2:],count+1);
        elif r == 1 :
            left,   count_1 = mergesort(x[:q+1],count+1);
            center, count_2 = mergesort(x[q+1:2*q+1],count+1);
            right,  count_3 = mergesort(x[2*q+1:],count+1);
        else :
            left,   count_1 = mergesort(x[:q],count+1);
            center, count_2 = mergesort(x[q:2*q],count+1);
            right,  count_3 = mergesort(x[2*q:],count+1);
        '''print(left)
        print(center)
        print(right)'''

        # merge three sublist
        
        return x, (count_1+count_2+count_3+1)
    else :
        return x, 0

if __name__ == '__main__':
    case = sys.argv[1]
    test_name = 'test_'+str(case)+'.txt'
    out_name = 'out_'+str(case)+'.txt'
    file_in = open(test_name, 'r')
    file_out = open(out_name, 'w')
    start_time = time.time()
    l = file_in.readline().split()
    l = list(map(int, l))
    print('origin list','')
    print(l)
    count = 0
    result, count = mergesort(l, count)
    for i in result:
        file_out.write(str(i)+' ')
    file_out.write('\n')
    file_out.write(str(count))
    print('Timer: ', time.time()-start_time)
