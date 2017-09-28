import merge_sort

for i in range(1, 4, 1):
    test_name = 'test_' + str(i) + '.txt'
    ans_name = 'ans_' + str(i) + '.txt'
    test_file = open(test_name, 'r')
    ans_file = open(ans_name, 'r')

    test = test_file.readline().split()
    test = list(map(int, test))
    count = 0
    ans = ans_file.readline().split()
    ans = list(map(int, ans))
    ans_count = int(ans_file.readline())
    result, count = merge_sort.mergesort(test, count)
    if result == ans and ans_count == count:
        print('Pass test case %d.' % i)
    else:
        print('Test case %d fail.' % i)

