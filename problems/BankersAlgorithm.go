package problems

import "fmt"

//https://en.wikipedia.org/wiki/Banker's_algorithm

//Banker's algorithm
//
//The Banker algorithm, sometimes referred to as the detection algorithm,
//is a resource allocation and deadlock avoidance algorithm developed by Edsger Dijkstra
//that tests for safety by simulating the allocation of predetermined maximum possible amounts of all resources,
//and then makes an "s-state" check to test for possible deadlock conditions for all other pending activities,
//before deciding whether allocation should be allowed to continue.
//
//The algorithm was developed in the design process for the THE operating system
//and originally described (in Dutch) in EWD108.[1]
//When a new process enters a system,
//it must declare the maximum number of instances of each resource type that it may ever claim;
//clearly, that number may not exceed the total number of resources in the system.
//Also, when a process gets all its requested resources it must return them in a finite amount of time.

////input case
//     Allocation　　　Max　　　Available
//　　  ＡＢＣＤ　　  ＡＢＣＤ　　ＡＢＣＤ
//P1   ００１４　　  ０６５６　　１５２０
//P2　 １４３２　　  １９４２
//P3　 １３５４　  　１３５６
//P4 　１０００　　  １７５０

//Allocation: for this process, currently allocated resources
//Max: for this process, maximum resources claimed when entering this system
//Available: currently available system resources

////pseudo-code
//P - 进程的集合
//Mp - 进程p的最大的请求数目
//Cp - 进程p当前被分配的资源
//A - 当前可用的资源
//
//StateIsSafe:
//	while (P != ∅) {
//		found = FALSE;
//		foreach (p ∈ P) {
//			if (Mp − Cp ≤ A) {
//				/* p可以獲得他所需的資源。假設他得到資源後執行；執行終止，並釋放所擁有的資源。*/
//				A = A + Cp ;
//				P = P − {p};
//				found = TRUE;
//			}
//		}
//		if (! found) return FAIL;
//	}
//	return OK;

type ProcessId int

type ProcessStatus struct {
	//currently allocated resources
	Allocation []int
	//maximum resources
	Max []int
}

//BankersAlgorithm()判断当前状态是否是安全的，安全的意思是：
//存在一个进程序列，进程们按此序列运行，每次运行进程都一口气请求系统分配给该进程该进程剩余所需所有资源，系统允许该请求，最终所有的进程都执行完毕。
//在构建某个安全的进程序列的过程中，如果当前子序列导致系统进入死锁，那么其他的子序列同样也会导致系统进入死锁，这在数学上可以被证明，
//所以BankersAlgorithm()没有回溯并尝试构建其他的序列。

//也即：
//在一个安全的状态中，所有的进程排列组合结果中有的序列安全，有的序列不安全，安全的序列个数大于等于1；
//在一个不安全的状态中，所有的进程排列组合结果都是不安全序列。

func BankersAlgorithm(processes map[ProcessId]ProcessStatus, systemAvailable []int) (systemStatusIsSafe bool, anyProcessSequence []ProcessId) {
	if len(processes) == 0 {
		return true, []ProcessId{}
	}
	resourceDimension := len(systemAvailable)
	var processSequence []ProcessId
	for len(processes) > 0 {
		foundNextProcess := false
		for processId_, processStatus := range processes {
			systemAvailableCanMeetRequirement := true
			//processNeed该程序所有剩余所需资源量
			processNeed := make([]int, resourceDimension)
			for resourceIndex := 0; resourceIndex < resourceDimension; resourceIndex++ {
				processNeed[resourceIndex] = processStatus.Max[resourceIndex] - processStatus.Allocation[resourceIndex]
				if processNeed[resourceIndex] > systemAvailable[resourceIndex] {
					systemAvailableCanMeetRequirement = false
					break
				}
			}
			if systemAvailableCanMeetRequirement {
				foundNextProcess = true
				for resourceIndex := 0; resourceIndex < resourceDimension; resourceIndex++ {
					systemAvailable[resourceIndex] += processStatus.Allocation[resourceIndex]
				}
				delete(processes, processId_)
				processSequence = append(processSequence, processId_)
				// 迭代过程中被迭代的容器结构和大小发生了变化，所以需要重新迭代。
				break
			}
		}
		if foundNextProcess == false {
			return false, []ProcessId{}
		}
	}
	return true, processSequence
}

