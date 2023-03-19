# python3
import heapq
def parallel_processing(n, m, data):
    output = []
    heap = [(0,i) for i in range(n)]
    heapq.heapify(heap)
    for i, bebrik in enumerate(data):
        time, thread = heapq.heappop(heap)
        output.append((thread, time))
        heapq.heappush(heap, (time + bebrik, thread)
                       
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    ina = list(map(int, input().split()))
    n = ina[0]
    m = ina[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for thread, time in result:
        print(thread, time)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
