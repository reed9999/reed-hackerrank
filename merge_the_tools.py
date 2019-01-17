# https://www.hackerrank.com/challenges/merge-the-tools/problem

def print_segment(segment):
    unique = []
    for c in segment:
        if not c in unique:
            unique.append(c)
    print(''.join(unique))

def merge_the_tools(the_string, k):
        assert len(the_string) % k == 0
        for i in range(int(len(the_string) / k)):
            print_segment(the_string[i*k:(i+1)*k])



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)