// 因为BankersAlgorithm()可以检测某个状态是否安全，所以它可以用于死锁提前避免：
//当某个进程向系统发出资源请求，请求立刻分配一定数量的资源时，系统思考：
//倘若允许该请求，那么系统的资源状态和进程状态都会进入新的状态，
//判断该新状态是否安全，如果安全，立刻允许该请求，如果不安全，那么拒绝该请求。
//该进程可以立即发出不同的新请求，或在未来发出相同或不同的新请求。

//When the system receives a request for resources,
//it runs the Banker's algorithm to determine if it is safe to grant the request.
//The algorithm is fairly straightforward once the distinction between safe and unsafe states is understood.
//
//    Can the request be granted?
//        If not, the request is impossible and must either be denied or put on a waiting list
//    Assume that the request is granted
//    Is the new state safe?
//        If so grant the request
//        If not, either deny the request or put it on a waiting list

//应用银行家算法的系统总能提前避免进入死锁状态，所以该系统实时都是安全状态的。

//银行家算法应用的系统有两个要求，
//1.进程进入系统的进程集合时要标明自己各个资源维度所使用的的最大资源量Max
//2.已经占用的资源不会中途释放，只会在所有的资源都得到满足后才会一起释放。

func OnResourceRequest(processes map[ProcessId]ProcessStatus, systemAvailable []int,
	requestingProcessId ProcessId, requestedResource []int) (grant bool) {

	return true
}

////input case
//Available system resources are:
//A B C D
//3 1 1 2
//
//Processes (currently allocated resources):
//   A B C D
//P1 1 2 2 1
//P2 1 0 3 3
//P3 1 2 1 0
//
//Processes (maximum resources):
//   A B C D
//P1 3 3 2 2
//P2 1 2 3 4
//P3 1 3 5 0

func TestBankersAlgorithm() {

	//初始状态，是安全的
	systemAvailable := []int{3, 1, 1, 2}
	processes := map[ProcessId]ProcessStatus{
		1: {
			Max:        []int{3, 3, 2, 2},
			Allocation: []int{1, 2, 2, 1},
		},
		2: {
			Max:        []int{1, 2, 3, 4},
			Allocation: []int{1, 0, 3, 3},
		},
		3: {
			Max:        []int{1, 3, 5, 0},
			Allocation: []int{1, 2, 1, 0},
		},
	}
	isSafe, anySeq := BankersAlgorithm(processes, systemAvailable)
	fmt.Println("Status is safe:", isSafe)
	fmt.Println("anySeq:", anySeq)

	//假如 process 3 requests 1 unit of resource C, 新的状态也是安全的。
	systemAvailable = []int{3, 1, 0, 2}
	processes = map[ProcessId]ProcessStatus{
		1: {
			Max:        []int{3, 3, 2, 2},
			Allocation: []int{1, 2, 2, 1},
		},
		2: {
			Max:        []int{1, 2, 3, 4},
			Allocation: []int{1, 0, 3, 3},
		},
		3: {
			Max:        []int{1, 3, 5, 0},
			Allocation: []int{1, 2, 2, 0},
		},
	}
	isSafe, anySeq = BankersAlgorithm(processes, systemAvailable)
	fmt.Println("Status is safe:", isSafe)
	fmt.Println("anySeq:", anySeq)

	//from the state we started at, assume that process 2 requests 1 unit of resource B.
	//回到初始状态，考虑这个请求导致的新状态，新状态是不安全的。
	systemAvailable = []int{3, 0, 1, 2}
	processes = map[ProcessId]ProcessStatus{
		1: {
			Max:        []int{3, 3, 2, 2},
			Allocation: []int{1, 2, 2, 1},
		},
		2: {
			Max:        []int{1, 2, 3, 4},
			Allocation: []int{1, 1, 3, 3},
		},
		3: {
			Max:        []int{1, 3, 5, 0},
			Allocation: []int{1, 2, 1, 0},
		},
	}
	isSafe, anySeq = BankersAlgorithm(processes, systemAvailable)
	fmt.Println("Status is safe:", isSafe)
	fmt.Println("anySeq:", anySeq)
}

//Status is safe: true
//anySeq: [1 2 3]
//Status is safe: true
//anySeq: [1 2 3]
//Status is safe: false
//anySeq: []
